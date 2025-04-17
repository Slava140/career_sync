from typing import Any

from task_queue.email import jobs
from config.redis import redis_settings


async def startup(context: dict[str, Any]) -> None:
    ...

async def shutdown(context: dict[str, Any]) -> None:
    ...


class WorkerSettings:
    functions = [jobs.send_email_job]
    on_startup = startup
    on_shutdown = shutdown
    redis_settings = redis_settings.arq_redis_settings