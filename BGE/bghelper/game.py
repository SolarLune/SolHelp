__author__ = 'SolarLune'

from bge import logic

import mathutils

from . import window


ML_LOCK_NONE = 0  # Constants for mouse-look axis locking
ML_LOCK_X = 1
ML_LOCK_Y = 2


# TODO: Add axis setting to allow for joystick analog controlled mouse-look

def mouse_look(obj=None, accel_speed=1.0, max_speed=45.0, friction=8.0, lock=ML_LOCK_NONE):

    if not obj:

        obj = logic.getCurrentController().owner

    if not 'mouse_look_info' in obj:

        obj['mouse_look_info'] = {

            'rot_x': 0.0,
            'speed': mathutils.Vector([0, 0]),
        }

    else:

        mouse_position = logic.mouse.position

        delta_x = 0.5 - mouse_position[0]
        delta_y = 0.5 - mouse_position[1]

        margin = 0.002

        if abs(delta_x) < margin:
            delta_x = 0.0
        if abs(delta_y) < margin:
            delta_y = 0.0

        divisor = .0025

        info = obj['mouse_look_info']
        speed = info['speed']

        if not lock & ML_LOCK_X:
            speed.x += delta_x * (accel_speed + friction * divisor)

        if not lock & ML_LOCK_Y:
            speed.y += (delta_y * (accel_speed + friction * divisor)) / window.get_aspect_ratio()

        speed.magnitude = min(speed.magnitude, max_speed * divisor)

        obj.applyRotation([0, 0, speed.x], 0)
        obj.applyRotation([speed.y, 0, 0], 1)

        if speed.magnitude > friction * divisor:
            speed.magnitude -= friction * divisor
        else:
            speed.magnitude = 0.0

        logic.mouse.position = .5, .5

