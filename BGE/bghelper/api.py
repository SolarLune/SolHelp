__author__ = 'SolarLune'

import sys

from bge import logic


class Scenes:
    def __str__(self):
        return str(logic.getSceneList())

    def __len__(self):
        return len(logic.getSceneList())

    def __iter__(self):
        return iter(logic.getSceneList())

    def __contains__(self, key):
        if isinstance(key, str):
            return True if key in {s.name for s in logic.getSceneList()} else False
        raise TypeError('must be str, not ' + type(key).__name__)

    def __getitem__(self, key):
        scenes = logic.getSceneList()
        if isinstance(key, str):
            return {s.name: s for s in scenes}[key]
        return scenes[key]

    def set(self, key):
        logic.getCurrentScene().replace(key)

    def add(self, key, overlay=True):
        logic.addScene(key, overlay)

    def __del__(self):
        del self

    def remove(self, key):
        self.__getitem__(key).end()

    def leave(self, *args):

        """
        Ends all scenes except the ones you specify.
        arguments = the names of the scenes you want to leave
        """
        for scene in logic.getSceneList():
            if not scene.name in args:
                scene.end()


scenes = Scenes()


class Callback(object):
    """
    A callback class for making callback objects. These objects are useful for telling when a value changes - for example, you
    could use a callback to tell when the Player collides with an object other than the one he is currently colliding with (None, if
    he isn't colliding with anything). You can use a callback object to execute a function when the callback returns - in the above
    example, you could create an object or particle when this callback returns positive.
    """

    def __init__(self):

        self.calls = dict({})
        self.idindex = 0

    def add(self, check, onchange, cb_name=None, defaultvalue=1, mode=0):

        """
        Add a callback to the list for this Callback object to take care of.

        check = Checking function for the callback (e.g. a function that returns obj.position.x < 10), like:

        lambda : obj.getDistanceTo(sce.objects['Dest']) < 5

        onchange = Returning function for the callback (e.g. a function that does: obj.endObject();
        this would run when obj.position.x < 10, but only the one frame that this is true (default))

        cb_name = Name / ID for the callback; Not necessary, but is used to refer to the callback later. Can be a number, string, etc.

        defaultvalue = What the default value is; when the callback is first added, if defaultvalue = 0,
        then the previous value recorded for the callback will be None. Unless the checking function returns None, then the returning function will run.

        mode = (0 by default); what mode the callback is; 0 == changed, 1 == equals,
        2 == greater than, 3 == less than; try to keep this set to 0.

        This function also returns the original callback ID, so you can get it later if you need to.
        """

        if defaultvalue == 0:
            callback = [check, onchange, mode, None]
        else:
            callback = [check, onchange, mode, check()]

        if cb_name is None:  # If you don't specify an ID, then it will return an internal ID counter
            cb_name = self.idindex
            self.idindex += 1

        self.calls[cb_name] = callback  # A list of all calls for this callback object - the checking function,
        # the function to return if the callback is true, the mode, as well as the previous value (used by the Change
        # mode, which is default)

        return cb_name  # Returns the ID number if you want to keep track of it and access the Callback
        # object's callbacks through object.calls[id]

    def remove(self, cb_name=None):

        """
        Removes the callback with the specified ID from the list of callback functions for this object.
        """

        if cb_name is None:
            self.calls.popitem()
        else:
            del self.calls[cb_name]

    def remove_all(self):

        self.calls.clear()

    def get(self, cb_name):

        return self.calls[cb_name]

    def update(self):
        """
        Update the callbacks, and run their associated functions if they change, or for whatever mode each callback is in.
        """

        for c in self.calls:

            call = self.calls[c]

            value = call[0]()

            mode = call[2]

            if call[3] != value and mode == 0:  # Changed (not equal)
                call[1](call[3])
                call[3] = value
            elif call[3] == value and mode == 1:  # Equals (experimental; stick with mode 0)
                call[1](call[3])
                call[3] = value
            elif call[3] > value and mode == 2:  # Greater than (experimental; stick with mode 0)
                call[1](call[3])
                call[3] = value
            elif call[3] < value and mode == 3:  # Less than (experimental; stick with mode 0)
                call[1](call[3])
                call[3] = value


callbacks = Callback()


def end_game_on_exception():
    """
    Ends the game if an exception is raised.
    :return: None
    """

    exc = sys.exc_info()

    if exc[0]:  # An exception has been raised; end the game

        # if not allow_missing_functions and not "'module' object has no attribute" in str(sys.last_value):
        # It's an actual error, not just an object's function that hasn't been implemented

        logic.endGame()


def mutate(intended_class, obj=None):

    """
    Mutates the object into an instance of the intended class.
    :param intended_class: class - The kind of class you want the object to override and become one of.
    :param obj: KX_GameObject - The object to mutate. If not specified or left to None,
    then it will use the calling object.
    :return: intended_class
    """

    if obj is None:

        obj = logic.getCurrentController().owner

    if isinstance(obj, intended_class):

        return obj

    else:

        return intended_class(obj)