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
#mydb = myclient[ "ZGTU0015_6_2024"]
#mycol = mydb[ "madurador"]

mydb = myclient[ "REPOSITORIO_6_2024"]
mycol = mydb[ "tunel"]

x = mycol.find_one
print(x)


#            $C = $api->crearContenedorM($nombrecontenedor, $tipo,$descripcion,$telemetria_id,$set_point, $temp_supply_1,$temp_supply_2,$return_air,$evaporation_coil,$condensation_coil, $compress_coil_1,$compress_coil_2,$ambient_air , $cargo_1_temp ,$cargo_2_temp,$cargo_3_temp,$cargo_4_temp,$relative_humidity,$avl , $suction_pressure ,$discharge_pressure,$line_voltage, $line_frequency,$consumption_ph_1,$consumption_ph_2 , $consumption_ph_3 ,$co2_reading,$o2_reading,$evaporator_speed,$condenser_speed,$battery_voltage , $power_kwh ,$power_trip_reading,$power_trip_duration, $suction_temp,$discharge_temp,$supply_air_temp , $return_air_temp ,$dl_battery_temp,$dl_battery_charge,$power_consumption,$power_consumption_avg,$alarm_present , $capacity_load ,$power_state,$controlling_mode,$humidity_control,$humidity_set_point,$fresh_air_ex_mode , $fresh_air_ex_rate ,$fresh_air_ex_delay,$set_point_o2, $set_point_co2,$defrost_term_temp,$defrost_interval , $water_cooled_conde ,$usda_trip,$evaporator_exp_valve,$suction_mod_valve,$hot_gas_valve,$economizer_valve,$ethylene , $stateProcess,$stateInyection, $timerOfProcess,$modelo,$latitud , $longitud ,$ultima_fecha,$empresaAsignada,$defrost_prueba,$ripener_prueba);

#        $consult = $this->pdo->prepare("INSERT INTO contenedores ( nombre_contenedor ,tipo, descripcionc, telemetria_id,set_point, temp_supply_1,temp_supply_2,return_air,evaporation_coil,condensation_coil, compress_coil_1,compress_coil_2,ambient_air , cargo_1_temp ,cargo_2_temp,cargo_3_temp,cargo_4_temp,relative_humidity,avl , suction_pressure ,discharge_pressure,line_voltage, line_frequency,consumption_ph_1,consumption_ph_2 , consumption_ph_3 ,co2_reading,o2_reading,evaporator_speed,condenser_speed,battery_voltage , power_kwh ,power_trip_reading,power_trip_duration, suction_temp,discharge_temp,supply_air_temp , return_air_temp ,dl_battery_temp,dl_battery_charge,power_consumption,power_consumption_avg,alarm_present , capacity_load ,power_state,controlling_mode,humidity_control,humidity_set_point,fresh_air_ex_mode , fresh_air_ex_rate ,fresh_air_ex_delay,set_point_o2, set_point_co2,defrost_term_temp,defrost_interval , water_cooled_conde ,usda_trip,evaporator_exp_valve,suction_mod_valve,hot_gas_valve,economizer_valve,ethylene , stateProcess,stateInyection, timerOfProcess,modelo,latitud , longitud ,ultima_fecha ,empresa_id,defrost_prueba,ripener_prueba ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)");

