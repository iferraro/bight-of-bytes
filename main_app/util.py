from django.db import connection
import json

def populatedb():
    with open('device_data.json', 'r') as myfile:
        device_data = myfile.read()

    device_obj = json.loads(device_data)

    with connection.cursor() as cursor:
        try:
            devices = device_obj['Devices']

            for i in range(len(devices)):
               device = devices[i] 
               param_list = [ device["id"], device["name"] ]
               cursor.execute("INSERT INTO main_app_device (id, name) VALUES (%s, %s) ON CONFLICT DO NOTHING", param_list)
               ## HERE WE CANT VALIDATE THE VARIANTS BC NO VARIANT ID IN JSON

            cursor.execute("SELECT count(*) FROM main_app_variant")
            returnCount = cursor.fetchone()
            count = returnCount[0]
            for device in devices:
                print(device['name'])
            print(count, "<---- ok, no variants")
            if(count == 0):
                for i in range(len(devices)):
                   device = devices[i] 
                   variants = device["variants"]
                   for j in range(len(variants)):
                       variant = variants[j]
                       param_list = [ device["id"], variant["price"], variant["storage"] ]
                       cursor.execute("INSERT INTO main_app_variant (device_id, price, storage) VALUES (%s, %s, %s)", param_list)
        finally: 
            cursor.close()