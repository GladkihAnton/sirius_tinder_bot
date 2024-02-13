from aiogram.fsm.state import StatesGroup, State


class LoginState(StatesGroup):
    unauthorized = State()

    enter_code = State()

    authorized = State()
