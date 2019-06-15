from django.conf import settings

DISCORD_BOT_PARAM_SEPARATOR = getattr(settings, 'DISCORD_BOT_PARAM_SEPARATOR', ' ')
DISCORD_BOT_PREFIX = getattr(settings, 'DISCORD_BOT_PREFIX', '!')
DISCORD_TOKEN = getattr(settings, 'DISCORD_TOKEN', None)
