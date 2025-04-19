from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from translations import get_text

def main_menu_keyboard(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=get_text("search", lang))],
        [KeyboardButton(text=get_text("blacklist", lang))],
        [KeyboardButton(text=get_text("settings", lang))],
        [KeyboardButton(text=get_text("private_messages", lang))],
        [KeyboardButton(text=get_text("generate_code", lang))]
    ], resize_keyboard=True)

def settings_menu_keyboard(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=get_text("change_nickname", lang))],
        [KeyboardButton(text=get_text("change_language", lang))],
        [KeyboardButton(text=get_text("back", lang))]
    ], resize_keyboard=True)

def language_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Русский")],
        [KeyboardButton(text="English")],
        [KeyboardButton(text="中文")],
        [KeyboardButton(text="Español")],
        [KeyboardButton(text="⬅ Назад")]
    ], resize_keyboard=True)
