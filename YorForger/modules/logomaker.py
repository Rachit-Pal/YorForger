import glob
import io
import os
import random

import requests
from PIL import Image, ImageDraw, ImageFont
from telethon import Button

from YorForger import OWNER_ID, SUPPORT_CHAT
from YorForger import telethn as tbot
from YorForger.events import register

LOGO_LINKS = [
    "https://telegra.ph/file/eca03ceddb387b38fdc73.jpg",
    "https://telegra.ph/file/e65e246fb1db004649e97.jpg",
    "https://telegra.ph/file/8b46a80e5750577cdde73.jpg",
    "https://telegra.ph/file/c3537ea071fe34df1c4ea.jpg",
    "https://telegra.ph/file/ceb490e6106dfccae5016.jpg",
    "https://telegra.ph/file/1c1eff19da3421fbe728b.jpg",
    "https://telegra.ph/file/176d00e7e85333cc79fed.jpg",
    "https://telegra.ph/file/ee66f1c74bcb768882032.jpg",
    "https://telegra.ph/file/bdb3693cba96acc7dfa03.jpg",
    "https://telegra.ph/file/0e4d1738f5fb1d54fcdd7.jpg",
    "https://telegra.ph/file/77c42b7382fb99797642e.jpg",
    "https://telegra.ph/file/df1331d378ea9f38a0090.jpg",
    "https://telegra.ph/file/735c44767dda2b00442ca.jpg",
    "https://telegra.ph/file/5503b1017a1f398090baa.jpg",
    "https://telegra.ph/file/4e0ed6862df9f988b9f30.jpg",
    "https://telegra.ph/file/111960e17dbae6bf20a5e.jpg",
    "https://telegra.ph/file/f074f976a2d4a94536cf5.jpg",
    "https://telegra.ph/file/2d7cf1d43dede0eaf1bfe.jpg",
    "https://telegra.ph/file/f8d9b19a2d25cfd92c7fb.jpg",
    "https://telegra.ph/file/bbf5f6ec869b3204d605c.jpg",
    "https://telegra.ph/file/8f231b362e9c09fdf6078.jpg",
    "https://telegra.ph/file/364185b5c141d05ad9a93.jpg",
    "https://telegra.ph/file/722d61ca0443758dcbbfb.jpg",
    "https://telegra.ph/file/8fe6e456525353b4c40c8.jpg",
    "https://telegra.ph/file/73decdfd88cf8697c3953.jpg",
    "https://telegra.ph/file/6664c32dcb5b134beb19c.jpg",
    "https://telegra.ph/file/d3dd435d6c52fca20bb8c.jpg",
    "https://telegra.ph/file/7647a1d211bdc1f50b82b.jpg",
    "https://telegra.ph/file/bf1e329dee39473943939.jpg",
    "https://telegra.ph/file/bf1ea5233b8f2759f50df.jpg",
    "https://telegra.ph/file/c5824a10b34fedf4c2e40.jpg",
    "https://telegra.ph/file/5652282e8c19b63e2a62a.jpg",
    "https://telegra.ph/file/87286356a328d839df92b.jpg",
    "https://telegra.ph/file/888f420d4dd3b168299a4.jpg",
    "https://telegra.ph/file/02bd94586664a22b1d63f.jpg",
    "https://telegra.ph/file/83437275bfc2b061320a3.jpg",
    "https://telegra.ph/file/742f66b37753d48acfb4a.jpg",
    "https://telegra.ph/file/3ff65d24bb2098e35261f.jpg",
    "https://telegra.ph/file/f4c4b0f5ecc569a73a892.jpg",
    "https://telegra.ph/file/53cf86072b5cb1d743626.jpg",
    "https://telegra.ph/file/c2789ee5e396038706964.jpg",
    "https://telegra.ph/file/3986db1f05132ec799ef4.jpg",
    "https://telegra.ph/file/7bea67082d9bb648c4210.jpg",
    "https://telegra.ph/file/a9d891dab340566de3882.jpg",
    "https://telegra.ph/file/a55e21cee1dd03be2f4d3.jpg",
    "https://telegra.ph/file/3f5051e8194d2a554c153.jpg",
    "https://telegra.ph/file/abacfba1c4f25912fa7b3.jpg",
    "https://telegra.ph/file/92baf91c90e2f784148fa.jpg",
]


@register(pattern="^/logo ?(.*)")
async def lego(event):
    quew = event.pattern_match.group(1)
    if event.sender_id != OWNER_ID and not quew:
        await event.reply("**Please Gimmie A Text For The Logo**.")
        return
    pesan = await event.reply("**ᴍᴀᴋɪɴɢ ʏᴏᴜʀ ʟᴏɢᴏ.**\n **ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ!!!**")
    try:
        text = event.pattern_match.group(1)
        randc = random.choice(LOGO_LINKS)
        img = Image.open(io.BytesIO(requests.get(randc).content))
        draw = ImageDraw.Draw(img)
        image_widthz, image_heightz = img.size
        fnt = glob.glob("./YorForger/resources/LOGOS/*")
        randf = random.choice(fnt)
        font = ImageFont.truetype(randf, 140)
        w, h = draw.textsize(text, font=font)
        h += int(h * 0.21)
        image_width, image_height = img.size
        draw.text(
            ((image_widthz - w) / 2, (image_heightz - h) / 2),
            text,
            font=font,
            fill=(255, 255, 255),
        )
        x = (image_widthz - w) / 2
        y = (image_heightz - h) / 2 + 6
        draw.text(
            (x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black"
        )
        fname = "logo.png"
        img.save(fname, "png")
        vegeta = [[Button.url("MADE BY YOR FORGER", "t.me/YorForgerRobot")]]
        await tbot.send_file(event.chat_id, file=fname, buttons=yor)

        await pesan.delete()
        if os.path.exists(fname):
            os.remove(fname)
    except Exception as e:
        await event.reply(f"Error, Report @{SUPPORT_CHAT}, {e}")
