import logging
from . import Property

log = logging.getLogger(__name__)  # pylint: disable=C0103


class Model:

    def __init__(self, **kwargs):
        log.debug('Model.__init__ %s', kwargs)

        cls = self.__class__
        for name in set(dir(cls)):
            prop = getattr(cls, name, None)
            if isinstance(prop, Property):
                prop.name = name
                setattr(self, name, kwargs.get(name, prop.default))

    def __repr__(self):
        props = []
        for name in dir(self.__class__):
            prop = getattr(self.__class__, name)
            if isinstance(prop, Property):
                props.append('{}={}'.format(name, getattr(self, name)))
        return "{}: {}".format(self.__class__.__name__, ', '.join(props))
