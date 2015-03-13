__author__ = 'SolarLune'

import math

from bge import logic

# input constants

KEY = 0  # Different input types; Keyboard key
JOYBUTTON = 1  # Joystick button
JOYHAT = 2  # Joystick hat (D-Pad on a lot of controllers)
JOYAXIS = 3  # Joystick axes (sticks and triggers on a 360 controller)
MOUSEAXIS = 4  # Mouse movement axes
MOUSEBUTTON = 5  # Mouse button

STATE_UP = 0
STATE_PRESSED = 1
STATE_DOWN = 2
STATE_RELEASED = 3

# Joystick profiles. They are objects of classes, rather than dictionaries. This was done so that
# it would be easier to work with when you're dealing with IDEs that can do code intelligence like Komodo Edit
# Note that they start with JP, but these are US controllers, not Japanese ones, haha


class _JP_GameCubeUSB():
    """
    Joystick profile for a GameCube controller connected via a USB adapter.
    Interestingly, the D-Pad can be detected as either buttons (the "Pad" ones below), or a standard Hat hat
    like most other joysticks (the Hat variables).

    The triggers are individual axes, unlike the 360's (which show up as a single axis).
    """

    A = 1
    B = 2
    X = 0
    Y = 3

    L = 4
    R = 5
    Z = 7

    Start = 9

    Pad_Up = 12  # D-pad registers as buttons and a hat, for some reason
    Pad_Right = 13
    Pad_Down = 14
    Pad_Left = 15

    Hat_Up = 1
    Hat_Right = 2
    Hat_Down = 4
    Hat_Left = 8
    Hat_None = 0

    Stick_LeftHori = 0
    Stick_LeftVert = 1
    Stick_RightHori = 2
    Stick_RightVert = 3
    Trigger_Right = 4
    Trigger_Left = 5


JPGamecubeUSB = _JP_GameCubeUSB()


class _JP_PS2USB():
    """
    Joystick profile for a PS2 controller connected via a USB adapter.
    """

    Triangle = 0
    Circle = 1
    Cross = 2
    Square = 3

    L2 = 4
    R2 = 5
    L1 = 6
    R1 = 7
    Select = 8
    Start = 9
    L3 = 10
    R3 = 11

    Hat_Up = 1
    Hat_Right = 2
    Hat_Down = 4
    Hat_Left = 8
    Hat_None = 0

    Stick_LeftHori = 0
    Stick_LeftVert = 1
    Stick_RightHori = 3
    Stick_RightVert = 2


JPPS2USB = _JP_PS2USB


class _JP_Chillstream():
    """
    Joystick profile for a Logitech Chillstream controller.
    """

    Triangle = 3
    Circle = 2
    Cross = 1
    Square = 0

    L2 = 6
    R2 = 7
    L1 = 4
    R1 = 5
    Select = 8
    Start = 9
    L3 = 10
    R3 = 11

    Hat_Up = 1
    Hat_Right = 2
    Hat_Down = 4
    Hat_Left = 8
    Hat_None = 0

    Stick_LeftHori = 0
    Stick_LeftVert = 1
    Stick_RightHori = 2
    Stick_RightVert = 3


JPChillstream = _JP_Chillstream


class _JP_Xbox360():
    """
    Joystick profile for an XBOX 360 or otherwise X-input controller.

    Note that the triggers are implemented as a single axis; the controls don't seem to add up correctly (i.e.
    LT = axis 5 < 0, RT = axis 5 > 0; added together, they approach 0...). There's no alternative way to tell
    which axis is being pressed, either. :1

    Note that this should be the profile used for X-input controllers, even if they aren't XBOX 360 controllers,
    like the Logitech F310.
    """

    A = 0
    B = 1
    X = 2
    Y = 3
    LB = 4
    RB = 5
    Back = 6
    Start = 7
    LS = 8
    RS = 9

    Hat_Up = 1
    Hat_Right = 2
    Hat_Down = 4
    Hat_Left = 8
    Hat_None = 0

    Stick_LeftHori = 0
    Stick_LeftVert = 1
    Stick_RightHori = 4
    Stick_RightVert = 3

    Triggers = 2


JPXbox360 = _JP_Xbox360()


# input classes

class InputKey():
    """
    Tests for input from keyboard and joystick.
    """

    def __init__(self, inputtype, keycode, axisdirection=1, deadzone=0.1, joyindex=0, scalar=1.0):

        """
        A input handling object.

        inputtype = input type from CinputKey (CinputKey.KEYDOWN, for example)
        keycode = key, axis, hat, or button code for the input device (for example, events.XKEY, 5 for the fifth button
        on a joystick, etc.)
        axisdirection = direction to check for axis values for joystick and mouse axis checks.
        deadzone = percentage to disregard joystick movement.
        joyindex = joystick index to check.
        scalar = how large the end number is. Defaults to 1.0. This is useful to make corresponding inputs match up
        (i.e. make the mouse move at the same rate as the right analog stick).
        """

        self.inputtype = inputtype
        self.keycode = keycode

        self.prevstate = 0
        self.prevpos = [0.0, 0.0]  # Previous position of the mouse
        self.active = 0.0
        self.state = STATE_UP  # The state of the key input (just pressed, released, down, up, etc.)

        self.scalar = scalar
        self.axisdirection = axisdirection  # Default for axis checking
        self.deadzone = deadzone  # Deadzone amount for axis checking
        self.joyindex = joyindex  # Defaults to the first one

    def poll(self):

        """
        Polls the input to check whether it's active or not.
        """

        joy = logic.joysticks[self.joyindex]

        if self.inputtype == KEY:

            if logic.keyboard.events[self.keycode] == logic.KX_INPUT_ACTIVE:

                self.active = self.scalar

            else:

                self.active = 0.0

        elif self.inputtype == MOUSEAXIS:

            av = logic.mouse.position[self.keycode] - self.prevpos[self.keycode]

            self.state = STATE_DOWN

            if math.copysign(1, av) == self.axisdirection and abs(av) > self.deadzone:

                self.active = abs(av) * self.scalar

            else:

                self.active = 0.0

            self.prevpos = [0.5, 0.5]

        elif self.inputtype == MOUSEBUTTON:

            if logic.mouse.events[self.keycode] == logic.KX_INPUT_ACTIVE:

                self.active = self.scalar

            else:

                self.active = 0.0

        elif joy is not None and joy.numAxis and joy.numButtons and joy.numHats:

            if self.inputtype == JOYBUTTON:

                if self.keycode in joy.activeButtons:

                    self.active = self.scalar

                else:

                    self.active = 0.0

            elif self.inputtype == JOYHAT:

                hat = joy.hatValues[0]  # TODO: Expand this to fit more than one hat

                if hat & self.keycode:

                    self.active = self.scalar

                else:

                    self.active = 0.0

            elif self.inputtype == JOYAXIS:

                av = joy.axisValues[self.keycode]

                pressed = abs(av) > self.deadzone and math.copysign(1, av) == self.axisdirection

                if pressed:

                    self.active = abs(av) * self.scalar

                else:

                    self.active = 0.0

        if self.active and not self.prevstate:

            self.state = STATE_PRESSED

        elif self.active and self.prevstate:

            self.state = STATE_DOWN

        elif not self.active and self.prevstate:

            self.state = STATE_RELEASED

        else:

            self.state = STATE_UP

        self.prevstate = self.active


class InputDevice():
    """
    A class for testing for input from different devices. Useful if you want to easily set up different bindings
    for your input.

    Basically, you add the inputs via their inputtype (retrieved from CinputKey's input type constant definitions)
    with the keycode that you need.

    You can also specify a group for each binding entry (i.e. you can add keyboard and joystick controls separately.)

    Then, you poll the device with the group that you specify (so you can easily switch between key setups, and so it
    won't matter which device you use).

    Finally, you can easily retrieve the key / button / axis being pressed by just checking the device's events
    dictionary:

    -------------

    device = InputDevice()

    device.add('jump', KEY, events.ZKEY, 'keyboard')

    device.poll('keyboard')

    print (device.bind_down('jump'))

    -------------

    Note that you can also not specify a group if you want all input devices to work at the same time
    (i.e. use the joystick or the keyboard at the same time.)

    """

    def __init__(self):

        """
        Example code usage:

        device = InputDevice()

        device.Add('jump', BGinput.KEYPRESSED, events.ZKEY, 'keyboard')

        device.Poll('keyboard')

        print (device.bindings['jump'])

        """

        self.events = {}
        self.bindings = {}
        self.states = {}  # The states of individual bindings (seemed easier than having to use bindings['active'] and bindings['state'])

    def add(self, bindingname, inputtype, keycode, axisdir=1, deadzone=0.1, joyindex=0, scalar=1.0, group="default"):

        """
        Add a key binding.

        bindingname = name of the binding to create (i.e. 'left', 'jump', 'run', 'interact'...)
        inputtype = input type from CinputKey (CinputKey.KEYDOWN, for example)
        keycode = key, axis, hat, or button code for the input device (for example, events.XKEY, 5 for the fifth button on a joystick, etc.)

        group = a string that designates what group to add this binding to. For example, you might add all of the joystick
        bindings to a 'joystick' group, and all of the keyboard bindings to a 'keyboard' group

        axisdir = direction to check for axis values for joystick and mouse axis checks.
        deadzone = Fraction to disregard joystick movement.
        joyindex = joystick index to check.
        scalar = how large the end number is. Defaults to 1.0. This is useful to make corresponding inputs match up (i.e. make
        the mouse move at the same rate as the right analog stick).

        """

        if not group in self.events:
            self.events[group] = {}

        if not bindingname in self.events[group]:
            # if not group in self.events:        # Set up the events dictionary

            # self.events[group] = {}

            self.events[group][bindingname] = []

            self.bindings[bindingname] = {'active': 0.0, 'type': KEY, 'state': 0}

        self.events[group][bindingname].append(InputKey(inputtype, keycode, axisdir, deadzone, joyindex, scalar))

    def poll(self, group=None):

        """
        Poll the bindings for updates.

        group = which set of bindings to poll in particular. If left to None, then it will poll all groups specified.
        If you specify, then it will poll that one in particular. Useful for switching input schemes.
        """

        if group is None:

            poll_groups = [gr for gr in self.events]

        else:

            poll_groups = [group]

        for group in poll_groups:

            for binding in self.events[group]:

                self.bindings[binding] = {'active': 0.0, 'type': None, 'state': 0}

                for input_o in self.events[group][binding]:

                    input_o.poll()

                    if input_o.active:

                        self.bindings[binding] = {'active': input_o.active, 'state': input_o.state,
                                                  'type': input_o.inputtype}

                    else:

                        if input_o.state == STATE_RELEASED:
                            self.bindings[binding]['state'] = input_o.state

    def type_active(self, input_type):

        """
        Checks to see if a certain kind of input type is active.
        """

        for b in self.bindings:

            if self.bindings[b]['type'] == input_type and self.bindings[b]['active']:
                return 1

        return 0

    def bind_down(self, bind):
        """
        Checks to see if the binding you specify is activated currently (down).

        bind = binding name
        """

        return self.bindings[bind]['active'] if self.bindings[bind]['state'] == STATE_DOWN else 0.0

    def bind_pressed(self, bind):
        """
        Checks to see if the binding you specify was just pressed this frame.

        bind = binding name
        """
        return self.bindings[bind]['active'] if self.bindings[bind]['state'] == STATE_PRESSED else 0.0

    def bind_released(self, bind):
        """
        Checks to see if the binding you specify was just released this frame. If it was, 1 is returned.

        bind = binding name
        """
        return 1.0 if self.bindings[bind]['state'] == STATE_RELEASED else 0.0

device = InputDevice()
