#define IR1 A0
#define IR2 A1
#define IR3 A2
#define IR4 A3 
#define IR5 A4
#define IR6 A5
#define IR7 A6
#define IR8 A7
#define left 9
#define right 11
#define RF 8
#define RB 7
#define LF 4
#define LB 2

char i;
char check;

int ir1, ir2, ir3, ir4, ir5, ir6, ir7, ir8;   //  ir variables
int  speedf = 70 , rev = 50 , setspeed,  sh = 100, sl = 0;

float kp = 1, ki = 0, kd =0 ;    // pid constants

float error = 0, P = 0, I = 0, D = 0, pidValue = 0, previous_error = 0; // pid variables
float speed_HIGH = 90, speed_right = 0, speed_left = 0;   // speed for pid



void setup() {
  pinMode(RF, OUTPUT);
  pinMode(RB, OUTPUT);
  pinMode(LF, OUTPUT);
  pinMode(LB, OUTPUT);
  pinMode(left, OUTPUT);
  pinMode(right, OUTPUT);
  pinMode(IR1, INPUT);
  pinMode(IR2, INPUT);
  pinMode(IR3, INPUT);
  pinMode(IR4, INPUT);
  pinMode(IR5, INPUT);
  pinMode(IR6, INPUT);
  pinMode(IR7, INPUT);
  pinMode(IR8, INPUT);
  Serial.begin(9600);

}


void moveForward();
void turnLeft();
void turnAround_left();
void turnAroud_right();
void turnRight();
void irReads();
void arc();
void pid_cal();
void read_error();
void conditions();

void loop() {

irReads();
read_error();
pid_cal();
arc();
conditions();


if(check=='f'){    // forward
  
  moveForward();
}



if(check=='l'){   // left turn
  turnLeft();
  delay(250);
}



if(check=='r'){  // turn right
  turnRight();
  delay(250);
  
}

if(check=='j'){  // junction
  turnRight();
  delay(400);
}

if(check=="al"){   // left trun around
  
  turnAround_left();
}



if(check=="ar")  // right around
{
  
  turnAround_right();
}



}











void irReads()
{
  ir1 = analogRead(IR1)>500 ? 1:0;
  ir2 = analogRead(IR2)>500 ? 1:0;
  ir3 = analogRead(IR3)>500 ? 1:0;
  ir4 = analogRead(IR4)>500 ? 1:0;
  ir5 = analogRead(IR5)>500 ? 1:0;
  ir6 = analogRead(IR6)>500 ? 1:0;
  ir7 = analogRead(IR7)>500 ? 1:0;
  ir8 = analogRead(IR8)>500 ? 1:0;
  
}


void moveForward()
{
  digitalWrite(RF, HIGH);
  digitalWrite(RB, LOW);
  digitalWrite(LF, HIGH);
  digitalWrite(LB, LOW);
  analogWrite(left, speedf);
  analogWrite(right, speedf);
}


void turnAround_right()
{ 
  digitalWrite(LF, HIGH);
  digitalWrite(LB, LOW);
  digitalWrite(RF, LOW);
  digitalWrite(RB, HIGH);
  analogWrite(right, rev);
  analogWrite(left, rev);

}

void turnAround_left()
{ 
  digitalWrite(LF, LOW);
  digitalWrite(LB, HIGH);
  digitalWrite(RF, HIGH);
  digitalWrite(RB, LOW);
  analogWrite(right, rev);
  analogWrite(left, rev);

}



void turnRight()
{
  digitalWrite(RB, LOW);
  digitalWrite(RF, LOW);
  digitalWrite(LB, LOW);
  digitalWrite(LF, HIGH);
  analogWrite(right, sl);
  analogWrite(left, sh);

}


void turnLeft()
{
  digitalWrite(RB, LOW);
  digitalWrite(RF, HIGH);
  digitalWrite(LF, LOW);
  digitalWrite(LB, LOW);
  analogWrite(right, sh);
  analogWrite(left, sl);

}

void read_error() {
  if (ir1 == 1 && ir2 == 0 && ir3 == 0 && ir4 == 0 && ir5 == 0 && ir6 == 0 && ir7 == 0 && ir8 == 0 ) {
    error = -7;
  }

  if (ir1 == 1 && ir2 == 1 && ir3 == 0 && ir4 == 0 && ir5 == 0 && ir6 == 0 && ir7 == 0 && ir8 == 0 ) {
    error = -6;
  }
  if (ir1 == 0 && ir2 == 1 && ir3 == 0 && ir4 == 0 && ir5 == 0 && ir6 == 0 && ir7 == 0 && ir8 == 0 ) {
    error = -5;
  }
  if (ir1 == 0 && ir2 == 1 && ir3 == 1 && ir4 == 0 && ir5 == 0 && ir6 == 0 && ir7 == 0 && ir8 == 0 ) {
    error = -4;
  }
  if (ir1 == 0 && ir2 == 0 && ir3 == 1 && ir4 == 0 && ir5 == 0 && ir6 == 0 && ir7 == 0 && ir8 == 0 ) {
    error = -3;
  }
  if (ir1 == 0 && ir2 == 0 && ir3 == 1  && ir4 == 1 && ir5 == 0 && ir6 == 0 && ir7 == 0 && ir8 == 0 ) {
    error = -2;
  }
  if (ir1 == 0 && ir2 == 0 && ir3 == 0 && ir4 == 1 && ir5 == 0 && ir6 == 0 && ir7 == 0 && ir8 == 0 ) {
    error = -1;
  }

  if (ir1 == 0 && ir2 == 0 && ir3 == 0 && ir4 == 0 && ir5 == 0 && ir6 == 0 && ir7 == 0 && ir8 == 1 ) {
    error = 7;
  }

  if (ir1 == 0 && ir2 == 0 && ir3 == 0 && ir4 == 0 && ir5 == 0 && ir6 == 0 && ir7 == 1 && ir8 == 1 ) {
    error = 6;
  }
  if (ir1 == 0 && ir2 == 0 && ir3 == 0 && ir4 == 0 && ir5 == 0 && ir6 == 0 && ir7 == 1 && ir8 == 0 ) {
    error = 5;
  }
  if (ir1 == 0 && ir2 == 0 && ir3 == 0 && ir4 == 0 && ir5 == 0 && ir6 == 1 && ir7 == 1 && ir8 == 0 ) {
    error = 4;
  }
  if (ir1 == 0 && ir2 == 0 && ir3 == 0 && ir4 == 0 && ir5 == 0 && ir6 == 1 && ir7 == 0 && ir8 == 0 ) {
    error = 3;
  }
  if (ir1 == 0 && ir2 == 0 && ir3 == 0 && ir4 == 0 && ir5 == 1 && ir6 == 1 && ir7 == 0 && ir8 == 0 ) {
    error = 2;
    
  }
  if (ir1 == 0 && ir2 == 0 && ir3 == 0 && ir4 == 0 && ir5 == 1 && ir6 == 0 && ir7 == 0 && ir8 == 0 ) {
    error = 1;
    
  }
  





}


void pid_cal()
{
  P = error;
  I = error + I;
  D = error - previous_error;

  pidValue = (kp * P) + (ki * I) + (kd * D);

  previous_error = error;
}

void arc()
{
  speed_right = speed_HIGH + pidValue;
  speed_left = speed_HIGH - pidValue;


  digitalWrite(RF, HIGH);
  digitalWrite(RB, LOW);
  digitalWrite(LF, HIGH);
  digitalWrite(LB, LOW);
  analogWrite(right, speed_right);
  analogWrite(left, speed_left);
}

void conditions(){

if(ir8==0 && ir7==0 && ir6==0 && ir5==1 && ir4==1 && ir3==0 && ir2==0 && ir1==0){
  
  check ='f';
}

if(ir8==0 && ir7==0 && ir6==0 && ir5==1 && ir4==1 && ir3==1 && ir2==1 && ir1==1){
  i='r';
  check ='r';
}
if(ir8==1 && ir7==1 && ir6==1 && ir5==1 && ir4==1 && ir3==0 && ir2==0 && ir1==0){
  i='l';
  check ='l';
  
}

if(ir8==1 && ir7==1 && ir6==1 && ir5==1 && ir4==1 && ir3==1 && ir2==1 && ir1==1){
  
  check ='j';
}

if(ir8==0 && ir7==0 && ir6==0 && ir5==0 && ir4==0 && ir3==0 && ir2==0 && ir1==0 && i=='r' ){
  
  check = "ar";
}

if(ir8==0 && ir7==0 && ir6==0 && ir5==0 && ir4==0 && ir3==0 && ir2==0 && ir1==0 && i=='l' ){
  
  check = "al";
}


}
