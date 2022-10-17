from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ближайшие события", callback_data="upcoming-events")
    ],
    [

        InlineKeyboardButton(text=f"Чат", url="https://t.me/neurofootball_chat"),
        InlineKeyboardButton(text="Результаты", url="https://t.me/neuro_football")

    ],
    [

        InlineKeyboardButton(text=f"Бонусы", callback_data="bonuses"),

    ],
    [

        InlineKeyboardButton(text="Связь с разработчиком", url="https://t.me/mikhail1_ru"),
    ],
    [
        InlineKeyboardButton(text="Закрыть", callback_data="menu-exit")
    ]

])

menu_one_button_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Меню", callback_data="menu")
    ],
])
