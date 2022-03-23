from firebase import firebase
import schedule
import time
import json
firebase = firebase.FirebaseApplication('https://gwc-iot-842cd-default-rtdb.firebaseio.com/', None)
result = firebase.get('/Data','')
def getData():
    my_dict={"Acetona":[],"CO":[],"CO2":[],"DateTime":[],"Humidity":[],"NH4":[],"Temperature":[],"Tolueno":[]}
    for k, v in result.items():
        for s,d in v.items():
            if(k=='Acetona'):
                my_dict['Acetona'].append((d))
            elif(k=='CO'):
                my_dict['CO'].append((d))
            elif(k=='CO2'):
                my_dict['CO2'].append((d))
            elif(k=='DateTime'):
                my_dict['DateTime'].append(d)
            elif(k=='Humidity'):
                my_dict['Humidity'].append(d)
            elif(k=='NH4'):
                my_dict['NH4'].append((d))
            elif(k=='Temperature'):
                my_dict['Temperature'].append(d)
            else:
                my_dict['Tolueno'].append((d))
    with open('out.json', 'w') as fp:
        json.dump(my_dict, fp)

schedule.every(60).minutes.do(getData)
while True:
    schedule.run_pending()
    time.sleep(1)