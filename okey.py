
z ="luis el terrible"

print(z)

from pymongo import MongoClient
client = MongoClient()

db = client.REPOSITORIO_6_2024

collection = db.tunel

#-1 para ver de mayor a menor (veo el ultimo dato ingresado a la base de datos)
#query = collection.find({"status":1}).sort("fecha",-1).limit(2)
query = collection.find({"status":1}).sort("fecha",-1)

for x in query:
    #print(x)
    db1 = client.ZGTU0015_6_2024
    collection1 = db1.madurador
    query1 = collection1.find_one()
    if query1 :
        id =query1["id"] +1
    else:
        id =100000000
    print(id)
    print(x['fecha'])
    datito = x['data']
    paquete = datito.split(',') 
    print(datito)
    print(float(paquete[42]))
    #contruir objeto 
    objeto1 = {
        "id": id,
        "set_point": float(paquete[3]), 
        "temp_supply_1": float(paquete[4]),
        "temp_supply_2": float(paquete[5]),
        "return_air": float(paquete[6]), 
        "evaporation_coil": float(paquete[7]),
        "condensation_coil": float(paquete[8]),
        "compress_coil_1": float(paquete[9]),
        "compress_coil_2": float(paquete[10]), 
        "ambient_air": float(paquete[11]), 
        "cargo_1_temp": float(paquete[12]),
        "cargo_2_temp": float(paquete[13]), 
        "cargo_3_temp": float(paquete[14]), 
        "cargo_4_temp": float(paquete[15]), 
        "relative_humidity": float(paquete[16]), 
        "avl": float(paquete[17]), 
        "suction_pressure": float(paquete[18]), 
        "discharge_pressure": float(paquete[19]), 
        "line_voltage": float(paquete[20]), 
        "line_frequency": float(paquete[21]), 
        "consumption_ph_1": float(paquete[22]), 
        "consumption_ph_2": float(paquete[23]), 
        "consumption_ph_3": float(paquete[24]), 
        "co2_reading": float(paquete[25]), 
        "o2_reading": float(paquete[26]), 
        "evaporator_speed": float(paquete[27]), 
        "condenser_speed": float(paquete[28]),
        "battery_voltage": float(paquete[29]),
        "power_kwh": float(paquete[30]),
        "power_trip_reading": float(paquete[31]),
        "power_trip_duration": None,
        "suction_temp": None,
        "discharge_temp": None,
        "supply_air_temp": None,
        "return_air_temp": None,
        "dl_battery_temp": None,
        "dl_battery_charge": None,
        "power_consumption": None,
        "power_consumption_avg": None,
        "alarm_present": float(paquete[42]), 
        "capacity_load": None,
        "power_state": None,
        "controlling_mode": "1",
        "humidity_control": None,
        "humidity_set_point": None,
        "fresh_air_ex_mode": None,
        "fresh_air_ex_rate": None,
        "fresh_air_ex_delay": None,
        "set_point_o2": None,
        "set_point_co2": None,
        "defrost_term_temp": None,
        "defrost_interval": None,
        "water_cooled_conde": None,
        "usda_trip": None,
        "evaporator_exp_valve": None,
        "suction_mod_valve": None,
        "hot_gas_valve": None,
        "economizer_valve": None,
        "ethylene": None,
        "stateProcess": None,
        "stateInyection": None,
        "timerOfProcess": None,
        "modelo": "THERMOKING",
        "latitud": -11.9803,
        "longitud": -77.1226,
        "created_at": x['fecha'],
        "telemetria_id": 1000000,
        "inyeccion_etileno": None,
        "defrost_prueba": None,
        "ripener_prueba": None,
        "sp_ethyleno": None,
        "inyeccion_hora": None,
        "inyeccion_pwm": None,
        "extra_1": 0,
        "extra_2": 0,
        "extra_3": 0,
        "extra_4": 0,
        "extra_5": 0
    }
    print(objeto1)
    #guardar en base de datos 
    query1.insert_one(objeto1)
#print(query)

print("jale ok!")
#print(query['fecha'])
#establecer proceso de datos 
#solicitar id


#db1 = client.ZGTU0015_6_2024
#collection1 = db1.madurador
#query1 = collection1.find_one()
#if query1 :
    #id =query1["id"] +1
#else:
    #id =100000000
#print(id)
