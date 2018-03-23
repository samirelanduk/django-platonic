
class Field:

    def __init__(self, label=None):
        if label is not None and not isinstance(label, str):
            raise TypeError(f"Label {label} is not a string")
        self._name = None
        self._value = None
        self._label = label


    @property
    def name(self):
        return self._name


    @property
    def value(self):
        return self._value


    @property
    def label(self):
        return self._label


    @label.setter
    def label(self, label):
        if not isinstance(label, str):
            raise TypeError(f"Label {label} is not a string")
        self._label = label
