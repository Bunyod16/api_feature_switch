# <b>API-FEATURE-SWITCH

#### This REST API is created to enable/disable feature flags for individual users
<br />

## <b>Examples

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

<br />

## <b>Database
### The database of choice <b>MongoDB</b>, it consist of 9 test users with an uninitalised `features` array

| `email`          |  `features`  |   
| ---------------- | ------------ |
| user1@gmail.com  |              |
| user2@gmail.com  |              |
| user3@gmail.com  |              |
| user4@gmail.com  |              |
| user5@gmail.com  |              |
| user6@gmail.com  |              |
| user7@gmail.com  |              |
| user8@gmail.com  |              |
| user9@gmail.com  |              |

<br />

## <b>Set up

1.  Requirements: Python 3.10 or later
2.  Navigate to root directory
3. Create a virtual environment
   - `python3 -m venv venv`
   - `source venv/bin/activate`
4. Install dependencies
   - `pip install -r requirements.txt`
5. Set up a .env file, follow .env_sample 
6. Launch API
   - `python3 run.py`

<br />

## <b>Unit tests

### ChangeFeatureAccessTest: `POST` -> `/feature`
```
- test_correct_disable (test_feature_switch.PostFeatureTest) ... ok
- test_correct_enable (test_feature_switch.PostFeatureTest) ... ok
- test_missing_email (test_feature_switch.PostFeatureTest) ... ok
- test_missing_enable (test_feature_switch.PostFeatureTest) ... ok
- test_missing_featureName (test_feature_switch.PostFeatureTest) ... ok
- test_wrong_email_data_type (test_feature_switch.PostFeatureTest) ... ok
- test_wrong_enable_data_type (test_feature_switch.PostFeatureTest) ... ok
- test_wrong_feature_name_data_type (test_feature_switch.PostFeatureTest) ... ok
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
