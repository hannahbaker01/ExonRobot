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

from pyrogram.types import CallbackQuery
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CallbackQueryHandler

from Exon import BOT_NAME, OWNER_ID, SUPPORT_CHAT
from Exon import Abishnoi as pbot
from Exon import dispatcher


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "ᴍ", "ʜ", "ᴅᴀʏs"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@pbot.on_callback_query()
async def close(Client, cb: CallbackQuery):
    if cb.data == "close2":
        await cb.answer()
        await cb.message.delete()


# CALLBACKS


def ABG_about_callback(update, context):
    query = update.callback_query
    if query.data == "ABG_":
        query.message.edit_text(
            text=f"๏ ɪ'ᴍ {BOT_NAME} ,ᴀ ᴘᴏᴡᴇʀғᴜʟ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ʙᴜɪʟᴛ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴇᴀsɪʟʏ."
            "\n• I scan ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs."
            "\n• I ᴄᴀɴ ɢʀᴇᴇᴛ ᴜsᴇʀs ᴡɪsh ᴄᴜsᴛᴏᴍɪᴢᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs ᴀɴᴅ ᴇᴠᴇɴ sᴇᴛ ᴀ ɢʀᴏᴜᴘ's ʀᴜʟᴇs."
            "\n• I ʜᴀᴠᴇ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴛɪ-ғʟᴏᴏᴅ sʏsᴛᴇᴍ."
            "\n• I ᴄᴀɴ ᴡᴀʀɴ ᴜsᴇʀs ᴜɴsɪʟ ᴛʜᴇʏ ʀᴇᴀᴄʜ ᴍᴀx ᴡᴀʀɴx, ᴡɪᴛʜ ᴇᴀᴄʜ ᴘʀᴇᴅᴇғɪɴᴇᴅ ᴀᴄᴛɪᴏɴs sᴜᴄʜ ᴀs ʙᴀɴ, ᴍᴜᴛᴇ, ᴋɪᴄᴋ, ᴇᴛᴄ."
            "\n• I ʜᴀᴠᴇ ᴀ ɴᴏᴛᴇ ᴋᴇᴇᴘɪɴɢ sʏsᴛᴇᴍ, ʙʟᴀᴄᴋʟɪsᴛs, ᴀɴᴅ ᴇᴠᴇɴ ᴘʀᴇᴅᴇᴛᴇʀᴍɪɴᴇᴅ ʀᴇᴘʟɪᴇs ᴏɴ ᴄᴇʀᴛᴀɪɴ ᴋᴇʏᴡᴏʀᴅs."
            "\n• I ᴄʜᴇᴄᴋ ғᴏʀ ᴀᴅᴍɪɴs ᴘᴇʀᴍɪssɪᴏɴs ʙᴇғᴏʀᴇ ᴇxᴇᴄᴜᴛɪɴɢ ᴀɴʏ ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴍᴏʀᴇ sᴛᴜғғs"
            "\n\n_Exᴏɴ ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ GNU ɢᴇɴᴇʀᴀʟ ᴘᴜʙʟɪᴄ ʟɪᴄᴇɴsᴇ v3.0_"
            "\n\n*ᴄʟɪᴄᴋ ᴏɴ ʙᴜᴛᴛᴏɴ ʙᴇʟʟᴏᴡ ᴛᴏ ɢᴇᴛ ʙᴀsɪᴄ ʜᴇʟᴘ ғᴏʀ ᴇxᴏɴʀᴏʙᴏᴛ*.",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ᴀᴅᴍɪɴs", callback_data="ABG_admin"),
                        InlineKeyboardButton(text="ɴᴏᴛᴇs", callback_data="ABG_notes"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="sᴜᴘᴘᴏʀᴛ", callback_data="ABG_support"
                        ),
                        InlineKeyboardButton(
                            text="ᴄʀᴇᴅɪᴛs", callback_data="ABG_credit"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="sᴏᴜʀᴄᴇ",
                            callback_data="source_",
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="ɢᴏ ʙᴀᴄᴋ", callback_data="start_back"
                        ),
                    ],
                ]
            ),
        )

    elif query.data == "ABG_admin":
        query.message.edit_text(
            text=f"━━━━━━━ *ᴀᴅᴍɪɴ* ━━━━━━━\nʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴛʜᴇ 𝙼ᴜsɪᴄ ᴍᴏᴅᴜʟᴇ\n⍟*ᴀᴅᴍɪɴ*\nᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs\n/pause/n»ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ.\n/resume\n» ʀᴇsᴜᴍᴇᴅ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.\n/skip ᴏʀ /next\n»sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ.\n/end ᴏʀ /stop\n» ᴇɴᴅ ᴛʜᴇ ᴄᴜʀᴇᴇɴᴛ ᴏɴɢᴏɪɴ sᴛʀᴇᴀᴍ.\n⍟*ᴀᴜᴛʜ*\nᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴀᴜᴛʜ/ᴜɴᴀᴜᴛʜ ᴀɴʏ ᴜsᴇʀ\n• ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ᴄᴀɴ sᴋɪᴩ, ᴩᴀᴜsᴇ, ʀᴇsᴜᴍᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ sᴛʀᴇᴀᴍ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs./n/auth ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ\n» ᴀᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.\n/unauth ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ \n» ʀᴇᴍᴏᴠᴇs ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ.\n/authusers \n» sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.\n⍟*ᴘʟᴀʏ*\nᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴩʟᴀʏ sᴏɴɢs\n/play <sᴏɴɢ ɴᴀᴍᴇ/ʏᴛ ᴜʀʟ>\n» sᴛᴀʀᴛs ᴩʟᴀʏɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ ᴏɴ ᴠᴄ.!",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🏡", callback_data="start_back"),
                        InlineKeyboardButton(text="🛡️", callback_data="AsuX_help"),
                        InlineKeyboardButton(text="💳", callback_data="ABG_credit"),
                        InlineKeyboardButton(text="🕹️", callback_data="source_"),
                        InlineKeyboardButton(text="🖥️", callback_data="help_back"),
                    ]
                ]
            ),
        )

    elif query.data == "ABG_notes":
        query.message.edit_text(
            text=f"<b>๏ sᴇᴛᴛɪɴɢ ᴜᴘ ɴᴏᴛᴇs</b>"
            f"\nʏᴏᴜ ᴄᴀɴ sᴀᴠᴇ ᴍᴇssᴀɢᴇ/ᴍᴇᴅɪᴀ/ᴀᴜᴅɪᴏ ᴏʀ ᴀɴʏᴛʜɪɴɢ ᴀs ɴᴏᴛᴇs"
            f"\nᴛᴏ ɢᴇᴛ ᴀ ɴᴏᴛᴇ sɪᴍᴘʟʏ ᴜsᴇ # ᴀᴛ ᴛʜᴇ ʙᴇɢɪɴɴɪɴɢ ᴏғ ᴀ ᴡᴏʀᴅ"
            f"\n\nʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ sᴇᴛ ʙᴜᴛᴛᴏɴs ғᴏʀ ɴᴏᴛᴇs ᴀɴᴅ ғɪʟᴛᴇʀs (ʀᴇғᴇʀ ʜᴇʟᴘ ᴍᴇɴᴜ)",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ɢᴏ ʙᴀᴄᴋ", callback_data="ABG_")]]
            ),
        )
    elif query.data == "ABG_support":
        query.message.edit_text(
            text=f"*๏ {BOT_NAME} sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛs*"
            "\nᴊᴏɪɴ ᴍʏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ғᴏʀ sᴇᴇ ᴏʀ ʀᴇᴘᴏʀᴛ ᴀ ᴘʀᴏʙʟᴇᴍ ᴏɴ ᴇxᴏɴ",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="sᴜᴘᴘᴏʀᴛ", url=f"t.me/{SUPPORT_CHAT}"
                        ),
                        InlineKeyboardButton(
                            text="ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Abishnoi_bots"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="ɢᴏ ʙᴀᴄᴋ", callback_data="ABG_"),
                    ],
                ]
            ),
        )

    elif query.data == "ABG_credit":  # Credit  i hope edit nai hoga
        query.message.edit_text(
            text=f"━━━━━━━ *ᴄʀᴇᴅɪᴛ* ━━━━━━━"
            "\n🛡️ *ᴄʀᴇᴅɪᴛ ꜰᴏʀ ᴇxᴏɴ ʀᴏʙᴏᴛ* 🛡️"
            "\n\nʜᴇʀᴇ ɪꜱ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴀɴᴅ"
            f"\nꜱᴘᴏɴꜱᴏʀ ᴏꜰ [{BOT_NAME}](t.me/Exon_Robot)"
            "\n\nʜᴇ ꜱᴘᴇɴᴛ ᴀ ʟᴏᴛ ᴏꜰ ᴛɪᴍᴇ ꜰᴏʀ"
            f"\nᴍᴀᴋɪɴɢ [{BOT_NAME}](t.me/{OWNER_USERNAME}) ᴀ"
            "\nꜱᴜᴘᴇʀ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🏡", callback_data="start_back"),
                        InlineKeyboardButton(text="🛡️", callback_data="ABG_admin"),
                        InlineKeyboardButton(text="💳", callback_data="AsuX_help"),
                        InlineKeyboardButton(text="🧑‍", callback_data="source_"),
                        InlineKeyboardButton(text="🖥️", callback_data="help_back"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="ᴀʙɪsʜɴᴏɪ", url="https://t.me/Abishnoi1M"
                        ),
                        InlineKeyboardButton(
                            text="ᴄʜᴀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"
                        ),
                    ],
                ]
            ),
        )


def Source_about_callback(update, context):
    query = update.callback_query
    if query.data == "source_":
        query.message.edit_text(
            text=f"""
*ʜᴇʏ,
 ᴛʜɪs ɪs {BOT_NAME} ,
ᴀɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ.*

ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ : [ᴛᴇʟᴇᴛʜᴏɴ](https://github.com/LonamiWebs/Telethon)
[ᴩʏʀᴏɢʀᴀᴍ](https://github.com/pyrogram/pyrogram)
[ᴩʏᴛʜᴏɴ-ᴛᴇʟᴇɢʀᴀᴍ-ʙᴏᴛ](https://github.com/python-telegram-bot/python-telegram-bot)
ᴀɴᴅ ᴜsɪɴɢ [sǫʟᴀʟᴄʜᴇᴍʏ](https://www.sqlalchemy.org) ᴀɴᴅ [ᴍᴏɴɢᴏ](https://cloud.mongodb.com) ᴀs ᴅᴀᴛᴀʙᴀsᴇ.

*ʜᴇʀᴇ ɪs ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ :* [{BOT_NAME}](https://github.com/『 𝑺𝜞𝜩𝜩𝜨𝜦𝜯𝜢 𝜝𝜢𝜜𝑺𝜤 』/ExonRobot)


ᴇxᴏɴ ʀᴏʙᴏᴛ ɪs ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ [ᴍɪᴛ ʟɪᴄᴇɴsᴇ](https://github.com/『 𝑺𝜞𝜩𝜩𝜨𝜦𝜯𝜢 𝜝𝜢𝜜𝑺𝜤 』/ExonRobot/blob/master/LICENSE).
© 2022 - 2023 [sᴜᴘᴘᴏʀᴛ](https://t.me/{SUPPORT_CHAT}) ᴄʜᴀᴛ, ᴀʟʟ ʀɪɢʜᴛs ʀᴇsᴇʀᴠᴇᴅ.
""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🏡", callback_data="start_back"),
                        InlineKeyboardButton(text="🛡️", callback_data="ABG_admin"),
                        InlineKeyboardButton(text="💳", callback_data="ABG_credit"),
                        InlineKeyboardButton(text="🧑‍", url=f"tg://user?id={OWNER_ID}"),
                        InlineKeyboardButton(text="🖥️", callback_data="help_back"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="ꜱᴏᴜʀᴄᴇ",
                            url="https://github.com/『 𝑺𝜞𝜩𝜩𝜨𝜦𝜯𝜢 𝜝𝜢𝜜𝑺𝜤 』/ExonRobot",  # DON'T CHANGE
                        ),
                    ],
                ]
            ),
        )


about_callback_handler = CallbackQueryHandler(
    ABG_about_callback, pattern=r"ABG_", run_async=True
)

source_callback_handler = CallbackQueryHandler(
    Source_about_callback, pattern=r"source_", run_async=True
)


dispatcher.add_handler(about_callback_handler)
dispatcher.add_handler(source_callback_handler)
