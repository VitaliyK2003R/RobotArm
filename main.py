#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Color, Direction, Stop
from pybricks.tools import wait

# objects
ev3 = EV3Brick()
motor_low =    Motor(Port.C, gears=[12, 36])
motor_medium = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears=[8, 40])
motor_top =    Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE, gears=[8, 12])
touch_sensor = TouchSensor(Port.S1)
color_sensor = ColorSensor(Port.S3)

# hubs
ev3.screen.load_image('img')
ev3.speaker.set_speech_options(language='ru', voice='m3', speed=70)
ev3.speaker.set_volume(6, which='Beep')
ev3.speaker.set_volume(100, which='PCM')

# for smooth motion
motor_low.control.limits(speed=100, acceleration=120)
motor_medium.control.limits(speed=100, acceleration=120)
motor_top.control.limits(speed=100, acceleration=120)

# CALIBRATION
ev3.light.on(Color.RED)
ev3.speaker.say('начинаю калибровку')

# low motor calibration
while not touch_sensor.pressed():
    motor_low.run(100)
motor_low.reset_angle(0)
motor_low.run_target(100, -120)
motor_low.hold()
# medium motor calibration
while color_sensor.color() != Color.WHITE:
    motor_medium.run(100)
motor_medium.reset_angle(0)
motor_medium.run_target(100, -40)
motor_medium.hold()
# top motor calibration
motor_top.run_until_stalled(100, then=Stop.HOLD, duty_limit=40)
motor_top.reset_angle(0)
motor_top.run_target(100, -70)
motor_top.hold()

# calibration is complete
for i in range(3):
    ev3.speaker.beep()
    wait(100)

# TASK
ev3.light.on(Color.GREEN)
ev3.speaker.say('начинаю выполнение задания')

# low motor move
motor_low.run_target(100, -30)
wait(2000)
motor_low.run_target(100, -120)
wait(3000)
motor_low.hold()
# medium motor move
motor_medium.run_target(100, 10)
wait(2000)
motor_medium.run_target(100, -40)
wait(3000)
motor_medium.hold()
# top motor move
motor_top.run_target(100, 0)
wait(2000)
motor_top.run_target(100, -70)
wait(3000)
motor_top.hold()

# task is complete
for i in range(3):
    ev3.speaker.beep()
    wait(100)
ev3.speaker.say('задание выполнено')
