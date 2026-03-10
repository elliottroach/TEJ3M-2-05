// created by Elliott Roach
// created on mar 2026
// this turns a servo 0 to 90

#include <Servo.h>

Servo servoPinTwo;


void setup() {
    // initializing pins/setup
    servoPinTwo.attach(2);
    servoPinTwo.write(0);
  delay(1000);
}


void loop() {
    // this blinks the light in infinite loop
    servoPinTwo.write(90);
    delay(1000);
    servoPinTwo.write(0);
    delay(1000);
}
