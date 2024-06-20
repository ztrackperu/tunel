#homolgar datos en texo plano a SQL para crear esrtructura de JSON 
# consultar ultimo dato de id , sino existe crear el dato ciehn millones 100 000 000  , 100000000
# Nombre del equipo ZGTU0015
# consultar fecha 20/06/2024
# buscar si existe ZGTU0015_6_2024
#coleccion de  MADURADOR
#SINO EXISTE empezar id con cien millones si capturar el id y agregar id+1
#hacer doble validacion y los datos que no existen pasar por None
#construir el json y guaradr cen la base de datos ZGTU0015_6_2024

import pymongo

myclient = pymongo.MongoClient( "mongodb://localhost:27170/")
mydb = myclient[ "ZGTU0015_6_2024"]
mycol = mydb[ "madurador"]

x = mycol.find_one()

print(x)