import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb = client['Employee']

information = mydb.employeeinformation

record = {
	'firstname':"Sundar","age":11,"dept":"Boss"
}

information.insert_one(record)