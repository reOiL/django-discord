from django.apps import AppConfig
import discord

from django_discord_bot.command import Command


class DjangoDiscordBotConfig(AppConfig):
    name = 'django_discord_bot'


class WebBot:
    _instance = None
    COMMANDS = {}

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, WebBot):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def register_command(self, command: Command):
        if not isinstance(command, Command):
            raise ValueError("%s is not a based on Command class" % command)
        if command.command in self.COMMANDS:
            raise ValueError("Command %s is already exist" % command.command)
        self.COMMANDS[command.command] = command
