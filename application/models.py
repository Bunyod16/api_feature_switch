import json
from application import mongo_client

class ResponseBody():
    def __init__(self, args):
        self.status = args['status']
        if ('json' in args):
            self.message = json.dumps(args['json'])
        elif ('message' in args):
            self.message = args['message']

class User():
    def __init__(self, email):
        self.email = email
        user_collection = mongo_client.db.users
        doc = user_collection.find_one({'email':self.email})
        self.doc = doc
    
    def update(self, command):
        user_collection = mongo_client.db.users
        r = user_collection.update_one({'_id':self.doc._id}, command, upsert=False)
        return (r)
