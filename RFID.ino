#include <SPI.h>
#include <MFRC522.h>

#define LED 8

#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);
 
void setup() 
{
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();
  
  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);
}
void loop() 
{
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    digitalWrite(LED,LOW);
    return;
  }
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
     digitalWrite(LED,HIGH);
  }
  Serial.println();
  content.toUpperCase();
  delay(3000);
} 
