import os
import logging
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

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define conversation states
START, SHOW_RULES, CHOOSE_CATEGORY = range(3)


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
                        self.category_selected,
                        pattern=f"^{self.callbacks.CATEGORY_PREFIX}"
                    )
                ],
            },
            fallbacks=[CommandHandler("cancel", self.cancel)],
        )

        self.application.add_handler(conv_handler)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Send welcome message and prompt user to continue."""
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

    async def category_selected(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle category selection."""
        query = update.callback_query
        await query.answer()

        # Extract selected category from callback data
        selected_category_id = query.data.split("_")[1]
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