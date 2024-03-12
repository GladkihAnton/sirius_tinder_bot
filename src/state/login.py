from aiogram.fsm.state import State, StatesGroup


class LoginState(StatesGroup):
    enter_code = State()
