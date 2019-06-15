"""
Basic command class
"""
from abc import abstractmethod


class BasicTypeArg:
    @abstractmethod
    def clean(self):
        """
        Clean argument, mut be overload in children
        :return: true if success
        """
        pass


class CharArg(BasicTypeArg):
    def clean(self):
        pass


class IntegerArg(BasicTypeArg):
    def clean(self):
        pass


class Command:
    """
    Command class used for commands in discord
    """
    command = ''
    help_text = ''

    def __init__(self):
        """
        Overload init method
        """
        pass

    @abstractmethod
    def exec(self):
        """
        If command success cleaned, this method will be called
        :return: None
        """
        pass

    def clean(self):
        pass
