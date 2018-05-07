#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <coopa_morse1> environment

Feel free to edit this template as you like!
"""

from morse.builder import *

# Add the MORSE mascott, MORSY.
# Out-the-box available robots are listed here:
# http://www.openrobots.org/morse/doc/stable/components_library.html
#
# 'morse add robot <name> coopa_morse1' can help you to build custom robots.
robot_alpha = Morsy() #Pioneer3DX()
robot_bravo = Morsy() #Pioneer3DX()
robot_charlie = Morsy() #Pioneer3DX()

# The list of the main methods to manipulate your components
# is here: http://www.openrobots.org/morse/doc/stable/user/builder_overview.html
robot_alpha.translate(1.0, 0.0, 0.0)
robot_alpha.rotate(0.0, 0.0, 3.5)

robot_bravo.translate(1.0, 5.0, 0.0)
robot_bravo.rotate(0.0, 0.0, 3.5)

robot_charlie.translate(1.0, 8.0, 0.0)
robot_charlie.rotate(0.0, 0.0, 3.5)

# Add a motion controller
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
#
# 'morse add actuator <name> coopa_morse1' can help you with the creation of a custom
# actuator.
motion_alpha = MotionVW()
motion_alpha.translate(z=0.3)
robot_alpha.append(motion_alpha)

# create and add a Collision sensor
collision_alpha = Collision()

# place it on the front side of the robot
collision_alpha.translate(0.43,0,0.3)

# only detect collision with objects which have the property 'Object'.
# see the documentation of `Passive Objects` for details:
# http://www.openrobots.org/morse/doc/latest/user/others/passive_objects.html
#collision_alpha.properties(only_objects_with_property="Object")

robot_alpha.append(collision_alpha)
# for this example, we use the socket interface
collision_alpha.add_interface("socket")


#--------- bravo
motion_bravo = MotionVW()
motion_bravo.translate(z=0.3)
robot_bravo.append(motion_bravo)

# create and add a Collision sensor
collision_bravo = Collision()

# place it on the front side of the robot
collision_bravo.translate(0.43,0,0.3)

# only detect collision with objects which have the property 'Object'.
# see the documentation of `Passive Objects` for details:
# http://www.openrobots.org/morse/doc/latest/user/others/passive_objects.html
# collision_bravo.properties(only_objects_with_property="Object")

robot_bravo.append(collision_bravo)
# for this example, we use the socket interface
collision_bravo.add_interface("socket")


#--------- Charlie

motion_charlie = MotionVW()
motion_charlie.translate(z=0.3)
robot_charlie.append(motion_charlie)
# create and add a Collision sensor
collision_charlie = Collision()

# place it on the front side of the robot
collision_charlie.translate(0.43,0,0.3)

# only detect collision with objects which have the property 'Object'.
# see the documentation of `Passive Objects` for details:
# http://www.openrobots.org/morse/doc/latest/user/others/passive_objects.html
# collision_bravo.properties(only_objects_with_property="Object")

robot_charlie.append(collision_charlie)
# for this example, we use the socket interface
collision_charlie.add_interface("socket")

#--------------


# Add a keyboard controller to move the robot with arrow keys.
keyboard = Keyboard()
robot_alpha.append(keyboard)
keyboard.properties(ControlType = 'Position')

# Add a pose sensor that exports the current location and orientation
# of the robot in the world frame
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#sensors
#
# 'morse add sensor <name> coopa_morse1' can help you with the creation of a custom
# sensor.
pose = Pose()
robot_alpha.append(pose)

# To ease development and debugging, we add a socket interface to our robot.
#
# Check here: http://www.openrobots.org/morse/doc/stable/user/integration.html
# the other available interfaces (like ROS, YARP...)
robot_alpha.add_default_interface('socket')
robot_bravo.add_default_interface('socket')
robot_charlie.add_default_interface('socket')

pose.add_stream('socket')
pose.add_service('socket')

motion_alpha.add_service('socket')
motion_bravo.add_service('socket')
motion_charlie.add_service('socket')


# set 'fastmode' to True to switch to wireframe mode
#env = Environment('sandbox', fastmode = False)
#env = Environment('indoors-1/indoor-1', fastmode = False)
#env.set_camera_location([-18.0, -6.7, 10.8])
#env.set_camera_rotation([1.09, 0, -1.14])

env = Environment('/Users/hadaytul/Documents/PostDoc_UoH/source/morse/data/environments/indoors-1/boxes-2', fastmode = False)
env.set_camera_location([-7.0, 2.5, 20.8])
env.set_camera_rotation([0, 0, -3.14])

