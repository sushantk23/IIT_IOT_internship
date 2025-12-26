#include <WiFi.h>
#include <ArduinoMqttClient.h>

/* ---------- WiFi Credentials ---------- */
const char* ssid = "pramod";
const char* password = "Pramod08";

/* ---------- MQTT Broker Details ---------- */
const char* broker = "broker.hivemq.com";
int port = 1883;
const char* topic = "room/light";

/* ---------- LED Pin ---------- */
#define LED_PIN 2   // Change if needed

WiFiClient wifiClient;
MqttClient subscriber(wifiClient);

void setup() {
  Serial.begin(9600);
  delay(1000);

  /* LED setup */
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  /* WiFi connection */
  Serial.print("Connecting to WiFi");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected");
  Serial.print("IP Address: 10.219.247.222");
  Serial.println(WiFi.localIP());

  /* MQTT connection */
  Serial.print("Connecting to MQTT Broker...");
  if (!subscriber.connect(broker, port)) {
    Serial.println("FAILED");
    while (1);
  }

  Serial.println("Connected to the Broker");

  /* Subscribe to topic */
  subscriber.subscribe(topic);
  Serial.println("Topic is subscribed");
}

void loop() {

  int messageSize = subscriber.parseMessage();

  if (messageSize) {
    Serial.print("Message received: ");

    String message = "";

    while (subscriber.available()) {
      char c = (char)subscriber.read();
      message += c;
    }

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
}
