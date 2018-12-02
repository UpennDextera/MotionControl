# Servo Control
import time
import wiringpi
 
# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()
 
# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT) #wrist pan
wiringpi.pinMode(19, wiringpi.GPIO.PWM_OUTPUT) #wrist tilt
 
# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
 
# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
 
delay_period = 0.01

int servoPan = 50 # placeholder, get from IK
int servoTilt = 50

wiringpi.pwmWrite(18, servoPan)
wiringpi.pwmWrite(19, servoTilt)
time.sleep(delay_period)

# while True:
#         for pulse in range(50, 250, 1):
#                 wiringpi.pwmWrite(18, pulse)
#                 time.sleep(delay_period)
#         for pulse in range(250, 50, -1):
#                 wiringpi.pwmWrite(18, pulse)
#                 time.sleep(delay_period)