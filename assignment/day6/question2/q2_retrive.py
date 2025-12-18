# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smartagriculture",
    use_pure = True
)

# form a query to be executed in mysql
query = "select * from soilmoisture";

# create cursor to execute query
cursor = connection.cursor()

# execute qeury with cursor
cursor.execute(query)

# get required data from cursor
sensor_readings = cursor.fetchall()

# print sensor readings data
#print(sensor_readings)

for iot_data in sensor_readings:
    print(iot_data)

# close the cursor
cursor.close()

# close connection with mysql server
connection.close()