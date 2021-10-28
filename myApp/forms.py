from flask_wtf omport FlaskForm
from wtforms import StringField, BooleanField, SubmitField

from wtdforms.validators import DataRequired

class TopCities(FlaskForm):
	city_name = StringField('City Name', validator=[DataRequired()]) #potentially add more validators later
	city_rank = StringField('City Rank', validator=[DataRequired()]) #only checks is atleadt one character is in the text box
	is_visted = BooleanField('Visted')
	submit = SubmitField('Submit')
	comments = StringField('Comments') #not to sure what this is needed for yet
