from aiogram import executor

from loader import dp, db
from utils.db_api import db_gino
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # scheduler.add_job(pars_schedule, 'interval', minutes=5)
    # scheduler.start()

    print("Подключаем БД")
    await db_gino.on_startup(dp)
    print("Готово")

    print("Чистим базу")
    await db.gino.drop_all()
    # print("Готово")
    print("Создаем таблицы")
    await db.gino.create_all()
    # await pars_schedule()
    # await pars_schedule()

    # task1  = asyncio.create_task(pars_schedule())
    # await task1

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
