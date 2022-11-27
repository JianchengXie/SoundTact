int doa = 45;
int intensity = 255;
const int pins[4] = {5, 6, 10, 11};
const int touch_pin = 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.setTimeout(1);
  for (int i = 0; i < 4; i++)
    pinMode(pins[i], OUTPUT);
  pinMode(touch_pin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    doa = Serial.readStringUntil(' ').toInt();
    intensity = Serial.readStringUntil('\n').toInt();
  } 
  if (doa<90) {
    analogWrite(pins[0], intensity*cos(doa*PI/180.));
    analogWrite(pins[1], intensity*sin(doa*PI/180.));
    analogWrite(pins[2], 0);
    analogWrite(pins[3], 0);
  }
  else if (doa<180) {
    analogWrite(pins[1], intensity*cos((doa-90)*PI/180.));
    analogWrite(pins[2], intensity*sin((doa-90)*PI/180.));
    analogWrite(pins[0], 0);
    analogWrite(pins[3], 0);
  }
  else if (doa<270) {
    analogWrite(pins[2], intensity*cos((doa-180)*PI/180.));
    analogWrite(pins[3], intensity*sin((doa-180)*PI/180.));
    analogWrite(pins[0], 0);
    analogWrite(pins[1], 0);
  }
  else {
    analogWrite(pins[3], intensity*cos((doa-270)*PI/180.));
    analogWrite(pins[0], intensity*sin((doa-270)*PI/180.));
    analogWrite(pins[1], 0);
    analogWrite(pins[2], 0);
  }
  Serial.println(digitalRead(touch_pin));
  delay(50);
}
