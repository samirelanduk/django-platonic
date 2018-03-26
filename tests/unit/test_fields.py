from unittest import TestCase
from unittest.mock import Mock, patch
from platonic.fields import Field

class FieldCreationTests(TestCase):

    def test_can_create_field(self):
        field = Field()
        self.assertIsNone(field._name)
        self.assertIsNone(field._label)


    def test_can_create_field_with_name(self):
        field = Field(name="NNN")
        self.assertEqual(field._name, "NNN")
        self.assertIsNone(field._label)


    def test_can_create_field_with_label(self):
        field = Field(label="LLL")
        self.assertIsNone(field._name)
        self.assertEqual(field._label, "LLL")


    def test_field_name_must_be_str(self):
        with self.assertRaises(TypeError):
            Field(name=100)


    def test_field_name_must_be_valid_str(self):
        Field(name="name-right"), Field(name="name_right"), Field(name="RIGHT")
        with self.assertRaises(ValueError): Field(name="name wrong")
        with self.assertRaises(ValueError): Field(name="name@wrong")
        with self.assertRaises(ValueError): Field(name="name\x00wrong")
        with self.assertRaises(ValueError): Field(name="name.wrong")


    def test_field_label_must_be_str(self):
        with self.assertRaises(TypeError):
            Field(label=100)




class NameTests(TestCase):

    def test_can_get_field_name(self):
        field = Field(name="xyz")
        self.assertIs(field._name, field.name)


    def test_can_set_field_name(self):
        field = Field(name="xyz")
        field.name = "bbb"
        self.assertEqual(field._name, "bbb")


    def test_field_name_must_be_str(self):
        field = Field(name="xyz")
        with self.assertRaises(TypeError):
            field.name = 100


    def test_field_name_must_be_valid_str(self):
        field = Field(name="xyz")
        for right in "name-right", "name_right", "NAMERIGHT":
            field.name = right
        for wrong in "name wrong", "name@wrong", "name\x00wrong", "name.wrong":
            with self.assertRaises(ValueError):
                field.name = wrong



class LabelTests(TestCase):

    def test_can_get_label(self):
        field = Field(label="xyz")
        self.assertIs(field._label, field.label)


    def test_can_set_label(self):
        field = Field(label="xyz")
        field.label = "bbb"
        self.assertEqual(field._label, "bbb")


    def test_field_label_must_be_str(self):
        field = Field(label="xyz")
        with self.assertRaises(TypeError):
            field.label = 100



class LabelGenerationTests(TestCase):

    def test_can_return_label_when_no_name(self):
        field = Field()
        self.assertEqual(field.label_from_name(), "")


    def test_can_return_simple_label(self):
        field = Field(name="xyz")
        self.assertEqual(field.label_from_name(), "Xyz:")


    def test_can_return_label_with_underscores(self):
        field = Field(name="xyz_abc_123")
        self.assertEqual(field.label_from_name(), "Xyz Abc 123:")



class RawExtractionTests(TestCase):

    def test_can_get_value_when_no_name(self):
        field = Field()
        self.assertIsNone(field.get_raw_from_data_dict({"a": "b"}))


    def test_can_get_value_using_name(self):
        field = Field(name="a")
        self.assertEqual(field.get_raw_from_data_dict({"a": "b", "c": "d"}), "b")


    def test_can_get_missing_value_using_name(self):
        field = Field(name="x")
        self.assertIsNone(field.get_raw_from_data_dict({"a": "b", "c": "d"}))



class StringToPythonTests(TestCase):

    def test_string_becomes_string(self):
        field = Field()
        self.assertEqual(field.to_python("abc"), "abc")


    def test_none_becomes_empty_string(self):
        field = Field()
        self.assertEqual(field.to_python(None), "")




    '''def test_can_create_field_with_label(self):
        field = Field(label="Field label")
        self.assertIsNone(field._value)
        self.assertIsNone(field._name)
        self.assertEqual(field._label, "Field label")
        self.assertEqual(field._input_type, "text")
        self.assertEqual(field._html_attrs, {})


    def test_can_create_field_with_input_type(self):
        field = Field(input_type="number")
        self.assertIsNone(field._value)
        self.assertIsNone(field._name)
        self.assertIsNone(field._label)
        self.assertEqual(field._input_type, "number")
        self.assertEqual(field._html_attrs, {})


    def test_can_create_field_with_html_attributes(self):
        field = Field(html_attrs={"a": "b"})
        self.assertIsNone(field._value)
        self.assertIsNone(field._name)
        self.assertIsNone(field._label)
        self.assertEqual(field._input_type, "text")
        self.assertEqual(field._html_attrs, {"a": "b"})


    def test_can_create_field_with_initial_value(self):
        field = Field(initial="III")
        self.assertEqual(field._value, "III")
        self.assertIsNone(field._name)
        self.assertIsNone(field._label)
        self.assertEqual(field._input_type, "text")
        self.assertEqual(field._html_attrs, {})


    def test_field_label_must_be_str(self):
        with self.assertRaises(TypeError):
            Field(label=100)


    def test_field_type_must_be_str(self):
        with self.assertRaises(TypeError):
            Field(input_type=100)


    def test_field_html_attrs_must_be_dict(self):
        with self.assertRaises(TypeError):
            Field(html_attrs=100)


    def test_field_html_attrs_must_be_valid(self):
        with self.assertRaises(ValueError):
            Field(html_attrs={100: "val"})
        with self.assertRaises(ValueError):
            Field(html_attrs={True: "val"})
        with self.assertRaises(ValueError):
            Field(html_attrs={"key": 100})
        Field(html_attrs={"key": True})



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
    def test_field_str(self, mock_render):
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







class InputTypePropertyTests(TestCase):

    def test_can_get_field_input_type(self):
        field = Field(input_type="xyz")
        self.assertEqual(field._input_type, field.input_type)


    def test_can_set_field_input_type(self):
        field = Field(input_type="xyz")
        field.input_type = "bbb"
        self.assertEqual(field._input_type, "bbb")


    def test_field_name_must_be_str(self):
        field = Field(input_type="xyz")
        with self.assertRaises(TypeError):
            field.input_type = 100



class HtmlAttrsPropertyTests(TestCase):

    def test_can_get_html_attrs(self):
        field = Field(html_attrs={"a": "b"})
        self.assertIs(field._html_attrs, field.html_attrs)



class FieldRenderingTests(TestCase):

    def test_basic_field_rendering(self):
        field = Field(input_type="xyz")
        self.assertEqual(field.render(), '<input type="xyz">')


    def test_field_with_name_rendering(self):
        field = Field()
        field._name = "N"
        self.assertEqual(field.render(), '<input type="text" name="N" id="id_N">')


    def test_field_with_value_rendering(self):
        field = Field()
        field._value = "V"
        self.assertEqual(field.render(), '<input type="text" value="V">')


    def test_field_with_label_rendering(self):
        field = Field(label="LLL")
        self.assertEqual(field.render(), '<label>LLL</label>\n<input type="text">')


    def test_field_with_label_and_name_rendering(self):
        field = Field(label="LLL")
        field._name = "N"
        self.assertEqual(
         field.render(),
         '<label for="id_N">LLL</label>\n<input type="text" name="N" id="id_N">'
        )


    def test_field_rendering_with_attribures(self):
        field = Field(html_attrs={"a": "b", "c": True, "d": False})
        self.assertEqual(field.render(), '<input type="text" a="b" c>')'''
