#include <LiquidCrystal.h>
#include <SoftwareSerial.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
SoftwareSerial BTSerial(8, 7);

const int buzzerPin = A0;
const int ledPin = A1;

const byte numChars = 32;
char receivedChars[numChars];
boolean newData = false;

void setup() {
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  
  lcd.begin(16, 2);
  lcd.clear();
  lcd.print("Sistem Aktif");
  delay(1000);
  lcd.clear();
  
  lcd.setCursor(0, 0);
  lcd.print("Mesafe:"); 
  
  BTSerial.begin(9600);
}

void loop() {
  recvWithStartEndMarkers();
  
  if (newData == true) {
    int visualDistance = atoi(receivedChars);
    
    if (visualDistance > 0) {
       lcd.setCursor(8, 0);
       lcd.print("        "); 
       lcd.setCursor(8, 0);
       lcd.print(visualDistance);
       lcd.print("cm");
       
       lcd.setCursor(0, 1);
       if (visualDistance < 100) {
         digitalWrite(buzzerPin, HIGH);
         digitalWrite(ledPin, HIGH);
         lcd.print("TEHLIKE!       "); 
       } else if (visualDistance < 200) {
         digitalWrite(buzzerPin, LOW);
         digitalWrite(ledPin, HIGH);
         lcd.print("DIKKAT!         "); 
       } else {
         digitalWrite(buzzerPin, LOW);
         digitalWrite(ledPin, LOW);
         lcd.print("GUVENLI         "); 
       }
    }
    newData = false;
  }
}

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
 
    while (BTSerial.available() > 0 && newData == false) {
        rc = BTSerial.read();
        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) ndx = numChars - 1;
            }
            else {
                receivedChars[ndx] = '\0';
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }
        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}
