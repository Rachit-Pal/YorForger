from datetime import datetime

from gtts import gTTS
from telegram import ChatAction, Update
from telegram.ext import CallbackContext

from YorForger import dispatcher
from YorForger.modules.disable import DisableAbleCommandHandler


def tts(update: Update, context: CallbackContext):
    args = context.args
    current_time = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
    datetime.now().strftime("%d%m%y-%H%M%S%f")
    reply = " ".join(args)
    update.message.chat.send_action(ChatAction.RECORD_AUDIO)
    lang = "ml"
    tts = gTTS(reply, lang)
    tts.save("k.mp3")
    with open("k.mp3", "rb") as f:
        linelist = list(f)
        linecount = len(linelist)
    if linecount == 1:
        update.message.chat.send_action(ChatAction.RECORD_AUDIO)
        lang = "en"
        tts = gTTS(reply, lang)
        tts.save("k.mp3")
    with open("k.mp3", "rb") as speech:
        update.message.reply_voice(speech, quote=False)


TTS_HANDLER = DisableAbleCommandHandler("tts", tts, pass_args=True, run_async=True)
dispatcher.add_handler(TTS_HANDLER)

__mod_name__ = "ᴛᴛs"
__command_list__ = ["tts"]
__handlers__ = [TTS_HANDLER]
