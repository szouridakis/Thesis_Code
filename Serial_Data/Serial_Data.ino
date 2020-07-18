
/**************************************************************************/
/*!
This is a demo for the Adafruit MCP9808 breakout
----> http://www.adafruit.com/products/1782
Adafruit invests time and resources providing this open source code,
please support Adafruit and open-source hardware by purchasing
products from Adafruit!
*/
/**************************************************************************/
#include <Arduino.h>
#include <include/twi.h>

#include <Wire.h>
#include "Adafruit_MCP9808.h"  //add "#define Wire Wire1" on the first row of the cpp file
#include <Adafruit_AMG88xx.h>
#include <Adafruit_MLX90614.h>
#include "DHT.h"

#define DHTPIN 2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321


#define ADDR      0x5A

//EEPROM 32x16
#define TO_MAX    0x00
#define TO_MIN    0x01
#define PWM_CTRL  0x02

//RAM 32x16
#define RAW_IR_1  0x04
#define RAW_IR_2  0x05
#define TA        0x06
#define TOBJ_1    0x07
#define TOBJ_2    0x08

#define SYNC_PIN  2

static const uint32_t TWI_CLOCK = 100000;
static const uint32_t RECV_TIMEOUT = 100000;
static const uint32_t XMIT_TIMEOUT = 100000;

Twi *pTwi = WIRE_INTERFACE;



// Create the MCP9808 temperature sensor object
Adafruit_MCP9808 tempsensor1 = Adafruit_MCP9808();
Adafruit_MCP9808 tempsensor2 = Adafruit_MCP9808();
//Adafruit_MLX90614 mlx = Adafruit_MLX90614();
Adafruit_AMG88xx amg;
float pixels[AMG88xx_PIXEL_ARRAY_SIZE];
DHT dht(DHTPIN, DHTTYPE);

int soilPin = A0;//Declare a variable for the soil moisture sensor 
int val = 0;

static void Wire_Init(void) {
  pmc_enable_periph_clk(WIRE_INTERFACE_ID);
  PIO_Configure(
  g_APinDescription[PIN_WIRE_SDA].pPort,
  g_APinDescription[PIN_WIRE_SDA].ulPinType,
  g_APinDescription[PIN_WIRE_SDA].ulPin,
  g_APinDescription[PIN_WIRE_SDA].ulPinConfiguration);
  PIO_Configure(
  g_APinDescription[PIN_WIRE_SCL].pPort,
  g_APinDescription[PIN_WIRE_SCL].ulPinType,
  g_APinDescription[PIN_WIRE_SCL].ulPin,
  g_APinDescription[PIN_WIRE_SCL].ulPinConfiguration);

  NVIC_DisableIRQ(TWI1_IRQn);
  NVIC_ClearPendingIRQ(TWI1_IRQn);
  NVIC_SetPriority(TWI1_IRQn, 0);
  NVIC_EnableIRQ(TWI1_IRQn);
}

static void Wire1_Init(void) {
    pmc_enable_periph_clk(WIRE1_INTERFACE_ID);
  PIO_Configure(
      g_APinDescription[PIN_WIRE1_SDA].pPort,
      g_APinDescription[PIN_WIRE1_SDA].ulPinType,
      g_APinDescription[PIN_WIRE1_SDA].ulPin,
      g_APinDescription[PIN_WIRE1_SDA].ulPinConfiguration);
  PIO_Configure(
      g_APinDescription[PIN_WIRE1_SCL].pPort,
      g_APinDescription[PIN_WIRE1_SCL].ulPinType,
      g_APinDescription[PIN_WIRE1_SCL].ulPin,
      g_APinDescription[PIN_WIRE1_SCL].ulPinConfiguration);

  NVIC_DisableIRQ(TWI0_IRQn);
  NVIC_ClearPendingIRQ(TWI0_IRQn);
  NVIC_SetPriority(TWI0_IRQn, 0);
  NVIC_EnableIRQ(TWI0_IRQn);
}




void setup() {
   
  Serial.begin(9600);
  
  pinMode(SYNC_PIN, OUTPUT);
  digitalWrite(SYNC_PIN, LOW);

  Wire_Init();
  // Disable PDC channel
  pTwi->TWI_PTCR = UART_PTCR_RXTDIS | UART_PTCR_TXTDIS;
  TWI_ConfigureMaster(pTwi, TWI_CLOCK, VARIANT_MCK);

  dht.begin();
  while (!Serial); //waits for serial terminal to be open, necessary in newer arduino boards.
  Serial.println("DAQ System booted!");
  
  // Make sure the sensor is found, you can also pass in a different i2c
  // address with tempsensor.begin(0x19) for example, also can be left in blank for default address use
  // Also there is a table with all addres possible for this sensor, you can connect multiple sensors
  // to the same i2c bus, just configure each sensor with a different address and define multiple objects for that
  //  A2 A1 A0 address
  //  0  0  0   0x18  this is the default address
  //  0  0  1   0x19
  //  0  1  0   0x1A
  //  0  1  1   0x1B
  //  1  0  0   0x1C
  //  1  0  1   0x1D
  //  1  1  0   0x1E
  //  1  1  1   0x1F
  if (!tempsensor1.begin(0x18)) {
    Serial.println("Couldn't find MCP9808! Check your connections and verify the address is correct.");
    while (1);
  }

   if (!tempsensor2.begin(0x19)) {
    Serial.println("Couldn't find MCP9808 19! Check your connections and verify the address is correct.");
    while (1);
  }

  if (!amg.begin()) {
        Serial.println("Could not find a valid AMG88xx sensor, check wiring!");
        while (1);
    }

  
  //mlx.begin();

   delay(100); // let sensor boot up
   
  // Serial.println("Found AMG!"); 
  // Serial.println();
  // Serial.println("Found MCP9808!");
  // Serial.println();

  tempsensor1.setResolution(3); // sets the resolution mode of reading, the modes are defined in the table bellow:
  tempsensor2.setResolution(3);
  // Mode Resolution SampleTime
  //  0    0.5°C       30 ms
  //  1    0.25°C      65 ms
  //  2    0.125°C     130 ms
  //  3    0.0625°C    250 ms
}

void loop() {
  
static char command ;
static bool sending = 0;
 
 if (Serial.available() >0 ) {
    
      command = Serial.read();
      
             }
                   
    switch (command) {
        case 'B':
          {
              sending= 1;
              break;
          }
          
         case 'S':
          {
             sending= 0;
             break;                      
          }
          
          default:
          {
            break;
            }
            
                } 

    switch(sending){
        case 1:{
              //delay(1000);
              
              printMCPTemp();
              printDHTmeas();
              printMLX();
              readSoil();
              printThermalTable();
              delay(1000);       
              break;
              }
              
        case 0:{
          
              break;
              }
        
                  }             
                              
  } 
      
  
 

              

void printThermalTable(){

    amg.readPixels(pixels);
    Serial.print("[");
    for(int i=1; i<=AMG88xx_PIXEL_ARRAY_SIZE; i++){
      Serial.print(pixels[i-1]);
      Serial.print(", ");
      if( i%8 == 0 ) Serial.println();
    }
    Serial.println("]");
    //Serial.println();
}

void printMCPTemp(){

    float c1 = tempsensor1.readTempC();
    float c2 = tempsensor2.readTempC();
    
    Serial.print("MCP9808 in address 0x18: ");
    Serial.println(c1, 2); //Serial.println("*C.");
  
    Serial.print("MCP9808 in address 0x19: ");
    Serial.println(c2, 2); //Serial.println("*C.");
}

void printDHTmeas(){

    float h = dht.readHumidity();
    float t = dht.readTemperature();
    // Compute heat index in Celsius (isFahreheit = false)
    float hic = dht.computeHeatIndex(t, h, false);

    
    Serial.print("DHTHum: ");
    Serial.println(h);
    
    Serial.print("DHTTemp: ");
    Serial.println(t);

    Serial.print("DHTHI: ");
    Serial.println(hic);
}

void printMLX(){

  //Serial.print("MLXAmb: "); Serial.println(mlx.readAmbientTempC()); 
  //Serial.print("MLXObj: "); Serial.println(mlx.readObjectTempC()); 


  uint16_t tempUK;
  float tempK;
  uint8_t hB, lB, pec;

  digitalWrite(SYNC_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(SYNC_PIN, LOW);

  TWI_StartRead(pTwi, ADDR, TOBJ_1, 1);

  lB = readByte();
  hB = readByte();
  
  //last read
  TWI_SendSTOPCondition(pTwi);
  pec = readByte();
  
  while (!TWI_TransferComplete(pTwi)) 
    ;
  //TWI_WaitTransferComplete(pTwi, RECV_TIMEOUT);

  tempUK = (hB << 8) | lB;
  if(tempUK & (1 << 16)) {
    Serial.print("Error !");
    Serial.println(tempK);
  } 
  else {
    tempK = ((float)tempUK * 2) / 100 ;
    //Serial.print("Temp UK: ");
    //Serial.print(tempUK);
    Serial.print("MLXObj: ");
    Serial.println(tempK - 273.15);
  }

TWI_StartRead(pTwi, ADDR, TA, 1);

  lB = readByte();
  hB = readByte();
  
  //last read
  TWI_SendSTOPCondition(pTwi);
  pec = readByte();
  
  while (!TWI_TransferComplete(pTwi)) 
    ;
  //TWI_WaitTransferComplete(pTwi, RECV_TIMEOUT);

  tempUK = (hB << 8) | lB;
  if(tempUK & (1 << 16)) {
    Serial.print("Error !");
    Serial.println(tempK);
  } 
  else {
    tempK = ((float)tempUK * 2) / 100 ;
    //Serial.print("Temp UK: ");
    //Serial.print(tempUK);
    Serial.print("MLXAmb: ");
    Serial.println(tempK - 273.15);
  }

}


uint8_t readByte() {
  //TWI_WaitByteReceived(pTwi, RECV_TIMEOUT);
  while (!TWI_ByteReceived(pTwi))
    ;
  return TWI_ReadByte(pTwi);
}

static inline bool TWI_WaitTransferComplete(Twi *_twi, uint32_t _timeout) {
  while (!TWI_TransferComplete(_twi)) {
    if (TWI_FailedAcknowledge(_twi))
      return false;
    if (--_timeout == 0)
      return false;
  }
  return true;
}

static inline bool TWI_WaitByteReceived(Twi *_twi, uint32_t _timeout) {
  while (!TWI_ByteReceived(_twi)) {
    if (TWI_FailedAcknowledge(_twi))
      return false;
    if (--_timeout == 0)
      return false;
  }
  return true;
}

static inline bool TWI_FailedAcknowledge(Twi *pTwi) {
  return pTwi->TWI_SR & TWI_SR_NACK;
}


void readSoil()
{
    val = analogRead(soilPin);//Read the SIG value form sensor 
    Serial.print("Soil Moisture: ");    
    //get soil moisture value from the function below and print it
    Serial.println(val);
}
