from flask import request
from application import mongo_client
import json


class ResponseBody():
    def __init__(self, args):
        self.status = args['status']
        self.json = json.dumps(args['json'])

def get_feature(*args):
    email = args('email')
    featureName = args('featureName')

    if (email == None or featureName == None):
        return ResponseBody({'status':422, 'json':{'error':'missing required parameters email/featureName'}})
    return ResponseBody({'status':200, 'json':{'canAccess':'True'}})

def post_feature(*args):
    email = args('email')
    featureName = args('featureName')
    enable = args('enable')


    if (email == None or featureName == None or enable == None):
        return ResponseBody({'status':422, 'json':{'error':'missing required parameters email/featureName/enable'}})
    user_collection = mongo_client.db.users
    q = user_collection.find({'email':email})
    return ResponseBody({'status':200, 'json':{'message':'ok'}})

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