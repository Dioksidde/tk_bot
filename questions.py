from typing import Dict, List
from models import QuestionModel

# Sample questions for each subcategory
QUESTIONS: Dict[str, List[QuestionModel]] = {
    # Strangers category
    "strangers": {
        "intro": [
            QuestionModel(
                id="intro_1",
                text="Если бы мы с тобой встретились год назад, чем бы ты тогда занимался?",
                subcategory_id="intro",
                category_id="strangers"
            ),
            QuestionModel(
                id="intro_2",
                text="Какой напиток лучше всего описывает твое настроение сейчас?",
                subcategory_id="intro",
                category_id="strangers"
            ),
            QuestionModel(
                id="intro_3",
                text="Что тебя удивило за последнюю неделю?",
                subcategory_id="intro",
                category_id="strangers"
            ),
        ],
        "world": [
            QuestionModel(
                id="world_1",
                text="Какое место в твоем городе ты считаешь особенным, но мало кто о нем знает?",
                subcategory_id="world",
                category_id="strangers"
            ),
            QuestionModel(
                id="world_2",
                text="Если бы ты мог отправиться в любую точку мира прямо сейчас, куда бы ты поехал?",
                subcategory_id="world",
                category_id="strangers"
            ),
        ],
        "memory": [
            QuestionModel(
                id="memory_1",
                text="Какой запах сразу переносит тебя в детство?",
                subcategory_id="memory",
                category_id="strangers"
            ),
            QuestionModel(
                id="memory_2",
                text="Какое блюдо вызывает у тебя самые теплые воспоминания?",
                subcategory_id="memory",
                category_id="strangers"
            ),
        ],
        "if": [
            QuestionModel(
                id="if_1",
                text="Если бы ты мог поговорить с любым историческим персонажем, кого бы ты выбрал?",
                subcategory_id="if",
                category_id="strangers"
            ),
            QuestionModel(
                id="if_2",
                text="Если бы ты мог обладать любым талантом в мире, что бы ты выбрал?",
                subcategory_id="if",
                category_id="strangers"
            ),
        ],
        "life": [
            QuestionModel(
                id="life_1",
                text="Какая история, которую ты слышал от другого человека, произвела на тебя сильное впечатление?",
                subcategory_id="life",
                category_id="strangers"
            ),
            QuestionModel(
                id="life_2",
                text="Что для тебя значит хорошо прожитый день?",
                subcategory_id="life",
                category_id="strangers"
            ),
        ],
        "joy": [
            QuestionModel(
                id="joy_1",
                text="Что из мелочей всегда поднимает тебе настроение?",
                subcategory_id="joy",
                category_id="strangers"
            ),
            QuestionModel(
                id="joy_2",
                text="Какую маленькую радость ты испытал недавно?",
                subcategory_id="joy",
                category_id="strangers"
            ),
        ],
    },
    
    # Acquaintances category
    "acquaintances": {
        "about_you": [
            QuestionModel(
                id="about_you_1",
                text="Какие три слова лучше всего описывают тебя?",
                subcategory_id="about_you",
                category_id="acquaintances"
            ),
            QuestionModel(
                id="about_you_2",
                text="Что о тебе мало кто знает, но ты не против рассказать?",
                subcategory_id="about_you",
                category_id="acquaintances"
            ),
        ],
        "rituals": [
            QuestionModel(
                id="rituals_1",
                text="Есть ли у тебя какой-то личный ритуал, который помогает тебе в сложные моменты?",
                subcategory_id="rituals",
                category_id="acquaintances"
            ),
            QuestionModel(
                id="rituals_2",
                text="Какие утренние привычки помогают тебе настроиться на день?",
                subcategory_id="rituals",
                category_id="acquaintances"
            ),
        ],
        "important": [
            QuestionModel(
                id="important_1",
                text="Что для тебя неприемлемо в отношениях с другими людьми?",
                subcategory_id="important",
                category_id="acquaintances"
            ),
            QuestionModel(
                id="important_2",
                text="Какие ценности для тебя важнее всего?",
                subcategory_id="important",
                category_id="acquaintances"
            ),
        ],
        "past": [
            QuestionModel(
                id="past_1",
                text="Какое решение из прошлого изменило твою жизнь значительно?",
                subcategory_id="past",
                category_id="acquaintances"
            ),
            QuestionModel(
                id="past_2",
                text="Какой период в твоей жизни ты вспоминаешь с особой теплотой?",
                subcategory_id="past",
                category_id="acquaintances"
            ),
        ],
        "others": [
            QuestionModel(
                id="others_1",
                text="Какие качества в людях ты ценишь больше всего?",
                subcategory_id="others",
                category_id="acquaintances"
            ),
            QuestionModel(
                id="others_2",
                text="Что в поведении других людей может вывести тебя из себя?",
                subcategory_id="others",
                category_id="acquaintances"
            ),
        ],
        "joy": [
            QuestionModel(
                id="joy_3",
                text="Что тебя по-настоящему радует в жизни?",
                subcategory_id="joy",
                category_id="acquaintances"
            ),
            QuestionModel(
                id="joy_4",
                text="Какое маленькое удовольствие ты никогда не пропускаешь?",
                subcategory_id="joy",
                category_id="acquaintances"
            ),
        ],
    },
    
    # Friends category
    "friends": {
        "base": [
            QuestionModel(
                id="base_1",
                text="Какой навык ты освоил, но редко используешь?",
                subcategory_id="base",
                category_id="friends"
            ),
            QuestionModel(
                id="base_2",
                text="За что тебя часто хвалят, но ты не считаешь это чем-то особенным?",
                subcategory_id="base",
                category_id="friends"
            ),
        ],
        "boundaries": [
            QuestionModel(
                id="boundaries_1",
                text="Когда ты чувствуешь, что твои личные границы нарушены?",
                subcategory_id="boundaries",
                category_id="friends"
            ),
            QuestionModel(
                id="boundaries_2",
                text="Как ты обычно реагируешь, когда кто-то пересекает твои границы?",
                subcategory_id="boundaries",
                category_id="friends"
            ),
        ],
        "voice": [
            QuestionModel(
                id="voice_1",
                text="О чем ты часто думаешь, но редко говоришь вслух?",
                subcategory_id="voice",
                category_id="friends"
            ),
            QuestionModel(
                id="voice_2",
                text="Что ты боишься признать самому себе?",
                subcategory_id="voice",
                category_id="friends"
            ),
        ],
        "traces": [
            QuestionModel(
                id="traces_1",
                text="Кто из людей оказал на тебя наибольшее влияние в жизни?",
                subcategory_id="traces",
                category_id="friends"
            ),
            QuestionModel(
                id="traces_2",
                text="Какой разговор изменил твой взгляд на мир?",
                subcategory_id="traces",
                category_id="friends"
            ),
        ],
        "drama": [
            QuestionModel(
                id="drama_1",
                text="Какой самый трудный период в жизни ты преодолел?",
                subcategory_id="drama",
                category_id="friends"
            ),
            QuestionModel(
                id="drama_2",
                text="Что заставляет тебя смеяться до слез?",
                subcategory_id="drama",
                category_id="friends"
            ),
        ],
        "real": [
            QuestionModel(
                id="real_1",
                text="В какие моменты ты чувствуешь себя по-настоящему живым?",
                subcategory_id="real",
                category_id="friends"
            ),
            QuestionModel(
                id="real_2",
                text="Когда ты в последний раз чувствовал себя полностью в гармонии с собой?",
                subcategory_id="real",
                category_id="friends"
            ),
        ],
    },
    
    # Lovers category
    "lovers": {
        "secret": [
            QuestionModel(
                id="secret_1",
                text="Что ты никогда никому не рассказывал, но хотел бы поделиться со мной?",
                subcategory_id="secret",
                category_id="lovers"
            ),
            QuestionModel(
                id="secret_2",
                text="Какой момент между нами ты хранишь как особенно ценный?",
                subcategory_id="secret",
                category_id="lovers"
            ),
        ],
        "pain": [
            QuestionModel(
                id="pain_1",
                text="Какое событие в прошлом до сих пор причиняет тебе боль?",
                subcategory_id="pain",
                category_id="lovers"
            ),
            QuestionModel(
                id="pain_2",
                text="Что для тебя самое трудное в отношениях?",
                subcategory_id="pain",
                category_id="lovers"
            ),
        ],
        "together": [
            QuestionModel(
                id="together_1",
                text="Какие моменты вместе делают тебя особенно счастливым?",
                subcategory_id="together",
                category_id="lovers"
            ),
            QuestionModel(
                id="together_2",
                text="Что ты больше всего ценишь в наших отношениях?",
                subcategory_id="together",
                category_id="lovers"
            ),
        ],
        "future": [
            QuestionModel(
                id="future_1",
                text="Как ты представляешь нашу жизнь через 5 лет?",
                subcategory_id="future",
                category_id="lovers"
            ),
            QuestionModel(
                id="future_2",
                text="Какие мечты ты хотел бы осуществить вместе со мной?",
                subcategory_id="future",
                category_id="lovers"
            ),
        ],
        "about_self": [
            QuestionModel(
                id="about_self_1",
                text="Что ты больше всего любишь в себе и почему?",
                subcategory_id="about_self",
                category_id="lovers"
            ),
            QuestionModel(
                id="about_self_2",
                text="В чем ты чувствуешь себя уязвимым и как я могу тебя поддержать?",
                subcategory_id="about_self",
                category_id="lovers"
            ),
        ],
        "separate": [
            QuestionModel(
                id="separate_1",
                text="Как ты находишь баланс между близостью и личным пространством?",
                subcategory_id="separate",
                category_id="lovers"
            ),
            QuestionModel(
                id="separate_2",
                text="Что ты делаешь, чтобы восстановить энергию, когда чувствуешь себя истощенным?",
                subcategory_id="separate",
                category_id="lovers"
            ),
        ],
    },
}

def get_questions_for_subcategories(category_id: str, subcategory_ids: List[str]) -> List[QuestionModel]:
    """
    Returns a list of questions for the specified category and subcategories.
    
    Args:
        category_id: The ID of the category
        subcategory_ids: A list of subcategory IDs
        
    Returns:
        A list of QuestionModel objects
    """
    result = []
    category_questions = QUESTIONS.get(category_id, {})
    
    for subcategory_id in subcategory_ids:
        if subcategory_id in category_questions:
            result.extend(category_questions[subcategory_id])
    
    return result 