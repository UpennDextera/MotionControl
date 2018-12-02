# DC motor control
import time
import wiringpi

bool goUp = false
bool goDown = false
int UP = 20
int DOWN = 21
int PWM = 22
int ENCODER = 23
float dutyCyc = 0.0
float Kp = 0.1 #gain

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(ENCODER, wiringpi.GPIO.INPUT) #encoder
wiringpi.pinMode(UP, wiringpi.GPIO.OUTPUT) #linear actuator dir 1
wiringpi.pinMode(DOWN, wiringpi.GPIO.OUTPUT) #linear actuator dir 2
wiringpi.pinMode(PWM, wiringpi.GPIO.PWM_OUTPUT) #linear actuator PWM

# divide down clock
wiringpi.pwmSetClock(192)

def getDuty(desiredPos):
	int currPos = wiringpi.analogRead(ENCODER) # map this to a linear position
	float error = desiredPos - currPos
	float propErr = Kp * error

	if propError > 0.1:
		goUp = true
		goDown = false
	elif propError < -0.1:
		goUp = false
		goDown = true
	else:
		goUp = false
		goDown = false

	dutyCyc = propError * 1024
	return;

def driveMotor():
	wiringpi.pwmWrite(PWM, dutyCyc)
	if goUp:
		wiringpi.digitalWrite(UP, 1)
		wiringpi.digitalWrite(DOWN, 0)
	elif goDown:
		wiringpi.digitalWrite(UP, 0)
		wiringpi.digitalWrite(DOWN, 1)
	else:
		wiringpi.digitalWrite(UP, 0)
		wiringpi.digitalWrite(DOWN, 0)
	return;
