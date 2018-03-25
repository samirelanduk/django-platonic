from platonic import Form, Field

class QuestionForm(Form):

    full_name = Field()
    favourite_number = Field(input_type="number")
    date_of_birth = Field(input_type="date")



class FullQuestionForm(Form):

    full_name = Field(label="What's you full name?")
    favourite_number = Field(
     input_type="number", label="You got a favourite number?"
    )
    date_of_birth = Field(input_type="date", label="When were you manufactured?")
