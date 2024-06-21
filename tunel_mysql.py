import mysql.connector
import datetime

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
    #print("aqui va :")
    print(db[0])
    #print("termino de dato")
    if db[0]==0 :
        #crear nuevo registro
        print("oli")
        consulta_tunel =(
            "INSERT INTO contenedores ( nombre_contenedor ,tipo, descripcionc, telemetria_id,set_point, temp_supply_1,temp_supply_2,return_air,evaporation_coil,"
            "condensation_coil, compress_coil_1,compress_coil_2,ambient_air , cargo_1_temp ,cargo_2_temp,cargo_3_temp,cargo_4_temp,relative_humidity,avl , suction_pressure "
            ",discharge_pressure,line_voltage, line_frequency,consumption_ph_1,consumption_ph_2 , consumption_ph_3 ,co2_reading,o2_reading,evaporator_speed,condenser_speed,"
            "battery_voltage,power_kwh,power_trip_reading,   power_trip_duration, suction_temp,discharge_temp,supply_air_temp , return_air_temp ,dl_battery_temp,dl_battery_charge"
            ",power_consumption,power_consumption_avg,alarm_present , capacity_load ,power_state,controlling_mode,humidity_control,humidity_set_point,fresh_air_ex_mode ,"
            "fresh_air_ex_rate ,fresh_air_ex_delay,set_point_o2, set_point_co2,defrost_term_temp,defrost_interval , water_cooled_conde ,usda_trip,evaporator_exp_valve,"
            "suction_mod_valve,hot_gas_valve,economizer_valve,ethylene , stateProcess,stateInyection, timerOfProcess,modelo,latitud , longitud ,ultima_fecha ,empresa_id,"
            "defrost_prueba,ripener_prueba) VALUES ('ZGTU0015','Madurador','Tunel USA',1000000,"
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0,0,0,0,0,0,0,0,0,0,0,%s,"
            "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'THERMOKING,0,0,10,1,0,0)"
        )
        #db_cursor.execute(consulta_tunel,(2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2, datetime.datetime(2024, 4, 16, 13, 51, 11)))
        db_cursor.execute(consulta_tunel,(2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2))

    else :
        #actualizar el 
        print("oliz")
print("trizteza")