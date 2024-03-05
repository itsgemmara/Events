from pydantic import types
from base import Event, EventMeta

class Fields:
    fieldnames = [attr for attr in dir(types) if not attr.startswith("__")]

    for fieldname in fieldnames:
        globals()[fieldname] = types.__dict__[fieldname]

    def __getattr__(self, _name):
        return getattr(types, _name)

fields = Fields()

from .decorators import event

@event
class A(Event):
    pass