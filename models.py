from django.db import models


# Create your models here.

class BotLog(models.Model):
    """
    Discord bot message log
    """
    discord_id = models.IntegerField(verbose_name='Discord user id')
    discord_name = models.CharField(max_length=32, verbose_name='Discord user ID')
    message = models.CharField(max_length=2000, verbose_name='Message')
