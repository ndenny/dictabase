from dictabase.base import Dictabase


class DictaQuery:
    def __init__(self, parent, statements):
        self.parent = parent
        self.statements = statements
        print('DictaQuery: {} statements'.format(len(self.statements)))

    def filter(self, statement):
        return DictaQuery(
            self.parent,
            self.statements + [statement])

    def run(self):
        answer = Dictabase()

        for statement in self.statements:
            if statement():
                prop = statement.property_name
                answer[prop] = statement.parent[prop]

        return answer
