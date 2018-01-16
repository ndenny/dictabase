import logging
from typing import Iterable
from . import Index
from . import Model
from . import View

log = logging.getLogger(__name__)  # pylint: disable=C0103


class DictaBase:

    def __init__(self, data: Iterable[Model], indexes: Iterable[Index]):
        self.data = data
        index = Index(indexes)
        self.view = View(index, data)

    def __enter__(self) -> View:
        log.debug("DictaBase.__enter__")
        return self.view

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug("DictaBase.__exit__ %s %s %s", exc_type, exc_val, exc_tb)
