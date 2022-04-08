from dynamixel_helper import DxlHelper

helper = DxlHelper("preset/example_0.json")

motor = helper.get_motor(4)
print(motor)
motor.set_torque(True)