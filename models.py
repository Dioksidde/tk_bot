from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class CategoryModel:
    id: str
    name: str
    description: Optional[str] = None


@dataclass
class Messages:
    # Welcome message shown on /start
    WELCOME_MESSAGE: str = (
        "Привет!\n\n"
        "Перед тобой игра, которая помогает людям по-настоящему узнать друг друга. "
        "Не поверхностно – а глубоко, честно, по-настоящему.\n\n"
        "Она подойдёт тем, кто хо-чет стать ближе, почувствовать рядом живого человека, "
        "услышать его – и быть услышанным.\n\n"
        "Это не совсем игра в привычном смысле. Это помощник. Повод для разговора, "
        "который, возможно, откроет в тебе или в другом то, на что раньше не хватало слов, "
        "времени или смелости.\n\n"
        "С ней ты можешь заново взглянуть на тех, кого знаешь сто лет – или мягко начать "
        "разговор с тем, кто был для тебя совсем незнаком."
    )

    # Rules message shown after clicking "Начать"
    RULES_MESSAGE: str = (
        "Отвечай так, как тебе комфортно. Если вопрос покажется странным, скучным или "
        "не в тему – просто пропусти его. Здесь никто не торопит и не оценивает.\n\n"
        "Игра создана для живого общения. В неё можно играть и онлайн, но если есть "
        "возможность – лучше встретиться вживую. Так тепло чувствуется ближе.\n\n"
        "Здесь нет победителей. Но если после разговора вы почувствуете, что стали "
        "ближе – значит, это уже победа.\n\n"
        "И главное – будь честен. С собой и с другим. Это не всегда просто, но именно "
        "в этом рождаются настоящие разговоры."
    )

    # Category selection prompt
    CATEGORY_SELECTION_MESSAGE: str = "Выберите категорию:"

    # Message after category selection
    CATEGORY_SELECTED_MESSAGE: str = (
        "Вы выбрали категорию: {category_name}\n\n"
        "Здесь будут появляться вопросы для обсуждения.\n"
        "(Функционал вопросов будет добавлен в следующем обновлении)"
    )

    # Conversation end message
    CONVERSATION_END_MESSAGE: str = "Беседа завершена. Чтобы начать заново, используйте /start"


@dataclass
class ButtonLabels:
    START_BUTTON: str = "Начать"
    CHOOSE_CATEGORY_BUTTON: str = "Выбрать категорию"


@dataclass
class CallbackData:
    START: str = "start"
    CHOOSE_CATEGORY: str = "choose_category"
    CATEGORY_PREFIX: str = "category_"


@dataclass
class AppConfig:
    CATEGORIES: Dict[str, CategoryModel] = None

    def __post_init__(self):
        self.CATEGORIES = {
            "strangers": CategoryModel(id="strangers", name="Незнакомцы"),
            "acquaintances": CategoryModel(id="acquaintances", name="Приятели"),
            "friends": CategoryModel(id="friends", name="Друзья"),
            "lovers": CategoryModel(id="lovers", name="Влюбленные")
        }
