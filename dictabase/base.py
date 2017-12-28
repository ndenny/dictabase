from dictabase.property import DictaProperty
from dictabase.query import DictaQuery


class Dictabase(dict):

    def __getattr__(self, property_name):
        return DictaProperty(
            parent=self,
            property_name=property_name)

    def query(self, statement=None):
        statements = [statement] if statement else []
        return DictaQuery(self, statements)

    def __enter__(self):
        return DictaQuery(self, [])

    def __exit__(self, *args, **kwargs):
        pass
