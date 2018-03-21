from collections import OrderedDict
from unittest import TestCase
from .examples import QuestionForm

class FormTests(TestCase):

    def test_blank_forms(self):
        # Create a blank form
        form = QuestionForm()

        # Check its fields
        self.assertEqual(form.fields, (
         form.name,
         form.favourite_number,
         form.date_of_birth
        ))
        for field in form:
            self.assertIsNone(field.value)
