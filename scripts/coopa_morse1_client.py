#! /usr/bin/env python3
"""
Test client for the <coopa_morse1> simulation environment.

This simple program shows how to control a robot from Python.

For real applications, you may want to rely on a full middleware,
like ROS (www.ros.org).
"""

import sys
from time import sleep

try:
    from pymorse import Morse
except ImportError:
    print("you need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)

print("Use WASD to control the robot")

robot_alpha = None
robot_bravo = None
robot_charlie = None

def collision_action(motion):
  #back track, turn and go forward again
  motion.publish({"v": -2, "w": 1})
  sleep(0.5)
  motion.publish({"v": 2, "w": 0})


def collision_callback_alpha(data):
  if data["collision"]:
    collision_action(robot_alpha.motion_alpha)

def collision_callback_charlie(data):
  if data["collision"]:
    collision_action(robot_charlie.motion_charlie)

def collision_callback_bravo(data):
  if data["collision"]:
    collision_action(robot_bravo.motion_bravo)


with Morse() as simu:

  robot_alpha = simu.robot_alpha
  robot_bravo = simu.robot_bravo
  robot_charlie = simu.robot_charlie

  motion_alpha = simu.robot_alpha.motion_alpha
  motion_bravo = simu.robot_bravo.motion_bravo
  motion_charlie = simu.robot_charlie.motion_charlie

  motion_alpha.publish({"v": 2, "w": 0})
  motion_bravo.publish({"v": 2, "w": 0})
  motion_charlie.publish({"v": 2, "w": 0})

  simu.robot_alpha.collision_alpha.subscribe(collision_callback_alpha)
  simu.robot_bravo.collision_bravo.subscribe(collision_callback_bravo)
  simu.robot_charlie.collision_charlie.subscribe(collision_callback_charlie)

  print("Press ctrl+C to stop")
  while True:
    sleep(2)

#  pose = simu.robot_alpha.pose
#
#  v = 0.0
#  w = 0.0
#
#  while True:
#      key = input("WASD?")
#
#      if key.lower() == "w":
#          v += 0.1
#      elif key.lower() == "s":
#          v -= 0.1
#      elif key.lower() == "a":
#          w += 0.1
#      elif key.lower() == "d":
#          w -= 0.1
#      else:
#          continue
#
#      # here, we call 'get' on the pose sensor: this is a blocking
#      # call. Check pymorse documentation for alternatives, including
#      # asynchronous stream subscription.
#      print("The robot is currently at: %s" % pose.get())
#
#      motion_alpha.publish({"v": v, "w": w})
