__author__ = 'SolarLune'

import os
import random

import aud
from bge import logic


class AudioDevice():

    BGM_STATUS_STOPPED = 0
    BGM_STATUS_FADING_IN = 1
    BGM_STATUS_PLAYING = 2
    BGM_STATUS_FADING_OUT = 3

    def __init__(self, sound_folder='//assets/snd/'):

        self.device = aud.device()

        self.sounds = {}

        self.set_audio_folder(sound_folder)

        self.bgm_list = []

        self.sound_volume = 1.0
        self.bgm_volume = 1.0

        self.fade_time = 1.0  # Fade time between BGM plays

    def set_audio_folder(self, sound_folder):

        if not sound_folder.endswith("/"):
            sound_folder += "/"  # Make sure there's a trailing slash for sound files to go

        sound_folder = logic.expandPath(sound_folder)

        self.sounds = {}

        for snd_info in os.walk(sound_folder):

            for f in snd_info[2]:

                filename = os.path.splitext(f)[0]  # Ignore the extension; we're just
                # interested in the audio file itself

                self.sounds[filename] = aud.Factory(sound_folder + f)

    def update_bgm(self):

        fr = ((1.0 / logic.getLogicTicRate()) * self.bgm_volume ) / self.fade_time

        list = self.bgm_list[:]

        for b in range(len(list)):

            bgm = list[b]

            if bgm['status'] == self.BGM_STATUS_STOPPED:

                bgm['handle'].stop()
                self.bgm_list.remove(bgm)

            if bgm['status'] == self.BGM_STATUS_FADING_IN:

                bgm['volume'] += fr * self.bgm_volume

                if bgm['volume'] > self.bgm_volume:

                    bgm['volume'] = self.bgm_volume
                    bgm['status'] = self.BGM_STATUS_PLAYING

            elif bgm['status'] == self.BGM_STATUS_PLAYING:

                if b < len(self.bgm_list) - 1:

                    bgm['status'] = self.BGM_STATUS_FADING_OUT  # Begin fading out "extra" tracks

            elif bgm['status'] == self.BGM_STATUS_FADING_OUT:

                bgm['volume'] -= fr * self.bgm_volume

                if bgm['volume'] <= 0:

                    self.bgm_list.remove(bgm)
                    bgm['handle'].stop()

            if bgm['handle'].status == aud.AUD_STATUS_PLAYING:

                bgm['handle'].volume = bgm['volume']

    def play_bgm(self, bgm):

        if self.bgm_volume > 0:

            if not self.bgm_list or self.bgm_list[-1]['name'] != bgm:

                h = self.device.play(self.sounds[bgm])
                h.loop_count = -1
                h.volume = 0.0

                d = {  # Create a new "BGM" entry.

                    'name': bgm,
                    'handle': h,
                    'volume': 0.0,
                    'status': self.BGM_STATUS_FADING_IN

                }

                self.bgm_list.append(d)

    def play_bgm_old(self, bgm, loop=-1):

        if self.bgm_volume > 0.0:

            if bgm != self.current_bgm_handle:

                self.current_bgm_handle = bgm
                self.current_bgm_handle = self.device.play(self.sounds[bgm])
                self.current_bgm_handle.loop_count = loop
                self.current_bgm_handle.volume = self.bgm_volume
                return self.current_bgm_handle

        return None

    def stop_bgm(self):

        if self.bgm_list:

            self.bgm_list[0]['status'] = self.BGM_STATUS_STOPPED

    def stop_all_bgm(self):

        for b in self.bgm_list:

            b['status'] = self.BGM_STATUS_STOPPED

    def play_sound(self, sound, volume_var=0.0, pitch_var=.1):

        if self.sound_volume > 0.0:

            handle = self.device.play(self.sounds[sound])
            handle.volume = self.sound_volume
            handle.volume += random.uniform(0.0, volume_var)
            handle.pitch += random.uniform(-pitch_var, pitch_var)
            return handle

    def get_bgm_handle(self):

        if self.bgm_list:
            return self.bgm_list[0]['handle']
        else:
            return None


device = AudioDevice()