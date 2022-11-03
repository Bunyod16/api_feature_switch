from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()
mongo = PyMongo().init_app(uri=os.environ['MONGO_URI'])