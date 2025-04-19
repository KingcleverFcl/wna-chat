from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню
main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔍 Поиск")],
        [KeyboardButton(text="🚫 Черный список")],
        [KeyboardButton(text="⚙️ Настройки")],
        [KeyboardButton(text="✉️ Личные сообщения")],
        [KeyboardButton(text="🧾 Сгенерировать код")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие:"
)

# Меню настроек
settings_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Смена ника")],
        [KeyboardButton(text="🌐 Смена языка")],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Настройки профиля:"
)

# Языковая клавиатура
language_selection_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Русский 🇷🇺"), KeyboardButton(text="English 🇬🇧")],
        [KeyboardButton(text="中文 🇨🇳"), KeyboardButton(text="Español 🇪🇸")],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите язык:"
)

# Клавиатура при смене ника (только кнопка «Отмена»)
nickname_cancel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Введите новый ник:"
)

# Меню генерации кода
generate_code_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎰 Генерация Casino")],
        [KeyboardButton(text="🐱 Генерация Cat")],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите платформу:"
)
