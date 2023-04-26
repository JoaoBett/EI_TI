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

//---------------------------------

char URL[] = "iot.dei.estg.ipleiria.pt";

int PORTO = 80;

WiFiClient clienteWifi;

HttpClient clienteHTTP = HttpClient(clienteWifi, URL, PORTO);

char responseBody[];


}

void loop() {
  // put your main code here, to run repeatedly:
clienteHTTP.get("/api/api.php?sensor=temp");

responseBody = clienteHTTP.responseBody();

Serial.println("%s",responseBody);
delay(5000);


}
