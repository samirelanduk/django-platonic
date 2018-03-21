from collections import OrderedDict
from .fields import Field
import inspect


class Form:

    def __new__(cls):
        form = super(Form, cls).__new__(cls)
        form._fields = []
        for attribute_name, attribute_obj in cls.__dict__.items():
            if isinstance(attribute_obj, Field):
                form.__dict__[attribute_name] = attribute_obj
                form._fields.append(attribute_obj)
        return form


    def __repr__(self):
        return "<{} ({} field{})>".format(
         self.__class__.__name__,
         len(self._fields),
         "" if len(self._fields) == 1 else "s"
        )


    @property
    def fields(self):
        return tuple(self._fields)
