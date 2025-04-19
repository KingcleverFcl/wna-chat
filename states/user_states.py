from aiogram.fsm.state import State, StatesGroup

class UserStates(StatesGroup):
    main_menu = State()
    main_menu_settings = State()
    main_menu_settings_nickname = State()
    main_menu_settings_language = State()
