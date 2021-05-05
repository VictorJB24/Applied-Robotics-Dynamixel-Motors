from dynamixel_sdk import *  # Uses Dynamixel SDK library
import os


def calcVelocities(IDs):
    print("In calcVelocities()")
    velocities = []
    for element in IDs:
        velocity = input(f"Input your velocity for motor with ID #{element}: ")
        velocities.append(int(velocity))
    return velocities

def pointTurn(sensorVals):
    #  write function to calculate motor speeds for point turn based on sensor values
    return ["Motor speed one", "motor speed two", "motor speed three", "motor speed four"]


def pointTurn(sensorVals):
    #  write function to calculate motor speeds for corner turn based on sensor values
    return ["Motor speed one", "motor speed two", "motor speed three", "motor speed four"]


def pointTurn(sensorVals):
    #  write function to calculate motor speeds for wide turn based on sensor values
    return ["Motor speed one", "motor speed two", "motor speed three", "motor speed four"]
