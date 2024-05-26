from app import db


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    building_type = db.Column(db.String(100))
    school_type = db.Column(db.String(50))
    limit = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __dict__(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())

    def __dict__(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
