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
#include <stdio.h>

char endOfTempDelimiter = ">";

int thermoDO = 3;
int thermoCS = 4;
int thermoCLK = 5;

Adafruit_MAX31855 thermocouple(thermoCLK, thermoCS, thermoDO);
  
void setup() {
  Serial.begin(9600);
  
  // Serial.println("MAX31855 test");
  // wait for MAX chip to stabilize
  delay(500);

}
  
//<II,FF,CC>  
 
void loop() {
		double readI = thermocouple.readInternal();
		double readC = thermocouple.readCelsius(); 
		double readF = thermocouple.readFarenheit();
		
		char* nan_placeholder = "00"; 
		char output[9]; 
				
  		if (isnan(readC))
  			readC = nan_placeholder;	
  		
  		if (isnan(readF)) 
  			readF = nan_placeholder; 
  		
  		// Option 1...
		Serial.print(readI); 
		Serial.print(","); 
		Serial.print(readC); 
		Serial.print(","); 
		Serial.print(readF);
		Serial.print(endOfTempDelimiter);
		
  		
  		snprintf(output, sizeof(output), "%2s,%2s,%2s\n", readI,
  				readC, readF);
  		  		
  		Serial.println(i);
  		
  		delay(1000);
  		
  		
	}
}
