import gpiozero


class DOF:

    def __init__(self):
        pass

    #Will be in degrees or inches
    def set_position(self, position):
        pass

    def set_velocity(self, velocity):
        pass

    def set_limits(self, minLimit, maxLimit):
        self.minLimit = minLimit
        self.maxLimit = maxLimit

class ServoDOF(DOF):

    def __init__(self, pin):
        super().__init__(ServoDOF, self)
        self.servo = gpiozero.AngularServo(pin)
        self.set_limits(-90, 90)

    def set_position(self, position):
        if position > self.minLimit and position < self.maxLimit:
            self.servo.angle = position
        else:
            print('Position input exceeds limits')


class MotorDOF(DOF):

    def __init__(self, pinA, pinB):
        super().__init__(ServoDOF, self)
        self.motor = gpiozero.motor(pinA, pinB)

    def setPower(self, power):
        if power > 0:
            self.motor.forward(power)
        else:
            self.motor.backward(power)
