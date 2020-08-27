import os
from django.conf import settings

# from dotenv import load_dotenv
#
# load_dotenv()

BOT_TOKEN = settings.BOT_TOKEN

admins = [
    settings.ADMIN_ID,
]

ip = settings.IP

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
