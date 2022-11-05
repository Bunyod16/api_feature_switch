import requests
import unittest

class PostFeatureTest(unittest.TestCase):
    
    API_URL = "http://127.0.0.1:5000"
    FEATURE_URL = f"{API_URL}/feature"

    def test_correct_enable(self):
        test_feature = "testFeature1"
        test_email = "user1@gmail.com"
        r = requests.post(f"{self.FEATURE_URL}?featureName={test_feature}&email={test_email}&enable=true")
        self.assertEqual(r.status_code, 200)
        self.assertIn("OK", r.text)
        r = requests.get(f"{self.FEATURE_URL}?featureName={test_feature}&email={test_email}")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(list(r.json()), ["canAccess"])
        self.assertIn(r.json()["canAccess"], [True])

    def test_correct_disable(self):
        test_feature = "testFeature1"
        test_email = "user1@gmail.com"
        r = requests.post(f"{self.FEATURE_URL}?featureName={test_feature}&email={test_email}&enable=false")
        self.assertEqual(r.status_code, 200)
        self.assertIn("OK", r.text)
        r = requests.get(f"{self.FEATURE_URL}?featureName={test_feature}&email={test_email}")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(list(r.json()), ["canAccess"])
        self.assertIn(r.json()["canAccess"], [False])

class GetFeatureTest(unittest.TestCase):
    
    API_URL = "http://127.0.0.1:5000"
    FEATURE_URL = f"{API_URL}/feature"

    def test_correct(self):
        r = requests.get(f"{self.FEATURE_URL}?featureName=creditScore&email=user1@gmail.com")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(list(r.json()), ["canAccess"])
        self.assertIn(r.json()["canAccess"], [True, False])

    def test_correct2(self):
        r = requests.get(f"{self.FEATURE_URL}?featureName=cryptoInvesting&email=user2@gmail.com")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(list(r.json()), ["canAccess"])
        self.assertIn(r.json()["canAccess"], [True, False])

    def test_unused_parameter(self):
        r = requests.get(f"{self.FEATURE_URL}?featureName=creditScore&email=user1@gmail.com&extraparam=test")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)

    def test_missing_parameters(self):
        r = requests.get(f"{self.FEATURE_URL}")
        self.assertEqual(r.status_code, 422)
        self.assertEqual(len(r.json()), 1)

    def test_missing_email(self):
        r = requests.get(f"{self.FEATURE_URL}?featureName=cryptoTrading")
        self.assertEqual(r.status_code, 422)
        self.assertEqual(len(r.json()), 1)

    def test_missing_featureName(self):
        r = requests.get(f"{self.FEATURE_URL}?email=user1@gmail.com")
        self.assertEqual(r.status_code, 422)
        self.assertEqual(len(r.json()), 1)
