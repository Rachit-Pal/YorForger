import requests
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from YorForger import pgram as bot

# in this plugins made by @NandhaxD in tg


@bot.on_message(filters.command(["ameme", "animememe"]))
async def animememes(_, m):
    res = requests.get("https://meme-api.herokuapp.com/gimme/animememes").json()
    url = res["url"]
    text = res["title"]
    link = res["postLink"]
    await m.reply_photo(
        url,
        caption=f"[{text}]({link})",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="ameme",
                    ),
                ],
            ],
        ),
    )


@bot.on_callback_query(filters.regex("ameme"))
async def ameme(_, query: CallbackQuery):
    query = query.message
    await query.delete()
    res = requests.get("https://meme-api.herokuapp.com/gimme/animememes").json()
    url = res["url"]
    text = res["title"]
    link = res["postLink"]
    await query.reply_photo(
        url,
        caption=f"[{text}]({link})",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="ameme",
                    ),
                ],
            ],
        ),
    )


@bot.on_message(filters.command("meme"))
async def memes(_, m):
    res = requests.get("https://meme-api.herokuapp.com/gimme/memes").json()
    url = res["url"]
    text = res["title"]
    link = res["postLink"]
    await m.reply_photo(
        url,
        caption=f"[{text}]({link})",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="bmeme",
                    ),
                ],
            ],
        ),
    )


@bot.on_callback_query(filters.regex("bmeme"))
async def memess(_, query: CallbackQuery):
    query = query.message
    await query.delete()
    res = requests.get("https://meme-api.herokuapp.com/gimme/memes").json()
    url = res["url"]
    text = res["title"]
    link = res["postLink"]
    await query.reply_photo(
        url,
        caption=f"[{text}]({link})",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="bmeme",
                    ),
                ],
            ],
        ),
    )


@bot.on_message(filters.command(["hmeme", "hentaimeme"]))
async def hetaimemes(_, m):
    res = requests.get("https://meme-api.herokuapp.com/gimme/hentaimemes").json()
    url = res["url"]
    text = res["title"]
    link = res["postLink"]
    await m.reply_photo(
        url,
        caption=f"[{text}]({link})",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="cmeme",
                    ),
                ],
            ],
        ),
    )


@bot.on_callback_query(filters.regex("cmeme"))
async def hmeme(_, query: CallbackQuery):
    query = query.message
    await query.delete()
    res = requests.get("https://meme-api.herokuapp.com/gimme/hentaimemes").json()
    url = res["url"]
    text = res["title"]
    link = res["postLink"]
    await query.reply_photo(
        url,
        caption=f"[{text}]({link})",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="cmeme",
                    ),
                ],
            ],
        ),
    )


__help__ = """ •
• Memes that make you laugh!
- /ameme: anime memes.
- /meme: random memes.
- /hmeme: hentai memes.
"""

__mod_name__ = "Meme"
