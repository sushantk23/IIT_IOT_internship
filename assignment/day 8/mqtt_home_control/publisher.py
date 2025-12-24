import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("MQTT Publisher started")

while True:
    appliance = input("Enter appliance (light/fan): ").lower()
    status = input("Enter status (ON/OFF): ").upper()

    if status not in ["ON", "OFF"]:
        print("Invalid status! Use ON or OFF")
        continue

    topic = f"home/{appliance}/control"
    client.publish(topic, status)

    print(f"Sent → {appliance.upper()} : {status}")
