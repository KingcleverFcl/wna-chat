from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_menu_kb(lang: str) -> ReplyKeyboardMarkup:
    texts = {
        "en": ["Dialogs", "Search", "Settings", "Blacklist"],
        "ru": ["Диалоги", "Поиск", "Настройки", "Чёрный список"],
        "zh": ["对话", "搜索", "设置", "黑名单"],
        "es": ["Diálogos", "Buscar", "Ajustes", "Lista negra"]
    }
    buttons = [KeyboardButton(text=t) for t in texts.get(lang, texts["en"])]
    builder = ReplyKeyboardBuilder()
    for btn in buttons:
        builder.add(btn)
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def settings_menu_kb(lang: str) -> ReplyKeyboardMarkup:
    texts = {
        "en": ["Nickname", "Language", "Back"],
        "ru": ["Ник", "Язык", "Назад"],
        "zh": ["昵称", "语言", "返回"],
        "es": ["Apodo", "Idioma", "Atrás"]
    }
    buttons = [KeyboardButton(text=t) for t in texts.get(lang, texts["en"])]
    builder = ReplyKeyboardBuilder()
    for btn in buttons:
        builder.add(btn)
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def language_selection_kb() -> ReplyKeyboardMarkup:
    buttons = [
        "English", "Русский", "中文", "Español"
    ]
    builder = ReplyKeyboardBuilder()
    for btn in buttons:
        builder.add(KeyboardButton(text=btn))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def back_kb(lang: str) -> ReplyKeyboardMarkup:
    texts = {
        "en": "Back",
        "ru": "Назад",
        "zh": "返回",
        "es": "Atrás"
    }
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=texts.get(lang, "Back"))]],
        resize_keyboard=True
    )
