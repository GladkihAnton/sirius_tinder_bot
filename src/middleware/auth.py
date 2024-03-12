from contextvars import ContextVar
from typing import Any, Awaitable, Callable, Coroutine

from aiogram import BaseMiddleware, Bot
from aiogram.dispatcher.event.bases import SkipHandler
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject

from src.state.login import LoginState

access_token_cxt: ContextVar[str] = ContextVar('access_token_cxt')


class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Coroutine[Any, Any, Coroutine[Any, Any, Any]]:
        state: FSMContext = data['state']
        access_token = (await state.get_data()).get('access_token')
        current_state = await state.get_state()

        if (
            access_token is None
            and (not data.get('command') or data['command'].command not in {'start', 'login'})
            and current_state != LoginState.enter_code
        ):
            bot: Bot = data['bot']
            await bot.send_message(text='Не авторизованы', chat_id=data['event_chat'].id)
            raise SkipHandler('Unauthorized')

        if access_token is not None:
            access_token_cxt.set(access_token)

        return await handler(event, data)
