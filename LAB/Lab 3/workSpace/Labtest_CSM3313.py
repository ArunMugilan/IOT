import time
import json
from dht import DHT11
from machine import Pin

dht11 = DHT11(Pin(14))

data_python = []
data_json = []

while True:
    time.sleep(3)
    dht11.measure()
    
    temperature = dht11.temperature()
    humidity = dht11.humidity()
    
    print("Temperature:", temperature, "C")
    print("Humidity:", humidity, "% RH")
    print("")
    
    data_python.append({"Temp": temperature, "Hum": humidity})
    
    data_json.append({"Temp": temperature, "Hum": humidity})
    
    print("Data in Python format..!")
    print(data_python)
    print("")
    
    print("Data in JSON format..!")
    print(json.dumps(data_json))
    print("")
