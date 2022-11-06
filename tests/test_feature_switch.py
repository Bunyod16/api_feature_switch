import unittest
import requests
from dotenv import load_dotenv

load_dotenv()
class PostFeatureTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"
    FEATURE_URL = f"{API_URL}/feature"
    test_feature = "testFeature1"
    test_email = "user1@gmail.com"

    def test_correct_enable(self):
        r = requests.post(self.FEATURE_URL, json={"featureName":self.test_feature, "email":self.test_email, "enable":True}, timeout=1)
        self.assertEqual(r.status_code, 200)
        self.assertEqual("OK", r.json())
        r = requests.get(f"{self.FEATURE_URL}?featureName={self.test_feature}&email={self.test_email}", timeout=1)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(list(r.json()), ["canAccess"])
        self.assertIn(r.json()["canAccess"], [True])

    def test_correct_disable(self):
        r = requests.post(self.FEATURE_URL, json={"featureName":self.test_feature, "email":self.test_email, "enable":False}, timeout=1)
        self.assertEqual(r.status_code, 200)
        self.assertEqual("OK", r.json())
        r = requests.get(f"{self.FEATURE_URL}?featureName={self.test_feature}&email={self.test_email}", timeout=1)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(list(r.json()), ["canAccess"])
        self.assertIn(r.json()["canAccess"], [False])

    def test_missing_feature_name(self):
        r = requests.post(self.FEATURE_URL, json={"email":self.test_email, "enable":False}, timeout=1)
        self.assertEqual(r.status_code, 304)

    def test_missing_email(self):
        r = requests.post(self.FEATURE_URL, json={"featureName": self.test_feature, "enable":False}, timeout=1)
        self.assertEqual(r.status_code, 304)

    def test_missing_enable(self):
        r = requests.post(self.FEATURE_URL, json={"featureName": self.test_feature, "email":self.test_email}, timeout=1)
        self.assertEqual(r.status_code, 304)

    def test_wrong_feature_name_data_type(self):
        r = requests.post(self.FEATURE_URL, json={"featureName":999, "email":self.test_email, "enable":True}, timeout=1)
        self.assertEqual(r.status_code, 304)

    def test_wrong_email_data_type(self):
        r = requests.post(self.FEATURE_URL, json={"featureName":self.test_feature, "email":999, "enable":True}, timeout=1)
        self.assertEqual(r.status_code, 304)

    def test_wrong_enable_data_type(self):
        r = requests.post(self.FEATURE_URL, json={"featureName":self.test_feature, "email":self.test_email, "enable":"True"}, timeout=1)
        self.assertEqual(r.status_code, 304)

    def test_bad_email(self):
        r = requests.post(self.FEATURE_URL, json={"featureName":self.test_feature, "email":"badmail@gmail", "enable":False}, timeout=1)
        self.assertEqual(r.status_code, 304)

    def test_bad_email2(self):
        r = requests.post(self.FEATURE_URL, json={"featureName":self.test_feature, "email":"@gmail.com", "enable":True}, timeout=1)
        self.assertEqual(r.status_code, 304)

    def test_bad_email3(self):
        r = requests.post(self.FEATURE_URL, json={"featureName":self.test_feature, "email":"badmail.com", "enable":False}, timeout=1)
        self.assertEqual(r.status_code, 304)

class GetFeatureTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"
    FEATURE_URL = f"{API_URL}/feature"

    def test_correct(self):
        r = requests.get(f"{self.FEATURE_URL}?featureName=creditScore&email=user1@gmail.com", timeout=1)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertIn("canAccess", r.json())
        self.assertIn(r.json()["canAccess"], [True, False])

    def test_correct2(self):
        r = requests.get(f"{self.FEATURE_URL}?featureName=cryptoInvesting&email=user2@gmail.com", timeout=1)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertIn("canAccess", r.json())
        self.assertIn(r.json()["canAccess"], [True, False])

    def test_unused_parameter(self):
        r = requests.get(f"{self.FEATURE_URL}?featureName=creditScore&email=user1@gmail.com&extraparam=test", timeout=1)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)

    def test_missing_parameters(self):
        r = requests.get(f"{self.FEATURE_URL}", timeout=1)
        self.assertEqual(r.status_code, 422)
        self.assertEqual(len(r.json()), 1)

    def test_missing_email(self):
        r = requests.get(f"{self.FEATURE_URL}?featureName=crypto-trading", timeout=1)
        self.assertEqual(r.status_code, 422)
        self.assertEqual(len(r.json()), 1)

    def test_missing_featureName(self):
        r = requests.get(f"{self.FEATURE_URL}?email=user1@gmail.com", timeout=1)
        self.assertEqual(r.status_code, 422)
        self.assertEqual(len(r.json()), 1)

    def test_bad_email1(self):
        r = requests.get(f"{self.FEATURE_URL}?email=badmail.com&featureName=insta-cash", timeout=1)
        self.assertEqual(r.status_code, 422)

    def test_bad_email2(self):
        r = requests.get(f"{self.FEATURE_URL}?email=bad@mail&featureName=insta-cash", timeout=1)
        self.assertEqual(r.status_code, 422)

    def test_bad_email3(self):
        r = requests.get(f"{self.FEATURE_URL}?email=badmail&featureName=insta-cash", timeout=1)
        self.assertEqual(r.status_code, 422)
