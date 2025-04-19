from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def settings_menu_keyboard(lang: str) -> ReplyKeyboardMarkup:
    buttons = {
        "ru": ["Смена ника", "Смена языка", "Назад"],
        "en": ["Change Nickname", "Change Language", "Back"],
        "es": ["Cambiar apodo", "Cambiar idioma", "Atrás"],
        "zh": ["更改昵称", "更改语言", "返回"]
    }
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text)] for text in buttons.get(lang, buttons["en"])],
        resize_keyboard=True
    )

def language_selection_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("Русский")],
            [KeyboardButton("English")],
            [KeyboardButton("Español")],
            [KeyboardButton("中文")]
        ],
        resize_keyboard=True
    )
