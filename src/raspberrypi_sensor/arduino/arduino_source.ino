#include <dht11.h>
dht11 DHT;
#define DHT11_PIN 4
  
void setup(){
  Serial.begin(9600);
}
  
void loop(){
  int chk;
  chk = DHT.read(DHT11_PIN);    // READ DATA
  switch (chk){
    case DHTLIB_OK:  
                Serial.print(""); 
                Serial.print(DHT.humidity,1);
                Serial.print(",");  
                Serial.print(DHT.temperature,1);
                break;
    case DHTLIB_ERROR_CHECKSUM: 
                break;
    case DHTLIB_ERROR_TIMEOUT: 
                break;
    default: 
                break;
  }
  Serial.print(",");
  Serial.println(analogRead(0));
  delay(3600000/2);//relevé de mesure à chaque demi-heure
}
