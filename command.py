"""
Basic command class
"""
from abc import abstractmethod


class BasicTypeArg:
    verbose_name = None
    val = ''

    def __str__(self):
        """Overload string cast"""
        return str(self.val)

    def __unicode__(self):
        """Overload unicode cast"""
        return self.val.encode('utf-8')

    def __int__(self):
        """Overload integer"""
        return int(self.val)

    def __float__(self):
        """Overload float"""
        return float(self.val)

    def __bool__(self):
        """Overload bool"""
        return bool(self.val)

    def __init__(self, verbose_name=None):
        """
        Init basic type
        :param verbose_name: Printable object name
        """
        self.verbose_name = verbose_name

    @abstractmethod
    def clean(self):
        """
        Clean argument, mut be overload in children
        :return: list if size = 0, no error
        """
        pass


class StrArg(BasicTypeArg):
    max_length = None
    min_length = None

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        """
        Initial string object
        :param max_length: maximum string length
        :param min_length: minimal string length
        :param args: args
        :param kwargs: kwargs
        """
        super().__init__(*args, **kwargs)
        self.max_length = max_length
        self.min_length = min_length

    def clean(self):
        _errors = []
        try:
            self.val = str(self.val)
        except ValueError:
            return ['Must be string']
        if isinstance(self.max_length, int):
            if len(self.val) > self.max_length:
                _errors.append('Max size is %i' % self.max_length)
        if isinstance(self.min_length, int):
            if len(self.val) < self.min_length:
                _errors.append('Min size is %i' % self.min_length)
        return _errors


class IntegerArg(BasicTypeArg):
    minimal = None
    maximum = None

    def __init__(self, minimal=None, maximum=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        _errors = []
        try:
            self.val = int(self.val)
        except ValueError:
            return ['Must be integer']
        if isinstance(self.maximum, int):
            if self.val > self.maximum:
                _errors.append('Maximum value is %s' % self.maximum)
        if isinstance(self.minimal, int):
            if self.val < self.minimal:
                _errors.append('Maximum value is %s' % self.minimal)
        return _errors


class Command:
    """
    Command class used for commands in discord
    """
    command = ''
    help_text = ''
    fields = []

    def __init__(self):
        """
        Overload init method
        """

    @abstractmethod
    async def exec(self, original_message):
        """
        If command success cleaned, this method will be called
        :type original_message: Discord original message
        :return: None
        """
        pass

    def clean(self, original_message):
        """
        Clean form
        :return: None
        """
        spliced_msg = original_message.content.split(' ')[1:]
        _error = {}
        if len(spliced_msg) != len(self.fields):
            return {'Command': ['Not enough arguments']}
        """
        for filed, value in self.fields, spliced_msg:
            filed.val = value
            errs = filed.clean()
            if len(errs):
                _error[filed.verbose_name] = errs
        """
        return _error
