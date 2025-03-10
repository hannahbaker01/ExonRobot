"""
MIT License

Copyright (c) 2022 ABISHNOI69

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
# TG :- @Sreenathbhasi_official
#     UPDATE   :- Abishnoi_bots
#     GITHUB :- ABISHNOI69 ""

from datetime import datetime
from functools import wraps

from telegram.ext import CallbackContext

from Exon.modules.helper_funcs.decorators import Exoncallback, Exoncmd
from Exon.modules.helper_funcs.misc import is_module_loaded

from ..modules.helper_funcs.anonymous import AdminPerms, user_admin

FILENAME = __name__.rsplit(".", 1)[-1]

if is_module_loaded(FILENAME):
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
    from telegram.error import BadRequest, Unauthorized
    from telegram.ext import JobQueue
    from telegram.utils.helpers import escape_markdown

    from Exon import EVENT_LOGS, LOGGER, dispatcher
    from Exon.modules.helper_funcs.chat_status import is_user_admin
    from Exon.modules.helper_funcs.chat_status import user_admin as u_admin
    from Exon.modules.sql import log_channel_sql as sql

    def loggable(func):
        @wraps(func)
        def log_action(
            update: Update,
            context: CallbackContext,
            job_queue: JobQueue = None,
            *args,
            **kwargs,
        ):
            if not job_queue:
                result = func(update, context, *args, **kwargs)
            else:
                result = func(update, context, job_queue, *args, **kwargs)

            chat = update.effective_chat
            message = update.effective_message

            if result:
                datetime_fmt = "%H:%M - %d-%m-%Y"
                result += f"\n<b>Event Stamp</b>: <code>{datetime.utcnow().strftime(datetime_fmt)}</code>"

                try:
                    if message.chat.type == chat.SUPERGROUP:
                        if message.chat.username:
                            result += f'\n<b>Link:</b> <a href="https://t.me/{chat.username}/{message.message_id}">click here</a>'
                        else:
                            cid = str(chat.id).replace("-100", "")
                            result += f'\n<b>Link:</b> <a href="https://t.me/c/{cid}/{message.message_id}">click here</a>'
                except AttributeError:
                    result += "\n<b>Link:</b> No link for manual actions."  # or just without the whole line
                log_chat = sql.get_chat_log_channel(chat.id)
                if log_chat:
                    send_log(context, log_chat, chat.id, result)

            return result

        return log_action

    def gloggable(func):
        @wraps(func)
        def glog_action(update: Update, context: CallbackContext, *args, **kwargs):
            result = func(update, context, *args, **kwargs)
            chat = update.effective_chat
            message = update.effective_message

            if result:
                datetime_fmt = "%H:%M - %d-%m-%Y"
                result += "\n<b>Event Stamp</b>: <code>{}</code>".format(
                    datetime.utcnow().strftime(datetime_fmt),
                )

                if message.chat.type == chat.SUPERGROUP and message.chat.username:
                    result += f'\n<b>Link:</b> <a href="https://t.me/{chat.username}/{message.message_id}">click here</a>'
                log_chat = str(EVENT_LOGS)
                if log_chat:
                    send_log(context, log_chat, chat.id, result)

            return result

        return glog_action

    def send_log(
        context: CallbackContext, log_chat_id: str, orig_chat_id: str, result: str
    ):
        bot = context.bot
        try:
            bot.send_message(
                log_chat_id,
                result,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
        except BadRequest as excp:
            if excp.message == "Chat not found":
                bot.send_message(
                    orig_chat_id,
                    "This log channel has been deleted - unsetting.",
                )
                sql.stop_chat_logging(orig_chat_id)
            else:
                LOGGER.warning(excp.message)
                LOGGER.warning(result)
                LOGGER.exception("Could not parse")

                bot.send_message(
                    log_chat_id,
                    result
                    + "\n\nFormatting has been disabled due to an unexpected error.",
                )

    @Exoncmd(command="logchannel")
    @u_admin
    def logging(update: Update, context: CallbackContext):
        bot = context.bot
        message = update.effective_message
        chat = update.effective_chat

        log_channel = sql.get_chat_log_channel(chat.id)
        if log_channel:
            log_channel_info = bot.get_chat(log_channel)
            message.reply_text(
                f"This group has all it's logs sent to:"
                f" {escape_markdown(log_channel_info.title)} (`{log_channel}`)",
                parse_mode=ParseMode.MARKDOWN,
            )

        else:
            message.reply_text("No log channel has been set for this group!")

    @Exoncmd(command="setlog")
    @user_admin(AdminPerms.CAN_CHANGE_INFO)
    def setlog(update: Update, context: CallbackContext):
        bot = context.bot
        message = update.effective_message
        chat = update.effective_chat
        if chat.type == chat.CHANNEL:
            message.reply_text(
                "Now, forward the /setlog to the group you want to tie this channel to!",
            )

        elif message.forward_from_chat:
            sql.set_chat_log_channel(chat.id, message.forward_from_chat.id)
            try:
                message.delete()
            except BadRequest as excp:
                if excp.message != "Message to delete not found":
                    LOGGER.exception(
                        "Error deleting message in log channel. Should work anyway though.",
                    )

            try:
                bot.send_message(
                    message.forward_from_chat.id,
                    f"This channel has been set as the log channel for {chat.title or chat.first_name}.",
                )
            except Unauthorized as excp:
                if excp.message == "Forbidden: bot is not a member of the channel chat":
                    bot.send_message(chat.id, "Successfully set log channel!")
                else:
                    LOGGER.exception("ERROR in setting the log channel.")

            bot.send_message(chat.id, "Successfully set log channel!")

        else:
            message.reply_text(
                "The steps to set a log channel are:\n"
                " - add bot to the desired channel\n"
                " - send /setlog to the channel\n"
                " - forward the /setlog to the group\n",
            )

    @Exoncmd(command="unsetlog")
    @user_admin(AdminPerms.CAN_CHANGE_INFO)
    def unsetlog(update: Update, context: CallbackContext):
        bot = context.bot
        message = update.effective_message
        chat = update.effective_chat

        log_channel = sql.stop_chat_logging(chat.id)
        if log_channel:
            bot.send_message(
                log_channel,
                f"Channel has been unlinked from {chat.title}",
            )
            message.reply_text("Log channel has been un-set.")

        else:
            message.reply_text("No log channel has been set yet!")

    def __stats__():
        return f"× {sql.num_logchannels()} log channels set."

    def __migrate__(old_chat_id, new_chat_id):
        sql.migrate_chat(old_chat_id, new_chat_id)

    def __chat_settings__(chat_id, user_id):
        log_channel = sql.get_chat_log_channel(chat_id)
        if log_channel:
            log_channel_info = dispatcher.bot.get_chat(log_channel)
            return f"This group has all it's logs sent to: {escape_markdown(log_channel_info.title)} (`{log_channel}`)"
        return "No log channel is set for this group!"

    __mod_name__ = "𝐋ᴏɢɢᴇʀ"

else:
    # run anyway if module not loaded
    def loggable(func):
        return func

    def gloggable(func):
        return func


@Exoncmd("logsettings")
@user_admin(AdminPerms.CAN_CHANGE_INFO)
def log_settings(update: Update, _: CallbackContext):
    chat = update.effective_chat
    chat_set = sql.get_chat_setting(chat_id=chat.id)
    if not chat_set:
        sql.set_chat_setting(
            setting=sql.LogChannelSettings(chat.id, True, True, True, True, True)
        )
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Warn", callback_data="log_tog_warn"),
                InlineKeyboardButton(text="Action", callback_data="log_tog_act"),
            ],
            [
                InlineKeyboardButton(text="Join", callback_data="log_tog_join"),
                InlineKeyboardButton(text="Leave", callback_data="log_tog_leave"),
            ],
            [InlineKeyboardButton(text="Report", callback_data="log_tog_rep")],
        ]
    )
    msg = update.effective_message
    msg.reply_text("Toggle channel log settings", reply_markup=btn)


from Exon.modules.sql import log_channel_sql as sql


@Exoncallback(pattern=r"log_tog_.*")
def log_setting_callback(update: Update, context: CallbackContext):
    cb = update.callback_query
    user = cb.from_user
    chat = cb.message.chat
    if not is_user_admin(update, user.id):
        cb.answer("You aren't admin", show_alert=True)
        return
    setting = cb.data.replace("log_tog_", "")
    chat_set = sql.get_chat_setting(chat_id=chat.id)
    if not chat_set:
        sql.set_chat_setting(
            setting=sql.LogChannelSettings(chat.id, True, True, True, True, True)
        )

    t = sql.get_chat_setting(chat.id)
    if setting == "warn":
        r = t.toggle_warn()
        cb.answer("Warning log set to {}".format(r))
        return
    if setting == "act":
        r = t.toggle_action()
        cb.answer("Action log set to {}".format(r))
        return
    if setting == "join":
        r = t.toggle_joins()
        cb.answer("Join log set to {}".format(r))
        return
    if setting == "leave":
        r = t.toggle_leave()
        cb.answer("Leave log set to {}".format(r))
        return
    if setting == "rep":
        r = t.toggle_report()
        cb.answer("Report log set to {}".format(r))
        return

    cb.answer("Now, What i need to do")


__mod_name__ = "𝐋ᴏɢs "

# ғᴏʀ ʜᴇʟᴘ ᴍᴇɴᴜ

from Exon.modules.language import gs


def get_help(chat):
    return gs(chat, "log_help")
