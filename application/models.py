from application import mongo_client

class User():
    def __init__(self, email):
        self.email = email
        user_collection = mongo_client.db.users
        doc = user_collection.find_one({'email':self.email})
        if (doc is None):
            doc = user_collection.insert_one({'email':self.email, 'features':[]})
            doc = user_collection.find_one({'email':self.email})
        self.doc = doc
    
    def update(self, command):
        user_collection = mongo_client.db.users
        r = user_collection.update_one({'_id':self.doc.get("_id")}, command, upsert=False)
        return (r)
