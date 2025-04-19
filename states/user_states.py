from aiogram.fsm.state import State, StatesGroup

class MainMenuState(StatesGroup):
    menu = State()

class SettingsState(StatesGroup):
    menu = State()
    nickname = State()
    language = State()

class DialogState(StatesGroup):
    search = State()
    select_user = State()
    messaging = State()

class BlacklistState(StatesGroup):
    view = State()

class MessagesState(StatesGroup):
    view_chats = State()
    chat_navigation = State()
    chatting = State()

class CodeGeneratorState(StatesGroup):
    menu = State()
