from platonic import Form, Field

class QuestionForm(Form):

    full_name = Field()
    favourite_number = Field()
    date_of_birth = Field()



class FullQuestionForm(Form):

    full_name = Field(label="What's you full name?")
    favourite_number = Field(label="You got a favourite number?")
    date_of_birth = Field(label="When were you manufactured?")
