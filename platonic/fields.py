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
    :param str input_type: The input type of the field when rendered as HTML.
    :raises TypeError: if the label is not a string.
    :raises TypeError: if the input_type is not a string."""

    def __init__(self, label=None, input_type="text", html_attrs=None, initial=None):
        if label is not None and not isinstance(label, str):
            raise TypeError(f"Label {label} is not a string")
        if not isinstance(input_type, str):
            raise TypeError(f"Input type {input_type} is not a string")
        if html_attrs is not None and not isinstance(html_attrs, dict):
            raise TypeError(f"HTML attributes {html_attrs} is not a dict")
        for k, v in html_attrs.items() if html_attrs else {}:
            if not isinstance(k, str) or not isinstance(v, (str, bool)):
                raise ValueError(f"{k}:{v} is not valid")
        self._name = None
        self._value = initial if initial else None
        self._label = label
        self._input_type = input_type
        self._html_attrs = {} if html_attrs is None else html_attrs


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
        new.__dict__ = self.__dict__.copy()
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


    @property
    def input_type(self):
        """The input type of the Field when rendered as HTML.

        :raises TypeError: if you try and set the input_type to be a non-string.
        :rtype: ``str``"""

        return self._input_type


    @property
    def html_attrs(self):
        """The HTML attributes of the Field.

        :rtype: ``dict``"""

        return self._html_attrs


    @input_type.setter
    def input_type(self, input_type):
        if not isinstance(input_type, str):
            raise TypeError(f"Input type {input_type} is not a string")
        self._input_type = input_type


    def render(self):
        """Renders the field as HTML.

        :rtype: ``str`"""

        name = f' name="{self._name}"' if self._name else ""
        value = f' value="{self._value}"' if self._value else ""
        id_ = f' id="id_{self._name}"' if self._name else ""
        for_ = f' for="id_{self._name}"' if self._name else ""
        label = f"<label{for_}>{self._label}</label>\n" if self._label else ""
        attrs = ""
        for k, v in self._html_attrs.items():
            if v: attrs += f' {k}' if isinstance(v, bool) else f' {k}="{v}"'
        return f'{label}<input type="{self._input_type}"{name}{value}{id_}{attrs}>'
