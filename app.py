import asyncio

import apscheduler.schedulers.asyncio
from aiogram import executor
from apscheduler import schedulers
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from data.config import NEUROFOOTBALL_CHAT_ID
from loader import dp, db, scheduler
import middlewares, filters, handlers
from utils.db_api import db_gino
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from apscheduler.schedulers.background import BackgroundScheduler
from utils.parser.parser_scheduler import pars_schedule





async def on_startup(dispatcher):
    scheduler.add_job(pars_schedule, 'interval', minutes=5)

    print("Подключаем БД")
    await db_gino.on_startup(dp)
    print("Готово")

    print("Чистим базу")
    # await db.gino.drop_all()
    print("Готово")
    print("Создаем таблицы")
    await db.gino.create_all()

    # task1  = asyncio.create_task(pars_schedule())
    # await task1

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)





if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)

