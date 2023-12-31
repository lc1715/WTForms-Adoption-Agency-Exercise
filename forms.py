from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, URL, Optional, NumberRange, Length


class PetForm(FlaskForm):

    pet_name = StringField('Pet Name', validators=[InputRequired("Name can't be blank")])
    species = SelectField('Species', choices=[('dog', 'Dog'), ('cat', 'Cat'), ('porcupine', 'Porcupine')])
    photo_url = StringField('Photo URL', validators=[URL("Invalid URL"), Optional()])
    age = IntegerField('Age', validators=[NumberRange(0, 30, 'Please put in an age between 0 and 30.')])
    notes = TextAreaField('Comments', validators=[Optional(), Length(min=10)])
    available = BooleanField('Available')
