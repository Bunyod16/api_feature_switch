from .models import ResponseBody, User

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
    if (email == None or feature_name == None or enable == None
        or type(email) != str or type(feature_name) != str or type(enable) != bool):
        return ResponseBody({'status':304, 'message':'Status Not Modified (304)'})
    
    user = User(email)
    if (user.doc == None):
        return ResponseBody({'status':304, 'message':'Status Not Modified (304)'})

    try:
        features = user.doc.get('features')
        if (features == None):
            features = []

        if (enable and feature_name not in features):
            features.append(feature_name)
        elif (not enable and len(features) != 0 and feature_name in features):
            features.remove(feature_name)

        r = user.update({"$set": {"features": features}})
        if (r.acknowledged):
            return ResponseBody({'status':200, 'message':'OK (200)'})
    except Exception as err:
        print(err)
        return ResponseBody({'status':304, 'message':'Status Not Modified (304)'})
