from functools import wraps

from flask import request
from jsonschema import ValidationError, validate

from api.utils.error import AppError


def validated(schema):
    def wrapper(fn):
        @wraps(fn)
        def decorated(*args, **kwargs):
            try:
                validate(request.json, schema)
            except ValidationError as e:
                raise AppError(
                    err_code="errors.validationError",
                    err_msg=str(e.message),
                    status=400,
                    context={
                        'required': e.schema.get('required', []),
                        'properties': e.schema.get('properties', {})
                    }
                )
            return fn(*args, **kwargs)

        return decorated

    return wrapper
