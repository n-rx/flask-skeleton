from IAPI import db


class Test(db.Model):
	__tablename__ = "api_data"
	id = db.Column(db.Integer, primary_key=True)
	data = db.Column(db.String, nullable=False)

	@staticmethod
	def create(data):
		test = Test(data=data)
		db.session.add(test)
		db.session.commit()
		return test

	@staticmethod
	def get(id):
		test = Test.query.get(id)
		return test

	@staticmethod
	def get_all():
		return Test.query.all()

	@staticmethod
	def to_dict(obj):
		if not obj:
			return None
		return {
			"id": obj.id,
			"data": obj.data
		}

	@staticmethod
	def to_dict_multy(objects):
		if not objects:
			return []
		return [Test.to_dict(obj) for obj in objects]
