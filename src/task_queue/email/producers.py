from typing import Literal

from arq import create_pool

from config.redis import redis_settings


async def send_email(recipient: str, subject: str, content: str, content_type: Literal['plain', 'html']):
    redis = await create_pool(redis_settings.arq_redis_settings)
    await redis.enqueue_job('send_email_job', recipient, subject, content, content_type)
