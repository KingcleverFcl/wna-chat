from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.reply import main_menu_kb
from states.user_states import MainMenuState

main_menu_router = Router()

@main_menu_router.message(F.text.in_([
    "Главное меню", "Main Menu", "主菜单", "Menú Principal"
]))
async def handle_main_menu(message: Message, state: FSMContext):
    await state.set_state(MainMenuState.menu)
    await message.answer("Вы в главном меню.", reply_markup=main_menu_kb)

def register_main_menu(router: Router):
    router.include_router(main_menu_router)
