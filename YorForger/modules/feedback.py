from YorForger import pgram as bot, DEV_USERS as dev_user, SUPPORT_CHAT
from pyrogram import filters, enums 
from pyrogram.enums import ChatType
import random
from datetime import datetime
from pyrogram.types import *
from YorForger import OWNER_ID

#made by t.me/SAlTAM4

vegeta_img = ["https://telegra.ph/file/acd729b9cd8ff513e568f.jpg"]

@bot.on_message(filters.command(["feedback","bug"]))
async def feedback(_, m):
         if m.chat.type == ChatType.PRIVATE:
               return await m.reply_text("**plz give your feedback or bug report in groups")
         USER = m.from_user
         if len(m.command) < 2:
               await m.reply_text("**Gime a Feedback!**")
               return
         text = m.text.split(None, 1)[1]
         feedback = "**#NewFeedBack**\n"
         if m.chat:
             feedback += f"**From chat:** `@{m.chat.username}`\n"
         feedback+= f"**user id**: `{USER.id}`\n"
         feedback+= f"**mention**: {USER.mention}\n"
         feedback += f"**Feedback**: `{text}`"
     
         msg = await bot.send_photo(f"@{SUPPORT_CHAT}",random.choice(vegeta_img),caption=feedback,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [    InlineKeyboardButton("Approve ✅", callback_data=f"approve={USER.id}={text}={USER.first_name}"),
                            InlineKeyboardButton("Reject ✖️", callback_data=f"reject={USER.id}={text}={USER.first_name}")
                        ],
                    ]
                )
            )
    

         await m.reply_text("Your feedback Successfully Reported On SupportChat!",
                    reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "📩 View Report", url=f"{msg.link}")]]))
  

@bot.on_callback_query(filters.regex("reject"))
async def rejected(_, query: CallbackQuery):
          mm = query.data.split("=")
          user_id = mm[1]
          text = mm[2]
          name = mm[3]
          if query.from_user.id in dev_user:
              await query.edit_message_caption(f"**Feedback :** {text} from {name} | {user_id} is Rejected by {query.from_user.mention} ✖️")
              await bot.send_message(user_id, f"**Your Feedback :** {text} Has been Rejected by {query.from_user.mention} ✖️")
          else:
              await query.answer("Only devs can Reject this feedback.", show_alert=True)

@bot.on_callback_query(filters.regex("approve"))
async def approved(_, query: CallbackQuery):
          mm = query.data.split("=")
          user_id = mm[1]
          text = mm[2]
          name = mm[3]
          if query.from_user.id in dev_user:
              await query.edit_message_caption(f"**Feedback :** {text} from {name} | {user_id} is Approved by {query.from_user.mention} ✅")
              await bot.send_message(user_id, f"**Your Feedback :** {text} Has been Approved by {query.from_user.mention} ✅")
          else:
              await query.answer("Only devs can Approve this feedback.", show_alert=True)