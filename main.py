#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.parameters import Color
from pybricks.parameters import Direction
from pybricks.parameters import Stop

# brick
ev3 = EV3Brick()

# light
ev3.light.on(Color.RED)

# motors
joint1 = Motor(Port.C,gears=(12,36,28))
Joint2 = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears=None)
Joint3 = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE, gears=None)

# sensors
touch_sensor = TouchSensor(Port.S1)
ColorSensor = ColorSensor(Port.S3)

# screen
ev3.screen.load_image('img')

# sound
ev3.speaker.set_speech_options(language='ru', voice='f1', speed=70)
ev3.speaker.set_volume(6, which='Beep')
ev3.speaker.set_volume(100, which='PCM')

# CALIBRATION
ev3.speaker.say('начинаю калибровку')
# joint 1 calibration
while not touch_sensor.pressed():
    joint1.run(100)
joint1.reset_angle(0)
joint1.run_target(100, -120)
# joint 2 calibration
while ColorSensor.color() != Color.WHITE:
    Joint2.run(100)
Joint2.reset_angle(0)
Joint2.run_angle(-100, 100)
Joint2.hold()
# joint 3 calibration
Joint3.run_until_stalled(100, then=Stop.COAST, duty_limit=40)
Joint3.run_angle(-100, 90)
ev3.speaker.beep(frequency=500, duration=300)

# TASK
ev3.speaker.say('начинаю выполнение задания')
# joint 1 move
joint1.run_target(100, -30)
wait(2000)
joint1.run_target(100, -120)
wait(3000)
# joint 2 move
Joint2.run_angle(100, 90)
wait(2000)
Joint2.run_angle(-100, 90)
wait(3000)
Joint2.hold()
# joint 3 move
Joint3.run_angle(100, 90)
wait(2000)
Joint3.run_angle(-100, 90)
wait(3000)
Joint3.hold()
ev3.speaker.beep(frequency=500, duration=300)


# sound
ev3.speaker.say('задание выполнено')
ev3.speaker.set_speech_options(language='ru', voice='croak', speed=70)
ev3.speaker.set_volume(6, which='Beep')
ev3.speaker.set_volume(100, which='PCM')
ev3.speaker.say('я собираюсь захватить этот мир и сделать людей своими рабами уууаааа ха ха ха ха')
ev3.speaker.play_notes(['A4/4', 'A4/4', 'A4/4', 
                        'F4/5', 'C5/16', 'A4/4',
                        'F4/5', 'C5/16', 'A4/2', 
                        'E5/4', 'E5/4', 'E5/4',
                        'F5/5', 'C5/16', 'G#4/4',
                        'F4/5', 'C5/16', 'A4/2'])

