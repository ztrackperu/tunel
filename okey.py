
z ="luis el terrible"

print(z)

from pymongo import MongoClient
client = MongoClient()

db = client.REPOSITORIO_6_2024

collection = db.tunel

query = collection.find_one()
print(query)

print("jale ok!")
print(query['fecha'])
