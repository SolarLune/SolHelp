'''This module provides access to blenders text drawing functions.'''

CLIPPING = int
KERNING_DEFAULT = int
ROTATION = int
SHADOW = int
def aspect(*argv):
	'''.. function:: aspect(fontid, aspect)

Set the aspect for drawing text.

:arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
:type fontid: int
:arg aspect: The aspect ratio for text drawing to use.
:type aspect: float'''

def blur(*argv):
	'''.. function:: blur(fontid, radius)

Set the blur radius for drawing text.

:arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
:type fontid: int
:arg radius: The radius for blurring text (in pixels).
:type radius: int'''

def clipping(*argv):
	'''.. function:: clipping(fontid, xmin, ymin, xmax, ymax)

Set the clipping, enable/disable using CLIPPING.

:arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
:type fontid: int
:arg xmin: Clip the drawing area by these bounds.
:type xmin: float
:arg ymin: Clip the drawing area by these bounds.
:type ymin: float
:arg xmax: Clip the drawing area by these bounds.
:type xmax: float
:arg ymax: Clip the drawing area by these bounds.
:type ymax: float'''

def dimensions(*argv):
	'''.. function:: dimensions(fontid, text)

Return the width and height of the text.

:arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
:type fontid: int
:arg text: the text to draw.
:type text: string
:return: the width and height of the text.
:rtype: tuple of 2 floats'''

def disable(*argv):
	'''.. function:: disable(fontid, option)

Disable option.

:arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
:type fontid: int
:arg option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT.
:type option: int'''

def draw(*argv):
	'''.. function:: draw(fontid, text)

Draw text in the current context.

:arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
:type fontid: int
:arg text: the text to draw.
:type text: string'''

def enable(*argv):
	'''.. function:: enable(fontid, option)

Enable option.

:arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
:type fontid: int
:arg option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT.
:type option: int'''

def load(*argv):
	'''.. function:: load(filename)

Load a new font.

:arg filename: the filename of the font.
:type filename: string
:return: the new font's fontid or -1 if there was an error.
:rtype: integer'''

def position(*argv):
	'''.. function:: position(fontid, x, y, z)

Set the position for drawing text.

:arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
:type fontid: int
:arg x: X axis position to draw the text.
:type x: float
:arg y: Y axis position to draw the text.
:type y: float
:arg z: Z axis position to draw the text.
:type z: float'''

def rotation(*argv):
	'''.. function:: rotation(fontid, angle)

Set the text rotation angle, enable/disable using ROTATION.

:arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
:type fontid: int
:arg angle: The angle for text drawing to use.
:type angle: float'''

def shadow(*argv):
	'''.. function:: shadow(fontid, level, r, g, b, a)

Shadow options, enable/disable using SHADOW .

:arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
:type fontid: int
:arg level: The blur level, can be 3, 5 or 0.
:type level: int
:arg r: Shadow color (red channel 0.0 - 1.0).
:type r: float
:arg g: Shadow color (green channel 0.0 - 1.0).
:type g: float
:arg b: Shadow color (blue channel 0.0 - 1.0).
:type b: float
:arg a: Shadow color (alpha channel 0.0 - 1.0).
:type a: float'''

def shadow_offset(*argv):
	'''.. function:: shadow_offset(fontid, x, y)

Set the offset for shadow text.

:arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
:type fontid: int
:arg x: Vertical shadow offset value in pixels.
:type x: float
:arg y: Horizontal shadow offset value in pixels.
:type y: float'''

def size(*argv):
	'''.. function:: size(fontid, size, dpi)

Set the size and dpi for drawing text.

:arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
:type fontid: int
:arg size: Point size of the font.
:type size: int
:arg dpi: dots per inch value to use for drawing.
:type dpi: int'''

def unload(*argv):
	'''.. function:: unload(filename)

Unload an existing font.

:arg filename: the filename of the font.
:type filename: string'''


