from pymongo import MongoClient, errors

from configure import settings

SETS = settings["MongoDB"]
setting = SETS["settings"]



def MongoClient_connection(db_name = SETS["MongoDB_name"],collection_name = SETS["Mongo_Collections"]):
    client = MongoClient(host=setting['host'],port=setting["port"])
    client.database.authenticate(name=setting["username"],password = setting["password"],source = "admin")
    db = client[db_name]
    colletions = db[collection_name]
    return colletions



if __name__ == '__main__':
    print(MongoClient_connection())
