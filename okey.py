
z ="luis el terrible"

print(z)

from pymongo import MongoClient
client = MongoClient()

db = client.REPOSITORIO_6_2024

collection = db.tunel

query = collection.find_one().sort("fecha",1)

print(query)

print("jale ok!")
print(query['fecha'])
#establecer proceso de datos 
#solicitar id

db1 = client.ZGTU0015_6_2024

collection1 = db1.madurador

query1 = collection1.find_one()
