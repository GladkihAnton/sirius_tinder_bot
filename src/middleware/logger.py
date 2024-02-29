import uuid

from aiogram import BaseMiddleware
from starlette.types import Scope, Receive, Send, ASGIApp

from src.logger import correlation_id_ctx


class LogServerMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        correlation_id_ctx.set(uuid.uuid4().hex)

        await self.app(scope, receive, send)


class LogMessageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler,
        event,
        data,
    ):
        try:
            correlation_id_ctx.get()
        except LookupError:
            correlation_id_ctx.set(uuid.uuid4().hex)

        resp = await handler(event, data)
        return resp
