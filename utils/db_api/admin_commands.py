from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.admin import Admin



# Команды связанные с юзером
async def add_admin(user_id: int):
    # Добавить пользователя
    try:
        admin = Admin(user_id=user_id)
        await admin.create()

    except UniqueViolationError:
        pass



async def check_if_admin_exist(admin_id: int) -> bool:
    return await Admin.get(admin_id) is not None
