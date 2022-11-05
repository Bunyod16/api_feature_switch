from flask import request
from .models import ResponseBody, User
from application import mongo_client

def get_feature(email, feature_name):
    if (email == None or feature_name == None):
        return ResponseBody({'status':422, 'json':{'error':'Missing required parameters email/featureName'}})
    user = User(email)
    if (user.doc == None):
        return ResponseBody({'status':404, 'json':{'error':'User not found'}})
    if (user.doc.get('features') != None and feature_name in user.doc.get('features')):
        return ResponseBody({'status':200, 'json':{"canAccess":True}})
    return ResponseBody({'status':200, 'json':{"canAccess":False}})
    

def post_feature(email, feature_name, enable):
    if (email == None or feature_name == None or enable == None):
        return ResponseBody({'status':304, 'message':'Status Not Modified (304)'})
    
    user = User(email)
    if (user.doc == None):
        return ResponseBody({'status':404, 'json':{'error':'User not found'}})
    try:
        features = user.doc.get('features')
        if (features == None):
            if (enable == True):
                features = [feature_name]
            else:
                features = []
        elif (enable == True and feature_name not in features):
            features.append(feature_name)
        elif (enable == False and feature_name in features):
            features.remove(feature_name)

        user.update({"$set": {"features": features}})
        return ResponseBody({'status':200, 'message':'OK (200)'})
    except Exception as err:
        print(err)
        return ResponseBody({'status':304, 'message':'Status Not Modified (304)'})

def post_account(*args):
    email = request.args.get('email')

    if (email == None ):
        return ResponseBody({'status':422, 'json':{'error':'missing required parameters email'}})
    user_collection = mongo_client.db.users
    user_collection.insert_one({'email':email})
    return ResponseBody({'status':200, 'json':{'message':'ok'}})

# {
# "featureName": "xxx", (string)
# "email": "xxx", (string) (user's name)
# "enable": true|false (boolean) (uses true to enable a user's access, otherwise
# }