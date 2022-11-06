from .models import User
from flask import jsonify

import re
 
 
# Define a function for
# for validating an Email
def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False

def get_feature(email, feature_name):
    if (email == None or feature_name == None):
        return jsonify({'message':'Error missing required parameters email/featureName'}), 422
    if (not validate_email(email)):
        return jsonify({'message':'Error malformed email'}), 422
    user = User(email)
    if (feature_name in user.doc.get('features')):
        return jsonify({'canAccess':True}), 200
    return jsonify({'canAccess':False}), 200

def post_feature(email, feature_name, enable):
    if (email == None or feature_name == None or enable == None
        or type(email) != str or type(feature_name) != str or type(enable) != bool
        or not validate_email(email)):
        return '', 304
    
    user = User(email)
    if (user.doc == None):
        return '', 304

    try:
        features = user.doc.get('features')
    except Exception as err:
            print(err)
            return '', 304

    if (enable and feature_name not in features):
        features.append(feature_name)
    elif (not enable and feature_name in features):
        features.remove(feature_name)
    r = user.update({"$set": {"features": features}})
    if (r.acknowledged):
        return jsonify('OK'), 200
    