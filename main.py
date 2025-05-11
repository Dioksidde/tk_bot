import os
import logging
import random
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    ConversationHandler
)

from models import Messages, ButtonLabels, CallbackData, AppConfig
from questions import get_questions_for_subcategories

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define conversation states
START, SHOW_RULES, CHOOSE_CATEGORY, CHOOSE_SUBCATEGORY, VIEW_SUBCATEGORIES, PLAY_GAME = range(6)


class ToKnowBot:
    def __init__(self, token):
        """Initialize the bot with token and configurations"""
        self.token = token
        self.messages = Messages()
        self.buttons = ButtonLabels()
        self.callbacks = CallbackData()
        self.config = AppConfig()

        # Setup application
        self.application = Application.builder().token(self.token).build()
        self._setup_handlers()

    def _setup_handlers(self):
        """Set up all necessary conversation handlers"""
        # Set up conversation handler
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", self.start)],
            states={
                START: [CallbackQueryHandler(self.show_rules, pattern=f"^{self.callbacks.START}$")],
                SHOW_RULES: [CallbackQueryHandler(self.choose_category, pattern=f"^{self.callbacks.CHOOSE_CATEGORY}$")],
                CHOOSE_CATEGORY: [
                    CallbackQueryHandler(
                        self.show_subcategories,
                        pattern=f"^{self.callbacks.CATEGORY_PREFIX}"
                    )
                ],
                CHOOSE_SUBCATEGORY: [
                    CallbackQueryHandler(
                        self.subcategory_selected,
                        pattern=f"^{self.callbacks.SUBCATEGORY_PREFIX}"
                    ),
                    CallbackQueryHandler(
                        self.view_selected_subcategories,
                        pattern=f"^{self.callbacks.VIEW_SELECTIONS}$"
                    ),
                    CallbackQueryHandler(
                        self.choose_category,
                        pattern=f"^{self.callbacks.BACK_TO_CATEGORIES}$"
                    ),
                    CallbackQueryHandler(
                        self.start_game,
                        pattern=f"^{self.callbacks.START_GAME}$"
                    ),
                ],
                VIEW_SUBCATEGORIES: [
                    CallbackQueryHandler(
                        self.show_subcategories,
                        pattern=f"^{self.callbacks.BACK_TO_SUBCATEGORIES}$"
                    ),
                    CallbackQueryHandler(
                        self.choose_category,
                        pattern=f"^{self.callbacks.BACK_TO_CATEGORIES}$"
                    ),
                ],
                PLAY_GAME: [
                    CallbackQueryHandler(
                        self.next_question,
                        pattern=f"^{self.callbacks.NEXT_QUESTION}$"
                    ),
                    CallbackQueryHandler(
                        self.previous_question,
                        pattern=f"^{self.callbacks.PREVIOUS_QUESTION}$"
                    ),
                    CallbackQueryHandler(
                        self.choose_category,
                        pattern=f"^{self.callbacks.BACK_TO_CATEGORIES}$"
                    ),
                ],
            },
            fallbacks=[CommandHandler("cancel", self.cancel)],
        )

        self.application.add_handler(conv_handler)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Send welcome message and prompt user to continue."""
        # Initialize selected subcategories list in user data
        context.user_data["selected_subcategories"] = []
        
        keyboard = [
            [InlineKeyboardButton(self.buttons.START_BUTTON, callback_data=self.callbacks.START)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            self.messages.WELCOME_MESSAGE,
            reply_markup=reply_markup
        )

        return START

    async def show_rules(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Show the rules and prompt user to continue."""
        query = update.callback_query
        await query.answer()

        keyboard = [
            [InlineKeyboardButton(self.buttons.CHOOSE_CATEGORY_BUTTON, callback_data=self.callbacks.CHOOSE_CATEGORY)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Delete previous message and send a new one instead of editing
        await query.delete_message()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=self.messages.RULES_MESSAGE,
            reply_markup=reply_markup
        )

        return SHOW_RULES

    async def choose_category(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Show category selection options."""
        query = update.callback_query
        await query.answer()

        # Reset selected subcategories when choosing a new category
        context.user_data["selected_subcategories"] = []

        # Create buttons for each category
        keyboard = []
        for category_id, category in self.config.CATEGORIES.items():
            keyboard.append(
                [InlineKeyboardButton(category.name, callback_data=f"{self.callbacks.CATEGORY_PREFIX}{category_id}")])

        reply_markup = InlineKeyboardMarkup(keyboard)

        # Delete previous message and send a new one
        await query.delete_message()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=self.messages.CATEGORY_SELECTION_MESSAGE,
            reply_markup=reply_markup
        )

        return CHOOSE_CATEGORY

    async def show_subcategories(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Show subcategories for the selected category."""
        query = update.callback_query
        await query.answer()

        # Extract selected category from callback data
        if query.data.startswith(self.callbacks.CATEGORY_PREFIX):
            selected_category_id = query.data[len(self.callbacks.CATEGORY_PREFIX):]
            # Reset selected subcategories when choosing a new category
            context.user_data["selected_subcategories"] = []
        else:
            # When returning from viewing selections
            selected_category_id = context.user_data.get("selected_category")
        
        category = self.config.CATEGORIES.get(selected_category_id)
        
        # Store the selected category in user data
        context.user_data["selected_category"] = selected_category_id

        # Build message with subcategories and descriptions
        message_parts = [self.messages.SUBCATEGORY_SELECTION_MESSAGE.format(category_name=category.name)]
        
        # Create buttons for each subcategory
        keyboard = []
        if category and category.subcategories:
            selected_subcategories = context.user_data.get("selected_subcategories", [])
            
            for subcategory_id, subcategory in category.subcategories.items():
                # Add check mark if subcategory is selected
                prefix = "✅ " if subcategory_id in selected_subcategories else ""
                button_text = f"{prefix}{subcategory.emoji} {subcategory.name}" if subcategory.emoji else f"{prefix}{subcategory.name}"
                
                keyboard.append([
                    InlineKeyboardButton(
                        button_text, 
                        callback_data=f"{self.callbacks.SUBCATEGORY_PREFIX}{subcategory_id}"
                    )
                ])
                
                # Add description to message
                message_parts.append(f"\n{subcategory.emoji} *{subcategory.name}*\n{subcategory.description}")
        
        # Add "Start Game" button if there are any subcategories selected
        if context.user_data.get("selected_subcategories", []):
            keyboard.append([
                InlineKeyboardButton(
                    self.buttons.START_GAME_BUTTON,
                    callback_data=self.callbacks.START_GAME
                )
            ])
        
        # Add back button
        keyboard.append([
            InlineKeyboardButton(
                self.buttons.BACK_TO_CATEGORIES_BUTTON, 
                callback_data=self.callbacks.BACK_TO_CATEGORIES
            )
        ])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        message_text = "\n".join(message_parts)

        # Delete previous message and send a new one with subcategories
        await query.delete_message()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message_text,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

        return CHOOSE_SUBCATEGORY

    async def subcategory_selected(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle subcategory selection."""
        query = update.callback_query
        await query.answer()

        # Extract selected subcategory from callback data - fixed to handle underscores in IDs
        selected_subcategory_id = query.data[len(self.callbacks.SUBCATEGORY_PREFIX):]
        selected_category_id = context.user_data.get("selected_category")
        
        if not selected_category_id:
            logger.error("No selected category found in user_data")
            await query.edit_message_text("An error occurred. Please use /start to begin again.")
            return ConversationHandler.END
            
        category = self.config.CATEGORIES.get(selected_category_id)
        if not category:
            logger.error(f"Category {selected_category_id} not found")
            await query.edit_message_text("An error occurred. Please use /start to begin again.")
            return ConversationHandler.END
            
        subcategory = category.subcategories.get(selected_subcategory_id)
        if not subcategory:
            logger.error(f"Subcategory {selected_subcategory_id} not found in category {selected_category_id}")
            await query.edit_message_text("An error occurred. Please use /start to begin again.")
            return ConversationHandler.END

        # Toggle selection of the subcategory
        selected_subcategories = context.user_data.get("selected_subcategories", [])
        
        if selected_subcategory_id in selected_subcategories:
            selected_subcategories.remove(selected_subcategory_id)
        else:
            selected_subcategories.append(selected_subcategory_id)
            
        context.user_data["selected_subcategories"] = selected_subcategories
        
        # Display subcategory selection message
        message_text = self.messages.SUBCATEGORY_TOGGLE_MESSAGE.format(
            subcategory_name=subcategory.name,
            status="selected" if selected_subcategory_id in selected_subcategories else "deselected"
        )
        
        await query.answer(message_text, show_alert=True)
        
        # Return to the subcategories screen with updated selections
        return await self.show_subcategories(update, context)

    async def view_selected_subcategories(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Show descriptions of all selected subcategories."""
        query = update.callback_query
        await query.answer()
        
        selected_category_id = context.user_data.get("selected_category")
        selected_subcategories = context.user_data.get("selected_subcategories", [])
        
        category = self.config.CATEGORIES.get(selected_category_id)
        
        if not selected_subcategories:
            await query.answer("No subcategories selected", show_alert=True)
            return CHOOSE_SUBCATEGORY
            
        # Create a message with all selected subcategory descriptions
        message_parts = [self.messages.SELECTIONS_HEADER.format(category_name=category.name)]
        
        for subcategory_id in selected_subcategories:
            subcategory = category.subcategories.get(subcategory_id)
            if subcategory:
                message_parts.append(f"{subcategory.emoji} *{subcategory.name}*\n{subcategory.description}\n")
        
        message_text = "\n\n".join(message_parts)
        
        # Create buttons to go back
        keyboard = [
            [InlineKeyboardButton(
                self.buttons.BACK_TO_SUBCATEGORIES_BUTTON, 
                callback_data=self.callbacks.BACK_TO_SUBCATEGORIES
            )],
            [InlineKeyboardButton(
                self.buttons.BACK_TO_CATEGORIES_BUTTON, 
                callback_data=self.callbacks.BACK_TO_CATEGORIES
            )]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Delete previous message and send the new one
        await query.delete_message()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message_text,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
        
        return VIEW_SUBCATEGORIES

    async def start_game(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Start the game with questions from selected subcategories."""
        query = update.callback_query
        await query.answer()
        
        selected_category_id = context.user_data.get("selected_category")
        selected_subcategories = context.user_data.get("selected_subcategories", [])
        
        if not selected_subcategories:
            await query.answer("Пожалуйста, выберите хотя бы одну тему", show_alert=True)
            return CHOOSE_SUBCATEGORY
        
        # Get questions for selected subcategories
        questions = get_questions_for_subcategories(selected_category_id, selected_subcategories)
        
        if not questions:
            await query.answer("Нет вопросов для выбранных тем", show_alert=True)
            return CHOOSE_SUBCATEGORY
        
        # Shuffle questions for a random order
        random.shuffle(questions)
        
        # Store questions and current question index in user data
        context.user_data["questions"] = questions
        context.user_data["current_question_index"] = 0
        
        # Show the first question
        return await self.show_question(update, context)
    
    async def show_question(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Display the current question to the user."""
        query = update.callback_query
        
        questions = context.user_data.get("questions", [])
        current_index = context.user_data.get("current_question_index", 0)
        
        if not questions:
            await query.edit_message_text("Произошла ошибка. Пожалуйста, используйте /start для начала заново.")
            return ConversationHandler.END
        
        # Get the current question
        current_question = questions[current_index]
        
        # Get the subcategory information
        selected_category_id = context.user_data.get("selected_category")
        category = self.config.CATEGORIES.get(selected_category_id)
        subcategory = category.subcategories.get(current_question.subcategory_id)
        subcategory_name = subcategory.name + " " + subcategory.emoji if subcategory else "Неизвестная тема"
        
        # Create keyboard with navigation buttons
        keyboard = []
        
        # Add Previous button if not at the first question
        if current_index > 0:
            keyboard.append([
                InlineKeyboardButton(
                    self.buttons.PREVIOUS_QUESTION_BUTTON,
                    callback_data=self.callbacks.PREVIOUS_QUESTION
                )
            ])
        
        # Add Next button if not at the last question
        if current_index < len(questions) - 1:
            next_button = InlineKeyboardButton(
                self.buttons.NEXT_QUESTION_BUTTON,
                callback_data=self.callbacks.NEXT_QUESTION
            )
            if current_index > 0:
                # If we have both Previous and Next buttons, put them in one row
                keyboard[-1].append(next_button)
            else:
                keyboard.append([next_button])
        
        # Add Back to categories button
        keyboard.append([
            InlineKeyboardButton(
                self.buttons.BACK_TO_CATEGORIES_BUTTON,
                callback_data=self.callbacks.BACK_TO_CATEGORIES
            )
        ])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Format the question message
        message_text = self.messages.QUESTION_MESSAGE.format(
            current_num=current_index + 1,
            total=len(questions),
            subcategory_name=subcategory_name,
            question_text=current_question.text
        )
        
        # Delete previous message and send the new one with question
        await query.delete_message()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message_text,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
        
        return PLAY_GAME
    
    async def next_question(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Show the next question."""
        query = update.callback_query
        await query.answer()
        
        questions = context.user_data.get("questions", [])
        current_index = context.user_data.get("current_question_index", 0)
        
        if current_index < len(questions) - 1:
            context.user_data["current_question_index"] = current_index + 1
            return await self.show_question(update, context)
        else:
            # If we're at the last question, show completion message
            await query.edit_message_text(
                text=self.messages.GAME_COMPLETED_MESSAGE,
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        self.buttons.BACK_TO_CATEGORIES_BUTTON,
                        callback_data=self.callbacks.BACK_TO_CATEGORIES
                    )
                ]])
            )
            return PLAY_GAME
    
    async def previous_question(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Show the previous question."""
        query = update.callback_query
        await query.answer()
        
        current_index = context.user_data.get("current_question_index", 0)
        
        if current_index > 0:
            context.user_data["current_question_index"] = current_index - 1
            return await self.show_question(update, context)
        else:
            # If we're at the first question, stay there
            return await self.show_question(update, context)

    async def category_selected(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle category selection."""
        query = update.callback_query
        await query.answer()

        # Extract selected category from callback data
        selected_category_id = query.data[len(self.callbacks.CATEGORY_PREFIX):]
        category = self.config.CATEGORIES.get(selected_category_id)

        # Delete previous message and send final message
        await query.delete_message()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=self.messages.CATEGORY_SELECTED_MESSAGE.format(category_name=category.name)
        )

        # Store the selected category in user data
        context.user_data["selected_category"] = selected_category_id

        return ConversationHandler.END

    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Cancel conversation."""
        # Handle both direct command and callback query
        if update.callback_query:
            query = update.callback_query
            await query.answer()
            await query.edit_message_text(self.messages.CONVERSATION_END_MESSAGE)
        else:
            await update.message.reply_text(self.messages.CONVERSATION_END_MESSAGE)

        return ConversationHandler.END

    def run(self):
        """Start the bot."""
        logger.info("Starting bot")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)


def main():
    """Main function to run the bot"""
    bot = ToKnowBot(TELEGRAM_TOKEN)
    bot.run()


if __name__ == "__main__":
    main()