"""DictaBase - Dictionaries are Magic. And maybe even Databases."""
from .statement import DictaStatement
from .property import DictaProperty
from .query import DictaQuery
from .base import DictaBase

__all__ = ['DictaBase', 'DictaProperty', 'DictaQuery', 'DictaStatement']

__version__ = '0.1'
