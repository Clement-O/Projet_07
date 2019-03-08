from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

""" Module to create HTML form """


class InputForm(FlaskForm):
    """
    Create an input field and a submit button
    """
    formInput = StringField(validators=[DataRequired()])
    submit = SubmitField()
