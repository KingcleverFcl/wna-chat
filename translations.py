translations = {
    "main_menu": {
        "ru": "Главное меню",
        "en": "Main menu",
        "zh": "主菜单",
        "es": "Menú principal"
    },
    "settings": {
        "ru": "Настройки",
        "en": "Settings",
        "zh": "设置",
        "es": "Configuraciones"
    },
    "search": {
        "ru": "Поиск",
        "en": "Search",
        "zh": "搜索",
        "es": "Buscar"
    },
    "blacklist": {
        "ru": "Черный список",
        "en": "Blacklist",
        "zh": "黑名单",
        "es": "Lista negra"
    },
    "private_messages": {
        "ru": "Личные сообщения",
        "en": "Private messages",
        "zh": "私信",
        "es": "Mensajes privados"
    },
    "generate_code": {
        "ru": "Сгенерировать код",
        "en": "Generate code",
        "zh": "生成代码",
        "es": "Generar código"
    },
    "change_nickname": {
        "ru": "Смена ника",
        "en": "Change nickname",
        "zh": "更改昵称",
        "es": "Cambiar apodo"
    },
    "change_language": {
        "ru": "Смена языка",
        "en": "Change language",
        "zh": "更改语言",
        "es": "Cambiar idioma"
    },
    "back": {
        "ru": "⬅ Назад",
        "en": "⬅ Back",
        "zh": "⬅ 返回",
        "es": "⬅ Atrás"
    }
}

def get_text(key: str, lang: str = "en") -> str:
    return translations.get(key, {}).get(lang, key)
