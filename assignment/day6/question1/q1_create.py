# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data",
    use_pure=True
)

# take input from user
id = int(input("Enter sensor id : "))
temperature = float(input("Enter temperature : "))
humidity = float(input("Enter humidity : "))
timestamp = input("Enter timestamp (YYYY-MM-DD HH:MM:SS) : ")

# form insert query
insert_query = f"""
INSERT INTO sensor_readings
VALUES ({id}, {temperature}, {humidity}, '{timestamp}');
"""

# create cursor
cursor = connection.cursor()

# execute insert query
cursor.execute(insert_query)

# commit changes
connection.commit()

cursor.close()
connection.close()