# Get Broker

Get the details of a Broker.

**URL** : `/api/v1/broker/:id`

**Method** : `GET`

**Headers** : 
```json
{
    "Content-Type": "application/json"
}
```

## Success Response

**Code** : `200 OK`

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

**Condition** : If `id` does not exist in DB.

**Code** : `404 NOT FOUND`

**Content** : 

```json
{
    "err_msg": "Broker was not found by given id: <application_id>",
    "err_code": "errors.brokerNotFound",
    "context": null,
    "reason": null
}
```