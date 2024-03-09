import uuid
from typing import Any, Awaitable, Callable, Coroutine

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from starlette.types import ASGIApp, Receive, Scope, Send

from src.logger import correlation_id_ctx


class LogServerMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope['type'] not in ('http', 'websocket'):
            await self.app(scope, receive, send)
            return

        for header, value in scope['headers']:
            if header == b'x-correlation-id':
                correlation_id_ctx.set(value.decode())
                break
        else:
            correlation_id_ctx.set(uuid.uuid4().hex)

        await self.app(scope, receive, send)


class LogMessageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Coroutine[Any, Any, Coroutine[Any, Any, Any]]:
        try:
            correlation_id_ctx.get()
        except LookupError:
            correlation_id_ctx.set(uuid.uuid4().hex)

        resp = await handler(event, data)
        return resp
