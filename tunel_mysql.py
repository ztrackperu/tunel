import mysql.connector

db_connection = mysql.connector.connect(
    host= "localhost",
    user= "ztrack2023",
    passwd= "lpmp2018",
    database="zgroupztrack"
)

# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()
# executing cursor with execute method and pass SQL query
db_cursor.execute("SELECT count(*) FROM  contenedores WHERE nombre_contenedor='ZGTU0015'")
#db_cursor.execute("SELECT * FROM  contenedores WHERE nombre_contenedor='ZGRU8747550'")

#db_cursor.execute("SELECT * FROM  contenedores ")

#db_cursor.execute("CREATE DATABASE my_first_db")


#print all databases
#for db in db_cursor:	
	#if db:
	    #print("con resultado")
    #else:
	    #print("no pasaa nada ")
	#print("ok")
	
#crear registro sino existe 
 #
update_old_salary = (
  "UPDATE salaries SET to_date = %s "
  "WHERE emp_no = %s AND from_date = %s")

print(db_cursor)

for db in db_cursor :
    print("aqui va :")
    print(db[0])
    print("termino de dato")

print("trizteza")