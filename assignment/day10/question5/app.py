from flask import Flask, request
import mysql.connector
from datetime import datetime
import paho.mqtt.publish as publish

app = Flask(__name__)

# ---------- MySQL Configuration ----------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smartagriculture"
)
cursor = db.cursor()

# ---------- MQTT Configuration ----------
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "alert/soilmoisture"

# ---------- Threshold ----------
THRESHOLD = 30

# ---------- API to Receive Moisture ----------
@app.route('/send_moisture', methods=['POST'])
def send_moisture():

    # Get data from request
    sensor_id = request.form.get('SensorID')
    moisture_raw = request.form.get('MoistureLevel')

    print("Received raw data -> SensorID:", sensor_id, "Moisture:", moisture_raw)

    # Convert moisture to integer safely
    moisture = int(moisture_raw.strip())
    reading_time = datetime.now()

    # Insert into database
    query = """
    INSERT INTO soilmoisture (SensorID, MoistureLevel, ReadingTime)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (sensor_id, moisture, reading_time))
    db.commit()

    print("Moisture data stored in database")

    # Check threshold and publish MQTT alert
    print("Threshold =", THRESHOLD)
    print("Moisture =", moisture)

    if moisture < THRESHOLD:
        alert_msg = f"ALERT! Sensor {sensor_id} moisture LOW: {moisture}"
        print("Publishing MQTT alert ->", alert_msg)

        publish.single(
            MQTT_TOPIC,
            alert_msg,
            hostname=MQTT_BROKER,
            port=MQTT_PORT
        )
    else:
        print("Moisture is normal, no MQTT alert")

    return "Moisture data stored successfully"

# ---------- Run Flask Server ----------
if __name__ == "__main__":
    app.run(debug=True)
