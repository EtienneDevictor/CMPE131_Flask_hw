from myApp import db

class City(db.Model):
	city = db.Column(db.String(64), index=True, unique=True)
	rank = db.Column(db.Integer, primary_key=True)
	visited = db.Column(db.Boolean)

	def __repr__(self):
		return f'{self.city}'

	def exists(self, city_name, rank):
		cities = self.query.all()
		for city in cities:
			if city_name == city.city:
				return -1
			if rank == city.rank:
				return 1
		return 0

