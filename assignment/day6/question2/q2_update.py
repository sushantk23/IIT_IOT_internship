# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smartagriculture",
    use_pure = True
)

# form a query to be executed
SensorID = input("Enter id whose moisture level to be updated : ")
moisturelevel = input("Enter new moisture level : ")

query = f"update soilmoisture SET moisturelevel = '{moisturelevel}' where SensorID = {SensorID};"


# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()