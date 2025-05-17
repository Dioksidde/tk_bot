from typing import Dict, List
from models import QuestionModel

# Questions for each subcategory
QUESTIONS: Dict[str, Dict[str, List[QuestionModel]]] = {
    "strangers": {
        "intro": [
            QuestionModel(id="intro_1", text="Как ты обычно проводишь выходные?", subcategory_id="intro", category_id="strangers"),
            QuestionModel(id="intro_2", text="Есть ли у тебя любимое место в городе?", subcategory_id="intro", category_id="strangers"),
            QuestionModel(id="intro_3", text="Какую музыку ты слушал(а) сегодня?", subcategory_id="intro", category_id="strangers"),
            QuestionModel(id="intro_4", text="Какой фильм или сериал ты недавно посмотрел(а)?", subcategory_id="intro", category_id="strangers"),
            QuestionModel(id="intro_5", text="Какой напиток ты предпочитаешь утром: кофе, чай или что-то другое?", subcategory_id="intro", category_id="strangers"),
        ],
        "world": [
            QuestionModel(id="world_1", text="Что тебе больше по душе — гулять пешком, ехать или просто никуда не спешить?", subcategory_id="world", category_id="strangers"),
            QuestionModel(id="world_2", text="Какие у тебя есть утренние или вечерние привычки?", subcategory_id="world", category_id="strangers"),
            QuestionModel(id="world_3", text="Какой сезон тебе больше всего нравится и почему?", subcategory_id="world", category_id="strangers"),
            QuestionModel(id="world_4", text="Как ты обычно проводишь свободное время?", subcategory_id="world", category_id="strangers"),
            QuestionModel(id="world_5", text="Ты больше любишь активный или спокойный отдых?", subcategory_id="world", category_id="strangers"),
        ],
        "memory": [
            QuestionModel(id="memory_1", text="Какое блюдо напоминает тебе о детстве?", subcategory_id="memory", category_id="strangers"),
            QuestionModel(id="memory_2", text="Есть ли запах, который вызывает у тебя приятные воспоминания?", subcategory_id="memory", category_id="strangers"),
            QuestionModel(id="memory_3", text="Какой звук ассоциируется у тебя с летом?", subcategory_id="memory", category_id="strangers"),
            QuestionModel(id="memory_4", text="Какой десерт ты любишь больше всего?", subcategory_id="memory", category_id="strangers"),
            QuestionModel(id="memory_5", text="Где ты был(а) в последний раз, и тебе не хотелось уезжать?", subcategory_id="memory", category_id="strangers"),
            QuestionModel(id="memory_6", text="Какое место тебе хочется иногда мысленно возвращать?", subcategory_id="memory", category_id="strangers"),
        ],
        "if": [
            QuestionModel(id="if_1", text="Представь, что ты можешь побывать в любой стране. Куда бы ты поехал(а) в первую очередь?", subcategory_id="if", category_id="strangers"),
            QuestionModel(id="if_2", text="Какой язык тебе хотелось бы знать, будто ты с ним родился(ась)?", subcategory_id="if", category_id="strangers"),
            QuestionModel(id="if_3", text="Кто из персонажей фильма или книги тебе близок настолько, что ты мог(ла) бы пожить его жизнью?", subcategory_id="if", category_id="strangers"),
            QuestionModel(id="if_4", text="Если у тебя появилась суперспособность на один день — что бы ты с ней сделал(а)?", subcategory_id="if", category_id="strangers"),
            QuestionModel(id="if_5", text="В какое время тебе интересно было бы заглянуть — в прошлое или в будущее?", subcategory_id="if", category_id="strangers"),
        ],
        "life": [
            QuestionModel(id="life_1", text="Где ты знакомился с новыми людьми последнее время?", subcategory_id="life", category_id="strangers"),
            QuestionModel(id="life_2", text="Какую традицию ты соблюдаешь каждый год?", subcategory_id="life", category_id="strangers"),
            QuestionModel(id="life_3", text="Какой твой любимый праздник? Почему?", subcategory_id="life", category_id="strangers"),
            QuestionModel(id="life_4", text="Какую историю ты больше всего любишь рассказывать новым людям?", subcategory_id="life", category_id="strangers"),
            QuestionModel(id="life_5", text="Что тебе обычно помогает начать разговор с незнакомцем?", subcategory_id="life", category_id="strangers"),
            QuestionModel(id="life_6", text="Ты больше любишь слушать истории или рассказывать?", subcategory_id="life", category_id="strangers"),
        ],
        "joy": [
            QuestionModel(id="joy_1", text="Что приносит тебе радость в повседневной жизни?", subcategory_id="joy", category_id="strangers"),
            QuestionModel(id="joy_2", text="Что ты любишь делать, когда никто не мешает?", subcategory_id="joy", category_id="strangers"),
            QuestionModel(id="joy_3", text="Какой момент дня ты любишь больше всего?", subcategory_id="joy", category_id="strangers"),
            QuestionModel(id="joy_4", text="Что ты обычно делаешь, чтобы поднять себе настроение?", subcategory_id="joy", category_id="strangers"),
            QuestionModel(id="joy_5", text="Что тебя радует, даже если день не задался?", subcategory_id="joy", category_id="strangers"),
        ],
    },
    "acquaintances": {
        "about_you": [
            QuestionModel(id="about_you_1", text="Какое занятие всегда улучшает твоё настроение?", subcategory_id="about_you", category_id="acquaintances"),
            QuestionModel(id="about_you_2", text="Чем ты любишь заниматься в свободное время?", subcategory_id="about_you", category_id="acquaintances"),
            QuestionModel(id="about_you_3", text="Ты скорее экстраверт или интроверт?", subcategory_id="about_you", category_id="acquaintances"),
            QuestionModel(id="about_you_4", text="Какую черту в людях ты ценишь больше всего?", subcategory_id="about_you", category_id="acquaintances"),
            QuestionModel(id="about_you_5", text="Что в твоём характере становится заметно, когда тебя узнаешь получше?", subcategory_id="about_you", category_id="acquaintances"),
        ],
        "rituals": [
            QuestionModel(id="rituals_1", text="Что ты любишь делать с утра, чтобы день начался хорошо?", subcategory_id="rituals", category_id="acquaintances"),
            QuestionModel(id="rituals_2", text="Есть ли у тебя привычка, без которой день какой-то не тот?", subcategory_id="rituals", category_id="acquaintances"),
            QuestionModel(id="rituals_3", text="Что ты обычно делаешь, когда хочется перезагрузиться?", subcategory_id="rituals", category_id="acquaintances"),
            QuestionModel(id="rituals_4", text="Как ты проводишь время, когда остаёшься один?", subcategory_id="rituals", category_id="acquaintances"),
            QuestionModel(id="rituals_5", text="Есть ли у тебя что-то вроде 'личного ритуала' — пусть даже странного?", subcategory_id="rituals", category_id="acquaintances"),
        ],
        "important": [
            QuestionModel(id="important_1", text="Что в людях тебя сразу располагает к общению?", subcategory_id="important", category_id="acquaintances"),
            QuestionModel(id="important_2", text="Когда разговор становится для тебя реально интересным?", subcategory_id="important", category_id="acquaintances"),
            QuestionModel(id="important_3", text="В какой момент ты понимаешь, что с человеком можно быть собой?", subcategory_id="important", category_id="acquaintances"),
            QuestionModel(id="important_4", text="Бывало ли, что ты чего-то хотел(а) в разговоре, но не сказал(а)?", subcategory_id="important", category_id="acquaintances"),
            QuestionModel(id="important_5", text="Что в общении для тебя точно — “Нет, спасибо”?", subcategory_id="important", category_id="acquaintances"),
        ],
        "past": [
            QuestionModel(id="past_1", text="Какой случай из твоей жизни ты любишь пересказывать?", subcategory_id="past", category_id="acquaintances"),
            QuestionModel(id="past_2", text="Что ты когда-то сделал(а) спонтанно — и это запомнилось надолго?", subcategory_id="past", category_id="acquaintances"),
            QuestionModel(id="past_3", text="Был момент, когда всё пошло не по плану, но вышло круто?", subcategory_id="past", category_id="acquaintances"),
            QuestionModel(id="past_4", text="Какое воспоминание вызывает у тебя улыбку каждый раз?", subcategory_id="past", category_id="acquaintances"),
            QuestionModel(id="past_5", text="Что ты пробовал(а) однажды — и теперь бы не повторил(а)?", subcategory_id="past", category_id="acquaintances"),
        ],
        "others": [
            QuestionModel(id="others_1", text="На что в людях ты обращаешь внимание в первую очередь?", subcategory_id="others", category_id="acquaintances"),
            QuestionModel(id="others_2", text="Есть ли что-то в людях, что тебе сложно принять, но ты стараешься понять?", subcategory_id="others", category_id="acquaintances"),
            QuestionModel(id="others_3", text="Какие качества в человеке тебя реально восхищают?", subcategory_id="others", category_id="acquaintances"),
            QuestionModel(id="others_4", text="С кем тебе обычно проще — с теми, кто похож на тебя, или наоборот?", subcategory_id="others", category_id="acquaintances"),
            QuestionModel(id="others_5", text="Что люди иногда делают в общении, и это тебе не нравится?", subcategory_id="others", category_id="acquaintances"),
        ],
        "joy": [
            QuestionModel(id="joy_6", text="Что ты всегда с удовольствием готов(а) делать, даже если устал(а)?", subcategory_id="joy", category_id="acquaintances"),
            QuestionModel(id="joy_7", text="Есть ли у тебя любимая мелочь, которая радует больше, чем должна?", subcategory_id="joy", category_id="acquaintances"),
            QuestionModel(id="joy_8", text="Что из недавнего подняло тебе настроение?", subcategory_id="joy", category_id="acquaintances"),
            QuestionModel(id="joy_9", text="Как ты обычно проводишь день, когда он полностью твой?", subcategory_id="joy", category_id="acquaintances"),
            QuestionModel(id="joy_10", text="Что бы ты делал(а) каждый день, если бы не надо было работать?", subcategory_id="joy", category_id="acquaintances"),
        ],
    },
    "friends": {
        "base": [
            QuestionModel(id="base_1", text="Что в тебе работает стабильно, даже когда всё летит к чертям?", subcategory_id="base", category_id="friends"),
            QuestionModel(id="base_2", text="Есть ли в тебе черта, которую ты почти не показываешь, но она тебе помогает?", subcategory_id="base", category_id="friends"),
            QuestionModel(id="base_3", text="Что в тебе сильное, но не всегда видно со стороны?", subcategory_id="base", category_id="friends"),
            QuestionModel(id="base_4", text="Ты умеешь что-то, что другие считают сложным, а тебе просто?", subcategory_id="base", category_id="friends"),
            QuestionModel(id="base_5", text="В чём ты себе реально доверяешь?", subcategory_id="base", category_id="friends"),
        ],
        "boundaries": [
            QuestionModel(id="boundaries_1", text="Что тебе точно не ок — даже если все говорят «да нормально»?", subcategory_id="boundaries", category_id="friends"),
            QuestionModel(id="boundaries_2", text="Тебе легко говорить «нет» — или с этим бывает непросто?", subcategory_id="boundaries", category_id="friends"),
            QuestionModel(id="boundaries_3", text="Что ты раньше терпел(а), а теперь больше не готов(а)?", subcategory_id="boundaries", category_id="friends"),
            QuestionModel(id="boundaries_4", text="Бывает, что сдерживаешься в моменте, а потом злишься?", subcategory_id="boundaries", category_id="friends"),
            QuestionModel(id="boundaries_5", text="Бывает, что человек вроде всё делает по-доброму, но тебе уже некомфортно?", subcategory_id="boundaries", category_id="friends"),
        ],
        "voice": [
            QuestionModel(id="voice_1", text="О чём ты обычно думаешь, когда остаёшься один?", subcategory_id="voice", category_id="friends"),
            QuestionModel(id="voice_2", text="Бывает, что ты сам(а) себя подбадриваешь? Как?", subcategory_id="voice", category_id="friends"),
            QuestionModel(id="voice_3", text="Какие мысли у тебя чаще всего крутятся перед сном?", subcategory_id="voice", category_id="friends"),
            QuestionModel(id="voice_4", text="Когда у тебя внутри появляются сомнения — что ты обычно с ними делаешь?", subcategory_id="voice", category_id="friends"),
            QuestionModel(id="voice_5", text="Когда у тебя появляется идея — как ты обычно к ней относишься вначале?", subcategory_id="voice", category_id="friends"),
        ],
        "traces": [
            QuestionModel(id="traces_1", text="Есть ли человек, которого ты редко вспоминаешь, но он на тебя повлиял?", subcategory_id="traces", category_id="friends"),
            QuestionModel(id="traces_2", text="Бывало, что кто-то сказал что-то простое — а ты запомнил(а) на годы?", subcategory_id="traces", category_id="friends"),
            QuestionModel(id="traces_3", text="Был ли человек, который повлиял на тебя, даже не осознав этого?", subcategory_id="traces", category_id="friends"),
            QuestionModel(id="traces_4", text="Что ты когда-то перенял(а) от кого-то — и оно так и осталось с тобой?", subcategory_id="traces", category_id="friends"),
            QuestionModel(id="traces_5", text="Бывают ли у тебя внутренние разговоры с кем-то, кого уже нет рядом?", subcategory_id="traces", category_id="friends"),
        ],
        "drama": [
            QuestionModel(id="drama_1", text="Какой неловкий момент ты до сих пор вспоминаешь с улыбкой?", subcategory_id="drama", category_id="friends"),
            QuestionModel(id="drama_2", text="Была ли у тебя ситуация, когда всё пошло не по плану, но теперь это весёлый рассказ?", subcategory_id="drama", category_id="friends"),
            QuestionModel(id="drama_3", text="Какую самую забавную отговорку ты придумал(а) — и она сработала?", subcategory_id="drama", category_id="friends"),
            QuestionModel(id="drama_4", text="Что из твоего прошлого ты бы не повторил(а), но рад(а), что это случилось?", subcategory_id="drama", category_id="friends"),
            QuestionModel(id="drama_5", text="Какой фейл ты точно не забудешь — но уже можешь про него шутить?", subcategory_id="drama", category_id="friends"),
        ],
        "real": [
            QuestionModel(id="real_1", text="Когда ты чувствуешь: вот сейчас — это реально ты?", subcategory_id="real", category_id="friends"),
            QuestionModel(id="real_2", text="Что помогает тебе возвращаться к себе, когда всё вокруг шумит?", subcategory_id="real", category_id="friends"),
            QuestionModel(id="real_3", text="В каких ситуациях ты ощущаешь внутреннюю опору?", subcategory_id="real", category_id="friends"),
            QuestionModel(id="real_4", text="Бывает, что ты делаешь что-то — и в этот момент будто всё на своих местах?", subcategory_id="real", category_id="friends"),
            QuestionModel(id="real_5", text="С кем или где ты чувствуешь, что не надо быть ‘каким-то’ — можно просто быть?", subcategory_id="real", category_id="friends"),
        ],
    },
    "lovers": {
        "secret": [
            QuestionModel(id="secret_1", text="Есть ли что-то, что я, возможно, не замечаю в тебе, а тебе бы хотелось, чтобы я знал(а)?", subcategory_id="secret", category_id="lovers"),
            QuestionModel(id="secret_2", text="Что ты хотел(а) бы разделить со мной — но пока держал(а) при себе?", subcategory_id="secret", category_id="lovers"),
            QuestionModel(id="secret_3", text="Какой твой маленький секрет ты мог(ла) бы доверить только мне?", subcategory_id="secret", category_id="lovers"),
            QuestionModel(id="secret_4", text="Когда я рядом, ты ведёшь себя иначе? Что меняется?", subcategory_id="secret", category_id="lovers"),
            QuestionModel(id="secret_5", text="Что ты чувствуешь, но пока не решался(ась) вслух это озвучить?", subcategory_id="secret", category_id="lovers"),
        ],
        "pain": [
            QuestionModel(id="pain_1", text="Бывает, что ты защищаешься, хотя на самом деле тебе просто страшно?", subcategory_id="pain", category_id="lovers"),
            QuestionModel(id="pain_2", text="Какая тема для тебя чувствительная, даже если ты не сразу это показываешь?", subcategory_id="pain", category_id="lovers"),
            QuestionModel(id="pain_3", text="Когда я рядом — тебе проще быть уязвимым(ой) или наоборот сложнее?", subcategory_id="pain", category_id="lovers"),
            QuestionModel(id="pain_4", text="Есть ли что-то в тебе, о чём раньше стеснялся(ась) говорить, а теперь можешь?", subcategory_id="pain", category_id="lovers"),
            QuestionModel(id="pain_5", text="Как бы ты хотел(а), чтобы я реагировал(а), когда тебе плохо?", subcategory_id="pain", category_id="lovers"),
        ],
        "together": [
            QuestionModel(id="together_1", text="Когда ты особенно остро чувствуешь: мы — это ‘мы’?", subcategory_id="together", category_id="lovers"),
            QuestionModel(id="together_2", text="Что ты замечаешь в себе, когда мы проводим много времени вместе?", subcategory_id="together", category_id="lovers"),
            QuestionModel(id="together_3", text="Есть ли что-то в наших встречах, к чему ты особенно привязан(а)?", subcategory_id="together", category_id="lovers"),
            QuestionModel(id="together_4", text="Что тебе особенно приятно в том, как я рядом с тобой?", subcategory_id="together", category_id="lovers"),
            QuestionModel(id="together_5", text="Когда мы рядом, тебе больше хочется говорить или молчать — и о чём чаще всего хочется говорить?", subcategory_id="together", category_id="lovers"),
        ],
        "future": [
            QuestionModel(id="future_1", text="Когда ты представляешь нас в будущем — что там видишь в первую очередь?", subcategory_id="future", category_id="lovers"),
            QuestionModel(id="future_2", text="Есть ли что-то, что тебе важно, чтобы мы сохранили между нами?", subcategory_id="future", category_id="lovers"),
            QuestionModel(id="future_3", text="Что бы тебе хотелось, чтобы мы попробовали вместе — когда будем к этому готовы?", subcategory_id="future", category_id="lovers"),
            QuestionModel(id="future_4", text="О чём ты иногда волнуешься, когда думаешь про ‘нас дальше’?", subcategory_id="future", category_id="lovers"),
            QuestionModel(id="future_5", text="Что ты в себе хочешь сохранить — даже если мы будем меняться?", subcategory_id="future", category_id="lovers"),
        ],
        "about_self": [
            QuestionModel(id="about_self_1", text="Что тебе особенно важно, чтобы я знал(а) о тебе — даже если это не всегда видно?", subcategory_id="about_self", category_id="lovers"),
            QuestionModel(id="about_self_2", text="Есть ли в тебе что-то, что ты часто не показываешь, хотя это часть тебя?", subcategory_id="about_self", category_id="lovers"),
            QuestionModel(id="about_self_3", text="Когда ты чувствуешь, что можешь быть собой — какой ты?", subcategory_id="about_self", category_id="lovers"),
            QuestionModel(id="about_self_4", text="Что тебе нравится в том, как ты любишь?", subcategory_id="about_self", category_id="lovers"),
            QuestionModel(id="about_self_5", text="Что тебе особенно приятно — получать или отдавать — но ты редко об этом говоришь?", subcategory_id="about_self", category_id="lovers"),
        ],
        "separate": [
            QuestionModel(id="separate_1", text="В чём мы с тобой совсем не похожи — и это даже приятно?", subcategory_id="separate", category_id="lovers"),
            QuestionModel(id="separate_2", text="Что тебя удивляет во мне, но при этом вызывает тепло?", subcategory_id="separate", category_id="lovers"),
            QuestionModel(id="separate_3", text="Есть ли что-то, в чём ты чувствуешь, что мы прям на одной волне?", subcategory_id="separate", category_id="lovers"),
            QuestionModel(id="separate_4", text="В чём мы можем не совпадать — и это не проблема?", subcategory_id="separate", category_id="lovers"),
            QuestionModel(id="separate_5", text="Что нас держит вместе, даже когда мы такие разные?", subcategory_id="separate", category_id="lovers"),
        ],
    },
}

def get_questions_for_subcategories(category_id: str, subcategory_ids: List[str]) -> List[QuestionModel]:
    """Returns a list of questions for the specified category and subcategories."""
    result: List[QuestionModel] = []
    category_questions = QUESTIONS.get(category_id, {})
    for subcategory_id in subcategory_ids:
        if subcategory_id in category_questions:
            result.extend(category_questions[subcategory_id])
    return result
