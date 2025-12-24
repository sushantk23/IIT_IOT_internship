import paho.mqtt.client as mqtt
import mysql.connector

# ---------- MySQL Connection ----------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="home_automation"
)

cursor = db.cursor()

# ---------- MQTT Callback ----------
def on_message(client, userdata, msg):
    print("MESSAGE RECEIVED")
    print(msg.topic, msg.payload.decode())

    appliance = msg.topic.split("/")[1]   # light / fan
    status = msg.payload.decode()         # ON / OFF

    query = """
    INSERT INTO appliance_status (appliance_name, status)
    VALUES (%s, %s)
    """
    cursor.execute(query, (appliance, status))
    db.commit()

    print(f"{appliance.upper()} turned {status}")

# ---------- MQTT Setup ----------
client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("home/+/control")

print("Subscriber started...")
client.loop_forever()
