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
In [12]: collection.insert_many(dict_many)

print(client.list_database_names())




