from flask import Flask, request
from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery
from datetime import datetime

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<h1>Smart Agriculture Server Running</h1>"


# ---------------- CREATE ----------------
@server.route('/soilmoisture', methods=['POST'])
def create_soil_moisture():
    data = request.get_json()

    sensor_id = data.get('SensorID')
    moisture = data.get('MoistureLevel')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    query = f"""
        INSERT INTO soilmoisture (SensorID, MoistureLevel, ReadingTime)
        VALUES ({sensor_id}, {moisture}, '{timestamp}');
    """

    executeQuery(query=query)
    return "Soil moisture reading added successfully"


# ---------------- READ ----------------
@server.route('/soilmoisture', methods=['GET'])
def retrieve_soil_moisture():
    query = "SELECT * FROM soilmoisture;"
    data = executeSelectQuery(query=query)
    return {"soilmoisture": data}


# ---------------- UPDATE ----------------
@server.route('/soilmoisture', methods=['PUT'])
def update_soil_moisture():
    data = request.get_json()

    sensor_id = data.get('SensorID')
    moisture = data.get('MoistureLevel')

    query = f"""
        UPDATE soilmoisture
        SET MoistureLevel = {moisture}
        WHERE SensorID = {sensor_id};
    """

    executeQuery(query=query)
    return "Soil moisture updated successfully"


# ---------------- DELETE ----------------
@server.route('/soilmoisture', methods=['DELETE'])
def delete_soil_moisture():
    data = request.get_json()
    sensor_id = data.get('SensorID')

    query = f"DELETE FROM soilmoisture WHERE SensorID = {sensor_id};"
    executeQuery(query=query)

    return "Soil moisture record deleted successfully"


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
