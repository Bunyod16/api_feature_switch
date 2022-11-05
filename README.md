# API-FEATURE-SWITCH

This REST API is created to enable/disable feature flags for individual users 


## Examples


* Get Feature Access : `GET /feature?email=user1@gmail.comfeatureName=insta-cash`
```
Response:
{
    "canAccess":true
}
```
* Change Feature Access : `POST /feature`
```
Request body:
{
    "featureName": "crypto-trading"
    "email": "user1@gmail.com"
    "enable": true
}

Response: 200, OK
```

## Unit tests

### UpdateFeatureAccessTest: `POST` -> `/feature`
```

```

### GetFeatureAccessTest: `GET` -> `/feature`
```

```
