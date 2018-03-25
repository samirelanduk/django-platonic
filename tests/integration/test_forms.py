from collections import OrderedDict
from unittest import TestCase
from .examples import *

class FormTests(TestCase):

    def test_basic_blank_forms(self):
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

        self.assertEqual(form.full_name.label, "Full Name:")
        self.assertEqual(form.favourite_number.label, "Favourite Number:")
        self.assertEqual(form.date_of_birth.label, "Date Of Birth:")

        # Fields are unique to instances
        form2 = QuestionForm()
        self.assertIsNot(form.full_name, form2.full_name)
        self.assertIsNot(form.favourite_number, form2.favourite_number)
        self.assertIsNot(form.date_of_birth, form2.date_of_birth)


    def test_fleshed_out_black_forms(self):
        # Create a fleshed out blank form
        form = FullQuestionForm()
        self.assertEqual(form.full_name.label, "What's you full name?")
        self.assertEqual(form.favourite_number.label, "You got a favourite number?")
        self.assertEqual(form.date_of_birth.label, "When were you manufactured?")
        form.full_name.label = "Give your name:"
        self.assertEqual(form.full_name.label, "Give your name:")


    def test_forms_html(self):
        form = QuestionForm()
        self.assertEqual(
         form.full_name.render(),
         '<input type="text" name="full_name" id="id_full_name">'
        )
        self.assertEqual(
         form.favourite_number.render(),
         '<input type="number" name="favourite_number" id="id_favourite_number">'
        )
        self.assertEqual(
         str(form.date_of_birth),
         '<input type="date" name="date_of_birth" id="id_date_of_birth">'
        )
        self.assertEqual(
         form.render().replace("\n", ""),
         '<form method="POST">'
         '<input type="text" name="full_name" id="id_full_name">'
         '<input type="number" name="favourite_number" id="id_favourite_number">'
         '<input type="date" name="date_of_birth" id="id_date_of_birth"></form>'
        )


    def test_fleshed_out_form_html(self):
        form = FullQuestionForm()
        self.assertEqual(
         form.render().replace("\n", ""),
         '<form method="POST">'
         '<label for="id_full_name">What\'s you full name?</label>'
         '<input type="text" name="full_name" id="id_full_name">'
         '<label for="id_favourite_number">You got a favourite number?</label>'
         '<input type="number" name="favourite_number" id="id_favourite_number">'
         '<label for="id_date_of_birth">When were you manufactured?</label>'
         '<input type="date" name="date_of_birth" id="id_date_of_birth"></form>'
        )
