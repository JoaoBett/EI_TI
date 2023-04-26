#include <WiFi101.h>
#include <ArduinoHttpClient.h>

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
while(!Serial);

char SSID[] = "labs";
char PASS_WIFI[] = "robot1cA!ESTG"
WiFi.begin(SSID,PASS_WIFI);
WiFi.status();

while(Wifi.status()!=1){
  Serial.println(.);
  delay(500);
}
}

void loop() {
  // put your main code here, to run repeatedly:


}
