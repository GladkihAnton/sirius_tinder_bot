from contextvars import ContextVar
from typing import Any, Awaitable, Callable, Coroutine

from aiogram import BaseMiddleware
from aiogram.dispatcher.event.bases import SkipHandler
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject

access_token_cxt: ContextVar[str] = ContextVar('access_token_cxt')


class BaseRoleMiddleware(BaseMiddleware):
    required_role: str

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Coroutine[Any, Any, Coroutine[Any, Any, Any]]:
        state: FSMContext = data['state']
        role = (await state.get_data()).get('role')

        if role != self.required_role:
            raise SkipHandler('Permission denied')

        return await handler(event, data)


class CustomerRoleMiddleware(BaseRoleMiddleware):
    required_role = 'customer'


class AdminRoleMiddleware(BaseRoleMiddleware):
    required_role = 'admin'


class DeliveryRoleMiddleware(BaseRoleMiddleware):
    required_role = 'delivery'
