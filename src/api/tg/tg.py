import asyncio
import logging
from asyncio import Task
from typing import Any

from aiogram import Bot, Dispatcher, types
from fastapi import Depends
from fastapi.responses import ORJSONResponse
from starlette.requests import Request

from src.api.tg.router import tg_router
from src.integrations.tg_bot import get_dispatcher, get_tg_bot
from src.utils.background_tasks import tg_background_tasks


@tg_router.post('/tg')
async def tg_api(
    request: Request,
    dp: Dispatcher = Depends(get_dispatcher),
    bot: Bot = Depends(get_tg_bot),
) -> ORJSONResponse:
    logging.info('tg_api')
    data = await request.json()
    update = types.Update(**data)

    task: Task[Any] = asyncio.create_task(dp.feed_webhook_update(bot, update))
    tg_background_tasks.add(task)

    logging.info(len(tg_background_tasks))

    task.add_done_callback(tg_background_tasks.discard)

    logging.info(data)

    return ORJSONResponse({'success': True})
