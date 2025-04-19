from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from states.user_states import UserStates
from keyboards.reply import settings_menu_keyboard, language_selection_keyboard
from messages import get_text
from database.models import get_user_language, is_nickname_taken, update_user_nickname, update_user_language

router = Router()


@router.message(UserStates.main_menu, lambda msg: msg.text in ["Настройки", "Settings", "Configuración", "设置"])
async def open_settings_menu(message: types.Message, state: FSMContext):
    lang = await get_user_language(message.from_user.id)
    await message.answer(get_text("settings_menu", lang), reply_markup=settings_menu_keyboard(lang))
    await state.set_state(UserStates.main_menu_settings)


@router.message(UserStates.main_menu_settings, lambda msg: msg.text in ["Смена ника", "Change Nickname", "Cambiar apodo", "更改昵称"])
async def prompt_nickname_change(message: types.Message, state: FSMContext):
    lang = await get_user_language(message.from_user.id)
    await message.answer(get_text("change_nickname_prompt", lang))
    await state.set_state(UserStates.main_menu_settings_nickname)


@router.message(UserStates.main_menu_settings_nickname)
async def change_nickname(message: types.Message, state: FSMContext):
    new_nickname = message.text.strip()
    lang = await get_user_language(message.from_user.id)
    if await is_nickname_taken(new_nickname):
        await message.answer(get_text("nickname_taken", lang))
        return
    await update_user_nickname(message.from_user.id, new_nickname)
    await message.answer(get_text("nickname_updated", lang))
    await open_settings_menu(message, state)


@router.message(UserStates.main_menu_settings, lambda msg: msg.text in ["Смена языка", "Change Language", "Cambiar idioma", "更改语言"])
async def prompt_language_change(message: types.Message, state: FSMContext):
    lang = await get_user_language(message.from_user.id)
    await message.answer(get_text("change_language_prompt", lang), reply_markup=language_selection_keyboard())
    await state.set_state(UserStates.main_menu_settings_language)


@router.message(UserStates.main_menu_settings_language)
async def change_language(message: types.Message, state: FSMContext):
    lang_map = {
        "Русский": "ru",
        "English": "en",
        "Español": "es",
        "中文": "zh"
    }
    selected_lang = lang_map.get(message.text)
    if selected_lang:
        await update_user_language(message.from_user.id, selected_lang)
        await message.answer(get_text("language_changed", selected_lang), reply_markup=settings_menu_keyboard(selected_lang))
        await state.set_state(UserStates.main_menu_settings)
    else:
        lang = await get_user_language(message.from_user.id)
        await message.answer(get_text("change_language_prompt", lang), reply_markup=language_selection_keyboard())


@router.message(UserStates.main_menu_settings, lambda msg: msg.text in ["Назад", "Back", "Atrás", "返回"])
async def return_to_main_menu(message: types.Message, state: FSMContext):
    lang = await get_user_language(message.from_user.id)
    await message.answer(get_text("main_menu", lang))  # предполагается, что это текст главного меню
    await state.set_state(UserStates.main_menu)
