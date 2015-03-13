__author__ = 'SolarLune'

from bge import logic

LT_POINT = 0
LT_SPOT = 1
LT_SUN = 2
LT_HEMI = 3


class LightManager():
    """

    A class for managing lights.

    The Poll() function looks through the scene to find objects that have a property named "DynLightNode", which indicates
    spots where lights should be dynamically.

    The Update() function spawns and places dynamic lights to these light node positions.

    TODO: Expand the Update() function to copy the nodes' energy, color, and other light properties if they're outlined
    in the group object (if it is one), and otherwise in the object itself.

    """

    def __init__(self):

        self.light_nodes = {'point': [],
                            'sun': [],
                            'spot': [],
        }  # [s for s in sce.objects if 'DynLightNode' in s]
        self.template_lights = {'point': [],
                                'sun': [],
                                'spot': [],
        }
        self.existing_lights = {'point': [],
                                'sun': [],
                                'spot': [],
        }

        self.default_energy = 2.0  # Default values for lights that can be overridden by
        # putting values in the dynamic light polling objects themselves (TODO: Actually implement that)

        self.default_distance = 10.0

        self.default_color = [1, 1, 1]

        self.default_spotsize = 45

        self.default_spotblend = 0.25

    def update(self, ref_obj=None, scene=None):

        """
        Create new lights from existing "template" lights and move them as necessary to the nodes closest to the ref_point.
        """

        cont = logic.getCurrentController()
        obj = cont.owner

        if scene == None:
            sce = logic.getCurrentScene()
        else:
            sce = scene

        if ref_obj == None:
            point = sce.active_camera
        else:
            point = ref_obj

        for l in self.light_nodes:

            if len(self.existing_lights[l]) == 0:

                for x in range(len(self.template_lights[l][:])):
                    light = sce.addObject(self.template_lights[l].pop(), obj)

                    light.energy = 0.0

                    self.existing_lights[l].append(light)

            nodes = self.light_nodes[l][:]
            nodes.sort(key=lambda x: point.getDistanceTo(x))

            for n in range(len(nodes)):

                node = nodes[n]

                if n <= len(self.existing_lights[l]) - 1:
                    cur_light = self.existing_lights[l][n]

                    cur_light.worldPosition = node.worldPosition
                    cur_light.worldOrientation = node.worldOrientation

                    cur_light.energy = self.default_energy  # TODO: Link these to the node objects or their group objects if possible

    def poll(self, scene=None):

        """
        Polls the scene for light nodes, and polls the inactive layer for template lights
        """

        if scene == None:
            sce = logic.getCurrentScene()
        else:
            sce = scene

        for s in sce.objects:

            if "DynLightNode" in s:

                if s['DynLightNode'].lower() == 'point':
                    self.light_nodes['point'].append(s)
                elif s['DynLightNode'].lower() == 'sun':
                    self.light_nodes['sun'].append(s)
                elif s['DynLightNode'].lower() == 'spot':
                    self.light_nodes['spot'].append(s)

        for s in sce.objectsInactive:

            if 'DynLight' in s:

                if s.type == s.NORMAL:
                    self.template_lights['point'].append(s)
                elif s.type == s.SUN:
                    self.template_lights['sun'].append(s)
                elif s.type == s.SPOT:
                    self.template_lights['spot'].append(s)


def add_light(light_type=LT_POINT, time=0, priority=0):
    """
    Spawns a light that was pre-placed in a hidden layer. Note that the light must have a property present
    in it named "DynLight". It must be set to "Point", "Sun", "Hemi", or "Spot" for it to spawn in correctly.

    time = how long the light should stick around in frames
    priority = what priority the light should spawn with. Higher priorities will delete and re-create
    (overwrite, if you will) existing lights if not enough pre-made lights are present.

    Basically, priority allows you to spawn lights with low
    priority at non important places, like spawn 10 torches with lights at priority 0, and then spawn a light
    for the player with a priority of 1. Since it has a higher priority, the player's light will spawn, and one
    of the torches' lights will be deleted.
    """

    sce = logic.getCurrentScene()

    obj = logic.getCurrentController().owner

    if not hasattr(logic, 'lights_used'):

        logic.lights_used = {
            # 'Point':{},
            # 'Sun':{},
            #'Hemi':{},
            #'Spot':{},
        }  # Create a mapping of lamps with their types to spawners

        # for lt in logic.lights_used:

        for l in [l for l in sce.objectsInactive if
                  "DynLight" in l]:  # Loop through the lamps that have the string "Dyn" + the type in their name (i.e. Point lamps named "Point", "Point.001", etc.)

            if not l['DynLight'] in logic.lights_used:
                logic.lights_used[l['DynLight']] = {}

            logic.lights_used[l['DynLight']][l.name.lower()] = {'reference': None,
                                                                'priority': 0}  # And set their "used" status to 0

    if light_type == LT_POINT:
        lt = 'point'
    elif light_type == LT_SPOT:
        lt = 'spot'
    elif light_type == LT_SUN:
        lt = 'sun'
    else:
        lt = 'hemi'

    for l in logic.lights_used[lt]:  # Then loop through all of the lamps

        light_dict = logic.lights_used[lt][l]

        if light_dict['reference'] == None:  # And when you find a lamp that hasn't been used

            light = sce.addObject(l, obj, time)  # Create that lamp,

            light_dict['priority'] = priority

            light_dict[
                'reference'] = light  # And set it to be used (mitts off to all other spawners until it's destroyed)

            return light  # And then break out of the loop, returning the spawned light

        else:

            if light_dict['reference'].invalid:
                # If the lamp you've "found" is used, but doesn't exist or has been deleted, or has a lower priority
                # than intended,

                light = sce.addObject(l, obj, time)

                light_dict['reference'] = light  # Then re-use that one, rather than looking for another lamp

                light_dict['priority'] = priority

                return light  # And then break out of the loop, returning the spawned light

    light_keys = list(logic.lights_used[lt].keys())

    lights_pri = sorted(light_keys, key=lambda light_in_use: logic.lights_used[lt][light_in_use]['priority'])

    for l in lights_pri:

        light_dict = logic.lights_used[lt][l]

        if light_dict['priority'] < priority:
            light_dict['reference'].endObject()

            light = sce.addObject(l, obj, time)

            light_dict['reference'] = light

            light_dict['priority'] = priority

            return light

    return None
