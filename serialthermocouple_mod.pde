/*************************************************** 
  This is an example for the Adafruit Thermocouple Sensor w/MAX31855K

  Designed specifically to work with the Adafruit Thermocouple Sensor
  ----> https://www.adafruit.com/products/269

  These displays use SPI to communicate, 3 pins are required to  
  interface
  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/

#include "Adafruit_MAX31855.h"

int thermoDO = 3;
int thermoCS = 4;
int thermoCLK = 5;

Adafruit_MAX31855 thermocouple(thermoCLK, thermoCS, thermoDO);
  
void setup() {
  Serial.begin(9600);
  
  Serial.println("MAX31855 test");
  // wait for MAX chip to stabilize
  delay(500);
  
  // basic readout test, just print the current temp
  if (Serial.available() > 0) {
		double i = thermocouple.readInternal();
  		double c = thermocouple.readCelsius();
  		double f = thermocouple.readFarenheit();
  		char nan_placeholder = "0"; 
  	
  		Serial.println(i)
  	
  		if (isnan(c)) {
  			Serial.println(nan_placeholder);	
  		} else {
  			Serial.println(c);
  		}
  	
 	 	if (isnan(f)) {
 	 		Serial.println(nan_placeholder);
  		} else {
  			Serial.println(f);
  		}
  	}
}
  
  
 
void loop() {
}