#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
ev3.speaker.beep()
touch_sensor = TouchSensor(Port.S1)
joint1 = Motor(Port.C)

ev3.speaker.beep()

while not touch_sensor.pressed():
    joint1.run(200)

joint1.reset_angle(0)
ev3.speaker.beep()
