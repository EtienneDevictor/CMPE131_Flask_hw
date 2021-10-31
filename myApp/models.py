from myApp import db

class City(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	city = db.Column(db.String(64), index=True, unique=True)
	rank = db.Column(db.Integer, index=True, unique=True)
	visited = db.Column(db.Boolean)

	def __repr__(self):
		return f'<City: {self.city}'
