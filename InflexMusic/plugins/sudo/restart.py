import asyncio
import os
import shutil
import socket
from datetime import datetime

import urllib3
from pyrogram import filters

import config
from config import OWNER_ID
from InflexMusic import app
from InflexMusic.misc import HAPP, SUDOERS, XCB
from InflexMusic.utils.database import (
    get_active_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from InflexMusic.utils.decorators.language import language
from InflexMusic.utils.pastebin import InflexBin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@app.on_message(filters.command(["getlog", "logs", "getlogs"]) & filters.user(OWNER_ID))
@language
async def log_(client, message, _):
    try:
        print("free")
    except:
        await message.reply_text(_["server_1"])



@app.on_message(filters.command(["restart"]) & SUDOERS)
async def restart_(_, message):
    response = await message.reply_text("Yenidən işə salınır...")
    ac_chats = await get_active_chats()
    for x in ac_chats:
        try:
            await app.send_message(
                chat_id=int(x),
                text=f"{app.mention} yenidən aktiv edilir...\n\n15 - 20 saniyədən sonra qoşa bilərsiniz.",
            )
            await remove_active_chat(x)
            await remove_active_video_chat(x)
        except:
            pass

    try:
        shutil.rmtree("downloads")
        shutil.rmtree("raw_files")
        shutil.rmtree("cache")
    except:
        pass
    await response.edit_text(
        "Yenidən aktiv etmək prosesi başladı. Zəhmət olmasa, bot aktiv edilənə qədər bir neçə saniyə gözləyin..."
    )
    os.system(f"kill -9 {os.getpid()} && python3 -m InflexMusic")
