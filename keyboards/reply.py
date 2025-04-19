from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню
main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Поиск")],
        [KeyboardButton(text="Черный список")],
        [KeyboardButton(text="Настройки")],
        [KeyboardButton(text="Личные сообщения")],
        [KeyboardButton(text="Сгенерировать код")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие из меню"
)

# Меню настроек
settings_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Смена ника")],
        [KeyboardButton(text="Смена языка")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Настройки"
)

# Меню смены языка
language_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Русский")],
        [KeyboardButton(text="Английский")],
        [KeyboardButton(text="中文")],
        [KeyboardButton(text="Español")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите язык"
)
