#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import logging
import ev3bluetooth

from random import randint

from common.robot import Robot

# default sleep timeout in sec
DEFAULT_SLEEP_TIMEOUT_IN_SEC = 0.1

# default speed
DEFAULT_SPEED = 200

# default threshold distance
DEFAULT_THRESHOLD_DISTANCE = 150

# config logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def main():

    logging.debug('Run robot, run!')
    robot = Robot()
    ev3bluetooth = BluetoothConnect()
    robot.set_speed(DEFAULT_SPEED)
    robot.forward()
    
    try:
        while True:
            message = ev3bluetooth.message()
            if message == "left"
                robot.turn(45)
                time.sleep(2)
            if message == "right"
                robot.forward(-45)
                time.sleep(2)

            if message == "forward"
                robot.forward(-45)
                time.sleep(5)

            if message == "backward"
                robot.forward(-45)
                time.sleep(5)

    # doing a cleanup action just before program ends
    # handle ctr+c and system exit
    except (KeyboardInterrupt, SystemExit) as e:
        logging.exception("message")

    # handle exceptions
    except Exception as e:
        logging.exception("message")

    finally:
        teardown(robot)
        logging.shutdown()


def teardown(robot):
    robot.brake()

if __name__ == "__main__":
    main()