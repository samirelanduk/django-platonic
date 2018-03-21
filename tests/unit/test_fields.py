from unittest import TestCase
from platonic.fields import Field

class FieldCreationTests(TestCase):

    def test_can_create_field(self):
        field = Field()
        self.assertIsNone(field._value)



class ValuePropertyTests(TestCase):

    def test_can_get_field_value(self):
        field = Field()
        field._value = "xyz"
        self.assertEqual(field._value, field.value)
