from unittest import TestCase
from collections import OrderedDict
from unittest.mock import Mock, patch
from platonic.forms import Form
from platonic.fields import Field

class FormTest(TestCase):

    def setUp(self):
        class FormSub(Form): pass
        self.Form = FormSub
        self.field1 = Mock(Field)
        self.field2 = Mock(Field)
        self.Form.f1, self.Form.f2, self.Form.x = self.field1, self.field2, "a"



class FormCreationTests(FormTest):

    def test_can_create_form_with_fields(self):
        form = self.Form()
        self.assertEqual(form._fields, [self.field1, self.field2])
        self.assertIs(form.f1, self.field1)
        self.assertIs(form.f2, self.field2)
        self.assertEqual(form.f1._name, "f1")
        self.assertEqual(form.f2._name, "f2")



class FormReprTests(FormTest):

    def test_form_repr_1_field(self):
        form = self.Form()
        form._fields = [1]
        self.assertEqual(repr(form), "<FormSub (1 field)>")


    def test_form_repr_2_fields(self):
        form = self.Form()
        self.assertEqual(repr(form), "<FormSub (2 fields)>")



class FormIterationTests(FormTest):

    def test_form_is_iterable(self):
        form = self.Form()
        self.assertEqual(list(iter(form)), form._fields)



class FormFieldTests(FormTest):

    def test_can_get_fields(self):
        form = self.Form()
        self.assertEqual(form.fields, tuple(form._fields))
