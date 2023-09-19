const int max_count = 1999;
char Input;

void setup() {
  DDRA = DDRA | B00000001;
  Serial.begin(115200);
  setTimerOne();
}

void setTimerOne() {
  cli();
  TCCR1A = 0;
  TCCR1B = (1 << WGM12);
  //TCCR1B |= (1 << CS11)|(1 << CS10);
  TCCR1B |= (1 << CS11);
  OCR1A = max_count;
  TCNT1 = 0;
  TIMSK1 |= (1 << OCIE1A);
  sei();
}

ISR(TIMER1_COMPA_vect) {
  isr();
}
void isr() {
  if(Serial.available()>0){
    Input = Serial.read();
    if (Input == '0') {
      PORTA &= !B00000001;
      //Serial.println(" ");
    }  else {
      PORTA |= B00000001;
      //Serial.println(" ");
  }
 }
}
void loop() {
//   if(Serial.available()>0){
//     Input = Serial.read();
//     if (Input == '0') {
//       PORTA &= !B00000001;
//       //Serial.println(" ");
//     }  else {
//       PORTA |= B00000001;
//       //Serial.println(" ");
//   }
//  }
//  delayMicroseconds(2000);
}