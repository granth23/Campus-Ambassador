import uuid
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://test:test@atmos.lpjtdf0.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client.get_database("campus-ambassador")
users_collection = db.get_collection("atmos-23")


def colleges():
    all = []
    for i in users_collection.find({}):
        all.append(i['college'])
    return all


def new_user(name, college, phone, email):
    if validate(email, phone) == True:
        return "Please verify the details entered."
    else:
        idt = str(uuid.uuid1())
        users_collection.insert_one({'_id': idt, 'name' : name, 'college' : college, 'phone' : phone, 'email': email, 'registered': 0})
        return idt


def validate(email, phone):
    for i in users_collection.find({}):
        if i['email'] == email:
            return True
        if i['phone'] == phone:
            return True
    else:
        return False