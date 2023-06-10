import time
from robot_control_class import RobotControl 
robotcontrol = RobotControl() 
class Robot:

    def __init__(self):
        print("initializing...")
        self.laser1 = robotcontrol.get_laser(360)
        self.robotmove_speed = 5
        self.robotmove_time = 1
        self.robotturn_clockwise = "clockwise"
        self.robotturn_speed = 1.4
        self.robotturn_time = 1
        self.row = 8
        self.col = 0
        self.turn = -1

    def robotmove(self):
        inputRow=8
        inputCol=9
        while self.laser1 > 1:
            robotcontrol.move_straight()
            self.laser1 = robotcontrol.get_laser(360)
            print("distance: ", self.laser1)
            if self.turn == -1:
                self.row -= 1
            elif self.turn == 1:
                self.row += 1
            elif self.turn == -2 :
                self.col -= 1
            else:
                self.col += 1 
            #print ("self col....................",self.col)
            #print ("self row....................",self.row)
            if inputRow == self.row and inputCol == self.col:
                print("I reached my destination!")
                return True

        robotcontrol.stop_robot()
        print("I'm too close to the wall... ")

    def robotturn(self):
        distance_right = robotcontrol.get_laser(180)
        distance_left = robotcontrol.get_laser(540)
        print("right",distance_right, "left", distance_left)
        if distance_right > distance_left:
            while self.laser1 < 1:
                robotcontrol.turn("counter-clockwise", self.robotturn_speed, self.robotturn_time)
                self.laser1 = robotcontrol.get_laser(360)
                print("right: distance: ", self.laser1)
            if self.turn == -1:
                self.turn = 2
            elif self.turn == 1:
                self.turn = -2
            elif self.turn == -2 :
                self.turn = -1
            else:
                self.turn = 1
        else:
            while self.laser1 < 1:
                robotcontrol.turn(self.robotturn_clockwise, self.robotturn_speed, self.robotturn_time)
                self.laser1 = robotcontrol.get_laser(360)
                print("left: distance: ", self.laser1)
            if self.turn == -1:
                self.turn = -2
            elif self.turn == 1:
                self.turn = 2
            elif self.turn == -2 :
                self.turn = 1
            else:
                self.turn = -1

        robotcontrol.stop_robot()
        print("I turned, let's go... ")

if __name__ == '__main__':

    robot = Robot()
    
    while not robotcontrol.ctrl_c:

        if robot.robotmove():
            robotcontrol.stop_robot()
            break
        robot.robotturn()