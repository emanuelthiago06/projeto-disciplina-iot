#include <SPI.h>
#include <LoRa.h>
#include <Wire.h>  
#include "SSD1306.h" 

#define SCK     5    // GPIO5  -- SX1278's SCK
#define MISO    19   // GPIO19 -- SX1278's MISnO
#define MOSI    27   // GPIO27 -- SX1278's MOSI
#define SS      18   // GPIO18 -- SX1278's CS
#define RST     14   // GPIO14 -- SX1278's RESET
#define DI0     26   // GPIO26 -- SX1278's IRQ(Interrupt Request)

unsigned int counter = 0;
unsigned int value;

SSD1306 display(0x3c, 21, 22);
String rssi = "RSSI --";
String packSize = "--";
String packet ;
int device = 3;
char message[256];

 

void setup() {
  pinMode(16,OUTPUT);
  pinMode(2,OUTPUT);
  randomSeed(millis());
  digitalWrite(16, LOW);    // set GPIO16 low to reset OLED
  delay(50); 
  digitalWrite(16, HIGH); // while OLED is running, must set GPIO16 in high
  
  Serial.begin(115200);
  while (!Serial);
  Serial.println();
  Serial.println("LoRa Sender Test");
  
  SPI.begin(SCK,MISO,MOSI,SS);
  LoRa.setPins(SS,RST,DI0);
  if (!LoRa.begin(868100000)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
  //LoRa.onReceive(cbk);
//  LoRa.receive();
  Serial.println("init ok");
  display.init();
  display.flipScreenVertically();  
  display.setFont(ArialMT_Plain_10);
   
  delay(1500);
}

void loop() {
  display.clear();
  display.setTextAlignment(TEXT_ALIGN_LEFT);
  display.setFont(ArialMT_Plain_10);
  value = random(0, 10);
  sprintf(message, "{\"value\": %d, \"device\": \"%d\", \"counter\": %d}\0", value, device, counter);
  display.drawString(0, 0, "Sending packet: ");
  display.drawString(90, 0, String(counter));
  display.drawString(0, 10, String("Device: ") + device);
  display.drawString(0, 20, String("Value: ") + String(value));
  display.display();
  LoRa.beginPacket( );
  LoRa.print(message);
  LoRa.endPacket();

  counter++;
  delay(10000);                       // wait for a second
}
