from api.application import db
from api.utils.sqlalchemy import to_json


class Agency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    domain = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text)

    def __repr__(self):
        return '<Agency %r>' % self.id

    @property
    def json(self):
        return to_json(self, self.__class__)
