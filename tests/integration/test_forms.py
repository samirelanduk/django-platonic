from collections import OrderedDict
from unittest import TestCase
from .examples import *

class FormTests(TestCase):

    def test_blank_forms(self):
        # Create a basic blank form
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

        # Create a fleshed out blank form
        form = FullQuestionForm()
        self.assertEqual(form.full_name.label, "What's you full name?")
        self.assertEqual(form.favourite_number.label, "You got a favourite number?")
        self.assertEqual(form.date_of_birth.label, "When were you manufactured?")
        form.full_name.label = "Give your name:"
        self.assertEqual(form.full_name.label, "Give your name:")
