import html

import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    run_async,
)
from telegram.utils.helpers import mention_html

from YorForger import (
    DEMONS,
    DEV_USERS,
    DRAGONS,
    LOGGER,
    OWNER_ID,
    TIGERS,
    WOLVES,
    dispatcher,
)
from YorForger.modules.disable import DisableAbleCommandHandler
from YorForger.modules.helper_funcs.chat_status import (
    bot_admin,
    can_delete,
    can_restrict,
    connection_status,
    is_user_admin,
    is_user_ban_protected,
    is_user_in_chat,
    user_admin,
    user_admin_no_reply,
    user_can_ban,
)
from YorForger.modules.helper_funcs.extraction import extract_user_and_text
from YorForger.modules.helper_funcs.string_handling import extract_time
from YorForger.modules.log_channel import gloggable, loggable

# this module ban type's and kick type make by @ctzfamily and some friends


UNBAN_IMG = "https://telegra.ph/file/b9af0c3c1a6cc8da18459.mp4"
BAN_IMG = "https://telegra.ph/file/023c328412eb339546230.mp4"
SELF_KICK_IMG = "https://telegra.ph/file/2e97caf7b4341744037e1.mp4"


@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def ban(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot = context.bot
    args = context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("I doubt that's a user.")
        return log_message
    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != "User not found":
            raise
        message.reply_text("Can't seem to find this person.")
        return log_message
    if user_id == bot.id:
        message.reply_text("Oh yeah, ban myself, noob!")
        return log_message

    if is_user_ban_protected(chat, user_id, member) and user not in DEV_USERS:
        if user_id == OWNER_ID:
            message.reply_text("Trying to put me against a God level disaster huh?")
        elif user_id in DEV_USERS:
            message.reply_text("I can't act against our own.")
        elif user_id in DRAGONS:
            message.reply_text(
                "Fighting this Dragon here will put civilian lives at risk."
            )
        elif user_id in DEMONS:
            message.reply_text(
                "Bring an order from Straw Hats to fight a Demon disaster."
            )
        elif user_id in TIGERS:
            message.reply_text(
                "Bring an order from Straw Hats to fight a Tiger disaster."
            )
        elif user_id in WOLVES:
            message.reply_text("Wolf abilities make them ban immune!")
        else:
            message.reply_text("This user has immunity and cannot be banned.")
        return log_message
    if message.text.startswith("/s"):
        silent = True
        if not can_delete(chat, context.bot.id):
            return ""
    else:
        silent = False
    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#{'S' if silent else ''}BANNED\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
    )
    if reason:
        log += "\n<b>Reason:</b> {}".format(reason)

    try:
        chat.kick_member(user_id)

        if silent:
            if message.reply_to_message:
                message.reply_to_message.delete()
            message.delete()
            return log

        # bot.send_sticker(chat.id, BAN_STICKER)  # banhammer marie sticker
        reply = (
            f"╔━「 <b>Ban Event</b> 」\n"
            f"❍ <b>Admin :</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"❍ <b>User :</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
        )
        if reason:
            reply += f"\n❍ <b>Reason :</b> {html.escape(reason)}"

        bot.send_animation(
            chat.id,
            BAN_IMG,
            caption=reply,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🔘 Unban", callback_data=f"unbanb_unban={user_id}"
                        ),
                        InlineKeyboardButton(
                            text="✖️ Delete", callback_data="unbanb_del"
                        ),
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML,
        )
        return log

    except BadRequest as excp:
        if excp.message == "Reply message not found":
            # Do not reply
            if silent:
                return log
            message.reply_text("Baka is Banned!", quote=False)
            return log
        else:
            LOGGER.warning(update)
            LOGGER.exception(
                "ERROR banning user %s in chat %s (%s) due to %s",
                user_id,
                chat.title,
                chat.id,
                excp.message,
            )
            message.reply_text("Uhm...that didn't work...")

    return log_message


@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def temp_ban(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("Dude! at least refer some user to ban...")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != "User not found":
            raise
        message.reply_text("I can't seem to find this user.")
        return log_message
    if user_id == bot.id:
        message.reply_text("I'm not gonna BAN myself, why are you so baka?")
        return log_message

    if is_user_ban_protected(chat, user_id, member):
        message.reply_text("I don't feel like it.")
        return log_message

    if not reason:
        message.reply_text("You haven't specified a time to ban this user for!")
        return log_message

    split_reason = reason.split(None, 1)

    time_val = split_reason[0].lower()
    reason = split_reason[1] if len(split_reason) > 1 else ""
    bantime = extract_time(message, time_val)

    if not bantime:
        return log_message

    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        "#TEMP BANNED\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}\n"
        f"<b>Time:</b> {time_val}"
    )
    if reason:
        log += "\n<b>Reason:</b> {}".format(reason)

    try:
        chat.kick_member(user_id, until_date=bantime)
        # bot.send_sticker(chat.id, BAN_STICKER)  # banhammer marie sticker

        reply_msg = (
            f"╔━「 <b>Temporary Ban</b> 」\n"
            f"❍ <b>Admin :</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"❍ <b>User :</b> {mention_html(member.user.id, html.escape(member.user.first_name))}\n"
            f"❍ <b>Banned for : {time_val}</b>"
        )

        if reason:
            reply_msg += f"\n❍ <b>Reason :</b> {html.escape(reason)}"

        bot.send_animation(
            chat.id,
            BAN_IMG,
            caption=reply_msg,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🔘 Unban", callback_data=f"unbanb_unban={user_id}"
                        ),
                        InlineKeyboardButton(
                            text="✖️ Delete", callback_data="unbanb_del"
                        ),
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML,
        )
        return log

    except BadRequest as excp:
        if excp.message == "Reply message not found":
            # Do not reply
            message.reply_text(
                f"Banned! User will be banned for {time_val}.", quote=False
            )
            return log
        else:
            LOGGER.warning(update)
            LOGGER.exception(
                "ERROR banning user %s in chat %s (%s) due to %s",
                user_id,
                chat.title,
                chat.id,
                excp.message,
            )
            message.reply_text("Well damn, I can't ban that user.")

    return log_message


@connection_status
@bot_admin
@can_restrict
@user_admin_no_reply
@user_can_ban
@loggable
def unbanb_btn(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    query = update.callback_query
    chat = update.effective_chat
    user = update.effective_user
    if query.data != "unbanb_del":
        splitter = query.data.split("=")
        query_match = splitter[0]
        if query_match == "unbanb_unban":
            user_id = splitter[1]
            if not is_user_admin(chat, int(user.id)):
                bot.answer_callback_query(
                    query.id,
                    text="You don't have enough rights to unmute people",
                    show_alert=True,
                )
                return ""
            try:
                member = chat.get_member(user_id)
            except BadRequest:
                pass
            chat.unban_member(user_id)
            query.message.delete()
            chat_name = "<b>{}</b>".format(html.escape(chat.title))
            bot.send_animation(
                chat.id,
                UNBAN_IMG,
                caption=f"╔━「 <b>Unban Event</b> 」\n❍ <b>Group</b> : {chat_name}\n❍ <b>Admin</b> : {mention_html(user.id, user.first_name)}\n❍ <b>User</b> : {mention_html(member.user.id, member.user.first_name)}",
                parse_mode=ParseMode.HTML,
            )
            bot.answer_callback_query(query.id, text="Unbanned!")
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"#UNBANNED\n"
                f"<b>Admin :</b> {mention_html(user.id, user.first_name)}\n"
                f"<b>User :</b> {mention_html(member.user.id, member.user.first_name)}"
            )

    else:
        if not is_user_admin(chat, int(user.id)):
            bot.answer_callback_query(
                query.id,
                text="You don't have enough rights to delete this message.",
                show_alert=True,
            )
            return ""
        query.message.delete()
        bot.answer_callback_query(query.id, text="Deleted!")
        return ""


@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def punch(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    api = requests.get("https://api.waifu.pics/sfw/kick").json()
    KICK_IMG = api["url"]
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("I doubt that's a user.")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != "User not found":
            raise

        message.reply_text("I can't seem to find this user.")
        return log_message
    if user_id == bot.id:
        message.reply_text("Yeahhh I'm not gonna do that.")
        return log_message

    if is_user_ban_protected(chat, user_id):
        message.reply_text("I really wish I could punch this user....")
        return log_message

    res = chat.unban_member(user_id)  # unban on current user = kick
    if res:
        # bot.send_sticker(chat.id, BAN_STICKER)  # banhammer marie sticker
        bot.send_animation(
            chat.id,
            KICK_IMG,
            caption=f"• <b>{html.escape(chat.title)}</b>\nRemoved! {mention_html(member.user.id, html.escape(member.user.first_name))}.",
            parse_mode=ParseMode.HTML,
        )
        log = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#KICKED\n"
            f"<b>Admin :</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User :</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
        )
        if reason:
            log += f"\n<b>Reason :</b> {reason}"

        return log

    else:
        message.reply_text("Well damn, I can't remove that user.")

    return log_message


@run_async
@bot_admin
@can_restrict
def punchme(update: Update, context: CallbackContext):
    user_id = update.effective_message.from_user.id
    if is_user_admin(update.effective_chat, user_id):
        update.effective_message.reply_text("I wish I could... but you're an admin.")
        return

    res = update.effective_chat.unban_member(user_id)  # unban on current user = kick
    if res:
        update.effective_message.reply_animation(
            SELF_KICK_IMG,
            caption="<b>❕Baka Noice Try!</b>",
            parse_mode=ParseMode.HTML,
        )

    else:
        update.effective_message.reply_text("Huh? I can't :/")


@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def unban(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    chat_name = "<b>• {}</b>".format(html.escape(chat.title))
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("I doubt that's a user.")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != "User not found":
            raise
        message.reply_text("I can't seem to find this user.")
        return log_message
    if user_id == bot.id:
        message.reply_text("How would I unban myself if I wasn't here...?")
        return log_message

    if is_user_in_chat(chat, user_id):
        message.reply_text("Isn't this person already here??")
        return log_message

    chat.unban_member(user_id)
    message.reply_animation(
        UNBAN_IMG,
        caption=f"{chat_name}\n**❕ Unbanned** : {mention_html(member.user.id, html.escape(member.user.first_name))}",
        parse_mode=ParseMode.HTML,
    )

    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#UNBANNED\n"
        f"<b>Admin :</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User :</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
    )
    if reason:
        log += f"\n<b>Reason :</b> {reason}"

    return log


@run_async
@connection_status
@bot_admin
@can_restrict
@gloggable
def selfunban(context: CallbackContext, update: Update) -> str:
    message = update.effective_message
    user = update.effective_user
    bot, args = context.bot, context.args
    if user.id not in DRAGONS or user.id not in TIGERS:
        return

    try:
        chat_id = int(args[0])
    except:
        message.reply_text("Give a valid chat ID.")
        return

    chat = bot.getChat(chat_id)

    try:
        member = chat.get_member(user.id)
    except BadRequest as excp:
        if excp.message == "User not found":
            message.reply_text("I can't seem to find this user.")
            return
        else:
            raise

    if is_user_in_chat(chat, user.id):
        message.reply_text("Aren't you already in the chat??")
        return

    chat.unban_member(user.id)
    message.reply_text("Yep, I have unbanned you.")

    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#UNBANNED\n"
        f"<b>User :</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
    )

    return log


__help__ = """
 ❍ `/punchme` : punches the user who issued the command.
 ❍ `/kickme` : kicks the user who issued the command.\n
**Mute User Commands:**
 ❍ `/mute` <userhandle> : silences a user. Can also be used as a reply, muting the replied to user.
 ❍ `/tmute` <userhandle> (m/h/d) : mutes a user for x time (m = minutes, h = hours, d = days)
 ❍ `/unmute` <userhandle : unmutes a user. Can also be used as a reply, muting the replied to user.\n
**Ban User Commands:**
 ❍ `/ban` <userhandle> : bans a user. (via handle, or reply)
 ❍ `/sban` <userhandle> : Silently ban a user. Deletes command, Replied message and doesn't reply.
 ❍ `/tban` <userhandle> (m/h/d) : bans a user for x time (m = minutes, h = hours, d = days)
 ❍ `/unban` <userhandle> : unbans a user.
 ❍ `/kick` <userhandle> : kick a user out of the group.
 ❍ `/punch` <userhandle> : Punches a user out of the group.\n
 **Ban Channel Commands:**
 ❍ `/cban` or `/channelban` ban a channel. 
 ❍ `/uncban` or `/channelunban`unban channel. 
"""

BAN_HANDLER = CommandHandler(["ban", "sban"], ban)
TEMPBAN_HANDLER = CommandHandler(["tban"], temp_ban)
PUNCH_HANDLER = CommandHandler(["punch", "kick"], punch)
UNBAN_HANDLER = CommandHandler("unban", unban)
UNBAN_BUTTON_HANDLER = CallbackQueryHandler(unbanb_btn, pattern=r"unbanb_")
ROAR_HANDLER = CommandHandler("roar", selfunban)
PUNCHME_HANDLER = DisableAbleCommandHandler(
    ["punchme", "kickme"], punchme, filters=Filters.group
)


dispatcher.add_handler(BAN_HANDLER)

dispatcher.add_handler(TEMPBAN_HANDLER)
dispatcher.add_handler(PUNCH_HANDLER)
dispatcher.add_handler(UNBAN_BUTTON_HANDLER)
dispatcher.add_handler(UNBAN_HANDLER)
dispatcher.add_handler(ROAR_HANDLER)
dispatcher.add_handler(PUNCHME_HANDLER)

__mod_name__ = "Bans-Mutes"
__handlers__ = [
    BAN_HANDLER,
    TEMPBAN_HANDLER,
    PUNCH_HANDLER,
    UNBAN_HANDLER,
    UNBAN_BUTTON_HANDLER,
    ROAR_HANDLER,
    PUNCHME_HANDLER,
]
