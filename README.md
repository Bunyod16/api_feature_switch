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

### ChangeFeatureAccessTest: `POST` -> `/feature`
```
- test_correct_disable (test_feature_switch.PostFeatureTest) ... ok
- test_correct_enable (test_feature_switch.PostFeatureTest) ... ok
```

### GetFeatureAccessTest: `GET` -> `/feature`
```
- test_correct (test_feature_switch.GetFeatureTest) ... ok
- test_correct2 (test_feature_switch.GetFeatureTest) ... ok
- test_missing_email (test_feature_switch.GetFeatureTest) ... ok
- test_missing_featureName (test_feature_switch.GetFeatureTest) ... ok
- test_missing_parameters (test_feature_switch.GetFeatureTest) ... ok
- test_unused_parameter (test_feature_switch.GetFeatureTest) ... ok
```
