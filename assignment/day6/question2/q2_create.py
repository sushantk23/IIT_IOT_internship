# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smartagriculture",
    use_pure=True
)

# take input from user
SensorID = int(input("Enter sensor ID : "))
MoistureLevel = float(input("Enter moisture level : "))
ReadingTime = input("Enter date and time (YYYY-MM-DD HH:MM:SS) : ")

# form insert query
insert_query = f"""
INSERT INTO soilmoisture  
VALUES ({SensorID}, {MoistureLevel}, '{ReadingTime}');
"""

# create cursor
cursor = connection.cursor()

# execute insert query
cursor.execute(insert_query)

# commit changes
connection.commit()

cursor.close()
connection.close()