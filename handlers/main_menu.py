from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.reply import main_menu_keyboard
from states import MainMenuState
from translations import get_text

router = Router()

@router.message(F.text.in_({"Главное меню", "Main menu", "主菜单", "Menú principal"}))
async def show_main_menu(message: Message, state: FSMContext):
    await state.set_state(MainMenuState.main_menu)
    await message.answer(get_text("main_menu", message.from_user.language_code), reply_markup=main_menu_keyboard(message.from_user.language_code))
