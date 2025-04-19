messages = {
    "main_menu": {
        "ru": "🏠 Главное меню:",
        "en": "🏠 Main menu:",
        "es": "🏠 Menú principal:",
        "zh": "🏠 主菜单："
    },
    "settings_menu": {
        "ru": "⚙️ Настройки:",
        "en": "⚙️ Settings:",
        "es": "⚙️ Configuración:",
        "zh": "⚙️ 设置："
    },
    "change_nickname_prompt": {
        "ru": "📝 Введите новый никнейм:",
        "en": "📝 Enter a new nickname:",
        "es": "📝 Introduce un nuevo apodo:",
        "zh": "📝 输入新的昵称："
    },
    "nickname_taken": {
        "ru": "❌ Этот никнейм уже занят.",
        "en": "❌ This nickname is already taken.",
        "es": "❌ Este apodo ya está en uso.",
        "zh": "❌ 此昵称已被使用。"
    },
    "nickname_updated": {
        "ru": "✅ Никнейм успешно изменён.",
        "en": "✅ Nickname successfully updated.",
        "es": "✅ Apodo actualizado con éxito.",
        "zh": "✅ 昵称已成功更改。"
    },
    "change_language_prompt": {
        "ru": "🌐 Выберите язык:",
        "en": "🌐 Choose a language:",
        "es": "🌐 Elige un idioma:",
        "zh": "🌐 选择语言："
    },
    "language_changed": {
        "ru": "✅ Язык успешно изменён.",
        "en": "✅ Language successfully changed.",
        "es": "✅ Idioma cambiado con éxito.",
        "zh": "✅ 语言已成功更改。"
    }
}


def get_text(key: str, lang: str) -> str:
    return messages.get(key, {}).get(lang, "")
