from aiogram.fsm.state import StatesGroup, State

class MainMenuState(StatesGroup):
    main_menu = State()

class SettingsState(StatesGroup):
    main_menu_settings = State()
    main_menu_settings_nickname = State()
    main_menu_settings_language = State()
