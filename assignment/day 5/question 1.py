import math 
import os
num =16
print("sqrrt of 16 is:",math.sqrt(num))
print("pow of 2^3 is:",math.pow(2,3))
print("factorial of 5 is:",math.factorial(5))


angle = math.pi/2
print("sin of 90 degree is:",math.sin(angle))
print("cos of 90 degree is:",math.cos(angle))


value = 2.7
print("ceil value:",math.ceil(value))
print("floor value:",math.floor(value))

print("value of e is:",math.e)
print("value of pi is:",math.pi)

def area_of_circle():
    radius = (float(input("enter the area of cirlce:")))
    area = math.pi *radius ** 2
    print("area of circle is:",area)

area_of_circle()


print("Current directory:", os.getcwd())

if not os.path.exists("test"):
    os.mkdir("test")
    print("Folder created")