const int max_count = 1999;  // 0.0001 sec when Prescaler == 64
volatile boolean signal;
void setup() {
  DDRA = DDRA | B00000000;
  Serial.begin(115200);
  setTimerOne();
}
void setTimerOne() {
  cli();  // 禁止中斷
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
void isr(){
  signal = !(PIND>>3);
  Serial.print(!(PIND>>3));
  Serial.print("\n");
}
void loop() {
}

