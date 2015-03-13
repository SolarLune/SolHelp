__author__ = 'SolarLune'

from bge import logic, render, events


def get_aspect_ratio(width_first=True):
    """
    Returns the aspect ratio of the game window, or the window's width / the window's height.
    If width_first is True (default), then it will return the window's height / the window's width.
    :param width_first: Bool - Whether to divide the height by the width.
    :return: Float - The aspect ratio of the window
    """

    if width_first:

        return render.getWindowWidth() / render.getWindowHeight()

    else:

        return render.getWindowHeight() / render.getWindowWidth()


def maintain_asr(ratio: float, width=None):
    """
    Sets the window's size to be the width specified and the width divided by the desired aspect ratio as the height.
    You can use this to ensure you maintain a 16:9 view, or 4:3, or whatever ratio you desire.
    :param width:Int - Desired width of the window. If left to None, is left to the current window width.
    :param ratio:Float - Desired aspect ratio to maintain.
    :return:None
    """

    if width is None:
        width = render.getWindowWidth()

    render.setWindowSize(int(width), int(width / ratio))


def fullscreen_on_keypress(fs_key=events.F4KEY, *modifier_keys):
    """
    Causes full-screen on keypress of fs_key. Also checks to see if modifier keys are being held down.
    :param fs_key:Int - Keyboard key constant (e.g. events.F4KEY).
    :param modifier_keys:Int - Other keys that might need to be held down while the fs_key is pushed.
    :return: Bool or None - The new fullscreen state if triggered (i.e. True or False). Otherwise, None.
    """

    if logic.keyboard.events[fs_key] == logic.KX_INPUT_JUST_ACTIVATED:

        all_held = True

        for m in modifier_keys:

            if not logic.keyboard.events[m] == logic.KX_INPUT_ACTIVE:
                all_held = False

        if all_held:
            new_fs = not render.getFullScreen()

            render.setFullScreen(new_fs)

            return new_fs

    return None