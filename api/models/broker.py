from sqlalchemy import func

from api.application import db


class Broker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)
    email = db.Column(db.Text, unique=True, nullable=False)
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=func.now())

    agency_id = db.Column(db.Integer, db.ForeignKey('agency.id'))
    agency = db.relationship("Agency", cascade="all,delete", backref=db.backref("agency", uselist=False))

    def __repr__(self):
        return '<Broker %r>' % self.id

    def as_dict(self, with_foreign=True):
        _dict = {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'created_at'}
        if with_foreign:
            return {**_dict, "title": self.agency.title, "domain": self.agency.domain}
        return _dict
