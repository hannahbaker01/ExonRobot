"""
MIT License

Copyright (c) 2022 『 𝑺𝜞𝜩𝜩𝜨𝜦𝜯𝜢 𝜝𝜢𝜜𝑺𝜤 』

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Abishnoi1m
#     UPDATE   :- Abishnoi_bots
#     GITHUB :- 『 𝑺𝜞𝜩𝜩𝜨𝜦𝜯𝜢 𝜝𝜢𝜜𝑺𝜤 』 ""
import os
import time

import psutil

import Exon.modules.no_sql.users_db as users_db
from Exon import BOT_NAME, StartTime
from Exon.modules.helper_funcs import formatter

# sᴛᴀᴛs ᴍᴏᴅᴜʟᴇ


async def bot_sys_stats():
    bot_uptime = int(time.time() - StartTime)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
------------------
⛖ {BOT_NAME} ᴜᴘᴛɪᴍᴇ : {formatter.get_readable_time((bot_uptime))}
⛖ ʙᴏᴛ ᴄᴀᴘᴀᴄɪᴛʏ : {round(process.memory_info()[0] / 1024 ** 2)} ᴍʙ
⛖ ᴄᴘᴜ ᴜsᴀɢᴇ : {cpu}%
⛖ ʀᴀᴍ ᴜsᴀɢᴇ : {mem}%
⛖ ᴅɪsᴋ ᴜsᴀɢᴇ : {disk}%
⛖ ᴜsᴇʀs : 0{users_db.num_users()} ᴜsᴇʀs.
⛖ ɢʀᴏᴜᴘs : 0{users_db.num_chats()} ɢʀᴏᴜᴘs.
"""

    return stats
