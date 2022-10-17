from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



final_day_bonus_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Подтвердить", callback_data="appr-adm-dy-bs")
        ],
        [
            InlineKeyboardButton(text="Начать сначала", callback_data="adm-dy-bs"),

        ]

    ])
