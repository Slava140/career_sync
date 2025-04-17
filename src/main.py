import uvicorn

from app import app
from config.app import app_settings


if __name__ == '__main__':
    uvicorn.run(app=app, host=app_settings.HOST, port=app_settings.PORT)
