#include <WiFi101.h>
#include <ArduinoHttpClient.h>

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
while(!Serial);

char SSID[] = "labs";
char PASS_WIFI[] = "robot1cA!ESTG";
WiFi.begin(SSID,PASS_WIFI);
int wifi = WiFi.status();

while(wifi!=1){
  Serial.println('.');
  delay(500);
}


WiFi.localIP(); //Endereço Ip local
WiFi.subnetMask(); //A mascara de rede
WiFi.gatewayIP(); //O endereço de Ip do default gateway
WiFi.RSSI(); //potencia do sinal

}

void loop() {
  // put your main code here, to run repeatedly:


}
