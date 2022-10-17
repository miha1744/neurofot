from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



admin_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Bonus дня(адм)", callback_data="adm-dy-bs")
        ],
        [
            InlineKeyboardButton(text="Stavka дня(адм)", callback_data="day-stavka"),
            InlineKeyboardButton(text="Express дня(адм)", callback_data="day-express")

        ],
        [
        InlineKeyboardButton(text="История покупок", callback_data="day-stavka"),

        ],
        [

            InlineKeyboardButton(text="История ставок", url="https://t.me/ru_stavka_history")
        ],
        [

            InlineKeyboardButton(text="Пользовательское меню", callback_data="menu")
        ],
        [
            InlineKeyboardButton(text="Закрыть", callback_data="menu-exit")
        ]
    ])


admin_one_button_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Меню админа", callback_data="adm-dy-bs")
        ]
    ])
