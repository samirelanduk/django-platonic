import re

class Field:
    """A field represents a data entry component in a form.

    All fields have a name and a label. The name is its internal identifier,
    and becomes the ``name`` attribute in the HTML. The label is the human
    readable description of the field, and becomes the ``<label>`` content.

    Fields also have a value - the data that has been entered into it. This is a
    Python object of some kind, though it will have to be converted to a string
    when it goes to HTML land.

    The name and value of a field are both ``None`` when a field is created.

    :param str label: The label of the field.
    :raises TypeError: if the label is not a string."""

    def __init__(self, label=None):
        if label is not None and not isinstance(label, str):
            raise TypeError(f"Label {label} is not a string")
        self._name = None
        self._value = None
        self._label = label


    def __repr__(self):
        name = f" name='{self._name}'" if self._name else ""
        value = f" value='{self._value}'" if self._value else ""
        return f"<Field{name}{value}>"


    def __str__(self):
        return self.render()


    def copy(self):
        """Creates a copy of this Field, with all the same attributes.

        :rtype: ``Field``"""

        new = Field()
        new.__dict__ = self.__dict__
        return new


    @property
    def name(self):
        """The name of the field - its internal identifier.

        :raises TypeError: if you try to set a name that isn't a string.
        :raises ValueError: if the name has invalid characters - letters,\
        numbers, dashes, and underscores are fine.
        :rtype: ``str``"""

        return self._name


    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError(f"Name {name} is not a string")
        if re.compile(r"[^a-zA-Z0-9\-\_]").search(name):
            raise ValueError(f"'{name}' is not a valid name")
        self._name = name


    @property
    def value(self):
        """The value of the field - the data that has been entered into the
        field.

        :rtype: ``str``"""

        return self._value


    @property
    def label(self):
        """The label of the field - the human understandable description of
        the field. If there isn't one, one will be generated from the name.

        :raises TypeError: if you try and set the label to be a non-string.
        :rtype: ``str``"""

        return self.label_from_name() if self._label is None else self._label


    @label.setter
    def label(self, label):
        if not isinstance(label, str):
            raise TypeError(f"Label {label} is not a string")
        self._label = label


    def label_from_name(self):
        """Generates a label from the field's name. Underscores will be turned
        into spaces, and words will be title cased.

        :rtype: ``str``"""

        words = map(str.title, self._name.split("_"))
        label = " ".join(words)
        return f"{label}:"


    def render(self):
        name = f' name="{self._name}"' if self._name else ""
        return f'<input type="text"{name}>'
