# <b>API-FEATURE-SWITCH🦁

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

```
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
#### The database of choice **MongoDB**, consist of a collection of users with a **features** array that contains *enabled* features

|    email           |    features  |   
| -------------------- | -------------- |
| exampleuser@mail.com | ['insta-cash'] |
<br />

## <b> Container
<ol>
<li>Change MONGO-URI in .env (connection string sent via email)
</li>
<li>Launch the API in a containerised environment `docker compose up`</li>
</ol>

##### note: use <b>port 5555</b> to communicate with the container as configured in the docker-compose or change it to port any unused port

<br />

## <b>Manual set up

1. Requirements: Python 3.6 or later
2. Navigate to root directory
3. Create and activate virtual environment
   - `python3 -m venv venv`
   - `source venv/bin/activate`
4. Install dependencies
   - `pip install -r dev-requirements.txt`
5. Change MONGO-URI in .env (connection string sent via email)
6. Launch API
   - `flask run`

<br />

## <b>Unit tests
### Configure `API_URL` in `tests/test_feature_switch.py`
### Launch unit tests `python3 -m unittest -v tests/test_feature_switch.py`
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
