import random

temp = random.randint(-10,35)
humid = random.randint(10,100)

print(temp)
print(humid)

csvout = str(f'{temp},{humid} \n')
print('temp is ' + str(temp) +'C and humidity is ' + str(humid) +'%')

print(csvout)

#append to file Code goes here
file = open("temp_data.csv" , 'a')

#TO READ THE FILE
#print(file.read())



print(file)
file.write(csvout)
file.close

file = open("temp_data.csv" , 'r')

#TO READ THE FILE
print(file.read())
file.close

#Loop back or wait till the next measurement

