from pydantic import types
from base import Event

class Fields:
    fieldnames = [attr for attr in dir(types) if not attr.startswith("__")]

    for fieldname in fieldnames:
        globals()[fieldname] = types.__dict__[fieldname]

    def __getattr__(self, _name):
        return getattr(types, _name)

fields = Fields()



# class testeve541nt(Event):
#     some_field: str = '4'
#     some: int

# class testeventdc2(Event):
#     fieldddd: str = '2'