from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["naiveskill"]

collection = db['myCollection']

dict1= {'job': 'softare engineer' , 'Grade':7}
collection.insert_one(dict1)

dict_many= [
	{'job': 'softare engineer' , 'Grade':7},
	{'job': 'Data engineer' , 'Grade':6},
	{'job': 'dataops engineer' , 'Grade':8},
	{'job': 'mlops engineer' , 'Grade':7},
	]

collection.insert_many(dict_many)

print(client.list_database_names())

print(client['naiveskill'].list_collection_names())

print(collection.find_one({'job': 'dataops engineer'}))

print(collection.find({'Grade': {"$gt": 7}}))

print(collection.find({'Grade': {"$lt": 8}}))

print(collection.find({'Grade': 7}, {'_id':0}))

print(collection.find({'Grade': 7}, {'job':1 ,'_id':0}))

print(collection.estimated_document_count())

pre_value= {'job': 'softare engineer'}

new_value = {"$set": {'job': 'software engineer'}}

collection.update_one(pre_value, new_value)

pre_value= {'job': 'softare engineer'}

new_value = {"$set": {'job': 'software engineer'}}

collection.update_many(pre_value, new_value)

rec= {'job': 'mlops engineer'}

collection.delete_many(rec)

kl= collection.delete_many(rec)

kl.deleted_count
