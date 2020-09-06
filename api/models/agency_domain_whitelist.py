from api.application import db
from api.utils.sqlalchemy import to_json


class AgencyDomainWhitelist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Agency Domain Whitelist %r>' % self.id

    @property
    def json(self):
        return to_json(self, self.__class__)
