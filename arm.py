from dof import DOF, MotorDOF, ServoDOF


class Arm:

    def __init__(self):
        self.vertical = MotorDOF(17, 11)
        self.wrist_rotate = ServoDOF(19)
        self.wrist_tilt = ServoDOF(26)
        self.gripper_A = MotorDOF(22, 10)
        #self.gripper_B = MotorDOF()

    def set_dofs(self, dof_positions):
        self.vertical.set_position(dof_positions[0])
        self.wrist_rotate.set_position(dof_positions[1])
        self.wrist_rotate.set_position(dof_positions[2])
        self.gripper_A.set_position(dof_positions[3])
        self.gripper_B.set_position(dof_positions[4])
