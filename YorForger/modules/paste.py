from requests import post, get
import os
import aiofiles
import requests 
import socket
from asyncio import get_running_loop
from functools import partial
from YorForger import pgram as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


def spacebin(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"


def _netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096).decode("utf-8").strip("\n\x00")
        if not data:
            break
        return data
    s.close()
    
async def ezup(content):
    loop = get_running_loop()
    link = await loop.run_in_executor(
        None, partial(_netcat, "ezup.dev", 9999, content)
    )
    return link



@bot.on_message(filters.command('paste'))
async def paste(_, m):
    reply = m.reply_to_message
    if not reply:
           await m.reply_text("Reply to Message or Text-File")
    if reply.document:
        doc = await m.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
          file_text = await f.read()
        os.remove(doc)
        spacebin_url = spacebin(file_text)
        link = await ezup(file_text)
        caption = f"[SPACEBIN]({spacebin_url}) | [EZUP.DEV]({link})"
        await m.reply_text(text=caption,
                      reply_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton("SPACEBIN", url=spacebin_url),
                         ],[ InlineKeyboardButton("EZUP.DEV", url=link)]]),disable_web_page_preview=True)
    elif reply.text or reply.caption:
          text = reply.text or reply.caption
          spacebin_url = spacebin(text)
          link = await ezup(text)
          caption = f"[SPACEBIN]({spacebin_url}) | [EZUP.DEV]({link})"
          await m.reply_text(text=caption,
                      reply_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton("SPACEBIN", url=spacebin_url),
                           ],[ InlineKeyboardButton("EZUP.DEV", url=link)]]),disable_web_page_preview=True)
    
        
        
