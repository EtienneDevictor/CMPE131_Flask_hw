from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

from wtforms.validators import DataRequired

class TopCities(FlaskForm):
	city_name = StringField('City Name', validators=[DataRequired()]) #potentially add more validators later
	city_rank = StringField('City Rank', validators=[DataRequired()]) #only checks is atleadt one character is in the text box
	is_visted = BooleanField('Visted')
	submit = SubmitField('Submit')
	comments = StringField('Comments') #not to sure what this is needed for yet

	
