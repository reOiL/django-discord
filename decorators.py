"""
Decorators
"""
from django_discord_bot.apps import WebBot


def register():
    """
    Register discord command
    :return:
    """

    def _class_wrapper(command_class):
        """
        Wrapped class to discord command
        :param command_class:
        :return:
        """
        WebBot().register_command(command_class)
        return command_class

    return _class_wrapper
