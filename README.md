# <b>API-FEATURE-SWITCH

#### This REST API is created to enable/disable feature flags for individual users

<ul>
 <li>Framework: Python/Flask</li>
 <li>Database:  MongoDB</li>
 <li>Deployment: Google Cloud Run</li> 
</ul>
<br />

## <b>Examples

  Get Feature Access :
```
curl -X GET http://127.0.0.1:5000/feature\?email=user1@gmail.com\&featureName=insta-cash
```

```json
   Response:
   {
      "canAccess":false
   }
```

  Modify Feature Access :
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"featureName":"crypto-trading","email":"user1@gmail.com","enable":true}' \
  http://127.0.0.1:5000/feature
```

```
   Response: 200, OK
```

<br />

## <b>Database
### The database of choice <b>MongoDB</b>, consist of a collection of users with a `features` array that contains *enabled* features

|    `email`           |    `features`  |   
| -------------------- | -------------- |
| exampleuser@mail.com | ['insta-cash'] |
<br />

## <b>Set up

1. Requirements: Python 3.6 or later
2. Navigate to root directory
3. Create and activate virtual environment
   - `python3 -m venv venv`
   - `source venv/bin/activate`
4. Install dependencies
   - `pip install -r requirements.txt`
5. Change MONGO-URI in .env (connection string sent in email)
6. Launch API
   - `flask run`

<br />

## <b>Unit tests
### To launch unit tests use `python3 -m unittest -v tests/test_feature_switch.py`
### ChangeFeatureAccessTest: `POST` -> `/feature`
```
- test_bad_email (test_feature_switch.PostFeatureTest) ... ok
- test_bad_email2 (test_feature_switch.PostFeatureTest) ... ok
- test_bad_email3 (test_feature_switch.PostFeatureTest) ... ok
- test_correct_disable (test_feature_switch.PostFeatureTest) ... ok
- test_correct_enable (test_feature_switch.PostFeatureTest) ... ok
- test_missing_email (test_feature_switch.PostFeatureTest) ... ok
- test_missing_enable (test_feature_switch.PostFeatureTest) ... ok
- test_missing_feature_name (test_feature_switch.PostFeatureTest) ... ok
- test_wrong_email_data_type (test_feature_switch.PostFeatureTest) ... ok
- test_wrong_enable_data_type (test_feature_switch.PostFeatureTest) ... ok
- test_wrong_feature_name_data_type (test_feature_switch.PostFeatureTest) ... ok
```

### GetFeatureAccessTest: `GET` -> `/feature`
```
- test_bad_email1 (test_feature_switch.GetFeatureTest) ... ok
- test_bad_email2 (test_feature_switch.GetFeatureTest) ... ok
- test_bad_email3 (test_feature_switch.GetFeatureTest) ... ok
- test_correct (test_feature_switch.GetFeatureTest) ... ok
- test_correct2 (test_feature_switch.GetFeatureTest) ... ok
- test_missing_email (test_feature_switch.GetFeatureTest) ... ok
- test_missing_featureName (test_feature_switch.GetFeatureTest) ... ok
- test_missing_parameters (test_feature_switch.GetFeatureTest) ... ok
- test_unused_parameter (test_feature_switch.GetFeatureTest) ... ok
```
