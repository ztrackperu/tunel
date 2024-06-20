
z ="luis el terrible"

print(z)

from pymongo import MongoClient
client = MongoClient()

db = client.REPOSITORIO_6_2024

collection = db.tunel

#-1 para ver de mayor a menor (veo el ultimo dato ingresado a la base de datos)
query = collection.find({"status":1}).sort("fecha",-1).limit(2)

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
    print(paquete[42])
    #contruir objeto 
    objeto = {
        "id": id,
        "set_point": paquete[3], 
        "temp_supply_1": paquete[4],
        "temp_supply_2": paquete[5],
        "return_air": paquete[6], 
        "evaporation_coil": paquete[7],
        "condensation_coil": paquete[8],
        "compress_coil_1": paquete[9],
        "compress_coil_2": paquete[10], 
        "ambient_air": paquete[11], 
        "cargo_1_temp": paquete[12],
        "cargo_2_temp": paquete[13], 
        "cargo_3_temp": paquete[14], 
        "cargo_4_temp": paquete[15], 
        "relative_humidity": paquete[16], 
        "avl": paquete[17], 
        "suction_pressure": paquete[18], 
        "discharge_pressure": paquete[19], 
        "line_voltage": paquete[20], 
        "line_frequency": paquete[21], 
        "consumption_ph_1": paquete[22], 
        "consumption_ph_2": paquete[23], 
        "consumption_ph_3": paquete[24], 
        "co2_reading": paquete[25], 
        "o2_reading": paquete[26], 
        "evaporator_speed": paquete[27], 
        "condenser_speed": paquete[28],
        "battery_voltage": paquete[29],
        "power_kwh": paquete[30],
        "power_trip_reading": paquete[31],
        "power_trip_duration": None,
        "suction_temp": None,
        "discharge_temp": None,
        "supply_air_temp": None,
        "return_air_temp": None,
        "dl_battery_temp": None,
        "dl_battery_charge": None,
        "power_consumption": None,
        "power_consumption_avg": None,
        "alarm_present": paquete[42], 
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
