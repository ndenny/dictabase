"""DictaBase - Dictionaries are Magic. And maybe even Databases."""
from .statement import Statement
from .property import Property
from .model import Model
from .view import View
from .query import Query
from .index import Index
from .base import DictaBase

__all__ = ['DictaBase', 'Index', 'Model', 'Property', 'Query', 'Statement', 'View', ]

__version__ = '0.1'
