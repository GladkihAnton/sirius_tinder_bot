from asyncio import Task
from typing import Any

tg_background_tasks: set[Task[Any]] = set()
