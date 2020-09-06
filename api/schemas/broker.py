CREATE = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'additionalProperties': False,
    'definitions': {
        'non-empty-string': {
            'type': 'string',
            'minLength': 1
        },
    },
    'properties': {
        'email': {
            'type': 'string',
            'format': 'email'
        },
        'firstname': {
            '$ref': '#/definitions/non-empty-string'
        },
        'lastname': {
            '$ref': '#/definitions/non-empty-string'
        },
        'address': {
            '$ref': '#/definitions/non-empty-string'
        }
    },
    'required': [
        'email',
        'firstname',
        'lastname',
        'address'
    ]
}

UPDATE = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'definitions': {
        'non-empty-string': {
            'type': 'string',
            'minLength': 1
        },
    },
    'properties': {
        'email': {
            'type': 'string',
            'format': 'email'
        },
        'firstname': {
            '$ref': '#/definitions/non-empty-string'
        },
        'lastname': {
            '$ref': '#/definitions/non-empty-string'
        },
        'address': {
            '$ref': '#/definitions/non-empty-string'
        }
    },
    'required': []
}
