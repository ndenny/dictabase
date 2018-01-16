import logging
from typing import Iterable
from . import Model

log = logging.getLogger(__name__)  # pylint: disable=C0103


class Index:

    def __init__(self, keys: Iterable[str]):
        log.debug('Index.__index__ %s', keys)
        self.keys = keys

    def __call__(self, model: Model) -> tuple:
        log.debug('Index.__call__ %s', model)
        # Sets and Lists are unhashable, so can't be keys of a dict!
        return tuple(getattr(model, key) for key in self.keys)

    def __repr__(self):
        return 'Index ({})'.format(self.keys)
