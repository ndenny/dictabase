import logging

log = logging.getLogger(__name__)  # pylint: disable=C0103


class Statement:

    def __init__(self, name: str, func_name: str, value: object):
        log.debug('Statement.__init__: %s %s %s', name, func_name, value)
        self.name = name
        self.func_name = func_name
        self.value = value

    def __call__(self, index: 'Index', key: object) -> object:
        log.debug('Statement.__call__: %s %s %s %s %s', self.name, self.func_name, self.value, index, key)
        key_pos = index.keys.index(self.name)
        index_key = key[key_pos]
        func = getattr(index_key, self.func_name)
        result = func(self.value)
        log.debug("Is %s %s %s? %s", index_key, self.func_name, self.value, result)
        return result
