import requests
import unittest

class ApiTest(unittest.TestCase):
    
    API_URL = "http://127.0.0.1:5000"
    FEATURE_URL = f"{API_URL}/feature"

    def test_correct(self):
        r = requests.get(f"{self.FEATURE_URL}?featureName=feat1&email=user1@gmail.com")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(list(r.json()), ["canAccess"])
        self.assertIn(r.json()["canAccess"], [True, False])


    def test_unused_parameter(self):
        r = requests.get(f"{self.FEATURE_URL}?featureName=feat1&email=user1@gmail.com&extraparam=test")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)

    def test_missing_parameters(self):
        r = requests.get(f"{self.FEATURE_URL}")
        self.assertEqual(r.status_code, 422)
        self.assertEqual(len(r.json()), 1)

    def test_missing_email(self):
        r = requests.get(f"{self.FEATURE_URL}?featureName=testfeat")
        self.assertEqual(r.status_code, 422)
        self.assertEqual(len(r.json()), 1)

    def test_missing_featureName(self):
        r = requests.get(f"{self.FEATURE_URL}?email=johndoe@gmail.com")
        self.assertEqual(r.status_code, 422)
        self.assertEqual(len(r.json()), 1)
