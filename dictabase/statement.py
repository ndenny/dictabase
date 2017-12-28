# pylint: disable=R0903


class DictaStatement:
    def __init__(self, parent, property_name,
                 func_name, value):
        print('DictaStatement: {} {} {}'.format(property_name, func_name, value))
        self.parent = parent
        self.property_name = property_name
        self.func_name = func_name
        self.value = value

    def __call__(self):
        dict_val = self.parent[self.property_name]
        func = getattr(dict_val, self.func_name)
        result = func(self.value)
        print("Is {} {} {}? {}".format(dict_val, self.func_name, self.value, result))
        return result
