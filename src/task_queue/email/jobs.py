from email.mime.text import MIMEText
from typing import Any, Literal

from aiosmtplib import SMTP

from config.email import email_settings


async def send_email_job(
        context: dict[str, Any],
        recipient: str,
        subject: str,
        content: str,
        content_type: Literal['plain', 'html']
):
    message = MIMEText(content, content_type)
    message['Subject'] = subject

    async with SMTP(hostname=email_settings.HOST, port=email_settings.PORT) as server:
        await server.login(email_settings.USER, email_settings.PASS)
        await server.sendmail(email_settings.USER, recipient, message.as_string())
