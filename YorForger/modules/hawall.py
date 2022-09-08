
import random, requests, time
from YorForger import telethn as asst, pgram as bot
from telethon import Button, events
from YorForger.events import register
from pyrogram import filters
from pyrogram.types import *


#credits to t.me/nandhaxd
@bot.on_message(filters.command("wish"))
async def wish(_, m):
            if len(m.command) <  2:
                  await m.reply("➕ **Add your wish** ➕")
                  return 
            api = requests.get("https://nekos.best/api/v2/happy").json()
            url = api["results"][0]['url']
            text = m.text.split(None, 1)[1]
            wish_count = random.randint(1,100)
            wish = f"✨ **Hey! {m.from_user.first_name}!** 🙋‍♀️\n"
            wish += f"✨ **Your wish :** {text} 🧚🏻‍♀️\n"
            wish += f"✨ **Possible to :** {wish_count}%"
            await m.reply_animation(url,caption=(wish),
              reply_markup=InlineKeyboardMarkup(
                    [ [InlineKeyboardButton("❔ What is This", url="https://t.me/StrawHatUpdates/14")]]))
            
         
BUTTON = [[Button.url("❔ What Is This", "https://t.me/StrawHatUpdates/11")]]
HOT = "https://telegra.ph/file/daad931db960ea40c0fca.gif"
SMEXY = "https://telegra.ph/file/a23e9fd851fb6bc771686.gif"
LEZBIAN = "https://telegra.ph/file/5609b87f0bd461fc36acb.gif"
BIGBALL = "https://i.gifer.com/8ZUg.gif"
LANG = "https://telegra.ph/file/423414459345bf18310f5.gif"
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"

@asst.on(events.NewMessage(pattern="/horny ?(.*)"))
async def horny(e):
         if not e.is_reply:
              user_id = e.sender.id
              user_name = e.sender.first_name
              mention = f"[{user_name}](tg://user?id={str(user_id)})"
              mm = random.randint(1,100)
              HORNY = f"**🔥** {mention} **Is** {mm}**% Horny!**"
              await e.reply(HORNY, buttons=BUTTON, file=HOT)
         if e.is_reply:
               replied = (await e.get_reply_message())
               id = replied.sender.id
               name = replied.sender.first_name
               mention = f"[{name}](tg://user?id={str(id)})"
               mm = random.randint(1,100)
               HORNY = f"**🔥** {mention} **Is** {mm}**% Horny!**"
               await e.reply(HORNY, buttons=BUTTON, file=HOT)

@asst.on(events.NewMessage(pattern="/gay ?(.*)"))
async def gay(e):
         if not e.is_reply:
              user_id = e.sender.id
              user_name = e.sender.first_name
              mention = f"[{user_name}](tg://user?id={str(user_id)})"
              mm = random.randint(1,100)
              GAY = f"**🏳‍🌈** {mention} **Is** {mm}**% Gay!**"
              await e.reply(GAY, buttons=BUTTON, file=SMEXY)
         if e.is_reply:
               replied = (await e.get_reply_message())
               id = replied.sender.id
               name = replied.sender.first_name
               mention = f"[{name}](tg://user?id={str(id)})"
               mm = random.randint(1,100)
               GAY = f"**🏳‍🌈** {mention} **Is** {mm}**% Gay!**"
               await e.reply(GAY, buttons=BUTTON, file=SMEXY)

@asst.on(events.NewMessage(pattern="/lezbian ?(.*)"))
async def lezbian(e):
         if not e.is_reply:
              user_id = e.sender.id
              user_name = e.sender.first_name
              mention = f"[{user_name}](tg://user?id={str(user_id)})"
              mm = random.randint(1,100)
              FEK = f"**💜** {mention} **Is** {mm}**% Lezbian!**"
              await e.reply(FEK, buttons=BUTTON, file=LEZBIAN)
         if e.is_reply:
               replied = (await e.get_reply_message())
               id = replied.sender.id
               name = replied.sender.first_name
               mention = f"[{name}](tg://user?id={str(id)})"
               mm = random.randint(1,100)
               FEK = f"**💜** {mention} **Is** {mm}**% Lezbian!**"
               await e.reply(FEK, buttons=BUTTON, file=LEZBIAN)

@asst.on(events.NewMessage(pattern="/boobs ?(.*)"))
async def boobs(e):
         if not e.is_reply:
              user_id = e.sender.id
              user_name = e.sender.first_name
              mention = f"[{user_name}](tg://user?id={str(user_id)})"
              mm = random.randint(1,100)
              BOOBS = f"**🍒** {mention}**'s Boobs Size Is** {mm}**!**"
              await e.reply(BOOBS, buttons=BUTTON, file=BIGBALL)
         if e.is_reply:
               replied = (await e.get_reply_message())
               id = replied.sender.id
               name = replied.sender.first_name
               mention = f"[{name}](tg://user?id={str(id)})"
               mm = random.randint(1,100)
               BOOBS = f"**🍒** {mention}**'s Boobs Size Is** {mm}**!**"
               await e.reply(BOOBS, buttons=BUTTON, file=BIGBALL)

@asst.on(events.NewMessage(pattern="/cock ?(.*)"))
async def cock(e):
         if not e.is_reply:
              user_id = e.sender.id
              user_name = e.sender.first_name
              mention = f"[{user_name}](tg://user?id={str(user_id)})"
              mm = random.randint(1,100)
              COCK = f"**🍆** {mention}**'s Cock Size Is** {mm}**cm**"
              await e.reply(COCK, buttons=BUTTON, file=LANG)
         if e.is_reply:
               replied = (await e.get_reply_message())
               id = replied.sender.id
               name = replied.sender.first_name
               mention = f"[{name}](tg://user?id={str(id)})"
               mm = random.randint(1,100)
               COCK = f"**🍆** {mention}**'s Cock Size Is** {mm}**cm**"
               await e.reply(COCK, buttons=BUTTON, file=LANG)

@asst.on(events.NewMessage(pattern="/cute ?(.*)"))
async def cute(e):
         if not e.is_reply:
              user_id = e.sender.id
              user_name = e.sender.first_name
              mention = f"[{user_name}](tg://user?id={str(user_id)})"
              mm = random.randint(1,100)
              CUTE = f"**🍑** {mention} {mm}**% Cute**"
              await e.reply(CUTE, buttons=BUTTON, file=CUTIE)
         if e.is_reply:
               replied = (await e.get_reply_message())
               id = replied.sender.id
               name = replied.sender.first_name
               mention = f"[{name}](tg://user?id={str(id)})"
               mm = random.randint(1,100)
               CUTE = f"**🍑** {mention} {mm}**% Cute**"
               await e.reply(CUTE, buttons=BUTTON, file=CUTIE)

__help__ = """
❔ **What is Wish:**
You have any kind of wish? Use `/wish` command to this bot to how possible to your wish!
Example:
❍ /wish I want to be a class topper

❔ **What is This (howall):**
In this Howell show you possibltly!
Example:
❍ /horny : reply to someone or self it well show you how horny
❍ /cute: reply to someone or self it well show you how cute
❍ /gay: reply to someone or self it well show you how gayness
❍ /lezbian: reply to someone or self it well show you how Lezbian
❍ /boobs: reply to someone or self it well show you how boob's size
❍ /cock: reply to someone or self it well show you how cock's size
"""

__mod_name__ = "Howall"
