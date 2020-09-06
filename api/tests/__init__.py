import json
import unittest

from api import application
from api.models.agency import Agency
from api.models.agency_domain_whitelist import AgencyDomainWhitelist


class BaseTest(unittest.TestCase):
    app = None
    pre_broker = None

    def fetch(self, url, data=None, method='GET'):
        if method.upper() == 'POST':
            return self.app.post(
                url,
                data=json.dumps(
                    data
                ),
                headers={
                    'Content-Type': 'application/json'
                },
                follow_redirects=True
            )
        elif method.upper() == 'GET':
            return self.app.get(
                url,
                headers={
                    'Content-Type': 'application/json'
                },
                follow_redirects=True
            )
        elif method.upper() == 'PUT':
            return self.app.put(
                url,
                data=json.dumps(
                    data
                ),
                headers={
                    'Content-Type': 'application/json'
                },
                follow_redirects=True
            )
        elif method.upper() == 'DELETE':
            return self.app.delete(
                url,
                data=json.dumps(
                    data
                ),
                headers={
                    'Content-Type': 'application/json'
                },
                follow_redirects=True
            )

    def prepeare_db(self):
        whitelists = [
            AgencyDomainWhitelist(email='cyberrisksolved.com'),
            AgencyDomainWhitelist(email='cyberinsurance.com'),
            AgencyDomainWhitelist(email='cyberworld.com'),
            AgencyDomainWhitelist(email='savefromcyber.com'),
            AgencyDomainWhitelist(email='cyberunderwriting.com')
        ]
        agencies = [
            Agency(domain='cyberrisksolved.com', title="Cyber Risk Solved Inc",
                   address="4418 N Rancho Dr, Las Vegas, NV 89130"),
            Agency(domain='cyberinsurance.com', title="Cyber Insurance LLC",
                   address="2025 E Florence Ave, Los Angeles, CA 90001"),
            Agency(domain='cyberworld.com', title="Cyber World Inc, San Francisco",
                   address="876 Geary St, San Francisco, CA 94109"),
            Agency(domain='cyberworld.com', title="Cyber World Inc, New York",
                   address="148 W 72nd St, New York, NY 10023"),
            Agency(domain='cyberworld.com', title="Cyber World Inc, Miami", address="1575 SW 8th St, Miami, FL 33135")
        ]
        db.session.bulk_save_objects(whitelists)
        db.session.bulk_save_objects(agencies)
        db.session.commit()

    def setUp(self):
        _app = application.create_app()
        _app.app_context().push()
        db.create_all()
        self.app = _app.test_client()
        self.prepeare_db()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        pass


if __name__ == "__main__":
    unittest.main()
