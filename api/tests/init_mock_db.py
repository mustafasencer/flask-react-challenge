from flask import Flask

from api.application import db
from api.models.agency import Agency
from api.models.agency_domain_whitelist import AgencyDomainWhitelist
from api.models.broker import Broker


def run():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        whitelists = [
            AgencyDomainWhitelist(domain='cyberrisksolved.com'),
            AgencyDomainWhitelist(domain='cyberinsurance.com'),
            AgencyDomainWhitelist(domain='cyberworld.com'),
            AgencyDomainWhitelist(domain='savefromcyber.com'),
            AgencyDomainWhitelist(domain='cyberunderwriting.com')
        ]
        agencies = [
            Agency(title="Cyber Risk Solved Inc", domain='cyberrisksolved.com',
                   address="4418 N Rancho Dr, Las Vegas, NV 89130"),
            Agency(title="Cyber Insurance LLC", domain='cyberinsurance.com',
                   address="2025 E Florence Ave, Los Angeles, CA 90001"),
            Agency(title="Cyber World Inc, San Francisco", domain='cyberworld.com',
                   address="876 Geary St, San Francisco, CA 94109"),
            Agency(title="Cyber World Inc, New York", domain='cyberworld.com',
                   address="148 W 72nd St, New York, NY 10023"),
            Agency(title="Cyber World Inc, Miami", domain='cyberworld.com',
                   address="1575 SW 8th St, Miami, FL 33135")
        ]
        brokers = [
            Broker(firstname="Ali", lastname="Özcan", email="ali@cyberrisksolved.com", address="Hamidiye", agency_id=1)
        ]
        db.session.bulk_save_objects(whitelists)
        db.session.bulk_save_objects(agencies)
        db.session.bulk_save_objects(brokers)
        db.session.commit()


if __name__ == '__main__':
    run()
