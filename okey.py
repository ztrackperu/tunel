
z ="luis el terrible"

print(z)

from pymongo import MongoClient
client = MongoClient()

db = client.REPOSITORIO_6_2024

collection = db.tunel

#-1 para ver de mayor a menor (veo el ultimo dato ingresado a la base de datos)
query = collection.find({"status":1}).sort("fecha",-1).limit(2)

for x in query:
    print(x)
#print(query)

print("jale ok!")
#print(query['fecha'])
#establecer proceso de datos 
#solicitar id


db1 = client.ZGTU0015_6_2024

collection1 = db1.madurador

query1 = collection1.find_one()

if query1 :
    id =query1["id"] +1
else:
    id =100000000

print(id)
