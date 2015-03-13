__author__ = 'SolarLune'

import math

from bge import logic


class _spritemap_base():

    def __init__(self, obj):

        """
        Creates a SpriteMap to animate an object by.

        :param obj: KX_GameObject - Sprite object to perform operations on
        :return: _spritemap_base
        """

        self.obj = obj

        self.subimage = 1.0

        self.prev_subimage = 1.0

        self.fps_lock = True  # Lock the animating process to the logic tic rate (i.e. target FPS) or not (use the
        # average frame-rate)

        self.adjust_by_sensor_frequency = True  # Attempts to take into account the first sensor's frequency when
        # animating

        self.anim_dict = {}

        self.current_animation = None  # The current animation

        self.prev_animation = None  # The previous animation

        self.is_playing = False  # If the sprite-map is currently playing an animation or is
        # stopped after playing a one-shot one

    def add(self, anim_name, animation, fps=15, loop=True):

        """
        :param anim_name: Str - Name of the animation
        :param animation: List - A list "describing" the animation
        :param fps: Int - The FPS to play the animation back at
        :param loop: Bool - Whether the animation should loop or not
        :return: None

        Registers the animation specified to the SpriteMap.
        """

        self.anim_dict[anim_name] = {'animation': animation, 'fps': fps, 'loop': loop}

    def remove(self, anim_name):
        """
        :param anim_name: Str
        :return: Bool
        Removes the specified animation from the animations registered in the SpriteMap. Returns True if the animation
        existed, and False otherwise.
        """

        if anim_name in self.anim_dict:
            del self.anim_dict[anim_name]
            return True
        else:
            return False

    def get_animation_names(self):
        """
        :return: List
        Returns a list of the names of each animation in the SpriteMap.
        """

        return [name for name in self.anim_dict]

    def get_animation_dict(self):
        """
        :return: Dictionary
        Returns each animation registered in the SpriteMap.
        """

        return self.anim_dict

    def set_fps(self, anim_name, fps):

        self.anim_dict[anim_name]['fps'] = fps

    def get_fps(self, anim_name):

        return self.anim_dict[anim_name]['fps']

    def set_loop(self, anim_name, loop):
        """
        Sets the loop value of the animation specified.
        :param anim_name: String - Name of the animation.
        :param loop: Bool - Whether to loop the animation when played or not.
        :return: None
        """

        self.anim_dict[anim_name]['loop'] = loop

    def get_loop(self, anim_name):

        """
        Returns the loop value of the animation specified.
        :param anim_name: String - Name of the animation to check.
        :return: None
        """

        return self.anim_dict[anim_name]['loop']

    def set_subimage(self, subimage):
        """
        Sets the subimage of the spritemap.
        :param subimage: Float - Subimage to set; 1 is the start of the animation.
        :return:None
        """

        self.subimage = float(subimage)

    def get_subimage(self):
        """
        Returns the current subimage of the sprite map.
        :return:None
        """

        return self.subimage

    def is_playing(self):
        """
        Returns if the spritemap is playing an animation or not. Only is set to False if it's playing an animation that
        doesn't loop, and the animation has finished.
        :return:Bool
        """

        return self.is_playing

    def has_animation(self, anim_name):

        """
        Returns if the spritemap has an animation named defined.
        :param anim_name: String - Name of the animation
        :return: Bool
        """

        return anim_name in self.anim_dict

    def play(self, anim_name, reset_subimage_on_change=True):

        if not anim_name in self.anim_dict:

            print("ERROR: SpriteMap owner " + self.obj.name + " has no animation named " + anim_name + ".")

            return False

        elif len(self.anim_dict[anim_name]['animation']) < 2:

            print("ERROR: SpriteMap owner " + self.obj.name + "'s animation " + anim_name + " does not contain data "
                                                                                            "for at least one frame of "
                                                                                            "animation.")

            return False

        self.current_animation = anim_name

        if self.current_animation != self.prev_animation:

            self.on_animation_change(self, self.current_animation, self.prev_animation)  # Callback

            if reset_subimage_on_change:
                self.subimage = 1.0

        if self.adjust_by_sensor_frequency:
            freq = logic.getCurrentController().sensors[0].frequency + 1
        else:
            freq = 1

        if self.fps_lock:
            scene_fps = logic.getLogicTicRate()
        else:
            scene_fps = logic.getAverageFrameRate()
            if scene_fps == 0.0:
                scene_fps = logic.getLogicTicRate()

        if anim_name and anim_name in self.anim_dict:

            anim = self.anim_dict[anim_name]['animation']
            anim_fps = self.anim_dict[anim_name]['fps']

            target_fps = anim_fps / scene_fps

            if len(anim) > 2:  # Don't advance if there's only one cell to the animation

                if target_fps != 0.0:
                    self.subimage += round(target_fps, 2) * freq

            subi = round(self.subimage, 4)

            if (self.subimage <= len(anim) - 2 and anim_fps > 0) or (self.subimage > 1.0 and anim_fps < 0):
                self.is_playing = True

            if self.anim_dict[anim_name]['loop']:  # The animation is to be looped

                fin = 0

                if len(anim) >= 2:

                    while math.floor(subi) > len(anim) - 1:
                        subi -= len(anim) - 1
                        fin = 1

                    while math.floor(subi) < 1.0:
                        subi += len(anim) - 1
                        fin = 1

                if fin:
                    self.on_animation_finished(self)  # Animation's finished because it's looping

                self.is_playing = True

            else:  # No loop

                if subi >= len(anim) - 1 or subi < 1.0:

                    if self.is_playing:
                        self.on_animation_finished(self)  # Animation's finished because it's at the end of a
                        # non-looping animation

                    if len(anim) >= 2:
                        subi = min(max(subi, 1.0), len(anim) - 1)
                    else:
                        subi = 1.0

                    self.is_playing = False

            if math.floor(subi) != math.floor(self.prev_subimage):
                self.on_subimage_change(self, math.floor(subi), math.floor(self.prev_subimage))
                # Callback for subimage change

            self.subimage = subi

        else:

            print("ERROR: ANIMATION NAME " + anim_name + " NOT IN SPRITEMAP OR NOT STRING.")

        self.prev_animation = self.current_animation
        self.prev_subimage = self.subimage

        if self.obj.invalid:  # You did something that killed the object; STOP PRODUCTION!

            print("ERROR: SPRITE MAP OPERATING ON NON-EXISTENT OBJECT!!!")

            return False

        return True

    def get_current_animation(self):
        """
        Returns the name of the current animation playing.
        :return: String
        """

        return self.current_animation

    def get_animation_length(self, anim_name):
        """
        Returns the length of the animation specified.
        :param anim_name: String - Name of the animation
        :return: Int
        """

        return len(self.anim_dict[anim_name]['animation']) - 1

    def copy_animations(self, other_spritemap):

        self.anim_dict = other_spritemap.anim_dict.copy()

    def on_last_frame(self):

        return self.subimage >= self.get_animation_length(self.current_animation)

    # CALLBACKS

    def on_subimage_change(self, sprite_map, current_subimage, prev_subimage):

        """
        Stub callback that runs when the animation's subimage changes (i.e. the animation changes frames).
        Should be overwritten with a custom function if wanted.

        :param sprite_map: _spritemap_base - The calling sprite map
        :param current_subimage: Int - The current subimage (rounded down to an integer)
        :param prev_subimage: Int - The previous subimage (rounded down to an integer)
        :return: None

        """

        pass

    def on_animation_change(self, sprite_map, current_anim, prev_anim):

        """
        Stub callback that runs when the SpriteMap changes animations (i.e. you use play() with a new animation).
        Should be overwritten with a custom function if wanted.

        :param sprite_map: _spritemap_base - The calling sprite map
        :param current_anim: Str - The name of the current animation
        :param prev_anim: Str - The name of the previous animation
        :return: None
        """

        pass

    def on_animation_finished(self, sprite_map):

        """
        Stub callback that runs when the SpriteMap finishes its current animation.
        Should be overwritten with a custom function if wanted.

        :param sprite_map: _spritemap_base - The calling sprite map
        :return: None
        """

        pass


class SpriteMapUV(_spritemap_base):

    def __init__(self, obj):

        """
        Creates a UV-based SpriteMap to animate an object by. UV SpriteMap animations take the form of:
        [column, row frame 0, row frame 1, row frame 2, etc]
        So if you have the sprite already defined in Blender, then 0, 0 would be the bottom left corner of the sprite
        sheet with the sprite size defined. If you have an animation of 4 frames in that column with the sprites
        ascending upwards, then the animation would be [0, 0, 1, 2, 3].

        :param obj: KX_GameObject - Sprite object to perform operations on
        :return: SpriteMapUV
        """

        super().__init__(obj)

        self.vertices = []

        for mesh in self.obj.meshes:

            for mat in range(len(mesh.materials)):

                for v in range(mesh.getVertexArrayLength(mat)):
                    self.vertices.append(mesh.getVertex(mat, v))  # For UV animation

        uvs = []

        for v in self.vertices:
            uv = v.getUV()

            uvs.append([v, uv.x + uv.y])

        uvs.sort(key=lambda vuv: vuv[1])

        self.uv_size = [abs(uvs[-1][0].getUV()[0] - uvs[0][0].getUV()[0]),
                        abs(uvs[-1][0].getUV()[1] - uvs[0][0].getUV()[1])]

        self.offset = {}

        self.flip_x = False
        self.flip_y = False

        for vert in self.vertices:
            self.offset[vert] = vert.getUV() - uvs[0][0].getUV()  # The offset from the bottom-left vertex

    def play(self, anim_name, reset_subimage_on_change=True):

        p = super().play(anim_name, reset_subimage_on_change)

        if p is False:  # There was an error; the spritemap probably is trying to play an animation without enough data
            return False

        anim = self.anim_dict[self.current_animation]['animation']

        subi = math.floor(self.subimage)

        for v in range(len(self.vertices)):

            vert = self.vertices[v]
            opposite = self.vertices[v - (len(self.vertices) // 2)]  # Note this won't work with oddly-numbered, uneven
            # meshes; heck, it might not work with subdivided simple planes. Best I can do under the circumstances.

            if self.flip_x:
                xcomp = self.offset[opposite].x + (self.uv_size[0] * anim[0])
            else:
                xcomp = self.offset[vert].x + (self.uv_size[0] * anim[0])

            if self.flip_y:
                ycomp = self.offset[opposite].y + (self.uv_size[1] * anim[subi])
            else:
                ycomp = self.offset[vert].y + (self.uv_size[1] * anim[subi])

            vert.setUV([xcomp, ycomp])

        return True


class SpriteMapMesh(_spritemap_base):
    def __init__(self, obj):

        """
        Creates a mesh-based SpriteMap to animate an object by. Mesh SpriteMap animations take the form of:
        [MeshAnimationSeriesName, frame 0, frame 1, frame 2, etc]

        So if you have the sprite meshes already defined in Blender, then the animation would be the prefix of the
        sprite mesh names before the frame index, like:

        ["Explosion", 0, 1, 2, 3]

        :param obj: KX_GameObject - Sprite object to perform operations on
        :return: SpritemapMesh
        """

        super().__init__(obj)

    def play(self, anim_name, reset_subimage_on_change=True):

        p = super().play(anim_name, reset_subimage_on_change)

        if p is False:
            return False

        anim = self.anim_dict[self.current_animation]['animation']

        subi = math.floor(self.subimage)

        anim_cell = anim[0] + str(anim[subi])

        if self.obj.meshes[0].name != anim_cell:
            self.obj.replaceMesh(anim_cell)

        return True

