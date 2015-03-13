__author__ = 'SolarLune'

# Random level generation module.
# TODO: Add rectangular rooms to the GenNodes room styles.

import random
import math
import copy

from bge import logic
import mathutils

from .mesh import get_dimensions
from .math import clamp

# CONSTANTS

# Connection styles for the GenNodes function;

GN_CONNECTION_STYLE_ONE = 0  # ONE = all nodes connect to another one (other than themselves) randomly
GN_CONNECTION_STYLE_ALL = 1  # ALL = Each node makes a connection to every other node
GN_CONNECTION_STYLE_HUB = 2  # HUB = Each node connects to a pre-determined node (like a spiderweb or a "splash")

GN_ROOM_STYLE_ROUND = 0  # Explodes a round room for the node
GN_ROOM_STYLE_SQUARE = 1  # Explodes a rectangular room for the node

RLG_POP_CEIL = 0  # When
RLG_POP_END = 1
RLG_POP_STRAIGHT = 2
RLG_POP_CORNER = 3
RLG_POP_T_END = 4
RLG_POP_4WAY = 5

GSC_EDGE_BLANK = 0
GSC_EDGE_VOID = 1
GSC_EDGE_EXTEND = 2
GSC_EDGE_WRAP = 3

# Helper Functions


def get_surrounding_cells(room, cell_y, cell_x, ignore=0, edge=0):
    """

    Author : SolarLune
    Date Updated : 11/24/13

    Gets and returns the values in the indices in the surrounding cells and count from the room array supplied.

    room = Room array
    celly, cellx = cell co-ordinates to check around
    ignore = Value to ignore (not count); If set to None, then no number will be ignored

    TODO: edge = What to do when checking cells on the edges of the list.

    0 = Blank; It's assumed the non-existent cell is 0.
    1 = Void; The non-existent cell's value returns None. This will affect the returned
        number of surrounding cells accordingly.
    2 = Extend; It's assumed the non-existent cell is the same as the current number.
    3 = Wrap; It's assumed the non-existent cell is the same as the cell on the opposite border.

    Y'know, wrapping around the map would be possible, too - you'd just have
    to check for that case.

    Returns a dictionary consisting of two keys.
    "cells" = value returned in the cell directly one value away
    (i.e. left is one to the left, right is one to the right, etc)
    "sum" = how many non-zero values were found

    """

    if cell_x > 0:
        left = room[cell_y][cell_x - 1]
    else:
        if edge == 0:  # Blank
            left = 0
        elif edge == 1:  # Void
            left = None
        elif edge == 2:  # Extend
            left = room[cell_y][cell_x]
        elif edge == 3:  # Wrap
            left = room[cell_y][len(room[cell_y]) - 1]

    if cell_x < len(room[cell_y]) - 1:
        right = room[cell_y][cell_x + 1]
    else:
        if edge == 0:
            right = 0
        elif edge == 1:
            right = None
        elif edge == 2:
            left = room[cell_y][cell_x]
        elif edge == 3:
            right = room[cell_y][0]

    if cell_y > 0:
        up = room[cell_y - 1][cell_x]
    else:
        if edge == 0:
            up = 0
        elif edge == 1:
            up = None
        elif edge == 2:
            left = room[cell_y][cell_x]
        elif edge == 3:
            up = room[len(room) - 1][cell_x]

    if cell_y < len(room) - 1:
        down = room[cell_y + 1][cell_x]
    else:
        if edge == 0:
            down = 0
        elif edge == 1:
            down = None
        elif edge == 2:
            left = room[cell_y][cell_x]
        elif edge == 3:
            down = room[0][cell_x]


    #print (down)

    cells = [left, right, up, down]

    num = len(cells) - cells.count(ignore) - cells.count(None)

    return ({'cells': {'left': left, 'right': right, 'up': up, 'down': down}, 'num': num})


# ~~~~ Generation Functions ~~~~~

def gen_line(size_x=9, size_y=9, line_y=None, random_seed=None, line_types=[1], fill_types=[2], empty_types=[0], room_list=None):

    randomstate = random.getstate()  # Used to preserve random settings before using the function

    random.seed(random_seed)  # Set the seed, if there is one

    if room_list is None:

        room = []

        for y in range(size_y):  # Create empty rooms
            room.append([])
            for x in range(size_x):
                room[y].append(random.choice(empty_types))

    else:

        room = copy.deepcopy(room_list)

    if line_y is None:

        ly = size_y // 2 + random.randint(-size_y // 4, size_y // 4)

    else:

        ly = line_y

    for x in range(len(room)):

        for y in range(len(room[x])):

            if y == ly:

                room[y][x] = random.choice(line_types)

            elif y < ly:

                room[y][x] = random.choice(fill_types)

        r = random.random
        ly -= int(round(r()))
        ly += int(round(r()))

        if ly < 0:
            ly = 0

        elif ly > len(room) - 1:
            ly = len(room) - 1

    random.setstate(randomstate)

    return room


def gen_growth(size_x=9, size_y=9, maxnum=0, random_seed=None, must_connect=1, maxcon=0, roomtypes=[1], room_list=None):
    """

        2D RANDOM ROOM GENERATOR

        Author: SolarLune
        Date Updated: 6/24/11

        xsize = X-size of the randomly generated room

        size_y = Y-size of the randomly generated room

        Note that if you use an even number, then there's no middle cell, so you can't be exactly sure which cell WILL be filled.

        maxnum = Maximum number of rooms; by default will make half of the total rooms populated (i.e. 5x5 = 25 / 2 = ~13)

        random_seed = Random seed value; this will (hopefully) make it so that each randomly generated map can be the same with a specific seed

        maxcon = Maximum connections each room can have. Hallways can only have one other connection,
        for example, and the default is 0, which is as many as possible (yes, hallways actually have two,
        but each hallway thinks it's the last one, basically)

        roomtypes = Room types (for example, you might want some rooms to be sand, others rock, etc.); basically, the
        generation will contain random selections of these numbers. So, if you wanted a map of sand, grass, and concrete,
        you could make a list of three numbers, and replace those numbers with the correct values later on

        room_list = A previous room list (maybe you have a list that you got and want to add on values, or change the theme by using the same seed
        as before and using different 'roomtypes'. Beware - ensuring that the room_list is the correct size is up to you.
    """

    currentnum = 0

    if room_list is None:

        room = []

        for y in range(size_y):  # Create empty rooms
            room.append([])
            for x in range(size_x):
                room[y].append(0)
    else:

        room = room_list[:]

        roomnumbers = 0

        for x in room:  # Add number of occupied rooms (not 0)

            currentnum += x.count(not 0)

        #print ([x.count(0) for x in room[:]])
        #print ('----')

    #### CELL GENERATION ####

    randomstate = random.getstate()  # Used to preserve random settings before using the function

    random.seed(random_seed)  # Set the seed, if there is one

    if must_connect and currentnum == 0:
        middley = math.floor(size_y / 2.0)  # Set the middle cell to be filled
        middlex = math.floor(size_x / 2.0)
        room[middley][middlex] = random.choice(roomtypes)

        currentnum += 1

    if maxnum > 0:
        maxsize = maxnum
    else:
        maxsize = (size_x * size_y) / 2

    rlgpass = 0  # Failsafe

    while (currentnum < maxsize):

        rlgpass += 1
        if rlgpass > 100000:  # If the number of passes exceeds a certain amount, it breaks out; unnecessary now
            currentnum = maxsize
            break

        randomy = math.floor(random.random() * size_y)  # Choose a random cell
        randomx = math.floor(random.random() * size_x)

        if room[randomy][randomx] == 0:  # Don't set a cell more than once

            if must_connect:

                sur = get_surrounding_cells(room, randomy, randomx)

                cellaround = 0  # If there's a connection around the current cell

                for c in sur['cells']:
                    cell = sur['cells'][c]
                    if cell != 0 and cell != None:
                        cellaround = 1  # If there's another cell surrounding this one that isn't 0 or None

                if sur['num'] > maxcon and maxcon > 0:
                    pass

                elif cellaround:
                    room[randomy][randomx] = random.choice(roomtypes)
                    currentnum += 1

            else:
                room[randomy][randomx] = random.choice(roomtypes)
                currentnum += 1

    random.setstate(randomstate)  # Reset random settings

    #print ('Room:')

    #for y in room:		# Quickie room debug
    #	print (y)

    return room


def gen_nodes(size_x=9, size_y=9, nodecount=None, spacing=1, random_seed=None, nodetypes=[1], halltypes=[1], empty_types=[0],
             straight_halls=False, connection_style=GN_CONNECTION_STYLE_ONE,
             room_style=GN_ROOM_STYLE_SQUARE, min_room_size=2, max_room_size=5, room_list=None):
    """

    This method of random generation spawns several nodes, and then connects those nodes with halls.

    x, size_y = size of the generated list

    nodecount = number of nodes to spawn; defaults to half of the width of the room.

    spacing = spawn nodes with a minimum number of >spacing< blank nodes between them (both x and y axes individually).
    An example would be a node at [4, 4] and another one at [18, 5]. If spacing == 1, then that won't work, since
    5 - 4 = 1 node difference.
    if spacing == 0 (default), distance has no bearing on where nodes are spawned

    Note! If spacing is too large and the room has too small a size, it will basically be tried for, but otherwise
    the room will generate however it can. Use small spacing amounts and large rooms.

    random_seed = random seed for spawning the same list each time

    nodetypes = a list of different (randomly chosen) numbers that can spawn for the nodes separating halls

    halltypes = a list of different (randomly chosen) numbers that can spawn for the halls in-between nodes

    empty_types = a list of different (randomly chosen) numbers that can spawn for the non-hall or node spots

    straight_halls = determines if the hallways basically only bend once max, or if they "stair-step" between nodes

    connection_style = determines how the nodes connect to each other.

    GN_CONNECTION_STYLE_ONE = All nodes each connect to one other randomly chosen node
    (this will result in the map being connected correctly, of course)

    GN_CONNECTION_STYLE_ALL = All nodes connect to each other. For an example, think of a square with four points -
    each point connects	to the three other points.

    GN_CONNECTION_STYLE_HUB = All nodes connect to one other node specifically; i.e., if you have 10 nodes, one
    node will connect to all other nodes, and every other node will only connect to the previous one

    room_style = determines how the nodes form rooms.

    GN_ROOM_STYLE_ROUND = Round rooms
    GN_ROOM_STYLE_SQUARE = Octopus-shaped rooms

    min_room_size, max_room_size = determines how large each node room can be minimum and maximum

    room_list = preexisting list to use; numbers that are specified in nodetypes are interpreted as nodes, numbers
    that are in halltypes are interpreted as halls, and numbers that are in empty_types are interpreted as "empties".
    The nodecount you specify is added to the existing nodes you have pre-existing in the room list.
    """

    if room_list != None:

        if not isinstance(room_list, list):
            print("ERROR: Provided room_list is not a list")

            return []

        maplist = room_list
        middle = [size_x // 2, size_y // 2]

        size_y = len(maplist)
        size_x = len(maplist[0])

    else:

        maplist = []

        for j in range(size_y):

            maplist.append([])

            for i in range(size_x):
                maplist[j].append(random.choice(empty_types))

        #maplist = [[random.choice(empty_types) for j in range(xsize)] for i in range(size_y)]

        middle = [size_x // 2, size_y // 2]

    randomstate = random.getstate()

    random.seed(random_seed)

    #maplist[middle[1]][middle[0]] = random.choice(

    nodelist = []  # List of nodes
    toconnect = {}  # List of nodes that are still up for connections and their connection counts

    if nodecount is None:
        ndc = int(size_x / 2)
    else:
        ndc = nodecount

    if room_list:

        list_node_count = 0

        for c in range(len(room_list)):
            for x in range(len(room_list[c])):
                if room_list[c][x] in nodetypes:
                    node = (c, x)
                    nodelist.append(node)
                    toconnect[node] = []

                    list_node_count += 1

    for n in range(ndc):  # Generate nodes

        node = None

        if spacing <= 0:

            while (node is None):

                cy = random.choice(range(len(maplist)))
                cx = random.choice(range(len(maplist[cy])))

                #if maplist[cy][cx] in empty_types:
                if not maplist[cy][cx] in nodetypes:
                    node = (cy, cx)

                    nodelist.append(node)
                    toconnect[node] = []  # What nodes the node is connected to

        else:

            for dist in range(spacing + 1, -1,
                              -1):  # If you can't find a node at the specified minimum distance, then search at a closer distance

                for i in range(1000):  # Set a limit so that it doesn't hang the game :/

                    cy = random.choice(range(len(maplist)))
                    cx = random.choice(range(len(maplist[cy])))

                    #if maplist[cy][cx] in empty_types or maplist[cy][cx] in halltypes:
                    if not maplist[cy][cx] in nodetypes:
                        node = (cy, cx)

                        for other in nodelist:
                            if other != node:

                                diffx = abs(node[1] - other[1])
                                diffy = abs(node[0] - other[0])

                                if diffx < dist or diffy < dist:  # Discard the node placement if it's too close to another node
                                    node = None  # And find another node placement (in the same 100x for loop above)
                                    break

                    if node != None:
                        nodelist.append(node)
                        toconnect[node] = []
                        break

                if node != None:
                    break

        maplist[node[0]][node[1]] = random.choice(nodetypes)

    if max_room_size > 0:  # Create rooms

        for n in nodelist:

            room_size = int(random.uniform(min_room_size, max_room_size))

            if room_size > 0:

                #rv = mathutils.Vector([random.random(), random.random()])

                #rv.magnitude = room_size

                for y in range(len(maplist)):

                    for x in range(len(maplist[y])):

                        #cell = room_list[y][x]

                        if room_style == GN_ROOM_STYLE_ROUND:

                            if (mathutils.Vector([y, x]) - mathutils.Vector([n[0], n[1]])).magnitude <= room_size:
                                maplist[y][x] = maplist[n[0]][n[1]]

                        else:

                            if abs(y - n[0]) < room_size and abs(x - n[1]) < room_size:
                                maplist[y][x] = maplist[n[0]][n[1]]

    if len(nodelist) <= 1:
        print("ERROR: nodecount needs to be larger than 1")
        return

    if connection_style == GN_CONNECTION_STYLE_HUB:
        connection_list = [random.choice(list(toconnect.keys()))]

    for node in list(toconnect.keys()):  # Connect nodes

        destnode = None

        while destnode is None:  # Find a destination node

            if len(toconnect[node]) >= len(toconnect.keys()) - 1:  # Connected to all available nodes

                break

            else:

                if connection_style == GN_CONNECTION_STYLE_ONE:
                    connection_list = [random.choice(list(toconnect.keys()))]  # Changes with connection_style
                elif connection_style == GN_CONNECTION_STYLE_ALL:
                    connection_list = [c for c in
                                       toconnect.keys()]  #[random.choice(list(toconnect.keys()))] # Changes with connection_style

                if connection_style == GN_CONNECTION_STYLE_HUB and connection_list[
                    0] == node:  # If you're set to HUB connection and the node selected is you,
                    break  # Break out of the while loop

                for dn in connection_list:

                    if dn != node and not dn in toconnect[node]:

                        destnode = dn

                        diff = mathutils.Vector(dn) - mathutils.Vector(node)

                        if straight_halls:

                            target = list(node)

                        else:

                            target = mathutils.Vector(node)
                            axis_x = 1

                        for x in range(1000):  # Can make a 10000 unit path

                            if straight_halls:

                                if destnode[0] > target[0]:
                                    target[0] += 1
                                elif destnode[0] < target[0]:
                                    target[0] -= 1
                                elif destnode[1] > target[1]:
                                    target[1] += 1
                                elif destnode[1] < target[1]:
                                    target[1] -= 1

                            else:

                                axis_x = not axis_x

                                if axis_x:
                                    target.x += diff.normalized().x
                                else:
                                    target.y += diff.normalized().y

                            target_rnd = (int(clamp(round(target[0]), 0, size_x - 1)),
                                          int(clamp(round(target[1]), 0, size_y - 1)))

                            if target_rnd == destnode:  #target_floor == destnode or target_ceil == destnode:									# Destination

                                maplist[destnode[0]][destnode[1]] = random.choice(
                                    nodetypes)  # Make sure we didn't overwrite it
                                maplist[node[0]][node[1]] = random.choice(nodetypes)

                                toconnect[tuple(node)].append(destnode)
                                toconnect[tuple(destnode)].append(node)

                                break

                            else:

                                #if maplist[target_rnd[0]][target_rnd[1]] in empty_types: # Not occupied
                                if not maplist[target_rnd[0]][target_rnd[1]] in nodetypes:  # Not occupied
                                    maplist[target_rnd[0]][target_rnd[1]] = random.choice(halltypes)

    random.setstate(randomstate)

    return (maplist)


##### Map population functions #####

def invert(room_list, inversion_dict):
    """

    Inverts the room_list provided. Provide a list of what values to invert, and what the inverted value should be.
    For example, for inversion_dict:

    {0:1, 3:4, ...}

    So that if you provide a list such as:

    [[0,0,0,0,1,1]
    [0,0,0,1,1,1,]
    [0,0,1,3,3,3]]

    You'll get returned

    [[1,1,1,1,0,0]
    [1,1,1,0,0,0,]
    [1,1,0,4,4,4,]]

    """

    l = copy.deepcopy(room_list)

    for y in range(len(l)):

        for x in range(len(l[y])):

            for i in inversion_dict:

                if l[y][x] == i:
                    l[y][x] = inversion_dict[i]

                #elif l[y][x] == inversion_dict[i]: # Vice-versa part; commented out for better capabilities

                #	l[y][x] = i

    return l


def clean_up(room_list):
    """

    Cleans up the room list provided so that if there's numbers that are isolated, they are changed to the surrounding number.

    I.e.

    [[0, 0, 0, 1]
    [0, 0, 1, 0]
    [0, 0, 0, 0]
    [1, 1, 1, 0],
    [1, 0, 1, 1,]]

    Gets turned to

    [[0, 0, 0, 0]
    [0, 0, 0, 0]
    [0, 0, 0, 0]
    [1, 1, 1, 0],
    [1, 1, 1, 1,]]

    """

    l = copy.deepcopy(room_list)

    for y in range(len(l)):

        for x in range(len(l[y])):

            this = l[y][x]

            sur = get_surrounding_cells(room_list, y, x, this, GSC_EDGE_VOID)

            cells = sur['cells']

            n = 0

            c = [cells['left'] is None, cells['right'] is None, cells['up'] is None, cells['down'] is None]

            for i in c:

                if i:
                    n += 1

            if sur['num'] == 4 or sur['num'] + n == 4:

                if cells['left'] != this and cells['left'] != None:
                    l[y][x] = cells['left']
                elif cells['right'] != this and cells['right'] != None:
                    l[y][x] = cells['right']
                elif cells['up'] != this and cells['up'] != None:
                    l[y][x] = cells['up']
                elif cells['down'] != None:
                    l[y][x] = cells['down']

    return l


def populate(room_list, room_4way, room_straight, room_end, room_corner, room_t, room_ceiling={0: None}, spawn_point=None,
             varying_size=0):
    """
    Populates the in-game world with floor pieces according to the room that you feed into the function.

    room_list = a room list to check that's generated with a Gen...() function.

    room_4way - room_middle = dictionaries of room pieces to choose from. The numbered indices correspond to the numbers
    you fed into the generation function. Will be randomly chosen from to allow for some good-looking random level
    design. The dictionaries should look like:

    room_4way = {1:['Room4WayRock', 'Room4WayStone', 'Room4WayStone2', etc], 2:[...]}

    The number represents the cell type (i.e. a 1 on the grid will spawn one of the rooms in the 1 list)

    room_4way = a room with four exits (a cross shape)
    room_straight = a room with two exits across from each other; turned horizontally
    room_end = a room with one exit (a dead end); opens to the west.
    room_corner = a room with two exits (an L-shaped room); opens to the west and turns north (left).
    room_t = a room with three exits (a T-shaped room); facing "upside-down", so that the flat part faces south.

    room_ceiling = the same as above, but optional. This would be the objects to place on every null value (i.e. 0)

    spawn_point = the center of the map, usually; if left to None, it will be the calling object's world position.

    varying_size = if the size of the rooms is individual (i.e. each room can be different sizes), or if they're all the
    same

    NOTE: Each game object that gets spawned gets a property called rlg_info with information about its place in the
    level generation recorded in it. The rlg_info property has three keys: "shape", "pos", and "type".

    The "shape" key equals one of the RLG_POP_xxxxx constants, which dictates what shape the object spawned was supposed to be.
    The "pos" key equals the grid position in the random level map, with the Y-coordinate (or row) first, and the X-coordinate second.
    The "type" key equals what type of object was spawned based on the random level map's numbers (i.e. it's a 1 if it was spawned
    where a 1 was on the random level map).

    Returns a dictionary comprised of two keys:
    "spawned: A list of all room objects spawned
    "room_map": The room_list that you fed in, but with the values replaced by references to the room objects spawned
    (useful for storage and looking up a room in the list later)

    """

    sce = logic.getCurrentScene()
    cont = logic.getCurrentController()
    obj = cont.owner

    spawned = []

    rl = copy.deepcopy(room_list)

    if not varying_size:

        i = list(room_4way.keys())[0]

        r = room_4way[i]

        roomsize = get_dimensions(r[0])[0]

    for ry in range(len(room_list)):

        cy = abs(ry - (len(
            room_list) - 1))  # We have to do this because otherwise, the check will go from bottom to top, incorrectly (the data will be turned around)

        for rx in range(len(room_list[ry])):

            if not room_list[ry][rx] in room_ceiling:  # Not blank

                cell = room_list[ry][rx]

                sur = get_surrounding_cells(room_list, ry, rx)

                if sur['num'] == 1:  # End

                    roomchoice = random.choice(room_end[cell])

                    r = sce.addObject(roomchoice, obj)
                    ori = r.orientation.to_euler()

                    d = sur['cells']

                    if d['right']:
                        ori.z = math.pi
                    elif d['left']:
                        ori.z = 0.0
                    elif d['up']:
                        ori.z = -math.pi / 2.0
                    elif d['down']:
                        ori.z = math.pi / 2.0

                elif sur['num'] == 2:  # Corner or Straight-through

                    d = sur['cells']

                    if (d['left'] and d['right']) or (d['up'] and d['down']):
                        straight = 1
                    else:
                        straight = 0

                    if straight:

                        roomchoice = random.choice(room_straight[cell])

                        r = sce.addObject(roomchoice, obj)
                        ori = r.orientation.to_euler()

                        if d['left'] and d['right']:
                            ori.z = 0.0
                        elif d['up'] and d['down']:
                            ori.z = math.pi / 2.0
                    else:

                        roomchoice = random.choice(room_corner[cell])

                        r = sce.addObject(roomchoice, obj)
                        ori = r.orientation.to_euler()

                        if d['left'] and d['up']:
                            ori.z = 0.0
                        elif d['left'] and d['down']:
                            ori.z = math.pi / 2.0
                        elif d['right'] and d['up']:
                            ori.z = -math.pi / 2.0
                        else:
                            ori.z = math.pi

                elif sur['num'] == 3:  # Middle

                    roomchoice = random.choice(room_t[cell])
                    r = sce.addObject(roomchoice, obj)
                    ori = r.orientation.to_euler()

                    d = sur['cells']

                    if d['left'] and d['right'] and d['up']:
                        ori.z = 0.0
                    elif d['left'] and d['up'] and d['down']:
                        ori.z = math.pi / 2.0
                    elif d['right'] and d['up'] and d['down']:
                        ori.z = -math.pi / 2.0
                    else:
                        ori.z = math.pi

                else:  # 4-way
                    roomchoice = random.choice(room_4way[cell])
                    r = sce.addObject(roomchoice, obj)
                    ori = r.orientation.to_euler()

                spawned.append(r)

                r.orientation = ori

                rlg_info = {'shape': None, 'type': cell, 'pos': (ry, rx)}

                if sur['num'] == 1:
                    rlg_info['shape'] = RLG_POP_END
                elif sur['num'] == 2:
                    if straight:
                        rlg_info['shape'] = RLG_POP_STRAIGHT
                    else:
                        rlg_info['shape'] = RLG_POP_CORNER
                elif sur['num'] == 3:
                    rlg_info['shape'] = RLG_POP_T_END
                else:
                    rlg_info['shape'] = RLG_POP_4WAY

                r['rlg_info'] = rlg_info

                rl[ry][rx] = r

                if varying_size:
                    roomsize = get_dimensions(r)

                halfmapw = math.floor(len(room_list[0]) / 2.0) * roomsize[0]
                halfmaph = math.floor(len(room_list) / 2.0) * roomsize[1]

                if spawn_point is None:
                    spawn_point = list(obj.worldPosition)
                else:
                    spawn_point = list(spawn_point)

                pos = [(rx * roomsize[0]) - (halfmapw) + spawn_point[0], (cy * roomsize[1]) - (halfmaph) + spawn_point[1], spawn_point[2]]

                r.worldPosition = pos

            else:  # Blank, so it's a ceiling piece.

                if not room_ceiling[room_list[ry][rx]] is None:

                    roomchoice = random.choice(room_ceiling[room_list[ry][rx]])
                    r = sce.addObject(roomchoice, obj)
                    spawned.append(r)

                    rl[ry][rx] = r

                    rlg_info = {'shape': RLG_POP_CEIL, 'type': room_list[ry][rx], 'pos': (ry, rx)}

                    r['rlg_info'] = rlg_info

                    halfmapw = math.floor(len(room_list[0]) / 2.0) * roomsize[0]
                    halfmaph = math.floor(len(room_list) / 2.0) * roomsize[1]

                    if spawn_point is None:
                        spawn_point = list(obj.worldPosition)
                    else:
                        spawn_point = list(spawn_point)

                    pos = [(rx * roomsize[0]) - (halfmapw) + spawn_point[0], (cy * roomsize[1]) - (halfmaph) + spawn_point[1],
                           spawn_point[2]]
                    r.worldPosition = pos

    return ({'spawned': spawned, 'room_map': rl})
