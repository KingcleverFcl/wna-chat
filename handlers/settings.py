from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.user_states import MainMenuSettingsState, MainMenuSettingsNicknameState, MainMenuSettingsLanguageState
from keyboards.reply import settings_menu_kb, language_selection_kb, main_menu_kb
from database.models import get_user_by_id, update_user_language, update_user_nickname, is_nickname_taken

router = Router()


# Вход в меню настроек
@router.message(F.text == "Настройки")
async def settings_menu(message: Message, state: FSMContext):
    await state.set_state(MainMenuSettingsState.settings)
    await message.answer("Настройки:", reply_markup=settings_menu_kb)


# Назад из меню настроек в главное меню
@router.message(MainMenuSettingsState.settings, F.text == "Назад")
async def settings_cancel(message: Message, state: FSMContext):
    await state.set_state(MainMenuSettingsState.main_menu)
    await message.answer("Вы вернулись в главное меню.", reply_markup=main_menu_kb)


# Смена ника — вход
@router.message(MainMenuSettingsState.settings, F.text == "Смена ника")
async def change_nickname_start(message: Message, state: FSMContext):
    await state.set_state(MainMenuSettingsNicknameState.waiting_for_nickname)
    await message.answer("Введите новый ник:")


# Смена ника — отмена
@router.message(MainMenuSettingsNicknameState.waiting_for_nickname, F.text == "Назад")
async def change_nickname_cancel(message: Message, state: FSMContext):
    await state.set_state(MainMenuSettingsState.settings)
    await message.answer("Отменено. Настройки:", reply_markup=settings_menu_kb)


# Смена ника — обработка ввода
@router.message(MainMenuSettingsNicknameState.waiting_for_nickname)
async def process_new_nickname(message: Message, state: FSMContext):
    new_nickname = message.text.strip()
    user_id = message.from_user.id

    if await is_nickname_taken(new_nickname):
        await message.answer("❌ Ник уже занят. Попробуйте другой:")
        return

    await update_user_nickname(user_id, new_nickname)
    await state.set_state(MainMenuSettingsState.settings)
    await message.answer(f"✅ Ник успешно изменён на {new_nickname}.", reply_markup=settings_menu_kb)


# Смена языка — вход
@router.message(MainMenuSettingsState.settings, F.text == "Смена языка")
async def change_language_start(message: Message, state: FSMContext):
    await state.set_state(MainMenuSettingsLanguageState.waiting_for_language)
    await message.answer("Выберите язык:", reply_markup=language_selection_kb)


# Смена языка — отмена
@router.message(MainMenuSettingsLanguageState.waiting_for_language, F.text == "Назад")
async def change_language_cancel(message: Message, state: FSMContext):
    await state.set_state(MainMenuSettingsState.settings)
    await message.answer("Отменено. Настройки:", reply_markup=settings_menu_kb)


# Смена языка — выбор
@router.message(MainMenuSettingsLanguageState.waiting_for_language)
async def process_language_selection(message: Message, state: FSMContext):
    selected_lang = message.text.strip()
    valid_languages = {
        "Русский": "ru",
        "Английский": "en",
        "中文": "zh",
        "Español": "es"
    }

    if selected_lang not in valid_languages:
        await message.answer("❌ Неверный язык. Выберите из списка.")
        return

    lang_code = valid_languages[selected_lang]
    user_id = message.from_user.id

    await update_user_language(user_id, lang_code)
    await state.set_state(MainMenuSettingsState.settings)
    await message.answer("✅ Язык успешно изменён.", reply_markup=settings_menu_kb)
