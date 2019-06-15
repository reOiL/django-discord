import asyncio

from django.apps import AppConfig
import discord
from threading import Thread

from django_discord_bot.command import Command

import django_discord_bot.settings as settings


class DjangoDiscordBotConfig(AppConfig):
    name = 'django_discord_bot'


class WebBot(Thread):
    _instance = None
    COMMANDS = {}
    event_loop = asyncio.new_event_loop()

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

    def run(self) -> None:
        if self.event_loop is not None:
            self.event_loop.add_signal_handler = lambda x, y: None
        client = discord.Client(loop=self.event_loop)

        @client.event
        async def on_message(message: discord.message.Message):
            """
            Discord event when user send message
            :param message: user message
            :return: None
            """

            if message.author == client.user:
                # Bot not need read him self message
                return
            command_msg_txt = message.content
            if command_msg_txt[0:len(settings.DISCORD_BOT_PREFIX)] != settings.DISCORD_BOT_PREFIX:
                return

            clear_msg_txt = str(command_msg_txt[len(settings.DISCORD_BOT_PREFIX):])
            if clear_msg_txt == '':
                return
            msg_separate = clear_msg_txt.split(settings.DISCORD_BOT_PARAM_SEPARATOR)
            if msg_separate[0] not in self.COMMANDS:
                # await self.COMMANDS['wrong_command'](message.channel, msg_separate, message)
                # TODO: Add help message
                pass
            else:
                # Execute command
                await self.COMMANDS[clear_msg_txt](message.channel, msg_separate, message)

        @client.event
        async def on_ready():
            """
            On bot ready
            :return: None
            """
            print('Bot has login success as {}\n'.format(client.user.name))

        if settings.DISCORD_TOKEN is None:
            raise ValueError("Undefined discord token in settings DISCORD_TOKEN")
        client.run(settings.DISCORD_TOKEN)
