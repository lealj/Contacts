from pymongo import MongoClient

# Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# Collection definitions
lenses_collection = db["contact_lenses"]


def get_lenses_collection():
    return lenses_collection
# def get_lenses():
#     return list(lens_collection.find({}, {"_id":0}))


# new_entry = {
#     "brand": "Brand0",
#     "type": "Monthly"
# }

# def insert_lenses():
 #    result = lens_collection.insert_one(new_entry)
 #    if result.inserted_id:
  #       print("Entry inserted")
  ##   else:
   #      print("Not inserted")


