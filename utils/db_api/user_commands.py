from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User



# Команды связанные с юзером
async def add_user(user_id: int, user_name: str, name: str, balance: int = 0):
    # Добавить пользователя
    try:
        user = User(id=user_id, name=name, balance=balance, user_name=user_name)
        await user.create()

    except UniqueViolationError:
        pass


async def select_all_users():
    # Возвращает всех пользователей
    users = await User.query.gino.all()
    return users



# async def top_up_balance(user_id: int, amount: int):
#     # Попалняет баланс пользователя
#     user = await User.get(user_id)
#     new_balance = User.balance + amount
#     await user.update(balance=new_balance).apply()

async def select_user(user_id: int):
    # Выбор конкретного пользователя по id
    user = await User.query.where(User.id == user_id).gino.first()
    return user


async def count_users():
    # Подсчет пользователей
    total = await db.func.count(User.id).gino.scalar()
    return total


async def find_user(user_id: int):
    # Выбор конкретного пользователя по id
    return await User.query.where(User.id == user_id).gino.first() is None
