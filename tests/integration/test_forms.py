from collections import OrderedDict
from unittest import TestCase
from .examples import QuestionForm

class FormTests(TestCase):

    def test_blank_forms(self):
        # Create a blank form
        form = QuestionForm()

        # Check its fields
        self.assertEqual(form.fields, (
         form.full_name,
         form.favourite_number,
         form.date_of_birth
        ))
        for field in form:
            self.assertIsNone(field.value)
        self.assertEqual(form.full_name.name, "full_name")
        self.assertEqual(form.favourite_number.name, "favourite_number")
        self.assertEqual(form.date_of_birth.name, "date_of_birth")
