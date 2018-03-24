from unittest import TestCase
from unittest.mock import Mock, patch
from platonic.fields import Field

class FieldCreationTests(TestCase):

    def test_can_create_field(self):
        field = Field()
        self.assertIsNone(field._value)
        self.assertIsNone(field._name)
        self.assertIsNone(field._label)


    def test_can_create_field_with_label(self):
        field = Field(label="Field label")
        self.assertIsNone(field._value)
        self.assertIsNone(field._name)
        self.assertEqual(field._label, "Field label")


    def test_field_label_must_be_str(self):
        with self.assertRaises(TypeError):
            Field(label=100)



class FieldReprTests(TestCase):

    def test_basic_field_repr(self):
        field = Field()
        self.assertEqual(repr(field), "<Field>")


    def test_field_repr_with_attributes(self):
        field = Field(label="Field label")
        field._name, field._value = "N", "V"
        self.assertEqual(repr(field), "<Field name='N' value='V'>")



class FieldStrTests(TestCase):

    @patch("platonic.fields.Field.render")
    def test_basic_field_str(self, mock_render):
        mock_render.return_value = "SSS"
        field = Field()
        self.assertEqual(str(field), "SSS")
        mock_render.assert_called_with()



class FieldCopyingTests(TestCase):

    def test_can_copy_field(self):
        field = Field(label="Field label")
        field2 = field.copy()
        self.assertIsNot(field, field2)
        self.assertEqual(field.__dict__, field2.__dict__)



class NamePropertyTests(TestCase):

    def test_can_get_field_name(self):
        field = Field()
        field._name = "xyz"
        self.assertEqual(field._name, field.name)


    def test_can_set_field_name(self):
        field = Field()
        field.name = "bbb"
        self.assertEqual(field._name, "bbb")


    def test_field_name_must_be_str(self):
        field = Field()
        with self.assertRaises(TypeError):
            field.name = 100


    def test_field_name_must_be_valid_str(self):
        field = Field()
        field.name = "name-right"
        field.name = "name_right"
        field.name = "NAMERIGHT"
        with self.assertRaises(ValueError):
            field.name = "name wrong"
        with self.assertRaises(ValueError):
            field.name = "name@wrong"
        with self.assertRaises(ValueError):
            field.name = "name\x00wrong"
        with self.assertRaises(ValueError):
            field.name = "name.wrong"



class ValuePropertyTests(TestCase):

    def test_can_get_field_value(self):
        field = Field()
        field._value = "xyz"
        self.assertEqual(field._value, field.value)



class LabelPropertyTests(TestCase):

    def test_can_get_label(self):
        field = Field(label="xyz")
        self.assertEqual(field._label, field.label)


    @patch("platonic.fields.Field.label_from_name")
    def test_can_generate_label_when_none(self, mock_label):
        mock_label.return_value = "XYZ"
        field = Field()
        self.assertEqual(field.label, "XYZ")
        mock_label.assert_called_with()



    def test_can_set_label(self):
        field = Field(label="xyz")
        field.label = "bbb"
        self.assertEqual(field._label, "bbb")


    def test_field_label_must_be_str(self):
        field = Field(label="xyz")
        with self.assertRaises(TypeError):
            field.label = 100



class LabelGenerationTests(TestCase):

    def test_can_return_simple_label(self):
        field = Field()
        field._name = "xyz"
        self.assertEqual(field.label_from_name(), "Xyz:")


    def test_can_return_label_with_underscores(self):
        field = Field()
        field._name = "xyz_abc_123"
        self.assertEqual(field.label_from_name(), "Xyz Abc 123:")



class FieldRenderingTests(TestCase):

    def test_basic_field_rendering(self):
        field = Field()
        self.assertEqual(field.render(), '<input type="text">')


    def test_field_with_name_rendering(self):
        field = Field()
        field._name = "N"
        self.assertEqual(field.render(), '<input type="text" name="N">')
