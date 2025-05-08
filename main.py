import os
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, ConversationHandler

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

# Category buttons
CATEGORIES = {
    "strangers": "Незнакомцы",
    "acquaintances": "Приятели",
    "friends": "Друзья",
    "lovers": "Влюбленные"
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send welcome message and prompt user to continue."""
    keyboard = [
        [InlineKeyboardButton("Начать", callback_data="start")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет!\n\n"
        "Перед тобой игра, которая помогает людям по-настоящему узнать друг друга. "
        "Не поверхностно – а глубоко, честно, по-настоящему.\n\n"
        "Она подойдёт тем, кто хо-чет стать ближе, почувствовать рядом живого человека, "
        "услышать его – и быть услышанным.\n\n"
        "Это не совсем игра в привычном смысле. Это помощник. Повод для разговора, "
        "который, возможно, откроет в тебе или в другом то, на что раньше не хватало слов, "
        "времени или смелости.\n\n"
        "С ней ты можешь заново взглянуть на тех, кого знаешь сто лет – или мягко начать "
        "разговор с тем, кто был для тебя совсем незнаком.",
        reply_markup=reply_markup
    )

    return START


async def show_rules(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show the rules and prompt user to continue."""
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("Выбрать категорию", callback_data="choose_category")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        "Отвечай так, как тебе комфортно. Если вопрос покажется странным, скучным или "
        "не в тему – просто пропусти его. Здесь никто не торопит и не оценивает.\n\n"
        "Игра создана для живого общения. В неё можно играть и онлайн, но если есть "
        "возможность – лучше встретиться вживую. Так тепло чувствуется ближе.\n\n"
        "Здесь нет победителей. Но если после разговора вы почувствуете, что стали "
        "ближе – значит, это уже победа.\n\n"
        "И главное – будь честен. С собой и с другим. Это не всегда просто, но именно "
        "в этом рождаются настоящие разговоры.",
        reply_markup=reply_markup
    )

    return SHOW_RULES


async def choose_category(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show category selection options."""
    query = update.callback_query
    await query.answer()

    # Create buttons for each category
    keyboard = []
    for category_id, category_name in CATEGORIES.items():
        keyboard.append([InlineKeyboardButton(category_name, callback_data=f"category_{category_id}")])

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        "Выберите категорию:",
        reply_markup=reply_markup
    )

    return CHOOSE_CATEGORY


async def category_selected(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle category selection."""
    query = update.callback_query
    await query.answer()

    # Extract selected category from callback data
    selected_category = query.data.split("_")[1]
    category_name = CATEGORIES.get(selected_category, "Unknown")

    await query.edit_message_text(
        f"Вы выбрали категорию: {category_name}\n\n"
        "Здесь будут появляться вопросы для обсуждения.\n"
        "(Функционал вопросов будет добавлен в следующем обновлении)"
    )

    # Store the selected category in user data
    context.user_data["selected_category"] = selected_category

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel conversation."""
    query = update.callback_query
    await query.answer()

    await query.edit_message_text("Беседа завершена. Чтобы начать заново, используйте /start")

    return ConversationHandler.END


def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Set up conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START: [CallbackQueryHandler(show_rules, pattern="^start$")],
            SHOW_RULES: [CallbackQueryHandler(choose_category, pattern="^choose_category$")],
            CHOOSE_CATEGORY: [
                CallbackQueryHandler(
                    category_selected,
                    pattern="^category_"
                )
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Start the Bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()