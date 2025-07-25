from pyrogram.types import InlineKeyboardButton

import config
from InflexMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_7"], url=config.SUPPORT_GROUP)
        ],        
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            )
        ],
    ]
    return buttons


#


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper"),
            InlineKeyboardButton(text=_["S_B_10"], callback_data="BASICBOTS"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_7"], url=config.SUPPORT_GROUP),
        ],[
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
        ],
    ]
    return buttons
