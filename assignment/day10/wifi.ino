#include <WiFi.h>

const char *ssid = "TEJAS";
const char *password = "1234567890";

void setup() {
  Serial.begin(115200);
  delay(1000);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  int retry = 0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    retry++;

    if (retry > 30) {
      Serial.println("\nFailed to connect!");
      Serial.println("Check WiFi name / password / 2.4GHz");
      return;
    }
  }

  Serial.println("\nWiFi Connected!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
}
