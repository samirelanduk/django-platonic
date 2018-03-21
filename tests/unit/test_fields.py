from unittest import TestCase
from platonic.fields import Field

class FieldCreationTests(TestCase):

    def test_can_create_field(self):
        field = Field()
