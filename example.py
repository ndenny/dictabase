import logging
import os
import sys
import dictabase as db

logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s:%(levelname)s: %(message)s',
    level=os.environ.get('DEBUG_LEVEL') or logging.INFO)

log = logging.getLogger(__name__)  # pylint: disable=C0103

class ExampleModel(db.Model):
    name = db.Property()
    last = db.Property()
    id_num = db.Property()


DATASET = [
    ExampleModel(name="Nick", last="Hunter-Walker", id_num=43564),
    ExampleModel(name="Nick", last="Denny", id_num=12435),
    ExampleModel(name="Alan", last="Vezina", id_num=54321),
    ExampleModel(name="Don", last="Sheu", id_num=34512),
]

def main():

    with db.DictaBase(DATASET, indexes=('name', 'id_num')) as view:
        query = view.query()
        query = query.filter(ExampleModel.name > 'Joe')
        query = query.filter(ExampleModel.id_num > 12436)
        results = query.fetch()
        
        for result in results:
            log.info(result)

if __name__ == '__main__':
    main()
