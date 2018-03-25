from .fields import Field

class Form:
    """Represents a form - an object with a list of data entry fields, the
    ability to produce an HTML representation of itself, and the ability to
    validate the data that is entered into it.

    When an instance of a form is created, the attributes of the Form class will
    be checked. If it is a field, four things will happen - (1) a copy of the
    field object will be made, (2) the form instance's field will be set to the
    copy rather than the original that lives in the class, (3) the field will
    be appended to the form's ``field`` attribute, (4) the new field's name will
    be set to whatever the class variable name was.

    Of course the base Form class has no such class attributes, but subclasses
    the user creates will.

    Forms are iterables of their fields."""

    def __new__(cls):
        form, form._fields = super(Form, cls).__new__(cls), []
        for attribute_name, attribute_obj in cls.__dict__.items():
            if isinstance(attribute_obj, Field):
                new_field = attribute_obj.copy()
                form.__dict__[attribute_name] = new_field
                form._fields.append(new_field)
                new_field.name = attribute_name
        return form


    def __repr__(self):
        return "<{} ({} field{})>".format(
         self.__class__.__name__,
         len(self._fields),
         "" if len(self._fields) == 1 else "s"
        )


    def __str__(self):
        return self.render()


    def __iter__(self):
        return iter(self._fields)


    @property
    def fields(self):
        """The fields that the form has, in the order that they were set.

        :rtype" ``tuple``"""

        return tuple(self._fields)


    def render(self):
        """Renders the form as HTML.

        :rtype: ``str`"""

        inputs = "\n".join([field.render() for field in self._fields])
        return f"<form method=\"POST\">\n{inputs}\n</form>"
