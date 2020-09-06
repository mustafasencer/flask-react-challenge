from flask import Blueprint, request, jsonify

from api.application import db, limiter
from api.models.agency import Agency
from api.models.agency_domain_whitelist import AgencyDomainWhitelist
from api.models.broker import Broker
from api.schemas.broker import CREATE, UPDATE
from api.services.geocode_service import get_nearest_agency
from api.utils.errors import AppError
from api.utils.validated import validated

bp = Blueprint('broker', __name__)


@bp.route('/api/v1/broker', methods=['POST'])
@limiter.limit("10 per minute")
@validated(CREATE)
def create():
    data = request.json
    domain = data['email'].split('@')[-1]
    exists = AgencyDomainWhitelist.query.filter_by(domain=domain).scalar() is not None
    if not exists:
        raise AppError(
            status=404,
            err_code='errors.domainNotFound',
            err_msg=f'Whitelist domain Not Found by Given Email domain <{domain}>'
        )
    email_exists = Broker.query.filter_by(email=data['email']).scalar() is not None
    if email_exists:
        raise AppError(
            status=409,
            err_code='errors.duplicateEmailError',
            err_msg=f'Email already exists <{data["email"]}>'
        )
    agencies = Agency.query.filter_by(domain=domain).all()
    if len(agencies) > 1:
        agency = get_nearest_agency(data['address'], agencies)
    else:
        agency = agencies[0]
    broker = Broker(**data, agency_id=agency.id)
    db.session.add(broker)
    db.session.commit()
    return jsonify(broker.as_dict()), 201


@bp.route('/api/v1/broker', methods=['GET'])
def get():
    brokers = Broker.query.join('agency').all()
    return jsonify([broker.as_dict() for broker in brokers]), 200


@bp.route('/api/v1/broker/<uuid:broker_id>', methods=['GET'])
def get_by_id(broker_id):
    broker = Broker.query.get_or_404(broker_id, description=f"Broker Not Found by given ID: {broker_id}")
    return jsonify(broker.as_dict()), 200


@bp.route('/api/v1/broker/<uuid:broker_id>', methods=['PUT'])
@validated(UPDATE)
def update(broker_id):
    data = request.json
    broker = Broker.query.get_or_404(broker_id, description=f"Broker Not Found by given ID: {broker_id}")
    for key, value in data.items():
        setattr(broker, key, value)
    db.session.commit()
    return jsonify(broker.as_dict()), 200


@bp.route('/api/v1/broker/<uuid:broker_id>', methods=['DELETE'])
def delete(broker_id):
    broker = Broker.query.get_or_404(broker_id, description=f"Broker Not Found by given ID: {broker_id}")
    db.session.delete(broker)
    db.session.commit()
    return jsonify(), 204
