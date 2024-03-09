from aiogram.fsm.state import State, StatesGroup


class LoginState(StatesGroup):
    unauthorized = State()

    enter_code = State()

    authorized = State()
