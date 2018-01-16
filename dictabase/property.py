import logging
from . import Statement

log = logging.getLogger(__name__)  # pylint: disable=C0103


class Property:
    def __init__(self, name: str = None, value: object = None):
        log.debug('Property.__init__ %s', name)
        self.name = name
        self.value = value

    def __eq__(self, value):
        return Statement(self.name, '__eq__', value)

    def __ge__(self, value):
        return Statement(self.name, '__ge__', value)

    def __ne__(self, value):
        return Statement(self.name, '__ne__', value)

    def __lt__(self, value):
        return Statement(self.name, '__lt__', value)

    def __le__(self, value):
        return Statement(self.name, '__le__', value)

    def __gt__(self, value):
        return Statement(self.name, '__gt__', value)
