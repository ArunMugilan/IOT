import time
import json
from dht import DHT22
from machine import Pin

dht22 = DHT22(Pin(14))

data_python = []
data_json = []

while True:
    time.sleep(3)
    dht11.measure()
    
    temperature = dht11.temperature()
    humidity = dht11.humidity()
    
    print("Temperature:", temperature, "C")
    print("Humidity:", humidity, "%")
    
    data_python.append({"temp": temperature, "hum": humidity})
    
    data_json.append({"temp": temperature, "hum": humidity})
    
    print("Data in Python format..!")
    print(data_python)
    
    print("Data in JSON format..!")
    print(json.dumps(data_json))
