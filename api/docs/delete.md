# Delete Broker

Delete a Broker.

**URL** : `/api/v1/broker/:id`

**Method** : `DELETE`

**Headers** : 
```json
{
    "Content-Type": "application/json"
}
```

## Success Response

**Code** : `204 NO CONTENT`

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