import logging
from typing import Optional, Iterable
from . import View
from . import Model
from . import Statement


log = logging.getLogger(__name__)  # pylint: disable=C0103


class Query:

    def __init__(self, view: View, statements: Optional[Iterable[Statement]] = None):
        log.debug('Query.__init__')
        self.view = view
        self.statements = statements or []

    def filter(self, statement: Statement) -> 'Query':
        log.debug('Query.filter')
        return Query(self.view, self.statements + [statement])

    def fetch(self) -> Iterable[Model]:
        log.debug('Query.fetch')
        return (val for key, val in self.view.items() if all(statement(self.view.indexer, key) for statement in self.statements))
