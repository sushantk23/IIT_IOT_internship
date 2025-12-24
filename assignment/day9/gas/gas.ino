#define mq2 34
#define val 2000

void setup() {
  Serial.begin(115200);
}

void loop() {
  int gas = analogRead(mq2);

  if(gas > val){
    Serial.print("Gas Value : ");
    Serial.println(gas);
    Serial.println("Gas Detected!...");
  }
  else{
    Serial.print("Gas Value : ");
    Serial.println(gas);
    Serial.println("No Gas Detected!...");
  }

  delay(1000);

}