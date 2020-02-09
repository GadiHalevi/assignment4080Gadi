from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CountryFormStructure(FlaskForm):
    name = StringField('Country Name?')
    validators = [DataRequired()]
    submit = SubmitField('Submit')
    


