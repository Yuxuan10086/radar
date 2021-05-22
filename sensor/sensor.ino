#include <MsTimer2.h>
const int Trig = 7;
const int Echo = 6; 
double distance, time;
int num = 0; 
void show(){
  Serial.println(num % 314 * 0.01); 
  Serial.println(distance);                                
  num++;
}
void setup() {
  Serial.begin(9600);
  MsTimer2::set(125, show); //设置中断，每1000ms进入一次中断服务程序 onTimer()
  MsTimer2::start();
  pinMode(Trig, OUTPUT); 
  pinMode(Echo, INPUT);         
}

void loop() {
  digitalWrite(Trig, LOW);                                 
  delayMicroseconds(2);                                   
  digitalWrite(Trig, HIGH);                               
  delayMicroseconds(10);                                  
  digitalWrite(Trig, LOW);                                
  time = pulseIn(Echo, HIGH);                              
  distance = time / 58 ;     
  if(distance > 200)
    distance = 200;                            
  delay(100); 
}
