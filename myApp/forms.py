from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

from wtforms.validators import DataRequired

class TopCities(FlaskForm):
	city_name = StringField('City Name', validators=[DataRequired()]) #potentially add more validators later
	city_rank = StringField('City Rank', validators=[DataRequired()]) #only checks is atleadt one character is in the text box
	is_visited = BooleanField('Visited')
	submit = SubmitField('Submit')
	

	
