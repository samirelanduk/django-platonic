'''from unittest import TestCase
from collections import OrderedDict
from unittest.mock import Mock, patch
from platonic.forms import Form
from platonic.fields import Field

class FormTest(TestCase):

    def setUp(self):
        class FormSub(Form): pass
        self.Form = FormSub
        self.fieldA, self.fieldB = Mock(Field), Mock(Field)
        self.field1, self.field2 = Mock(Field), Mock(Field)
        self.Form.f1, self.Form.f2, self.Form.x = self.fieldA, self.fieldB, "a"
        self.fieldA.copy.return_value = self.field1
        self.fieldB.copy.return_value = self.field2



class FormCreationTests(FormTest):

    def test_can_create_form_with_fields(self):
        form = self.Form()
        self.fieldA.copy.assert_called_with()
        self.fieldB.copy.assert_called_with()
        self.assertIs(form.f1, self.field1)
        self.assertIs(form.f2, self.field2)
        self.assertEqual(form._fields, [self.field1, self.field2])
        self.assertEqual(form.f1.name, "f1")
        self.assertEqual(form.f2.name, "f2")



class FormReprTests(FormTest):

    def test_form_repr_1_field(self):
        form = self.Form()
        form._fields = [1]
        self.assertEqual(repr(form), "<FormSub (1 field)>")


    def test_form_repr_2_fields(self):
        form = self.Form()
        self.assertEqual(repr(form), "<FormSub (2 fields)>")



class FormStrTests(FormTest):

    @patch("platonic.forms.Form.render")
    def test_form_str(self, mock_render):
        mock_render.return_value = "SSS"
        form = self.Form()
        self.assertEqual(str(form), "SSS")
        mock_render.assert_called_with()



class FormIterationTests(FormTest):

    def test_form_is_iterable(self):
        form = self.Form()
        self.assertEqual(list(iter(form)), form._fields)



class FormFieldTests(FormTest):

    def test_can_get_fields(self):
        form = self.Form()
        self.assertEqual(form.fields, tuple(form._fields))



class FormRenderingTests(FormTest):

    def setUp(self):
        FormTest.setUp(self)
        self.field1.render.return_value = "AAA"
        self.field2.render.return_value = "BBB"


    def test_can_render_form(self):
        form = self.Form()
        self.assertEqual(
         form.render(),
         "<form method=\"POST\">\nAAA\nBBB\n</form>"
        )
        self.field1.render.assert_called_with()
        self.field2.render.assert_called_with()
'''
