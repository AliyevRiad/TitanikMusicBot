from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from InflexMusic import app

# Komutu işle
@app.on_message(filters.command(["song"]))
async def fsfsfs(client, message):
    # Yanıtlanacak mesajı oluştur
    reply_message = await message.reply_text("Mahnı yükləmək üçün aşağıdakı bota daxil olun.")
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("➡️ Bota daxil ol", url="https://t.me/RahidRobot")]]
    )
    await reply_message.edit_reply_markup(reply_markup=keyboard)
