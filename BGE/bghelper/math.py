__author__ = 'SolarLune'

import mathutils

from bge import logic, render


def lerp(a, b, scalar):
    """Lerp - Linearly interpolates between 'a'
    when 'scalar' is 0 and 'b' when 'scalar' is 1.
    a = number or Vector
    b = number or Vector
    scaler = number between 0 and 1
    """
    return (a + scalar * (b - a))


def clamp(value, minimum, maximum):
    """
    Clamp: Clamps the specified 'value' between the maximum and minimum values.
    Returns 'max' when 'value' is greater than 'max', 'min' when 'value' is less than 'min',
    and 'value' itself when neither is true.
    """
    return (min(max(value, minimum), maximum))


def wrap(value, minimum, maximum, preserve_remainder=True):

    if value < minimum:

        value = maximum

        if preserve_remainder:

            value -= abs(value - minimum)

    elif value > maximum:

        value = minimum

        if preserve_remainder:

            value += abs(value - maximum)

    return value


def sign(value):
    """
    Returns the sign of the inputted 'value'; i.e. 5 = 1, -9.1 = -1, 0 = 0
    """
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0


def sort_closest_gameobjects(first, others):

    l = others[:]

    l.sort(key=lambda x: first.getDistanceTo(x))

    return l


def sort_closest_vectors(first, others):

    l = others[:]

    l.sort(key=lambda x: (first - x).magnitude)

    return l


def raycast_line(anglevect, anglewidth, topos, frompos=None, raynum=3,
                center=1, from_scalar=1.0, to_scalar=1.0, dist=0, prop='', face=1, xray=1,
                poly=0, obj=None, debug=False, objdebug=None):
    """
    Casts several rays in a line, starting from frompos and going to topos, and then iterating along the line indicated by anglevect.

    The function returns a dictionary, consisting of four items:

    'rays': The return of the raycasts (either a hit, or an empty list, depending on what the rays hit; the output from a raycast() function, basically)
    'ray_end': The ending position of the last successful raycast, or None if there wasn't a successful raycast
    'ray_start' The starting position of the last successful raycast, or None if there wasn't a successful raycast
    'offset' The offset between the starting point of the successful ray cast and the provided starting ray cast position. Useful in case
    you want to reorient the position of an object from the ray cast (i.e. move to contact point), but still want to use the object's
    center position (don't move to where the ray hit, but move to where it hit relative to the object's center position).

    anglevect = The angle that the rays should be cast on.

    anglewidth = How wide the rays should be cast in Blender Units (i.e. a value of 1 means that from the left-most ray to the right-most ray is 1 BU).

    raynum = number of rays to cast

    center = if the rays should be centered on the anglevect Vector or not
    (i.e. treat frompos and topos as the center ray, or as the ray starting from anglevect)

    from / to_scalar = A percentage of the width to stretch (i.e. to have a wider end "edge" than starting "edge")

    dist = distance of each raycast; defaults to 0, which equals the distance between the from position and end position of the vectors

    prop = property to check for with each raycast; defaults = '', which detects any object

    face = whether to return a face if the ray hits something

    xray = whether to go through objects that don't match the property criteria (objects that don't have the property
    named by 'prop')

    poly = whether to return the polygon / UV hit; check the api documentation for more information

    obj = object to use for the ray casts; if left set to default (None), then it will use whatever object is calling
    the function.

    objdebug = default None; an object to use for debugging

    -----

    Okay, so now what is this actually used for? Mainly, to do kind of a 'ray cast wall'. An example would be if you
    want to cast multiple rays for a character in a platforming game. You would do this instead of using the built-in Bullet
    physics engine to handle gravity and collisions so that you could have partially impassable objects, for example.

    An example of using this function would look something like this:

    width = 0.6

    frompos = obj.worldPosition.copy()
    topos = frompos.copy()
    topos.z -= 1

    dist = 0.5 + abs(obj.worldLinearVelocity.z)

    ground = bghelper.RaycastLine(obj.worldOrientation.col[0], width, topos, frompos, 3, 1, dist, 'ground', debug = 1)[0]

    This will cast three rays in a straight line, with the center one being below the object's world position. Debug is on,
    so it will draw the lines visibly onscreen (barring a bug with the render engine about drawing lines with overlay or
    underlay scenes activated). It will return an object with the 'ground' property, if it finds one. If so, then it will
    return a list consisting of the successful raycast and its starting and ending position (i.e. [ray, topos, frompos]).
    Otherwise, it will return a list consisting of a list with a None in it, and two other Nones (i.e. [[None], None, None]).
    This way you can check: if bghelper.LineRayCast()[0] == None to see if the ray was successful (or any other index of the
    returned list).

    """

    anglevect = anglevect.copy()
    anglevect.magnitude = anglewidth

    if obj is None:
        obj = logic.getCurrentController().owner
    if frompos is None:
        frompos = obj.worldPosition.copy()

    if not isinstance(topos, mathutils.Vector):
        topos = mathutils.Vector(topos)
    if not isinstance(frompos, mathutils.Vector):
        frompos = mathutils.Vector(frompos)

    rtp = topos.copy()
    rfp = frompos.copy()

    rn = raynum - 1

    if rn <= 0:
        rn = 1

    ray = [None]

    if center:
        rtp -= (anglevect / 2) * to_scalar
        rfp -= (anglevect / 2) * from_scalar

    output = {}

    for x in range(raynum):

        ray = obj.rayCast(rtp, rfp, dist, prop, face, xray, poly)

        if debug:

            to = rtp - rfp
            to.magnitude = dist

            if ray[0]:
                render.drawLine(rfp, rfp + to, [0, 1, 0])
            else:
                render.drawLine(rfp, rfp + to, [1, 0, 0])

        if objdebug:

            to = rtp - rfp

            sce = logic.getCurrentScene()

            db = sce.addObject(objdebug, obj, 1)
            db.worldPosition = rfp
            db.alignAxisToVect(to, 0)
            db.worldScale = [to.magnitude, 1, 1]

            if ray[0]:
                db.color = [0, 1, 0, 1]
            else:
                db.color = [1, 0, 0, 1]

        if ray[0] is not None:

            if output == {}:
                output["rays"] = ray
                output["ray_start"] = rfp
                output["ray_end"] = rtp
                output["offset"] = rfp - frompos
            else:

                if (rfp - ray[1]).magnitude < (output['ray_end'] - output['rays'][1]).magnitude:
                    # Only overwrite previous raycast results if this one is closer
                    output["rays"] = ray
                    output["ray_start"] = rfp
                    output["ray_end"] = rtp
                    output["offset"] = rfp - frompos

        av = anglevect / rn

        rtp += av * to_scalar
        rfp += av * from_scalar

        # if not converge:
        #	rfp += av

    if output:
        return output

    return {'rays': ray, 'ray_start': None, 'ray_end': None, 'offset': None}