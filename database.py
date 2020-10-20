from Configuration import Configuration
import pymongo
client  = pymongo.MongoClient(Configuration.MONGO_URI)
db = client.get_database(Configuration.MONGO_DB)
print (Configuration.MONGO_URI)