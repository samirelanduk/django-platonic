from datetime import datetime
from platonic import Form, Field

class QuestionForm(Form):

    full_name = Field()
    favourite_number = Field(input_type="number")
    date_of_birth = Field(input_type="date")



class FullQuestionForm(Form):

    full_name = Field(
     label="What's you full name?",
     initial="Joe Blow"
    )
    favourite_number = Field(
     input_type="number",
     label="You got a favourite number?",
     initial=50,
     html_attrs={"placeholder": "A number", "autocomplete": "off", "readonly": True},
    )

    date_of_birth = Field(
     input_type="date",
     label="When were you manufactured?",
     initial=datetime(2009, 4, 9).date()
    )
