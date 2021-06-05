import json
from firebase import firebase

from random import randint
import time

cont = 0

while (True):
    temp = str(randint(25,31))
    rpm = str(randint(50,60))
    vel = str(randint(40,60))
    lux = str(randint(0,10))

    # print(temp, rpm, vel, lux)

    json_data = {'temp' : temp, 'rpm' : rpm, 'vel' : vel, 'lux' : lux}
    json_data = json.dumps(json_data, indent=4, sort_keys=False)

    parsed_json = (json.loads(json_data))
    print(json_data)

    if (cont == 0):
        firebase = firebase.FirebaseApplication('https://lapisco-trainee-iot-default-rtdb.firebaseio.com/', authentication=None)
        print(firebase)
        result = firebase.post('/', parsed_json)
    #     print(result)
    #
    else:
        firebase.put('/', result['name'], parsed_json)

    time.sleep(2)
    cont += 1