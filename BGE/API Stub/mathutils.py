'''This module provides access to matrices, eulers, quaternions and vectors.'''

class Color:
	'''This object gives access to Colors in Blender.'''

	b = getset_descriptor
	'''This object gives access to Colors in Blender.'''

	def copy(*argv):
		'''.. function:: copy()

Returns a copy of this color.

:return: A copy of the color.
:rtype: :class:`Color`

.. note:: use this to get a copy of a wrapped color with
   no reference to the original data.'''

	g = getset_descriptor
	'''This object gives access to Colors in Blender.'''

	h = getset_descriptor
	'''This object gives access to Colors in Blender.'''

	hsv = getset_descriptor
	'''This object gives access to Colors in Blender.'''

	is_wrapped = getset_descriptor
	'''This object gives access to Colors in Blender.'''

	owner = getset_descriptor
	'''This object gives access to Colors in Blender.'''

	r = getset_descriptor
	'''This object gives access to Colors in Blender.'''

	s = getset_descriptor
	'''This object gives access to Colors in Blender.'''

	v = getset_descriptor
	'''This object gives access to Colors in Blender.'''


class Euler:
	'''This object gives access to Eulers in Blender.'''

	def copy(*argv):
		'''.. function:: copy()

Returns a copy of this euler.

:return: A copy of the euler.
:rtype: :class:`Euler`

.. note:: use this to get a copy of a wrapped euler with
   no reference to the original data.'''

	is_wrapped = getset_descriptor
	'''This object gives access to Eulers in Blender.'''

	def make_compatible(*argv):
		'''.. method:: make_compatible(other)

Make this euler compatible with another,
so interpolating between them works as intended.

.. note:: the rotation order is not taken into account for this function.'''

	order = getset_descriptor
	'''This object gives access to Eulers in Blender.'''

	owner = getset_descriptor
	'''This object gives access to Eulers in Blender.'''

	def rotate(*argv):
		'''.. method:: rotate(other)

Rotates the euler a by another mathutils value.

:arg other: rotation component of mathutils value
:type other: :class:`Euler`, :class:`Quaternion` or :class:`Matrix`'''

	def rotate_axis(*argv):
		'''.. method:: rotate_axis(axis, angle)

Rotates the euler a certain amount and returning a unique euler rotation
(no 720 degree pitches).

:arg axis: single character in ['X, 'Y', 'Z'].
:type axis: string
:arg angle: angle in radians.
:type angle: float'''

	def to_matrix(*argv):
		'''.. method:: to_matrix()

Return a matrix representation of the euler.

:return: A 3x3 roation matrix representation of the euler.
:rtype: :class:`Matrix`'''

	def to_quaternion(*argv):
		'''.. method:: to_quaternion()

Return a quaternion representation of the euler.

:return: Quaternion representation of the euler.
:rtype: :class:`Quaternion`'''

	x = getset_descriptor
	'''This object gives access to Eulers in Blender.'''

	y = getset_descriptor
	'''This object gives access to Eulers in Blender.'''

	z = getset_descriptor
	'''This object gives access to Eulers in Blender.'''

	def zero(*argv):
		'''.. method:: zero()

Set all values to zero.'''


class Matrix:
	'''This object gives access to Matrices in Blender.'''

	def Identity(*argv):
		'''.. classmethod:: Identity(size)

Create an identity matrix.

:arg size: The size of the identity matrix to construct [2, 4].
:type size: int
:return: A new identity matrix.
:rtype: :class:`Matrix`'''

	def OrthoProjection(*argv):
		'''.. classmethod:: OrthoProjection(axis, size)

Create a matrix to represent an orthographic projection.

:arg axis: Can be any of the following: ['X', 'Y', 'XY', 'XZ', 'YZ'],
   where a single axis is for a 2D matrix.
   Or a vector for an arbitrary axis
:type axis: string or :class:`Vector`
:arg size: The size of the projection matrix to construct [2, 4].
:type size: int
:return: A new projection matrix.
:rtype: :class:`Matrix`'''

	def Rotation(*argv):
		'''.. classmethod:: Rotation(angle, size, axis)

Create a matrix representing a rotation.

:arg angle: The angle of rotation desired, in radians.
:type angle: float
:arg size: The size of the rotation matrix to construct [2, 4].
:type size: int
:arg axis: a string in ['X', 'Y', 'Z'] or a 3D Vector Object
   (optional when size is 2).
:type axis: string or :class:`Vector`
:return: A new rotation matrix.
:rtype: :class:`Matrix`'''

	def Scale(*argv):
		'''.. classmethod:: Scale(factor, size, axis)

Create a matrix representing a scaling.

:arg factor: The factor of scaling to apply.
:type factor: float
:arg size: The size of the scale matrix to construct [2, 4].
:type size: int
:arg axis: Direction to influence scale. (optional).
:type axis: :class:`Vector`
:return: A new scale matrix.
:rtype: :class:`Matrix`'''

	def Shear(*argv):
		'''.. classmethod:: Shear(plane, size, factor)

Create a matrix to represent an shear transformation.

:arg plane: Can be any of the following: ['X', 'Y', 'XY', 'XZ', 'YZ'],
   where a single axis is for a 2D matrix only.
:type plane: string
:arg size: The size of the shear matrix to construct [2, 4].
:type size: int
:arg factor: The factor of shear to apply. For a 3 or 4 *size* matrix
   pass a pair of floats corresponding with the *plane* axis.
:type factor: float or float pair
:return: A new shear matrix.
:rtype: :class:`Matrix`'''

	def Translation(*argv):
		'''.. classmethod:: Translation(vector)

Create a matrix representing a translation.

:arg vector: The translation vector.
:type vector: :class:`Vector`
:return: An identity matrix with a translation.
:rtype: :class:`Matrix`'''

	def adjugate(*argv):
		'''.. method:: adjugate()

Set the matrix to its adjugate.

.. note:: When the matrix cant be adjugated a :exc:`ValueError` exception is raised.

.. seealso:: <http://en.wikipedia.org/wiki/Adjugate_matrix>'''

	def adjugated(*argv):
		'''.. method:: adjugated()

Return an adjugated copy of the matrix.

:return: the adjugated matrix.
:rtype: :class:`Matrix`

.. note:: When the matrix cant be adjugated a :exc:`ValueError` exception is raised.'''

	col = getset_descriptor
	'''This object gives access to Matrices in Blender.'''

	def copy(*argv):
		'''.. method:: copy()

Returns a copy of this matrix.

:return: an instance of itself
:rtype: :class:`Matrix`'''

	def decompose(*argv):
		'''.. method:: decompose()

Return the location, rotation and scale components of this matrix.

:return: loc, rot, scale triple.
:rtype: (:class:`Vector`, :class:`Quaternion`, :class:`Vector`)'''

	def determinant(*argv):
		'''.. method:: determinant()

Return the determinant of a matrix.

:return: Return a the determinant of a matrix.
:rtype: float

.. seealso:: <http://en.wikipedia.org/wiki/Determinant>'''

	def identity(*argv):
		'''.. method:: identity()

Set the matrix to the identity matrix.

.. note:: An object with zero location and rotation, a scale of one,
   will have an identity matrix.

.. seealso:: <http://en.wikipedia.org/wiki/Identity_matrix>'''

	def invert(*argv):
		'''.. method:: invert()

Set the matrix to its inverse.

.. note:: When the matrix cant be inverted a :exc:`ValueError` exception is raised.

.. seealso:: <http://en.wikipedia.org/wiki/Inverse_matrix>'''

	def inverted(*argv):
		'''.. method:: inverted()

Return an inverted copy of the matrix.

:return: the inverted matrix.
:rtype: :class:`Matrix`

.. note:: When the matrix cant be inverted a :exc:`ValueError` exception is raised.'''

	is_negative = getset_descriptor
	'''This object gives access to Matrices in Blender.'''

	is_orthogonal = getset_descriptor
	'''This object gives access to Matrices in Blender.'''

	is_orthogonal_axis_vectors = getset_descriptor
	'''This object gives access to Matrices in Blender.'''

	is_wrapped = getset_descriptor
	'''This object gives access to Matrices in Blender.'''

	def lerp(*argv):
		'''.. function:: lerp(other, factor)

Returns the interpolation of two matrices.

:arg other: value to interpolate with.
:type other: :class:`Matrix`
:arg factor: The interpolation value in [0.0, 1.0].
:type factor: float
:return: The interpolated matrix.
:rtype: :class:`Matrix`'''

	median_scale = getset_descriptor
	'''This object gives access to Matrices in Blender.'''

	def normalize(*argv):
		'''.. method:: normalize()

Normalize each of the matrix columns.'''

	def normalized(*argv):
		'''.. method:: normalized()

Return a column normalized matrix

:return: a column normalized matrix
:rtype: :class:`Matrix`'''

	owner = getset_descriptor
	'''This object gives access to Matrices in Blender.'''

	def resize_4x4(*argv):
		'''.. method:: resize_4x4()

Resize the matrix to 4x4.'''

	def rotate(*argv):
		'''.. method:: rotate(other)

Rotates the matrix a by another mathutils value.

:arg other: rotation component of mathutils value
:type other: :class:`Euler`, :class:`Quaternion` or :class:`Matrix`

.. note:: If any of the columns are not unit length this may not have desired results.'''

	row = getset_descriptor
	'''This object gives access to Matrices in Blender.'''

	def to_3x3(*argv):
		'''.. method:: to_3x3()

Return a 3x3 copy of this matrix.

:return: a new matrix.
:rtype: :class:`Matrix`'''

	def to_4x4(*argv):
		'''.. method:: to_4x4()

Return a 4x4 copy of this matrix.

:return: a new matrix.
:rtype: :class:`Matrix`'''

	def to_euler(*argv):
		'''.. method:: to_euler(order, euler_compat)

Return an Euler representation of the rotation matrix
(3x3 or 4x4 matrix only).

:arg order: Optional rotation order argument in
   ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
:type order: string
:arg euler_compat: Optional euler argument the new euler will be made
   compatible with (no axis flipping between them).
   Useful for converting a series of matrices to animation curves.
:type euler_compat: :class:`Euler`
:return: Euler representation of the matrix.
:rtype: :class:`Euler`'''

	def to_quaternion(*argv):
		'''.. method:: to_quaternion()

Return a quaternion representation of the rotation matrix.

:return: Quaternion representation of the rotation matrix.
:rtype: :class:`Quaternion`'''

	def to_scale(*argv):
		'''.. method:: to_scale()

Return a the scale part of a 3x3 or 4x4 matrix.

:return: Return a the scale of a matrix.
:rtype: :class:`Vector`

.. note:: This method does not return negative a scale on any axis because it is not possible to obtain this data from the matrix alone.'''

	def to_translation(*argv):
		'''.. method:: to_translation()

Return a the translation part of a 4 row matrix.

:return: Return a the translation of a matrix.
:rtype: :class:`Vector`'''

	translation = getset_descriptor
	'''This object gives access to Matrices in Blender.'''

	def transpose(*argv):
		'''.. method:: transpose()

Set the matrix to its transpose.

.. seealso:: <http://en.wikipedia.org/wiki/Transpose>'''

	def transposed(*argv):
		'''.. method:: transposed()

Return a new, transposed matrix.

:return: a transposed matrix
:rtype: :class:`Matrix`'''

	def zero(*argv):
		'''.. method:: zero()

Set all the matrix values to zero.

:return: an instance of itself
:rtype: :class:`Matrix`'''


class Quaternion:
	'''This object gives access to Quaternions in Blender.'''

	angle = getset_descriptor
	'''This object gives access to Quaternions in Blender.'''

	axis = getset_descriptor
	'''This object gives access to Quaternions in Blender.'''

	def conjugate(*argv):
		'''.. function:: conjugate()

Set the quaternion to its conjugate (negate x, y, z).'''

	def conjugated(*argv):
		'''.. function:: conjugated()

Return a new conjugated quaternion.

:return: a new quaternion.
:rtype: :class:`Quaternion`'''

	def copy(*argv):
		'''.. function:: copy()

Returns a copy of this quaternion.

:return: A copy of the quaternion.
:rtype: :class:`Quaternion`

.. note:: use this to get a copy of a wrapped quaternion with
   no reference to the original data.'''

	def cross(*argv):
		'''.. method:: cross(other)

Return the cross product of this quaternion and another.

:arg other: The other quaternion to perform the cross product with.
:type other: :class:`Quaternion`
:return: The cross product.
:rtype: :class:`Quaternion`'''

	def dot(*argv):
		'''.. method:: dot(other)

Return the dot product of this quaternion and another.

:arg other: The other quaternion to perform the dot product with.
:type other: :class:`Quaternion`
:return: The dot product.
:rtype: :class:`Quaternion`'''

	def identity(*argv):
		'''.. function:: identity()

Set the quaternion to an identity quaternion.

:return: an instance of itself.
:rtype: :class:`Quaternion`'''

	def invert(*argv):
		'''.. function:: invert()

Set the quaternion to its inverse.'''

	def inverted(*argv):
		'''.. function:: inverted()

Return a new, inverted quaternion.

:return: the inverted value.
:rtype: :class:`Quaternion`'''

	is_wrapped = getset_descriptor
	'''This object gives access to Quaternions in Blender.'''

	magnitude = getset_descriptor
	'''This object gives access to Quaternions in Blender.'''

	def negate(*argv):
		'''.. function:: negate()

Set the quaternion to its negative.

:return: an instance of itself.
:rtype: :class:`Quaternion`'''

	def normalize(*argv):
		'''.. function:: normalize()

Normalize the quaternion.'''

	def normalized(*argv):
		'''.. function:: normalized()

Return a new normalized quaternion.

:return: a normalized copy.
:rtype: :class:`Quaternion`'''

	owner = getset_descriptor
	'''This object gives access to Quaternions in Blender.'''

	def rotate(*argv):
		'''.. method:: rotate(other)

Rotates the quaternion a by another mathutils value.

:arg other: rotation component of mathutils value
:type other: :class:`Euler`, :class:`Quaternion` or :class:`Matrix`'''

	def rotation_difference(*argv):
		'''.. function:: rotation_difference(other)

Returns a quaternion representing the rotational difference.

:arg other: second quaternion.
:type other: :class:`Quaternion`
:return: the rotational difference between the two quat rotations.
:rtype: :class:`Quaternion`'''

	def slerp(*argv):
		'''.. function:: slerp(other, factor)

Returns the interpolation of two quaternions.

:arg other: value to interpolate with.
:type other: :class:`Quaternion`
:arg factor: The interpolation value in [0.0, 1.0].
:type factor: float
:return: The interpolated rotation.
:rtype: :class:`Quaternion`'''

	def to_axis_angle(*argv):
		'''.. method:: to_axis_angle()

Return the axis, angle representation of the quaternion.

:return: axis, angle.
:rtype: (:class:`Vector`, float) pair'''

	def to_euler(*argv):
		'''.. method:: to_euler(order, euler_compat)

Return Euler representation of the quaternion.

:arg order: Optional rotation order argument in
   ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
:type order: string
:arg euler_compat: Optional euler argument the new euler will be made
   compatible with (no axis flipping between them).
   Useful for converting a series of matrices to animation curves.
:type euler_compat: :class:`Euler`
:return: Euler representation of the quaternion.
:rtype: :class:`Euler`'''

	def to_matrix(*argv):
		'''.. method:: to_matrix()

Return a matrix representation of the quaternion.

:return: A 3x3 rotation matrix representation of the quaternion.
:rtype: :class:`Matrix`'''

	w = getset_descriptor
	'''This object gives access to Quaternions in Blender.'''

	x = getset_descriptor
	'''This object gives access to Quaternions in Blender.'''

	y = getset_descriptor
	'''This object gives access to Quaternions in Blender.'''

	z = getset_descriptor
	'''This object gives access to Quaternions in Blender.'''


class Vector:
	'''This object gives access to Vectors in Blender.'''

	def Fill(*argv):
		'''.. classmethod:: Fill(size, fill=0.0)

Create a vector of length size with all values set to fill.

:arg size: The length of the vector to be created.
:type size: int
:arg fill: The value used to fill the vector.
:type fill: float'''

	def Linspace(*argv):
		'''.. classmethod:: Linspace(start, stop, size)

Create a vector of the specified size which is filled with linearly spaced values between start and stop values.

:arg start: The start of the range used to fill the vector.
:type start: int
:arg stop: The end of the range used to fill the vector.
:type stop: int
:arg size: The size of the vector to be created.
:type size: int'''

	def Range(*argv):
		'''.. classmethod:: Range(start=0, stop, step=1)

Create a filled with a range of values.

:arg start: The start of the range used to fill the vector.
:type start: int
:arg stop: The end of the range used to fill the vector.
:type stop: int
:arg step: The step between successive values in the vector.
:type step: int'''

	def Repeat(*argv):
		'''.. classmethod:: Repeat(vector, size)

Create a vector by repeating the values in vector until the required size is reached.

:arg tuple: The vector to draw values from.
:type tuple: :class:`mathutils.Vector`
:arg size: The size of the vector to be created.
:type size: int'''

	def angle(*argv):
		'''.. function:: angle(other, fallback)

Return the angle between two vectors.

:arg other: another vector to compare the angle with
:type other: :class:`Vector`
:arg fallback: return this value when the angle cant be calculated
   (zero length vector)
:type fallback: any
:return: angle in radians or fallback when given
:rtype: float

.. note:: Zero length vectors raise an :exc:`ValueError`.'''

	def angle_signed(*argv):
		'''.. function:: angle_signed(other, fallback)

Return the signed angle between two 2D vectors (clockwise is positive).

:arg other: another vector to compare the angle with
:type other: :class:`Vector`
:arg fallback: return this value when the angle cant be calculated
   (zero length vector)
:type fallback: any
:return: angle in radians or fallback when given
:rtype: float

.. note:: Zero length vectors raise an :exc:`ValueError`.'''

	def copy(*argv):
		'''.. function:: copy()

Returns a copy of this vector.

:return: A copy of the vector.
:rtype: :class:`Vector`

.. note:: use this to get a copy of a wrapped vector with
   no reference to the original data.'''

	def cross(*argv):
		'''.. method:: cross(other)

Return the cross product of this vector and another.

:arg other: The other vector to perform the cross product with.
:type other: :class:`Vector`
:return: The cross product.
:rtype: :class:`Vector`

.. note:: both vectors must be 3D'''

	def dot(*argv):
		'''.. method:: dot(other)

Return the dot product of this vector and another.

:arg other: The other vector to perform the dot product with.
:type other: :class:`Vector`
:return: The dot product.
:rtype: :class:`Vector`'''

	is_wrapped = getset_descriptor
	'''This object gives access to Vectors in Blender.'''

	length = getset_descriptor
	'''This object gives access to Vectors in Blender.'''

	length_squared = getset_descriptor
	'''This object gives access to Vectors in Blender.'''

	def lerp(*argv):
		'''.. function:: lerp(other, factor)

Returns the interpolation of two vectors.

:arg other: value to interpolate with.
:type other: :class:`Vector`
:arg factor: The interpolation value in [0.0, 1.0].
:type factor: float
:return: The interpolated vector.
:rtype: :class:`Vector`'''

	magnitude = getset_descriptor
	'''This object gives access to Vectors in Blender.'''

	def negate(*argv):
		'''.. method:: negate()

Set all values to their negative.'''

	def normalize(*argv):
		'''.. method:: normalize()

Normalize the vector, making the length of the vector always 1.0.

.. warning:: Normalizing a vector where all values are zero has no effect.

.. note:: Normalize works for vectors of all sizes,
   however 4D Vectors w axis is left untouched.'''

	def normalized(*argv):
		'''.. method:: normalized()

Return a new, normalized vector.

:return: a normalized copy of the vector
:rtype: :class:`Vector`'''

	owner = getset_descriptor
	'''This object gives access to Vectors in Blender.'''

	def project(*argv):
		'''.. function:: project(other)

Return the projection of this vector onto the *other*.

:arg other: second vector.
:type other: :class:`Vector`
:return: the parallel projection vector
:rtype: :class:`Vector`'''

	def reflect(*argv):
		'''.. method:: reflect(mirror)

Return the reflection vector from the *mirror* argument.

:arg mirror: This vector could be a normal from the reflecting surface.
:type mirror: :class:`Vector`
:return: The reflected vector matching the size of this vector.
:rtype: :class:`Vector`'''

	def resize(*argv):
		'''.. method:: resize(size=3)

Resize the vector to have size number of elements.'''

	def resize_2d(*argv):
		'''.. method:: resize_2d()

Resize the vector to 2D  (x, y).'''

	def resize_3d(*argv):
		'''.. method:: resize_3d()

Resize the vector to 3D  (x, y, z).'''

	def resize_4d(*argv):
		'''.. method:: resize_4d()

Resize the vector to 4D (x, y, z, w).'''

	def resized(*argv):
		'''.. method:: resized(size=3)

Return a resized copy of the vector with size number of elements.

:return: a new vector
:rtype: :class:`Vector`'''

	def rotate(*argv):
		'''.. function:: rotate(other)

Rotate the vector by a rotation value.

:arg other: rotation component of mathutils value
:type other: :class:`Euler`, :class:`Quaternion` or :class:`Matrix`'''

	def rotation_difference(*argv):
		'''.. function:: rotation_difference(other)

Returns a quaternion representing the rotational difference between this
vector and another.

:arg other: second vector.
:type other: :class:`Vector`
:return: the rotational difference between the two vectors.
:rtype: :class:`Quaternion`

.. note:: 2D vectors raise an :exc:`AttributeError`.'''

	def to_2d(*argv):
		'''.. method:: to_2d()

Return a 2d copy of the vector.

:return: a new vector
:rtype: :class:`Vector`'''

	def to_3d(*argv):
		'''.. method:: to_3d()

Return a 3d copy of the vector.

:return: a new vector
:rtype: :class:`Vector`'''

	def to_4d(*argv):
		'''.. method:: to_4d()

Return a 4d copy of the vector.

:return: a new vector
:rtype: :class:`Vector`'''

	def to_track_quat(*argv):
		'''.. method:: to_track_quat(track, up)

Return a quaternion rotation from the vector and the track and up axis.

:arg track: Track axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z'].
:type track: string
:arg up: Up axis in ['X', 'Y', 'Z'].
:type up: string
:return: rotation from the vector and the track and up axis.
:rtype: :class:`Quaternion`'''

	def to_tuple(*argv):
		'''.. method:: to_tuple(precision=-1)

Return this vector as a tuple with.

:arg precision: The number to round the value to in [-1, 21].
:type precision: int
:return: the values of the vector rounded by *precision*
:rtype: tuple'''

	w = getset_descriptor
	'''This object gives access to Vectors in Blender.'''

	ww = getset_descriptor
	www = getset_descriptor
	wwww = getset_descriptor
	wwwx = getset_descriptor
	wwwy = getset_descriptor
	wwwz = getset_descriptor
	wwx = getset_descriptor
	wwxw = getset_descriptor
	wwxx = getset_descriptor
	wwxy = getset_descriptor
	wwxz = getset_descriptor
	wwy = getset_descriptor
	wwyw = getset_descriptor
	wwyx = getset_descriptor
	wwyy = getset_descriptor
	wwyz = getset_descriptor
	wwz = getset_descriptor
	wwzw = getset_descriptor
	wwzx = getset_descriptor
	wwzy = getset_descriptor
	wwzz = getset_descriptor
	wx = getset_descriptor
	wxw = getset_descriptor
	wxww = getset_descriptor
	wxwx = getset_descriptor
	wxwy = getset_descriptor
	wxwz = getset_descriptor
	wxx = getset_descriptor
	wxxw = getset_descriptor
	wxxx = getset_descriptor
	wxxy = getset_descriptor
	wxxz = getset_descriptor
	wxy = getset_descriptor
	wxyw = getset_descriptor
	wxyx = getset_descriptor
	wxyy = getset_descriptor
	wxyz = getset_descriptor
	wxz = getset_descriptor
	wxzw = getset_descriptor
	wxzx = getset_descriptor
	wxzy = getset_descriptor
	wxzz = getset_descriptor
	wy = getset_descriptor
	wyw = getset_descriptor
	wyww = getset_descriptor
	wywx = getset_descriptor
	wywy = getset_descriptor
	wywz = getset_descriptor
	wyx = getset_descriptor
	wyxw = getset_descriptor
	wyxx = getset_descriptor
	wyxy = getset_descriptor
	wyxz = getset_descriptor
	wyy = getset_descriptor
	wyyw = getset_descriptor
	wyyx = getset_descriptor
	wyyy = getset_descriptor
	wyyz = getset_descriptor
	wyz = getset_descriptor
	wyzw = getset_descriptor
	wyzx = getset_descriptor
	wyzy = getset_descriptor
	wyzz = getset_descriptor
	wz = getset_descriptor
	wzw = getset_descriptor
	wzww = getset_descriptor
	wzwx = getset_descriptor
	wzwy = getset_descriptor
	wzwz = getset_descriptor
	wzx = getset_descriptor
	wzxw = getset_descriptor
	wzxx = getset_descriptor
	wzxy = getset_descriptor
	wzxz = getset_descriptor
	wzy = getset_descriptor
	wzyw = getset_descriptor
	wzyx = getset_descriptor
	wzyy = getset_descriptor
	wzyz = getset_descriptor
	wzz = getset_descriptor
	wzzw = getset_descriptor
	wzzx = getset_descriptor
	wzzy = getset_descriptor
	wzzz = getset_descriptor
	x = getset_descriptor
	'''This object gives access to Vectors in Blender.'''

	xw = getset_descriptor
	xww = getset_descriptor
	xwww = getset_descriptor
	xwwx = getset_descriptor
	xwwy = getset_descriptor
	xwwz = getset_descriptor
	xwx = getset_descriptor
	xwxw = getset_descriptor
	xwxx = getset_descriptor
	xwxy = getset_descriptor
	xwxz = getset_descriptor
	xwy = getset_descriptor
	xwyw = getset_descriptor
	xwyx = getset_descriptor
	xwyy = getset_descriptor
	xwyz = getset_descriptor
	xwz = getset_descriptor
	xwzw = getset_descriptor
	xwzx = getset_descriptor
	xwzy = getset_descriptor
	xwzz = getset_descriptor
	xx = getset_descriptor
	xxw = getset_descriptor
	xxww = getset_descriptor
	xxwx = getset_descriptor
	xxwy = getset_descriptor
	xxwz = getset_descriptor
	xxx = getset_descriptor
	xxxw = getset_descriptor
	xxxx = getset_descriptor
	xxxy = getset_descriptor
	xxxz = getset_descriptor
	xxy = getset_descriptor
	xxyw = getset_descriptor
	xxyx = getset_descriptor
	xxyy = getset_descriptor
	xxyz = getset_descriptor
	xxz = getset_descriptor
	xxzw = getset_descriptor
	xxzx = getset_descriptor
	xxzy = getset_descriptor
	xxzz = getset_descriptor
	xy = getset_descriptor
	xyw = getset_descriptor
	xyww = getset_descriptor
	xywx = getset_descriptor
	xywy = getset_descriptor
	xywz = getset_descriptor
	xyx = getset_descriptor
	xyxw = getset_descriptor
	xyxx = getset_descriptor
	xyxy = getset_descriptor
	xyxz = getset_descriptor
	xyy = getset_descriptor
	xyyw = getset_descriptor
	xyyx = getset_descriptor
	xyyy = getset_descriptor
	xyyz = getset_descriptor
	xyz = getset_descriptor
	xyzw = getset_descriptor
	xyzx = getset_descriptor
	xyzy = getset_descriptor
	xyzz = getset_descriptor
	xz = getset_descriptor
	xzw = getset_descriptor
	xzww = getset_descriptor
	xzwx = getset_descriptor
	xzwy = getset_descriptor
	xzwz = getset_descriptor
	xzx = getset_descriptor
	xzxw = getset_descriptor
	xzxx = getset_descriptor
	xzxy = getset_descriptor
	xzxz = getset_descriptor
	xzy = getset_descriptor
	xzyw = getset_descriptor
	xzyx = getset_descriptor
	xzyy = getset_descriptor
	xzyz = getset_descriptor
	xzz = getset_descriptor
	xzzw = getset_descriptor
	xzzx = getset_descriptor
	xzzy = getset_descriptor
	xzzz = getset_descriptor
	y = getset_descriptor
	'''This object gives access to Vectors in Blender.'''

	yw = getset_descriptor
	yww = getset_descriptor
	ywww = getset_descriptor
	ywwx = getset_descriptor
	ywwy = getset_descriptor
	ywwz = getset_descriptor
	ywx = getset_descriptor
	ywxw = getset_descriptor
	ywxx = getset_descriptor
	ywxy = getset_descriptor
	ywxz = getset_descriptor
	ywy = getset_descriptor
	ywyw = getset_descriptor
	ywyx = getset_descriptor
	ywyy = getset_descriptor
	ywyz = getset_descriptor
	ywz = getset_descriptor
	ywzw = getset_descriptor
	ywzx = getset_descriptor
	ywzy = getset_descriptor
	ywzz = getset_descriptor
	yx = getset_descriptor
	yxw = getset_descriptor
	yxww = getset_descriptor
	yxwx = getset_descriptor
	yxwy = getset_descriptor
	yxwz = getset_descriptor
	yxx = getset_descriptor
	yxxw = getset_descriptor
	yxxx = getset_descriptor
	yxxy = getset_descriptor
	yxxz = getset_descriptor
	yxy = getset_descriptor
	yxyw = getset_descriptor
	yxyx = getset_descriptor
	yxyy = getset_descriptor
	yxyz = getset_descriptor
	yxz = getset_descriptor
	yxzw = getset_descriptor
	yxzx = getset_descriptor
	yxzy = getset_descriptor
	yxzz = getset_descriptor
	yy = getset_descriptor
	yyw = getset_descriptor
	yyww = getset_descriptor
	yywx = getset_descriptor
	yywy = getset_descriptor
	yywz = getset_descriptor
	yyx = getset_descriptor
	yyxw = getset_descriptor
	yyxx = getset_descriptor
	yyxy = getset_descriptor
	yyxz = getset_descriptor
	yyy = getset_descriptor
	yyyw = getset_descriptor
	yyyx = getset_descriptor
	yyyy = getset_descriptor
	yyyz = getset_descriptor
	yyz = getset_descriptor
	yyzw = getset_descriptor
	yyzx = getset_descriptor
	yyzy = getset_descriptor
	yyzz = getset_descriptor
	yz = getset_descriptor
	yzw = getset_descriptor
	yzww = getset_descriptor
	yzwx = getset_descriptor
	yzwy = getset_descriptor
	yzwz = getset_descriptor
	yzx = getset_descriptor
	yzxw = getset_descriptor
	yzxx = getset_descriptor
	yzxy = getset_descriptor
	yzxz = getset_descriptor
	yzy = getset_descriptor
	yzyw = getset_descriptor
	yzyx = getset_descriptor
	yzyy = getset_descriptor
	yzyz = getset_descriptor
	yzz = getset_descriptor
	yzzw = getset_descriptor
	yzzx = getset_descriptor
	yzzy = getset_descriptor
	yzzz = getset_descriptor
	z = getset_descriptor
	'''This object gives access to Vectors in Blender.'''

	def zero(*argv):
		'''.. method:: zero()

Set all values to zero.'''

	zw = getset_descriptor
	zww = getset_descriptor
	zwww = getset_descriptor
	zwwx = getset_descriptor
	zwwy = getset_descriptor
	zwwz = getset_descriptor
	zwx = getset_descriptor
	zwxw = getset_descriptor
	zwxx = getset_descriptor
	zwxy = getset_descriptor
	zwxz = getset_descriptor
	zwy = getset_descriptor
	zwyw = getset_descriptor
	zwyx = getset_descriptor
	zwyy = getset_descriptor
	zwyz = getset_descriptor
	zwz = getset_descriptor
	zwzw = getset_descriptor
	zwzx = getset_descriptor
	zwzy = getset_descriptor
	zwzz = getset_descriptor
	zx = getset_descriptor
	zxw = getset_descriptor
	zxww = getset_descriptor
	zxwx = getset_descriptor
	zxwy = getset_descriptor
	zxwz = getset_descriptor
	zxx = getset_descriptor
	zxxw = getset_descriptor
	zxxx = getset_descriptor
	zxxy = getset_descriptor
	zxxz = getset_descriptor
	zxy = getset_descriptor
	zxyw = getset_descriptor
	zxyx = getset_descriptor
	zxyy = getset_descriptor
	zxyz = getset_descriptor
	zxz = getset_descriptor
	zxzw = getset_descriptor
	zxzx = getset_descriptor
	zxzy = getset_descriptor
	zxzz = getset_descriptor
	zy = getset_descriptor
	zyw = getset_descriptor
	zyww = getset_descriptor
	zywx = getset_descriptor
	zywy = getset_descriptor
	zywz = getset_descriptor
	zyx = getset_descriptor
	zyxw = getset_descriptor
	zyxx = getset_descriptor
	zyxy = getset_descriptor
	zyxz = getset_descriptor
	zyy = getset_descriptor
	zyyw = getset_descriptor
	zyyx = getset_descriptor
	zyyy = getset_descriptor
	zyyz = getset_descriptor
	zyz = getset_descriptor
	zyzw = getset_descriptor
	zyzx = getset_descriptor
	zyzy = getset_descriptor
	zyzz = getset_descriptor
	zz = getset_descriptor
	zzw = getset_descriptor
	zzww = getset_descriptor
	zzwx = getset_descriptor
	zzwy = getset_descriptor
	zzwz = getset_descriptor
	zzx = getset_descriptor
	zzxw = getset_descriptor
	zzxx = getset_descriptor
	zzxy = getset_descriptor
	zzxz = getset_descriptor
	zzy = getset_descriptor
	zzyw = getset_descriptor
	zzyx = getset_descriptor
	zzyy = getset_descriptor
	zzyz = getset_descriptor
	zzz = getset_descriptor
	zzzw = getset_descriptor
	zzzx = getset_descriptor
	zzzy = getset_descriptor
	zzzz = getset_descriptor

class geometry:
	'''The Blender geometry module'''

	def area_tri(*argv):
		'''.. function:: area_tri(v1, v2, v3)

Returns the area size of the 2D or 3D triangle defined.

:arg v1: Point1
:type v1: :class:`mathutils.Vector`
:arg v2: Point2
:type v2: :class:`mathutils.Vector`
:arg v3: Point3
:type v3: :class:`mathutils.Vector`
:rtype: float'''

	def barycentric_transform(*argv):
		'''.. function:: barycentric_transform(point, tri_a1, tri_a2, tri_a3, tri_b1, tri_b2, tri_b3)

Return a transformed point, the transformation is defined by 2 triangles.

:arg point: The point to transform.
:type point: :class:`mathutils.Vector`
:arg tri_a1: source triangle vertex.
:type tri_a1: :class:`mathutils.Vector`
:arg tri_a2: source triangle vertex.
:type tri_a2: :class:`mathutils.Vector`
:arg tri_a3: source triangle vertex.
:type tri_a3: :class:`mathutils.Vector`
:arg tri_a1: target triangle vertex.
:type tri_a1: :class:`mathutils.Vector`
:arg tri_a2: target triangle vertex.
:type tri_a2: :class:`mathutils.Vector`
:arg tri_a3: target triangle vertex.
:type tri_a3: :class:`mathutils.Vector`
:return: The transformed point
:rtype: :class:`mathutils.Vector`'s'''

	def box_fit_2d(*argv):
		'''.. function:: box_fit_2d(points)

Returns an angle that best fits the points to an axis aligned rectangle

:arg points: list of 2d points.
:type points: list
:return: angle
:rtype: float'''

	def box_pack_2d(*argv):
		'''.. function:: box_pack_2d(boxes)

Returns the normal of the 3D tri or quad.

:arg boxes: list of boxes, each box is a list where the first 4 items are [x, y, width, height, ...] other items are ignored.
:type boxes: list
:return: the width and height of the packed bounding box
:rtype: tuple, pair of floats'''

	def convex_hull_2d(*argv):
		'''.. function:: convex_hull_2d(points)

Returns a list of indices into the list given

:arg points: list of 2d points.
:type points: list
:return: a list of indices
:rtype: list of ints'''

	def distance_point_to_plane(*argv):
		'''.. function:: distance_point_to_plane(pt, plane_co, plane_no)

Returns the signed distance between a point and a plane    (negative when below the normal).

:arg pt: Point
:type pt: :class:`mathutils.Vector`
:arg plane_co: A point on the plane
:type plane_co: :class:`mathutils.Vector`
:arg plane_no: The direction the plane is facing
:type plane_no: :class:`mathutils.Vector`
:rtype: float'''

	def interpolate_bezier(*argv):
		'''.. function:: interpolate_bezier(knot1, handle1, handle2, knot2, resolution)

Interpolate a bezier spline segment.

:arg knot1: First bezier spline point.
:type knot1: :class:`mathutils.Vector`
:arg handle1: First bezier spline handle.
:type handle1: :class:`mathutils.Vector`
:arg handle2: Second bezier spline handle.
:type handle2: :class:`mathutils.Vector`
:arg knot2: Second bezier spline point.
:type knot2: :class:`mathutils.Vector`
:arg resolution: Number of points to return.
:type resolution: int
:return: The interpolated points
:rtype: list of :class:`mathutils.Vector`'s'''

	def intersect_line_line(*argv):
		'''.. function:: intersect_line_line(v1, v2, v3, v4)

Returns a tuple with the points on each line respectively closest to the other.

:arg v1: First point of the first line
:type v1: :class:`mathutils.Vector`
:arg v2: Second point of the first line
:type v2: :class:`mathutils.Vector`
:arg v3: First point of the second line
:type v3: :class:`mathutils.Vector`
:arg v4: Second point of the second line
:type v4: :class:`mathutils.Vector`
:rtype: tuple of :class:`mathutils.Vector`'s'''

	def intersect_line_line_2d(*argv):
		'''.. function:: intersect_line_line_2d(lineA_p1, lineA_p2, lineB_p1, lineB_p2)

Takes 2 lines (as 4 vectors) and returns a vector for their point of intersection or None.

:arg lineA_p1: First point of the first line
:type lineA_p1: :class:`mathutils.Vector`
:arg lineA_p2: Second point of the first line
:type lineA_p2: :class:`mathutils.Vector`
:arg lineB_p1: First point of the second line
:type lineB_p1: :class:`mathutils.Vector`
:arg lineB_p2: Second point of the second line
:type lineB_p2: :class:`mathutils.Vector`
:return: The point of intersection or None when not found
:rtype: :class:`mathutils.Vector` or None'''

	def intersect_line_plane(*argv):
		'''.. function:: intersect_line_plane(line_a, line_b, plane_co, plane_no, no_flip=False)

Calculate the intersection between a line (as 2 vectors) and a plane.
Returns a vector for the intersection or None.

:arg line_a: First point of the first line
:type line_a: :class:`mathutils.Vector`
:arg line_b: Second point of the first line
:type line_b: :class:`mathutils.Vector`
:arg plane_co: A point on the plane
:type plane_co: :class:`mathutils.Vector`
:arg plane_no: The direction the plane is facing
:type plane_no: :class:`mathutils.Vector`
:return: The point of intersection or None when not found
:rtype: :class:`mathutils.Vector` or None'''

	def intersect_line_sphere(*argv):
		'''.. function:: intersect_line_sphere(line_a, line_b, sphere_co, sphere_radius, clip=True)

Takes a lines (as 2 vectors), a sphere as a point and a radius and
returns the intersection

:arg line_a: First point of the first line
:type line_a: :class:`mathutils.Vector`
:arg line_b: Second point of the first line
:type line_b: :class:`mathutils.Vector`
:arg sphere_co: The center of the sphere
:type sphere_co: :class:`mathutils.Vector`
:arg sphere_radius: Radius of the sphere
:type sphere_radius: sphere_radius
:return: The intersection points as a pair of vectors or None when there is no intersection
:rtype: A tuple pair containing :class:`mathutils.Vector` or None'''

	def intersect_line_sphere_2d(*argv):
		'''.. function:: intersect_line_sphere_2d(line_a, line_b, sphere_co, sphere_radius, clip=True)

Takes a lines (as 2 vectors), a sphere as a point and a radius and
returns the intersection

:arg line_a: First point of the first line
:type line_a: :class:`mathutils.Vector`
:arg line_b: Second point of the first line
:type line_b: :class:`mathutils.Vector`
:arg sphere_co: The center of the sphere
:type sphere_co: :class:`mathutils.Vector`
:arg sphere_radius: Radius of the sphere
:type sphere_radius: sphere_radius
:return: The intersection points as a pair of vectors or None when there is no intersection
:rtype: A tuple pair containing :class:`mathutils.Vector` or None'''

	def intersect_plane_plane(*argv):
		'''.. function:: intersect_plane_plane(plane_a_co, plane_a_no, plane_b_co, plane_b_no)

Return the intersection between two planes

:arg plane_a_co: Point on the first plane
:type plane_a_co: :class:`mathutils.Vector`
:arg plane_a_no: Normal of the first plane
:type plane_a_no: :class:`mathutils.Vector`
:arg plane_b_co: Point on the second plane
:type plane_b_co: :class:`mathutils.Vector`
:arg plane_b_no: Normal of the second plane
:type plane_b_no: :class:`mathutils.Vector`
:return: The line of the intersection represented as a point and a vector
:rtype: tuple pair of :class:`mathutils.Vector` or None if the intersection can't be calculated'''

	def intersect_point_line(*argv):
		'''.. function:: intersect_point_line(pt, line_p1, line_p2)

Takes a point and a line and returns a tuple with the closest point on the line and its distance from the first point of the line as a percentage of the length of the line.

:arg pt: Point
:type pt: :class:`mathutils.Vector`
:arg line_p1: First point of the line
:type line_p1: :class:`mathutils.Vector`
:arg line_p1: Second point of the line
:type line_p1: :class:`mathutils.Vector`
:rtype: (:class:`mathutils.Vector`, float)'''

	def intersect_point_quad_2d(*argv):
		'''.. function:: intersect_point_quad_2d(pt, quad_p1, quad_p2, quad_p3, quad_p4)

Takes 5 vectors (using only the x and y coordinates): one is the point and the next 4 define the quad, 
only the x and y are used from the vectors. Returns 1 if the point is within the quad, otherwise 0.
Works only with convex quads without singular edges.
:arg pt: Point
:type pt: :class:`mathutils.Vector`
:arg quad_p1: First point of the quad
:type quad_p1: :class:`mathutils.Vector`
:arg quad_p2: Second point of the quad
:type quad_p2: :class:`mathutils.Vector`
:arg quad_p3: Third point of the quad
:type quad_p3: :class:`mathutils.Vector`
:arg quad_p4: Forth point of the quad
:type quad_p4: :class:`mathutils.Vector`
:rtype: int'''

	def intersect_point_tri_2d(*argv):
		'''.. function:: intersect_point_tri_2d(pt, tri_p1, tri_p2, tri_p3)

Takes 4 vectors (using only the x and y coordinates): one is the point and the next 3 define the triangle. Returns 1 if the point is within the triangle, otherwise 0.

:arg pt: Point
:type v1: :class:`mathutils.Vector`
:arg tri_p1: First point of the triangle
:type tri_p1: :class:`mathutils.Vector`
:arg tri_p2: Second point of the triangle
:type tri_p2: :class:`mathutils.Vector`
:arg tri_p3: Third point of the triangle
:type tri_p3: :class:`mathutils.Vector`
:rtype: int'''

	def intersect_ray_tri(*argv):
		'''.. function:: intersect_ray_tri(v1, v2, v3, ray, orig, clip=True)

Returns the intersection between a ray and a triangle, if possible, returns None otherwise.

:arg v1: Point1
:type v1: :class:`mathutils.Vector`
:arg v2: Point2
:type v2: :class:`mathutils.Vector`
:arg v3: Point3
:type v3: :class:`mathutils.Vector`
:arg ray: Direction of the projection
:type ray: :class:`mathutils.Vector`
:arg orig: Origin
:type orig: :class:`mathutils.Vector`
:arg clip: When False, don't restrict the intersection to the area of the triangle, use the infinite plane defined by the triangle.
:type clip: boolean
:return: The point of intersection or None if no intersection is found
:rtype: :class:`mathutils.Vector` or None'''

	def intersect_sphere_sphere_2d(*argv):
		'''.. function:: intersect_sphere_sphere_2d(p_a, radius_a, p_b, radius_b)

Returns 2 points on between intersecting circles.

:arg p_a: Center of the first circle
:type p_a: :class:`mathutils.Vector`
:arg radius_a: Radius of the first circle
:type radius_a: float
:arg p_b: Center of the second circle
:type p_b: :class:`mathutils.Vector`
:arg radius_b: Radius of the second circle
:type radius_b: float
:rtype: tuple of :class:`mathutils.Vector`'s or None when there is no intersection'''

	def normal(*argv):
		'''.. function:: normal(v1, v2, v3, v4=None)

Returns the normal of the 3D tri or quad.

:arg v1: Point1
:type v1: :class:`mathutils.Vector`
:arg v2: Point2
:type v2: :class:`mathutils.Vector`
:arg v3: Point3
:type v3: :class:`mathutils.Vector`
:arg v4: Point4 (optional)
:type v4: :class:`mathutils.Vector`
:rtype: :class:`mathutils.Vector`'''

	def points_in_planes(*argv):
		'''.. function:: points_in_planes(planes)

Returns a list of points inside all planes given and a list of index values for the planes used.

:arg planes: List of planes (4D vectors).
:type planes: list of :class:`mathutils.Vector`
:return: two lists, once containing the vertices inside the planes, another containing the plane indices used
:rtype: pair of lists'''

	def tessellate_polygon(*argv):
		'''.. function:: tessellate_polygon(veclist_list)

Takes a list of polylines (each point a vector) and returns the point indices for a polyline filled with triangles.

:arg veclist_list: list of polylines
:rtype: list'''

	def volume_tetrahedron(*argv):
		'''.. function:: volume_tetrahedron(v1, v2, v3, v4)

Return the volume formed by a tetrahedron (points can be in any order).

:arg v1: Point1
:type v1: :class:`mathutils.Vector`
:arg v2: Point2
:type v2: :class:`mathutils.Vector`
:arg v3: Point3
:type v3: :class:`mathutils.Vector`
:arg v4: Point4
:type v4: :class:`mathutils.Vector`
:rtype: float'''


class kdtree:
	'''Generic 3-dimentional kd-tree to perform spatial searches.'''

	class KDTree:
		'''KdTree(size) -> new kd-tree initialized to hold ``size`` items.

.. note::

   :class:`KDTree.balance` must have been called before using any of the ``find`` methods.'''

		def balance(*argv):
			'''.. method:: balance()

Balance the tree.'''

		def find(*argv):
			'''.. method:: find(co)

Find nearest point to ``co``.

:arg co: 3d coordinates.
:type co: float triplet
:return: Returns (:class:`Vector`, index, distance).
:rtype: :class:`tuple`'''

		def find_n(*argv):
			'''.. method:: find_n(co, n)

Find nearest ``n`` points to ``co``.

:arg co: 3d coordinates.
:type co: float triplet
:arg n: Number of points to find.
:type n: int
:return: Returns a list of tuples (:class:`Vector`, index, distance).
:rtype: :class:`list`'''

		def find_range(*argv):
			'''.. method:: find_range(co, radius)

Find all points within ``radius`` of ``co``.

:arg co: 3d coordinates.
:type co: float triplet
:arg radius: Distance to search for points.
:type radius: float
:return: Returns a list of tuples (:class:`Vector`, index, distance).
:rtype: :class:`list`'''

		def insert(*argv):
			'''.. method:: insert(index, co)

Insert a point into the KDTree.

:arg co: Point 3d position.
:type co: float triplet
:arg index: The index of the point.
:type index: int'''



class noise:
	'''The Blender noise module'''

	def cell(*argv):
		'''.. function:: cell(position)

Returns cell noise value at the specified position.

:arg position: The position to evaluate the selected noise function at.
:type position: :class:`mathutils.Vector`
:return: The cell noise value.
:rtype: float'''

	def cell_vector(*argv):
		'''.. function:: cell_vector(position)

Returns cell noise vector at the specified position.

:arg position: The position to evaluate the selected noise function at.
:type position: :class:`mathutils.Vector`
:return: The cell noise vector.
:rtype: :class:`mathutils.Vector`'''

	class distance_metrics:
		CHEBYCHEV = int
		DISTANCE = int
		DISTANCE_SQUARED = int
		MANHATTAN = int
		MINKOVSKY = int
		MINKOVSKY_FOUR = int
		MINKOVSKY_HALF = int

	def fractal(*argv):
		'''.. function:: fractal(position, H, lacunarity, octaves, noise_basis=noise.types.STDPERLIN)

Returns the fractal Brownian motion (fBm) noise value from the noise basis at the specified position.

:arg position: The position to evaluate the selected noise function at.
:type position: :class:`mathutils.Vector`
:arg H: The fractal increment factor.
:type H: float
:arg lacunarity: The gap between successive frequencies.
:type lacunarity: float
:arg octaves: The number of different noise frequencies used.
:type octaves: int
:arg noise_basis: The type of noise to be evaluated.
:type noise_basis: Value in noise.types or int
:return: The fractal Brownian motion noise value.
:rtype: float'''

	def hetero_terrain(*argv):
		'''.. function:: hetero_terrain(position, H, lacunarity, octaves, offset, noise_basis=noise.types.STDPERLIN)

Returns the heterogeneous terrain value from the noise basis at the specified position.

:arg position: The position to evaluate the selected noise function at.
:type position: :class:`mathutils.Vector`
:arg H: The fractal dimension of the roughest areas.
:type H: float
:arg lacunarity: The gap between successive frequencies.
:type lacunarity: float
:arg octaves: The number of different noise frequencies used.
:type octaves: int
:arg offset: The height of the terrain above 'sea level'.
:type offset: float
:arg noise_basis: The type of noise to be evaluated.
:type noise_basis: Value in noise.types or int
:return: The heterogeneous terrain value.
:rtype: float'''

	def hybrid_multi_fractal(*argv):
		'''.. function:: hybrid_multi_fractal(position, H, lacunarity, octaves, offset, gain, noise_basis=noise.types.STDPERLIN)

Returns hybrid multifractal value from the noise basis at the specified position.

:arg position: The position to evaluate the selected noise function at.
:type position: :class:`mathutils.Vector`
:arg H: The fractal dimension of the roughest areas.
:type H: float
:arg lacunarity: The gap between successive frequencies.
:type lacunarity: float
:arg octaves: The number of different noise frequencies used.
:type octaves: int
:arg offset: The height of the terrain above 'sea level'.
:type offset: float
:arg gain: Scaling applied to the values.
:type gain: float
:arg noise_basis: The type of noise to be evaluated.
:type noise_basis: Value in noise.types or int
:return: The hybrid multifractal value.
:rtype: float'''

	def multi_fractal(*argv):
		'''.. function:: multi_fractal(position, H, lacunarity, octaves, noise_basis=noise.types.STDPERLIN)

Returns multifractal noise value from the noise basis at the specified position.

:arg position: The position to evaluate the selected noise function at.
:type position: :class:`mathutils.Vector`
:arg H: The fractal increment factor.
:type H: float
:arg lacunarity: The gap between successive frequencies.
:type lacunarity: float
:arg octaves: The number of different noise frequencies used.
:type octaves: int
:arg noise_basis: The type of noise to be evaluated.
:type noise_basis: Value in noise.types or int
:return: The multifractal noise value.
:rtype: float'''

	def noise(*argv):
		'''.. function:: noise(position, noise_basis=noise.types.STDPERLIN)

Returns noise value from the noise basis at the position specified.

:arg position: The position to evaluate the selected noise function at.
:type position: :class:`mathutils.Vector`
:arg noise_basis: The type of noise to be evaluated.
:type noise_basis: Value in noise.types or int
:return: The noise value.
:rtype: float'''

	def noise_vector(*argv):
		'''.. function:: noise_vector(position, noise_basis=noise.types.STDPERLIN)

Returns the noise vector from the noise basis at the specified position.

:arg position: The position to evaluate the selected noise function at.
:type position: :class:`mathutils.Vector`
:arg noise_basis: The type of noise to be evaluated.
:type noise_basis: Value in noise.types or int
:return: The noise vector.
:rtype: :class:`mathutils.Vector`'''

	def random(*argv):
		'''.. function:: random()

Returns a random number in the range [0, 1].

:return: The random number.
:rtype: float'''

	def random_unit_vector(*argv):
		'''.. function:: random_unit_vector(size=3)

Returns a unit vector with random entries.

:arg size: The size of the vector to be produced.
:type size: Int
:return: The random unit vector.
:rtype: :class:`mathutils.Vector`'''

	def ridged_multi_fractal(*argv):
		'''.. function:: ridged_multi_fractal(position, H, lacunarity, octaves, offset, gain, noise_basis=noise.types.STDPERLIN)

Returns ridged multifractal value from the noise basis at the specified position.

:arg position: The position to evaluate the selected noise function at.
:type position: :class:`mathutils.Vector`
:arg H: The fractal dimension of the roughest areas.
:type H: float
:arg lacunarity: The gap between successive frequencies.
:type lacunarity: float
:arg octaves: The number of different noise frequencies used.
:type octaves: int
:arg offset: The height of the terrain above 'sea level'.
:type offset: float
:arg gain: Scaling applied to the values.
:type gain: float
:arg noise_basis: The type of noise to be evaluated.
:type noise_basis: Value in noise.types or int
:return: The ridged multifractal value.
:rtype: float'''

	def seed_set(*argv):
		'''.. function:: seed_set(seed)

Sets the random seed used for random_unit_vector, random_vector and random.

:arg seed: Seed used for the random generator.
:type seed: Int'''

	def turbulence(*argv):
		'''.. function:: turbulence(position, octaves, hard, noise_basis=noise.types.STDPERLIN, amplitude_scale=0.5, frequency_scale=2.0)

Returns the turbulence value from the noise basis at the specified position.

:arg position: The position to evaluate the selected noise function at.
:type position: :class:`mathutils.Vector`
:arg octaves: The number of different noise frequencies used.
:type octaves: int
:arg hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
:type hard: :boolean
:arg noise_basis: The type of noise to be evaluated.
:type noise_basis: Value in mathutils.noise.types or int
:arg amplitude_scale: The amplitude scaling factor.
:type amplitude_scale: float
:arg frequency_scale: The frequency scaling factor
:type frequency_scale: Value in noise.types or int
:return: The turbulence value.
:rtype: float'''

	def turbulence_vector(*argv):
		'''.. function:: turbulence_vector(position, octaves, hard, noise_basis=noise.types.STDPERLIN, amplitude_scale=0.5, frequency_scale=2.0)

Returns the turbulence vector from the noise basis at the specified position.

:arg position: The position to evaluate the selected noise function at.
:type position: :class:`mathutils.Vector`
:arg octaves: The number of different noise frequencies used.
:type octaves: int
:arg hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
:type hard: :boolean
:arg noise_basis: The type of noise to be evaluated.
:type noise_basis: Value in mathutils.noise.types or int
:arg amplitude_scale: The amplitude scaling factor.
:type amplitude_scale: float
:arg frequency_scale: The frequency scaling factor
:type frequency_scale: Value in noise.types or int
:return: The turbulence vector.
:rtype: :class:`mathutils.Vector`'''

	class types:
		BLENDER = int
		CELLNOISE = int
		NEWPERLIN = int
		STDPERLIN = int
		VORONOI_CRACKLE = int
		VORONOI_F1 = int
		VORONOI_F2 = int
		VORONOI_F2F1 = int
		VORONOI_F3 = int
		VORONOI_F4 = int

	def variable_lacunarity(*argv):
		'''.. function:: variable_lacunarity(position, distortion, noise_type1=noise.types.STDPERLIN, noise_type2=noise.types.STDPERLIN)

Returns variable lacunarity noise value, a distorted variety of noise, from noise type 1 distorted by noise type 2 at the specified position.

:arg position: The position to evaluate the selected noise function at.
:type position: :class:`mathutils.Vector`
:arg distortion: The amount of distortion.
:type distortion: float
:arg noise_type1: The type of noise to be distorted.
:type noise_type1: Value in noise.types or int
:arg noise_type2: The type of noise used to distort noise_type1.
:type noise_type2: Value in noise.types or int
:return: The variable lacunarity noise value.
:rtype: float'''

	def voronoi(*argv):
		'''.. function:: voronoi(position, distance_metric=noise.distance_metrics.DISTANCE, exponent=2.5)

Returns a list of distances to the four closest features and their locations.

:arg position: The position to evaluate the selected noise function at.
:type position: :class:`mathutils.Vector`
:arg distance_metric: Method of measuring distance.
:type distance_metric: Value in noise.distance_metrics or int
:arg exponent: The exponent for Minkowski distance metric.
:type exponent: float
:return: A list of distances to the four closest features and their locations.
:rtype: list of four floats, list of four :class:`mathutils.Vector` types'''



