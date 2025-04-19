from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.user_states import SettingsState
from keyboards.reply import settings_menu_kb, language_selection_kb, back_kb
from database.models import get_user_settings, update_nickname, update_language
from messages import MESSAGES

router = Router()


@router.message(F.text.lower() == "settings")
async def open_settings_menu(message: Message, state: FSMContext):
    user_id = message.from_user.id
    settings = await get_user_settings(user_id)
    lang = settings.language if settings else "en"

    await message.answer(
        MESSAGES[lang]["settings_menu"],
        reply_markup=settings_menu_kb(lang)
    )
    await state.set_state(SettingsState.menu)


@router.message(SettingsState.menu, F.text.lower().in_(["nickname", "ник", "昵称", "apodo"]))
async def change_nickname(message: Message, state: FSMContext):
    user_id = message.from_user.id
    settings = await get_user_settings(user_id)
    lang = settings.language if settings else "en"

    await message.answer(MESSAGES[lang]["ask_nickname"], reply_markup=back_kb(lang))
    await state.set_state(SettingsState.nickname)


@router.message(SettingsState.nickname)
async def save_nickname(message: Message, state: FSMContext):
    user_id = message.from_user.id
    nickname = message.text.strip()

    settings = await get_user_settings(user_id)
    lang = settings.language if settings else "en"

    if nickname.lower() == MESSAGES[lang]["back"].lower():
        await open_settings_menu(message, state)
        return

    if not (3 <= len(nickname) <= 20):
        await message.answer(MESSAGES[lang]["invalid_nickname"])
        return

    await update_nickname(user_id, nickname)
    await message.answer(MESSAGES[lang]["nickname_updated"])
    await open_settings_menu(message, state)


@router.message(SettingsState.menu, F.text.lower().in_(["language", "язык", "语言", "idioma"]))
async def select_language(message: Message, state: FSMContext):
    user_id = message.from_user.id
    settings = await get_user_settings(user_id)
    lang = settings.language if settings else "en"

    await message.answer(
        MESSAGES[lang]["choose_language"],
        reply_markup=language_selection_kb()
    )
    await state.set_state(SettingsState.language)


@router.message(SettingsState.language)
async def save_language(message: Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text.strip().lower()

    language_map = {
        "english": "en",
        "английский": "en",
        "英语": "en",
        "inglés": "en",
        "russian": "ru",
        "русский": "ru",
        "俄语": "ru",
        "ruso": "ru",
        "chinese": "zh",
        "китайский": "zh",
        "中文": "zh",
        "chino": "zh",
        "spanish": "es",
        "испанский": "es",
        "西班牙语": "es",
        "español": "es"
    }

    settings = await get_user_settings(user_id)
    lang = settings.language if settings else "en"

    if text == MESSAGES[lang]["back"].lower():
        await open_settings_menu(message, state)
        return

    selected_lang = language_map.get(text)
    if selected_lang:
        await update_language(user_id, selected_lang)
        await message.answer(MESSAGES[selected_lang]["language_updated"])
        await open_settings_menu(message, state)
    else:
        await message.answer(MESSAGES[lang]["invalid_language"])
