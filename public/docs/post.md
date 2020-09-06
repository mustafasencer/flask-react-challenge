# Post Broker

Post a Broker.

**URL** : `/api/v1/broker`

**Method** : `POST`

**Headers** : 
```json
{
    "Content-Type": "application/json"
}
```

## Success Response

**Code** : `201 CREATED`

**Content example**

```json
{
    "firstname": "ali",
    "lastname": "veli",
    "email": "joe@gmail.com",
    "address": "sarıyer, istanbul"
}
```


## Error Responses

**Condition** : If [Here API](https://www.here.com/) is not responding or have an issue.

**Code** : `400 BAD REQUEST`

**Content** : 

```json
{
    "err_msg": "Here API response body",
    "err_code": "errors.hereApiError",
    "context": null,
    "reason": null
}
```