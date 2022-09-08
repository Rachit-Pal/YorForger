from geopy.geocoders import Nominatim
from telegram import Location, ParseMode
from telegram.ext import CommandHandler, run_async

from YorForger import dispatcher
from YorForger.modules.helper_funcs.chat_status import user_admin

GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"



def gps(update, context, *args, **kwargs):

    args = context.args
    message = update.effective_message
    if len(args) == 0:
        message.reply_text(
            "That was a funny joke, but no really, put in a location"
        )
    try:
        geolocator = Nominatim(user_agent="SkittBot")
        location = " ".join(args)
        geoloc = geolocator.geocode(location)
        chat_id = update.effective_chat.id
        lon = geoloc.longitude
        lat = geoloc.latitude
        the_loc = Location(lon, lat)
        gm = "https://www.google.com/maps/search/{},{}".format(lat, lon)
        dispatcher.bot.send_location(chat_id, location=the_loc)
        message.reply_text(
            f"*Check from google:*\n[google Location]({gm})",
            parse_mode=ParseMode.MARKDOWN
        )
    except AttributeError:
        update.message.reply_text("I can't find that")


    
GPS_HANDLER = CommandHandler("gps", gps,run_async=True)

dispatcher.add_handler(GPS_HANDLER)


