from flask import request
from extensions import mongo
import json


class ResponseBody():
    def __init__(self, args):
        self.status = args['status']
        self.json = json.dumps(args['json'])

def get_feature(*args):
    email = request.args.get('email')
    featureName = request.args.get('featureName')

    if (email == None or featureName == None):
        return ResponseBody({'status':422, 'json':{'error':'missing required parameters email/featureName'}})
    return ResponseBody({'status':200, 'json':{'canAccess':'True'}})

def post_feature(*args):
    print(args)
    return ResponseBody(200, 'ok')

def post_account(*args):
    email = request.args.get('email')

    if (email == None ):
        return ResponseBody({'status':422, 'json':{'error':'missing required parameters email'}})
    user_collection = mongo.db.users
    user_collection.insert_one({'email':email})
    return ResponseBody({'status':200, 'json':{'message':'ok'}})