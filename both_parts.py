'''
First part reads temperature_c from a DHT connecto to the pi

second part save the data as CSV
'''

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
#record entrys to a list hen a file using a DHT temperature_cetur sensor
import time
import board
import adafruit_dht
import random

# temperature_c = random.randint(-10,35)
# humidity = random.randint(10,100)
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

temperature_c_list =[]
humi_list =[]

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_cerature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "temperature_c: {:.1f} F / {:.1f} C    humidityity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
        
        temperature_c_list.append(temperature_c)
        humi_list.append(humidity)
        print(humi_list)
        print(temperature_c_list)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        break

    time.sleep(2.0)
'''
#second part  write csv
import random

temperature_c = random.randint(-10,35)
humidity = random.randint(10,100)
'''


print(temperature_c)
print(humidity)

csvout = str(f'{temperature_c},{humidity} \n')
print('temperature_c is ' + str(temperature_c) +'C and humidityity is ' + str(humidity) +'%')

print(csvout)

#append to file Code goes here
file = open("temperature_c_data.csv" , 'a')

#TO READ THE FILE
#print(file.read())



print(file)
file.write(csvout)
file.close

file = open("temperature_c_data.csv" , 'r')

#TO READ THE FILE
print(file.read())
file.close

#Loop back or wait till the next measurement

