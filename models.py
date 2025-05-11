from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class SubcategoryModel:
    id: str
    name: str
    description: str
    emoji: Optional[str] = None


@dataclass
class CategoryModel:
    id: str
    name: str
    description: Optional[str] = None
    subcategories: Optional[Dict[str, SubcategoryModel]] = None


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
    
    # Subcategory selection prompt
    SUBCATEGORY_SELECTION_MESSAGE: str = "Выбор категории: {category_name}"
    
    # Message for subcategory toggle
    SUBCATEGORY_TOGGLE_MESSAGE: str = "Категория '{subcategory_name}' {status}"
    
    # Header for selected subcategories view
    SELECTIONS_HEADER: str = "Выбранные темы из категории {category_name}:"
    
    # Message after subcategory selection
    SUBCATEGORY_SELECTED_MESSAGE: str = "{subcategory_description}"

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
    BACK_TO_CATEGORIES_BUTTON: str = "Назад к категориям"
    VIEW_SELECTIONS_BUTTON: str = "Посмотреть выбранные темы"
    BACK_TO_SUBCATEGORIES_BUTTON: str = "Назад к выбору тем"


@dataclass
class CallbackData:
    START: str = "start"
    CHOOSE_CATEGORY: str = "choose_category"
    CATEGORY_PREFIX: str = "category_"
    SUBCATEGORY_PREFIX: str = "subcategory_"
    BACK_TO_CATEGORIES: str = "back_to_categories"
    VIEW_SELECTIONS: str = "view_selections"
    BACK_TO_SUBCATEGORIES: str = "back_to_subcategories"


@dataclass
class AppConfig:
    CATEGORIES: Dict[str, CategoryModel] = None

    def __post_init__(self):
        # Define subcategories for "Незнакомцы"
        strangers_subcategories = {
            "intro": SubcategoryModel(
                id="intro",
                name="Для самого начала",
                description="Приятные, чтобы разговорить человека",
                emoji="💎"
            ),
            "world": SubcategoryModel(
                id="world",
                name="Ты и мир",
                description="О том, как человек ощущает себя в повседневности",
                emoji="🌎"
            ),
            "memory": SubcategoryModel(
                id="memory",
                name="Память на вкус",
                description="Милые воспоминания: запахи, еда, звуки и ощущения",
                emoji="🍕"
            ),
            "if": SubcategoryModel(
                id="if",
                name="Если бы...",
                description="Выбирай, что возможно всё — просто играем",
                emoji="🧠"
            ),
            "life": SubcategoryModel(
                id="life",
                name="О людях и жизни",
                description="Про человеческие истории, не слишком личные, но интересные",
                emoji="🏙️"
            ),
            "joy": SubcategoryModel(
                id="joy",
                name="Маленькие радости",
                description="О том, что делает человека собой, без драмы и пафоса",
                emoji="☘️"
            ),
        }
        
        # Define subcategories for "Приятели"
        acquaintances_subcategories = {
            "about_you": SubcategoryModel(
                id="about_you",
                name="Подробнее о тебе",
                description="Кто ты, если убрать всё лишнее?",
                emoji="😊"
            ),
            "rituals": SubcategoryModel(
                id="rituals",
                name="Твои ритуалы",
                description="То, что делает тебя собой – без всего того", 
                emoji="🥬"
            ),
            "important": SubcategoryModel(
                id="important",
                name="Мне важно...",
                description="Что для тебя «всё по-настоящему»?",
                emoji="🧶"
            ),
            "past": SubcategoryModel(
                id="past",
                name="Что было дальше?",
                description="Расскажи про себя – на как бывало",
                emoji="📽️"
            ),
            "others": SubcategoryModel(
                id="others",
                name="Ты и другие",
                description="Что тебя цепляет, бесит или вдохновляет в людях?",
                emoji="👥"
            ),
            "joy": SubcategoryModel(
                id="joy",
                name="О радостях жизни",
                description="Маленькие и большие удовольствия жизни",
                emoji="🧋"
            ),
        }
        
        # Define subcategories for "Друзья"
        friends_subcategories = {
            "base": SubcategoryModel(
                id="base",
                name="Это база",
                description="Что ты умеешь, но не эксплуатируешь никогда?",
                emoji="⚖️"
            ),
            "boundaries": SubcategoryModel(
                id="boundaries",
                name="Ты и границы",
                description="Где заканчивается твой космос и начинается мой хаос?",
                emoji="⛔"
            ),
            "voice": SubcategoryModel(
                id="voice",
                name="Голос внутри",
                description="О чём ты часто молчишь даже наедине с собой?",
                emoji="🗣️"
            ),
            "traces": SubcategoryModel(
                id="traces",
                name="Люди и следы",
                description="Кто оставил в тебе отпечаток – и почему?",
                emoji="👣"
            ),
            "drama": SubcategoryModel(
                id="drama",
                name="Драмы и комедии",
                description="Драмы большие и маленькие... И когда мы смеялись вместе.",
                emoji="🍿"
            ),
            "real": SubcategoryModel(
                id="real",
                name="По-настоящему",
                description="В каких моментах ты чувствуешь себя особенно «собой»?",
                emoji="🏵️"
            ),
        }
        
        # Define subcategories for "Влюбленные"
        lovers_subcategories = {
            "secret": SubcategoryModel(
                id="secret",
                name="Наш с тобой секрет",
                description="Про тайное, неудобное, стеснительное — дорогое",
                emoji="🔐"
            ),
            "pain": SubcategoryModel(
                id="pain",
                name="Места боли",
                description="О сломанном, уязвимом, стыдном — но оно не одиноко",
                emoji="💔"
            ),
            "together": SubcategoryModel(
                id="together",
                name="Когда мы рядом", 
                description="О том, как хорошо вдыхать на пару, твой запах и шаг твой",
                emoji="👫"
            ),
            "future": SubcategoryModel(
                id="future",
                name="Что дальше?",
                description="Про мечты, будущее, верность, взросление года",
                emoji="📷"
            ),
            "about_self": SubcategoryModel(
                id="about_self",
                name="О себе до конца",
                description="Где ты говоришь, что ты любишь все в тебе каждый раз?",
                emoji="💎"
            ),
            "separate": SubcategoryModel(
                id="separate",
                name="Вместе и отдельно",
                description="Про интимное, пространство, отдых и печали",
                emoji="📱"
            ),
        }

        self.CATEGORIES = {
            "strangers": CategoryModel(id="strangers", name="Незнакомцы", subcategories=strangers_subcategories),
            "acquaintances": CategoryModel(id="acquaintances", name="Приятели", subcategories=acquaintances_subcategories),
            "friends": CategoryModel(id="friends", name="Друзья", subcategories=friends_subcategories),
            "lovers": CategoryModel(id="lovers", name="Влюбленные", subcategories=lovers_subcategories)
        }
