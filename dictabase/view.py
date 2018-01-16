import logging
from typing import Iterable

log = logging.getLogger(__name__)  # pylint: disable=C0103


class View(dict):

    def __init__(self, index: 'Index', data: Iterable['Model'], *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)
        log.debug('View.__init__')
        self.index = index

        sorted_data = sorted(data, key=index)
        for datum in sorted_data:
            self[self.index(datum)] = datum

    def query(self) -> 'Query':
        from .query import Query
        log.debug('View.query')
        return Query(self)
