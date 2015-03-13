__author__ = 'SolarLune'

from bge import logic, render

import math,time

# Nodemaps for game space navigation.


class Node():

    def __init__(self, obj):

        self.obj = obj

        self.obj['nm_node'] = self  # Place yourself in the "owner" game object

        self.position = self.obj.worldPosition

        self.neighbors = []

        #self.cost = 1

        self.costs = []

        self.parent = None  # Parent node for path-finding

        #self.g_score = 0
        #self.f_score = 0
        #self.h_score = 0

    def reset_costs(self, cost_num):

        self.costs = [0 for x in range(cost_num)]

    def set_cost(self, value, cost_index=0):

        self.costs[cost_index] = value

    def get_cost(self, cost_index=0):

        return self.costs[cost_index]

    def add_cost(self, value, cost_index=0):

        self.costs[cost_index] += value

    def sub_cost(self, value, cost_index=0):

        self.costs[cost_index] -= value


class Path():

    def __init__(self, path):

        self.points = path[:]
        self.temp_points = self.points[:]

    def on_reached_end(self):

        pass

    def navigate(self, turn_spd=0.0, accel_spd=1.0, max_spd=10.0, friction=1.0, close_enough=0.5, obj=None):

        if obj is None:

            obj = logic.getCurrentController().owner

        else:

            obj = obj

        if len(self.temp_points) > 0:

            next_point = self.temp_points[0].obj.worldPosition

            next_dir = obj.getVectTo(next_point)[1]

            vel = obj.worldLinearVelocity.copy()

            vel.z = 0.0

            vel.magnitude -= friction if vel.magnitude > friction else vel.magnitude

            vel.xy += next_dir.xy * (accel_spd + friction)

            if (obj.worldLinearVelocity.xy + vel.xy).magnitude < (max_spd):

                obj.worldLinearVelocity.xy = vel.xy

            if (obj.worldPosition - next_point).magnitude < close_enough:

                self.temp_points.pop(0)

        else:

            print('done')

            self.on_reached_end()

            vel = obj.worldLinearVelocity.copy()
            vel.magnitude -= friction if vel.magnitude > friction else vel.magnitude
            obj.worldLinearVelocity.xy = vel.xy

    def reset_path(self):

        self.temp_points = self.points[:]


class NodeMap():

    def __init__(self, cost_num=1):

        self.nodes = []

        self.cost_num = cost_num  # Number of costs per node; useful if you need multiple
        #  costs for different values (terrain, risk, wants, dislikes, etc)

    def add_node(self, node):

        """
        Adds the node to the nodemap. Also adds cost slots to the node.
        :param node:
        :return:
        """

        node.reset_costs(self.cost_num)

        self.nodes.append(node)

    def remove_node(self, node):

        self.nodes.remove(node)

    def update_neighbors(self, min_dist=0, max_dist=9999, max_connections=9999):

        cont = logic.getCurrentController()
        obj = cont.owner

        evaluated = []

        for n in self.nodes:

            for m in self.nodes:

                if n != m and not m in evaluated:

                    d = (n.position - m.position).magnitude

                    if max_dist >= d >= min_dist:

                        ray = obj.rayCast(n.position, m.position, 0, 'nm_solid', 1, 1)

                        if not ray[0]:

                            if len(n.neighbors) < max_connections and len(m.neighbors) < max_connections:

                                n.neighbors.append(m)
                                m.neighbors.append(n)

            evaluated.append(n)

    def get_closest_node(self, position):

        cont = logic.getCurrentController()

        obj = cont.owner

        sorted_nodes = self.nodes[:]

        sorted_nodes.sort(key=lambda n: (n.position - position).magnitude)

        closest = None

        for n in sorted_nodes:

            ray = obj.rayCast(n.position, position, 0, 'nm_solid', 1, 1, 1)

            if not ray[0]:

                closest = n

                break

        return closest

    def get_path_to(self, ending_point, starting_point=None, max_check_num=1000, cost_coefficient=None):

        if cost_coefficient is None:

            cost_coefficient = [1 for x in range(self.cost_num)]

        if starting_point is None:

            starting_point = logic.getCurrentController().owner.worldPosition.copy()

        goal = self.get_closest_node(ending_point)
        starting_node = self.get_closest_node(starting_point)

        def get_f_score(node):

            costs = [x*y for x,y in zip(node.costs, cost_coefficient)]

            return (starting_node.obj.position - node.obj.position).magnitude + (node.obj.position - goal.obj.position).magnitude + sum(costs)

        if not goal:

            print("ERROR: GOAL POSITION CANNOT BE REACHED FROM ANY NODE ON MAP.")
            return

        if not starting_node:

            print("ERROR: STARTING NODE CANNOT BE REACHED FROM ANY NODE ON MAP.")
            return

        open_list = [starting_node]
        closed_list = []

        exit_loop = False

        for x in range(max_check_num):

            open_list.sort(key=get_f_score)

            current_node = open_list.pop(0)
            closed_list.append(current_node)

            for neighbor in current_node.neighbors:

                if neighbor in closed_list:

                    continue

                if neighbor not in open_list:

                    neighbor.parent = current_node

                    open_list.append(neighbor)

                    if neighbor == goal:

                        exit_loop = True  # A path has been found

                        break

            if exit_loop:

                break

        path = []

        target_square = goal

        for x in range(1000):

            path.append(target_square)

            if target_square == starting_node:

                break

            target_square = target_square.parent

        path.reverse()  # Go from the start to the goal

        if len(path):

            return Path(path)  # Create a path object

        else:

            print("No path found")

    def get_path_costs(self, path):

        costs = [0 for x in range(self.cost_num)]

        for node in path.points:

            costs = [x + y for x, y in zip(costs, node.costs)]

        return costs

    def debug_node_connections(self):

        for node in self.nodes:

            for neighbor in node.neighbors:

                render.drawLine(node.position, neighbor.position, [1, 0, 0])

    def debug_node_path(self, path):

        #print("______")

        for node in path.points:

            #print(node.obj)

            s = abs(math.sin(time.clock() * math.pi))

            node.obj.color = [s, s, s, 1]