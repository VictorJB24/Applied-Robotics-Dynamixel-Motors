from dynamixel_sdk import *  # Uses Dynamixel SDK library
import os


"""
Logic of line following:

 - 7 sensors
 - 6 should see white (Not on line)
 - 7th should see black
 - 7th sensor in middle of robot; in between all other sensors
 - 3 on left and right side of middle sensor should all see white

When the middle sensor sees black and all others see white:

    def goForward():
        All motors on at same velocity

When sensor(s) to left of middle sensor see black:

    def turnLeft():
        Motors on right side of robot will continue moving forward
        Motors on left side of robot will go slower than right side motors
        Keep turning until middle sensor once again sees black

When sensor(s) to right of middle sensor see black:

    def turnRight():
        Motors on left side of robot will continue moving forward
        Motors on right side of robot will go slower than left side motors
        Keep turning until middle sensor once again sees black


"""


def calcVelocities(IDs, sensorVals):  #  sensorVals = list of all seven sensor values
    print("In calcVelocities()")
    print("Sensor Vals: \n", sensorVals)
    velocities = []
    for element in IDs:
        velocity = input(f"Input your velocity for motor with ID #{element}: ")
        velocities.append(int(velocity))
        
    if sensorVals[3] == 0:  # sensor vals is black
        return goForward(sensorVals)
    
    elif sensorVals[2] == 0:  # if left side sensor reads black
        return leftTurn()

    elif sensorVals[4] == 0:  # if right side sensor reads black
        return rightTurn()
    
    def goForward(sensorVals):
        return [265, 265, 265, 265]
    
    def leftTurn():
        return [100, 100, 265, 265]

    def rightTurn():
        return [265, 265, 100, 100]
    
    def pointTurn(sensorVals):
        #  write function to calculate motor speeds for point turn based on sensor values
        return ["Motor speed one", "motor speed two", "motor speed three", "motor speed four"]


    def cornerTurn(sensorVals):
        #  write function to calculate motor speeds for corner turn based on sensor values
        return ["Motor speed one", "motor speed two", "motor speed three", "motor speed four"]


    def wideTurn(sensorVals):
        #  write function to calculate motor speeds for wide turn based on sensor values
        return ["Motor speed one", "motor speed two", "motor speed three", "motor speed four"]

    return velocities

