'''This module provides access to the audaspace audio library.'''

AUD_DEVICE_JACK = int
AUD_DEVICE_NULL = int
AUD_DEVICE_OPENAL = int
AUD_DEVICE_SDL = int
AUD_DISTANCE_MODEL_EXPONENT = int
AUD_DISTANCE_MODEL_EXPONENT_CLAMPED = int
AUD_DISTANCE_MODEL_INVALID = int
AUD_DISTANCE_MODEL_INVERSE = int
AUD_DISTANCE_MODEL_INVERSE_CLAMPED = int
AUD_DISTANCE_MODEL_LINEAR = int
AUD_DISTANCE_MODEL_LINEAR_CLAMPED = int
AUD_FORMAT_FLOAT32 = int
AUD_FORMAT_FLOAT64 = int
AUD_FORMAT_INVALID = int
AUD_FORMAT_S16 = int
AUD_FORMAT_S24 = int
AUD_FORMAT_S32 = int
AUD_FORMAT_U8 = int
AUD_STATUS_INVALID = int
AUD_STATUS_PAUSED = int
AUD_STATUS_PLAYING = int
AUD_STATUS_STOPPED = int
class Device:
	'''Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.'''

	channels = getset_descriptor
	'''Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.'''

	distance_model = getset_descriptor
	'''Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.'''

	doppler_factor = getset_descriptor
	'''Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.'''

	format = getset_descriptor
	'''Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.'''

	listener_location = getset_descriptor
	'''Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.'''

	listener_orientation = getset_descriptor
	'''Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.'''

	listener_velocity = getset_descriptor
	'''Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.'''

	def lock(*argv):
		'''lock()

Locks the device so that it's guaranteed, that no samples are read from the streams until :meth:`unlock` is called.
This is useful if you want to do start/stop/pause/resume some sounds at the same time.

.. note:: The device has to be unlocked as often as locked to be able to continue playback.

.. warning:: Make sure the time between locking and unlocking is as short as possible to avoid clicks.'''

	def play(*argv):
		'''play(factory, keep=False)

Plays a factory.

:arg factory: The factory to play.
:type factory: :class:`Factory`
:arg keep: See :attr:`Handle.keep`.
:type keep: bool
:return: The playback handle with which playback can be controlled with.
:rtype: :class:`Handle`'''

	rate = getset_descriptor
	'''Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.'''

	speed_of_sound = getset_descriptor
	'''Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.'''

	def stopAll(*argv):
		'''stopAll()

Stops all playing and paused sounds.'''

	def unlock(*argv):
		'''unlock()

Unlocks the device after a lock call, see :meth:`lock` for details.'''

	volume = getset_descriptor
	'''Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.'''


class Factory:
	'''Factory objects are immutable and represent a sound that can be played simultaneously multiple times. They are called factories because they create reader objects internally that are used for playback.'''

	def buffer(*argv):
		'''buffer()

Buffers a factory into RAM.
This saves CPU usage needed for decoding and file access if the underlying factory reads from a file on the harddisk, but it consumes a lot of memory.

:return: The created :class:`Factory` object.
:rtype: :class:`Factory`

.. note:: Only known-length factories can be buffered.

.. warning:: Raw PCM data needs a lot of space, only buffer short factories.'''

	def delay(*argv):
		'''delay(time)

Delays by playing adding silence in front of the other factory's data.

:arg time: How many seconds of silence should be added before the factory.
:type time: float
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`'''

	def fadein(*argv):
		'''fadein(start, length)

Fades a factory in by raising the volume linearly in the given time interval.

:arg start: Time in seconds when the fading should start.
:type start: float
:arg length: Time in seconds how long the fading should last.
:type length: float
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`

.. note:: Before the fade starts it plays silence.'''

	def fadeout(*argv):
		'''fadeout(start, length)

Fades a factory in by lowering the volume linearly in the given time interval.

:arg start: Time in seconds when the fading should start.
:type start: float
:arg length: Time in seconds how long the fading should last.
:type length: float
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`

.. note:: After the fade this factory plays silence, so that the length of the factory is not altered.'''

	def file(*argv):
		'''file(filename)

Creates a factory object of a sound file.

:arg filename: Path of the file.
:type filename: string
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`

.. warning:: If the file doesn't exist or can't be read you will not get an exception immediately, but when you try to start playback of that factory.'''

	def filter(*argv):
		'''filter(b, a = (1))

Filters a factory with the supplied IIR filter coefficients.
Without the second parameter you'll get a FIR filter.
If the first value of the a sequence is 0 it will be set to 1 automatically.
If the first value of the a sequence is neither 0 nor 1, all filter coefficients will be scaled by this value so that it is 1 in the end, you don't have to scale yourself.

:arg b: The nominator filter coefficients.
:type b: sequence of float
:arg a: The denominator filter coefficients.
:type a: sequence of float
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`'''

	def highpass(*argv):
		'''highpass(frequency, Q=0.5)

Creates a second order highpass filter based on the transfer function H(s) = s^2 / (s^2 + s/Q + 1)

:arg frequency: The cut off trequency of the highpass.
:type frequency: float
:arg Q: Q factor of the lowpass.
:type Q: float
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`'''

	def join(*argv):
		'''join(factory)

Plays two factories in sequence.

:arg factory: The factory to play second.
:type factory: :class:`Factory`
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`

.. note:: The two factories have to have the same specifications (channels and samplerate).'''

	def limit(*argv):
		'''limit(start, end)

Limits a factory within a specific start and end time.

:arg start: Start time in seconds.
:type start: float
:arg end: End time in seconds.
:type end: float
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`'''

	def loop(*argv):
		'''loop(count)

Loops a factory.

:arg count: How often the factory should be looped. Negative values mean endlessly.
:type count: integer
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`

.. note:: This is a filter function, you might consider using :attr:`Handle.loop_count` instead.'''

	def lowpass(*argv):
		'''lowpass(frequency, Q=0.5)

Creates a second order lowpass filter based on the transfer function H(s) = 1 / (s^2 + s/Q + 1)

:arg frequency: The cut off trequency of the lowpass.
:type frequency: float
:arg Q: Q factor of the lowpass.
:type Q: float
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`'''

	def mix(*argv):
		'''mix(factory)

Mixes two factories.

:arg factory: The factory to mix over the other.
:type factory: :class:`Factory`
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`

.. note:: The two factories have to have the same specifications (channels and samplerate).'''

	def pingpong(*argv):
		'''pingpong()

Plays a factory forward and then backward.
This is like joining a factory with its reverse.

:return: The created :class:`Factory` object.
:rtype: :class:`Factory`'''

	def pitch(*argv):
		'''pitch(factor)

Changes the pitch of a factory with a specific factor.

:arg factor: The factor to change the pitch with.
:type factor: float
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`

.. note:: This is done by changing the sample rate of the underlying factory, which has to be an integer, so the factor value rounded and the factor may not be 100 % accurate.

.. note:: This is a filter function, you might consider using :attr:`Handle.pitch` instead.'''

	def reverse(*argv):
		'''reverse()

Plays a factory reversed.

:return: The created :class:`Factory` object.
:rtype: :class:`Factory`

.. note:: The factory has to have a finite length and has to be seekable. It's recommended to use this only with factories       with fast and accurate seeking, which is not true for encoded audio files, such ones should be buffered using :meth:`buffer` before being played reversed.

.. warning:: If seeking is not accurate in the underlying factory you'll likely hear skips/jumps/cracks.'''

	def sine(*argv):
		'''sine(frequency, rate=44100)

Creates a sine factory which plays a sine wave.

:arg frequency: The frequency of the sine wave in Hz.
:type frequency: float
:arg rate: The sampling rate in Hz. It's recommended to set this value to the playback device's samling rate to avoid resamping.
:type rate: int
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`'''

	def square(*argv):
		'''square(threshold = 0)

Makes a square wave out of an audio wave by setting all samples with a amplitude >= threshold to 1, all <= -threshold to -1 and all between to 0.

:arg threshold: Threshold value over which an amplitude counts non-zero.
:type threshold: float
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`'''

	def volume(*argv):
		'''volume(volume)

Changes the volume of a factory.

:arg volume: The new volume..
:type volume: float
:return: The created :class:`Factory` object.
:rtype: :class:`Factory`

.. note:: Should be in the range [0, 1] to avoid clipping.

.. note:: This is a filter function, you might consider using :attr:`Handle.volume` instead.'''


class Handle:
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	attenuation = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	cone_angle_inner = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	cone_angle_outer = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	cone_volume_outer = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	distance_maximum = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	distance_reference = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	keep = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	location = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	loop_count = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	orientation = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	def pause(*argv):
		'''pause()

Pauses playback.

:return: Whether the action succeeded.
:rtype: bool'''

	pitch = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	position = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	relative = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	def resume(*argv):
		'''resume()

Resumes playback.

:return: Whether the action succeeded.
:rtype: bool'''

	status = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	def stop(*argv):
		'''stop()

Stops playback.

:return: Whether the action succeeded.
:rtype: bool

.. note:: This makes the handle invalid.'''

	velocity = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	volume = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	volume_maximum = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''

	volume_minimum = getset_descriptor
	'''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.'''


def device(*argv):
	'''device()

Returns the application's :class:`Device`.

:return: The application's :class:`Device`.
:rtype: :class:`Device`'''

class error:
	args = getset_descriptor
	def with_traceback(*argv):
		'''Exception.with_traceback(tb) --
set self.__traceback__ to tb and return self.'''



