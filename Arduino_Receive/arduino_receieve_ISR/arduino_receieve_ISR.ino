const byte interrupt = 18;
volatile boolean Potential = true;
volatile boolean a = false;
float Interval = 1000;
volatile unsigned long int Last_time = 0;
volatile unsigned long int Now = 0;
volatile float count;

void InterruptChange(){  
    a = true;
}

void Counting_Signal(){
  Now = micros();
  count = round((Now - Last_time)/Interval);
  // Serial.print(count);
  Last_time = Now;
  // Serial.print("\n");
}

void setup (){
    attachInterrupt(digitalPinToInterrupt(interrupt), InterruptChange, CHANGE);
    Serial.begin(115200);
}

void loop (){
    if(a == true){
      Counting_Signal();
      Potential = !Potential;
      if(count < 19 && count > 0){
        for(int i=1 ; i<=count ; i++){
          Serial.print(Potential);
          Serial.print("\n");
        }
       }
      a = false;       
    }
}


