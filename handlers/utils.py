from database.models import get_user_language
from translations import get_text

def get_lang(user_id: int) -> str:
    """ Получить язык пользователя из базы данных """
    return get_user_language(user_id)
