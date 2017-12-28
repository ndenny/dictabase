# pylint: disable=R0903
from dictabase.statement import DictaStatement


class DictaProperty:

    def __init__(self, parent, property_name):
        print('DictaProperty {}'.format(property_name))
        self.parent = parent
        self.property_name = property_name

    def __eq__(self, value):
        return DictaStatement(
            self.parent,
            self.property_name,
            '__eq__',
            value)

    def __ge__(self, value):
        return DictaStatement(
            self.parent,
            self.property_name,
            '__ge__',
            value)

    def __ne__(self, value):
        return DictaStatement(
            self.parent,
            self.property_name,
            '__ne__',
            value)

    def __lt__(self, value):
        return DictaStatement(
            self.parent,
            self.property_name,
            '__lt__',
            value)

    def __le__(self, value):
        return DictaStatement(
            self.parent,
            self.property_name,
            '__le__',
            value)

    def __gt__(self, value):
        return DictaStatement(
            self.parent,
            self.property_name,
            '__gt__',
            value)
