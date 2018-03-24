
class Field:

    def __init__(self, label=None):
        if label is not None and not isinstance(label, str):
            raise TypeError(f"Label {label} is not a string")
        self._name = None
        self._value = None
        self._label = label


    def copy(self):
        new = Field()
        new.__dict__ = self.__dict__
        return new


    @property
    def name(self):
        return self._name


    @property
    def value(self):
        return self._value


    @property
    def label(self):
        return self.label_from_name() if self._label is None else self._label


    @label.setter
    def label(self, label):
        if not isinstance(label, str):
            raise TypeError(f"Label {label} is not a string")
        self._label = label


    def label_from_name(self):
        words = map(str.title, self._name.split("_"))
        label = " ".join(words)
        return f"{label}:"
