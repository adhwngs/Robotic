from robot_control_class import RobotControl
import time

robotcontrol = RobotControl(robot_name="summit")

def move_x_seconds(secs):
    robotcontrol.move_straight()
    time.sleep(secs) #progres will hang here for 5 seconds
    robotcontrol.stop_robot()


move_x_seconds(5)