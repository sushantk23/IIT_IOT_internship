#include <WiFi.h>
#include <PubSubClient.h>

/* -------- WiFi Credentials -------- */
const char* ssid = "Tejas";
const char* password = "1234567890";

/* -------- MQTT Broker -------- */
const char* mqttServer = "broker.hivemq.com";
const int mqttPort = 1883;
const char* mqttTopic = "home/led/control";

/* -------- LED Pin -------- */
#define LED_PIN 2

WiFiClient espClient;
PubSubClient client(espClient);

/* -------- MQTT Callback -------- */
void callback(char* topic, byte* payload, unsigned int length) {
  String message = "";

  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  Serial.print("Message received: ");
  Serial.println(message);

  if (message == "ON") {
    digitalWrite(LED_PIN, HIGH);
    Serial.println("LED ON");
  } 
  else if (message == "OFF") {
    digitalWrite(LED_PIN, LOW);
    Serial.println("LED OFF");
  }
}

/* -------- Connect to WiFi -------- */
void connectWiFi() {
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected");
}

/* -------- Connect to MQTT -------- */
void connectMQTT() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");

    if (client.connect("ESP32_LED_CLIENT")) {
      Serial.println("Connected");
      client.subscribe(mqttTopic);
      Serial.println("Subscribed to topic");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);

  connectWiFi();

  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    connectMQTT();
  }
  client.loop();
}
