class Buffer:
	dimensions = getset_descriptor
	def to_list(*argv):
		'''return the buffer as a list'''


GL_2D = int
GL_2_BYTES = int
GL_3D = int
GL_3D_COLOR = int
GL_3D_COLOR_TEXTURE = int
GL_3_BYTES = int
GL_4D_COLOR_TEXTURE = int
GL_4_BYTES = int
GL_ACCUM = int
GL_ACCUM_ALPHA_BITS = int
GL_ACCUM_BLUE_BITS = int
GL_ACCUM_BUFFER_BIT = int
GL_ACCUM_CLEAR_VALUE = int
GL_ACCUM_GREEN_BITS = int
GL_ACCUM_RED_BITS = int
GL_ACTIVE_TEXTURE = int
GL_ADD = int
GL_ALL_ATTRIB_BITS = int
GL_ALPHA = int
GL_ALPHA_BIAS = int
GL_ALPHA_BITS = int
GL_ALPHA_SCALE = int
GL_ALPHA_TEST = int
GL_ALPHA_TEST_FUNC = int
GL_ALPHA_TEST_REF = int
GL_ALWAYS = int
GL_AMBIENT = int
GL_AMBIENT_AND_DIFFUSE = int
GL_AND = int
GL_AND_INVERTED = int
GL_AND_REVERSE = int
GL_ATTRIB_STACK_DEPTH = int
GL_AUTO_NORMAL = int
GL_AUX0 = int
GL_AUX1 = int
GL_AUX2 = int
GL_AUX3 = int
GL_AUX_BUFFERS = int
GL_BACK = int
GL_BACK_LEFT = int
GL_BACK_RIGHT = int
GL_BITMAP = int
GL_BITMAP_TOKEN = int
GL_BLEND = int
GL_BLEND_DST = int
GL_BLEND_SRC = int
GL_BLUE = int
GL_BLUE_BIAS = int
GL_BLUE_BITS = int
GL_BLUE_SCALE = int
GL_BYTE = int
GL_CCW = int
GL_CLAMP = int
GL_CLEAR = int
GL_CLIENT_ALL_ATTRIB_BITS = int
GL_CLIP_PLANE0 = int
GL_CLIP_PLANE1 = int
GL_CLIP_PLANE2 = int
GL_CLIP_PLANE3 = int
GL_CLIP_PLANE4 = int
GL_CLIP_PLANE5 = int
GL_COEFF = int
GL_COLOR = int
GL_COLOR_BUFFER_BIT = int
GL_COLOR_CLEAR_VALUE = int
GL_COLOR_INDEX = int
GL_COLOR_INDEXES = int
GL_COLOR_MATERIAL = int
GL_COLOR_MATERIAL_FACE = int
GL_COLOR_MATERIAL_PARAMETER = int
GL_COLOR_WRITEMASK = int
GL_COMPILE = int
GL_COMPILE_AND_EXECUTE = int
GL_COMPILE_STATUS = int
GL_CONSTANT_ATTENUATION = int
GL_COPY = int
GL_COPY_INVERTED = int
GL_COPY_PIXEL_TOKEN = int
GL_CULL_FACE = int
GL_CULL_FACE_MODE = int
GL_CURRENT_BIT = int
GL_CURRENT_COLOR = int
GL_CURRENT_INDEX = int
GL_CURRENT_NORMAL = int
GL_CURRENT_RASTER_COLOR = int
GL_CURRENT_RASTER_DISTANCE = int
GL_CURRENT_RASTER_INDEX = int
GL_CURRENT_RASTER_POSITION = int
GL_CURRENT_RASTER_POSITION_VALID = int
GL_CURRENT_RASTER_TEXTURE_COORDS = int
GL_CURRENT_TEXTURE_COORDS = int
GL_CW = int
GL_DECAL = int
GL_DECR = int
GL_DEPTH = int
GL_DEPTH_BIAS = int
GL_DEPTH_BITS = int
GL_DEPTH_BUFFER_BIT = int
GL_DEPTH_CLEAR_VALUE = int
GL_DEPTH_COMPONENT = int
GL_DEPTH_COMPONENT32 = int
GL_DEPTH_FUNC = int
GL_DEPTH_RANGE = int
GL_DEPTH_SCALE = int
GL_DEPTH_TEST = int
GL_DEPTH_WRITEMASK = int
GL_DIFFUSE = int
GL_DITHER = int
GL_DOMAIN = int
GL_DONT_CARE = int
GL_DOUBLE = int
GL_DOUBLEBUFFER = int
GL_DRAW_BUFFER = int
GL_DRAW_PIXEL_TOKEN = int
GL_DST_ALPHA = int
GL_DST_COLOR = int
GL_EDGE_FLAG = int
GL_EMISSION = int
GL_ENABLE_BIT = int
GL_EQUAL = int
GL_EQUIV = int
GL_EVAL_BIT = int
GL_EXP = int
GL_EXP2 = int
GL_EXTENSIONS = int
GL_EYE_LINEAR = int
GL_EYE_PLANE = int
GL_FALSE = int
GL_FASTEST = int
GL_FEEDBACK = int
GL_FILL = int
GL_FLAT = int
GL_FLOAT = int
GL_FOG = int
GL_FOG_BIT = int
GL_FOG_COLOR = int
GL_FOG_DENSITY = int
GL_FOG_END = int
GL_FOG_HINT = int
GL_FOG_INDEX = int
GL_FOG_MODE = int
GL_FOG_START = int
GL_FRAGMENT_SHADER = int
GL_FRONT = int
GL_FRONT_AND_BACK = int
GL_FRONT_FACE = int
GL_FRONT_LEFT = int
GL_FRONT_RIGHT = int
GL_GEQUAL = int
GL_GREATER = int
GL_GREEN = int
GL_GREEN_BIAS = int
GL_GREEN_BITS = int
GL_GREEN_SCALE = int
GL_HINT_BIT = int
GL_INCR = int
GL_INDEX_BITS = int
GL_INDEX_CLEAR_VALUE = int
GL_INDEX_MODE = int
GL_INDEX_OFFSET = int
GL_INDEX_SHIFT = int
GL_INDEX_WRITEMASK = int
GL_INT = int
GL_INVALID_ENUM = int
GL_INVALID_OPERATION = int
GL_INVALID_VALUE = int
GL_INVERT = int
GL_KEEP = int
GL_LEFT = int
GL_LEQUAL = int
GL_LESS = int
GL_LIGHT0 = int
GL_LIGHT1 = int
GL_LIGHT2 = int
GL_LIGHT3 = int
GL_LIGHT4 = int
GL_LIGHT5 = int
GL_LIGHT6 = int
GL_LIGHT7 = int
GL_LIGHTING = int
GL_LIGHTING_BIT = int
GL_LIGHT_MODEL_AMBIENT = int
GL_LIGHT_MODEL_LOCAL_VIEWER = int
GL_LIGHT_MODEL_TWO_SIDE = int
GL_LINE = int
GL_LINEAR = int
GL_LINEAR_ATTENUATION = int
GL_LINEAR_MIPMAP_LINEAR = int
GL_LINEAR_MIPMAP_NEAREST = int
GL_LINES = int
GL_LINE_BIT = int
GL_LINE_LOOP = int
GL_LINE_RESET_TOKEN = int
GL_LINE_SMOOTH = int
GL_LINE_SMOOTH_HINT = int
GL_LINE_STIPPLE = int
GL_LINE_STIPPLE_PATTERN = int
GL_LINE_STIPPLE_REPEAT = int
GL_LINE_STRIP = int
GL_LINE_TOKEN = int
GL_LINE_WIDTH = int
GL_LINE_WIDTH_GRANULARITY = int
GL_LINE_WIDTH_RANGE = int
GL_LIST_BASE = int
GL_LIST_BIT = int
GL_LIST_INDEX = int
GL_LIST_MODE = int
GL_LOAD = int
GL_LOGIC_OP = int
GL_LOGIC_OP_MODE = int
GL_LUMINANCE = int
GL_LUMINANCE_ALPHA = int
GL_MAP1_COLOR_4 = int
GL_MAP1_GRID_DOMAIN = int
GL_MAP1_GRID_SEGMENTS = int
GL_MAP1_INDEX = int
GL_MAP1_NORMAL = int
GL_MAP1_TEXTURE_COORD_1 = int
GL_MAP1_TEXTURE_COORD_2 = int
GL_MAP1_TEXTURE_COORD_3 = int
GL_MAP1_TEXTURE_COORD_4 = int
GL_MAP1_VERTEX_3 = int
GL_MAP1_VERTEX_4 = int
GL_MAP2_COLOR_4 = int
GL_MAP2_GRID_DOMAIN = int
GL_MAP2_GRID_SEGMENTS = int
GL_MAP2_INDEX = int
GL_MAP2_NORMAL = int
GL_MAP2_TEXTURE_COORD_1 = int
GL_MAP2_TEXTURE_COORD_2 = int
GL_MAP2_TEXTURE_COORD_3 = int
GL_MAP2_TEXTURE_COORD_4 = int
GL_MAP2_VERTEX_3 = int
GL_MAP2_VERTEX_4 = int
GL_MAP_COLOR = int
GL_MAP_STENCIL = int
GL_MATRIX_MODE = int
GL_MAX_ATTRIB_STACK_DEPTH = int
GL_MAX_CLIP_PLANES = int
GL_MAX_EVAL_ORDER = int
GL_MAX_LIGHTS = int
GL_MAX_LIST_NESTING = int
GL_MAX_MODELVIEW_STACK_DEPTH = int
GL_MAX_NAME_STACK_DEPTH = int
GL_MAX_PIXEL_MAP_TABLE = int
GL_MAX_PROJECTION_STACK_DEPTH = int
GL_MAX_TEXTURE_SIZE = int
GL_MAX_TEXTURE_STACK_DEPTH = int
GL_MAX_VIEWPORT_DIMS = int
GL_MODELVIEW = int
GL_MODELVIEW_MATRIX = int
GL_MODELVIEW_STACK_DEPTH = int
GL_MODULATE = int
GL_MULT = int
GL_NAME_STACK_DEPTH = int
GL_NAND = int
GL_NEAREST = int
GL_NEAREST_MIPMAP_LINEAR = int
GL_NEAREST_MIPMAP_NEAREST = int
GL_NEVER = int
GL_NICEST = int
GL_NONE = int
GL_NOOP = int
GL_NOR = int
GL_NORMALIZE = int
GL_NOTEQUAL = int
GL_NO_ERROR = int
GL_OBJECT_LINEAR = int
GL_OBJECT_PLANE = int
GL_ONE = int
GL_ONE_MINUS_DST_ALPHA = int
GL_ONE_MINUS_DST_COLOR = int
GL_ONE_MINUS_SRC_ALPHA = int
GL_ONE_MINUS_SRC_COLOR = int
GL_OR = int
GL_ORDER = int
GL_OR_INVERTED = int
GL_OR_REVERSE = int
GL_OUT_OF_MEMORY = int
GL_PACK_ALIGNMENT = int
GL_PACK_LSB_FIRST = int
GL_PACK_ROW_LENGTH = int
GL_PACK_SKIP_PIXELS = int
GL_PACK_SKIP_ROWS = int
GL_PACK_SWAP_BYTES = int
GL_PASS_THROUGH_TOKEN = int
GL_PERSPECTIVE_CORRECTION_HINT = int
GL_PIXEL_MAP_A_TO_A = int
GL_PIXEL_MAP_A_TO_A_SIZE = int
GL_PIXEL_MAP_B_TO_B = int
GL_PIXEL_MAP_B_TO_B_SIZE = int
GL_PIXEL_MAP_G_TO_G = int
GL_PIXEL_MAP_G_TO_G_SIZE = int
GL_PIXEL_MAP_I_TO_A = int
GL_PIXEL_MAP_I_TO_A_SIZE = int
GL_PIXEL_MAP_I_TO_B = int
GL_PIXEL_MAP_I_TO_B_SIZE = int
GL_PIXEL_MAP_I_TO_G = int
GL_PIXEL_MAP_I_TO_G_SIZE = int
GL_PIXEL_MAP_I_TO_I = int
GL_PIXEL_MAP_I_TO_I_SIZE = int
GL_PIXEL_MAP_I_TO_R = int
GL_PIXEL_MAP_I_TO_R_SIZE = int
GL_PIXEL_MAP_R_TO_R = int
GL_PIXEL_MAP_R_TO_R_SIZE = int
GL_PIXEL_MAP_S_TO_S = int
GL_PIXEL_MAP_S_TO_S_SIZE = int
GL_PIXEL_MODE_BIT = int
GL_POINT = int
GL_POINTS = int
GL_POINT_BIT = int
GL_POINT_SIZE = int
GL_POINT_SIZE_GRANULARITY = int
GL_POINT_SIZE_RANGE = int
GL_POINT_SMOOTH = int
GL_POINT_SMOOTH_HINT = int
GL_POINT_TOKEN = int
GL_POLYGON = int
GL_POLYGON_BIT = int
GL_POLYGON_MODE = int
GL_POLYGON_OFFSET_FACTOR = int
GL_POLYGON_OFFSET_FILL = int
GL_POLYGON_OFFSET_LINE = int
GL_POLYGON_OFFSET_POINT = int
GL_POLYGON_OFFSET_UNITS = int
GL_POLYGON_SMOOTH = int
GL_POLYGON_SMOOTH_HINT = int
GL_POLYGON_STIPPLE = int
GL_POLYGON_STIPPLE_BIT = int
GL_POLYGON_TOKEN = int
GL_POSITION = int
GL_PROJECTION = int
GL_PROJECTION_MATRIX = int
GL_PROJECTION_STACK_DEPTH = int
GL_Q = int
GL_QUADRATIC_ATTENUATION = int
GL_QUADS = int
GL_QUAD_STRIP = int
GL_R = int
GL_READ_BUFFER = int
GL_RED = int
GL_RED_BIAS = int
GL_RED_BITS = int
GL_RED_SCALE = int
GL_RENDER = int
GL_RENDERER = int
GL_RENDER_MODE = int
GL_REPEAT = int
GL_REPLACE = int
GL_RETURN = int
GL_RGB = int
GL_RGBA = int
GL_RGBA_MODE = int
GL_RIGHT = int
GL_S = int
GL_SCISSOR_BIT = int
GL_SCISSOR_BOX = int
GL_SCISSOR_TEST = int
GL_SELECT = int
GL_SET = int
GL_SHADE_MODEL = int
GL_SHININESS = int
GL_SHORT = int
GL_SMOOTH = int
GL_SPECULAR = int
GL_SPHERE_MAP = int
GL_SPOT_CUTOFF = int
GL_SPOT_DIRECTION = int
GL_SPOT_EXPONENT = int
GL_SRC_ALPHA = int
GL_SRC_ALPHA_SATURATE = int
GL_SRC_COLOR = int
GL_STACK_OVERFLOW = int
GL_STACK_UNDERFLOW = int
GL_STENCIL = int
GL_STENCIL_BITS = int
GL_STENCIL_BUFFER_BIT = int
GL_STENCIL_CLEAR_VALUE = int
GL_STENCIL_FAIL = int
GL_STENCIL_FUNC = int
GL_STENCIL_INDEX = int
GL_STENCIL_PASS_DEPTH_FAIL = int
GL_STENCIL_PASS_DEPTH_PASS = int
GL_STENCIL_REF = int
GL_STENCIL_TEST = int
GL_STENCIL_VALUE_MASK = int
GL_STENCIL_WRITEMASK = int
GL_STEREO = int
GL_SUBPIXEL_BITS = int
GL_T = int
GL_TEXTURE = int
GL_TEXTURE0 = int
GL_TEXTURE1 = int
GL_TEXTURE2 = int
GL_TEXTURE3 = int
GL_TEXTURE4 = int
GL_TEXTURE5 = int
GL_TEXTURE6 = int
GL_TEXTURE7 = int
GL_TEXTURE8 = int
GL_TEXTURE_1D = int
GL_TEXTURE_2D = int
GL_TEXTURE_BINDING_1D = int
GL_TEXTURE_BINDING_2D = int
GL_TEXTURE_BIT = int
GL_TEXTURE_BORDER = int
GL_TEXTURE_BORDER_COLOR = int
GL_TEXTURE_COMPARE_MODE = int
GL_TEXTURE_COMPONENTS = int
GL_TEXTURE_ENV = int
GL_TEXTURE_ENV_COLOR = int
GL_TEXTURE_ENV_MODE = int
GL_TEXTURE_GEN_MODE = int
GL_TEXTURE_GEN_Q = int
GL_TEXTURE_GEN_R = int
GL_TEXTURE_GEN_S = int
GL_TEXTURE_GEN_T = int
GL_TEXTURE_HEIGHT = int
GL_TEXTURE_MAG_FILTER = int
GL_TEXTURE_MATRIX = int
GL_TEXTURE_MIN_FILTER = int
GL_TEXTURE_PRIORITY = int
GL_TEXTURE_RESIDENT = int
GL_TEXTURE_STACK_DEPTH = int
GL_TEXTURE_WIDTH = int
GL_TEXTURE_WRAP_S = int
GL_TEXTURE_WRAP_T = int
GL_TRANSFORM_BIT = int
GL_TRIANGLES = int
GL_TRIANGLE_FAN = int
GL_TRIANGLE_STRIP = int
GL_TRUE = int
GL_UNPACK_ALIGNMENT = int
GL_UNPACK_LSB_FIRST = int
GL_UNPACK_ROW_LENGTH = int
GL_UNPACK_SKIP_PIXELS = int
GL_UNPACK_SKIP_ROWS = int
GL_UNPACK_SWAP_BYTES = int
GL_UNSIGNED_BYTE = int
GL_UNSIGNED_INT = int
GL_UNSIGNED_SHORT = int
GL_VENDOR = int
GL_VERSION = int
GL_VERTEX_SHADER = int
GL_VIEWPORT = int
GL_VIEWPORT_BIT = int
GL_XOR = int
GL_ZERO = int
GL_ZOOM_X = int
GL_ZOOM_Y = int
def glAccum(*argv):
	'''no string'''

def glActiveTexture(*argv):
	'''no string'''

def glAlphaFunc(*argv):
	'''no string'''

def glAreTexturesResident(*argv):
	'''no string'''

def glAttachShader(*argv):
	'''no string'''

def glBegin(*argv):
	'''no string'''

def glBindTexture(*argv):
	'''no string'''

def glBitmap(*argv):
	'''no string'''

def glBlendFunc(*argv):
	'''no string'''

def glCallList(*argv):
	'''no string'''

def glCallLists(*argv):
	'''no string'''

def glClear(*argv):
	'''no string'''

def glClearAccum(*argv):
	'''no string'''

def glClearColor(*argv):
	'''no string'''

def glClearDepth(*argv):
	'''no string'''

def glClearIndex(*argv):
	'''no string'''

def glClearStencil(*argv):
	'''no string'''

def glClipPlane(*argv):
	'''no string'''

def glColor3b(*argv):
	'''no string'''

def glColor3bv(*argv):
	'''no string'''

def glColor3d(*argv):
	'''no string'''

def glColor3dv(*argv):
	'''no string'''

def glColor3f(*argv):
	'''no string'''

def glColor3fv(*argv):
	'''no string'''

def glColor3i(*argv):
	'''no string'''

def glColor3iv(*argv):
	'''no string'''

def glColor3s(*argv):
	'''no string'''

def glColor3sv(*argv):
	'''no string'''

def glColor3ub(*argv):
	'''no string'''

def glColor3ubv(*argv):
	'''no string'''

def glColor3ui(*argv):
	'''no string'''

def glColor3uiv(*argv):
	'''no string'''

def glColor3us(*argv):
	'''no string'''

def glColor3usv(*argv):
	'''no string'''

def glColor4b(*argv):
	'''no string'''

def glColor4bv(*argv):
	'''no string'''

def glColor4d(*argv):
	'''no string'''

def glColor4dv(*argv):
	'''no string'''

def glColor4f(*argv):
	'''no string'''

def glColor4fv(*argv):
	'''no string'''

def glColor4i(*argv):
	'''no string'''

def glColor4iv(*argv):
	'''no string'''

def glColor4s(*argv):
	'''no string'''

def glColor4sv(*argv):
	'''no string'''

def glColor4ub(*argv):
	'''no string'''

def glColor4ubv(*argv):
	'''no string'''

def glColor4ui(*argv):
	'''no string'''

def glColor4uiv(*argv):
	'''no string'''

def glColor4us(*argv):
	'''no string'''

def glColor4usv(*argv):
	'''no string'''

def glColorMask(*argv):
	'''no string'''

def glColorMaterial(*argv):
	'''no string'''

def glCompileShader(*argv):
	'''no string'''

def glCopyPixels(*argv):
	'''no string'''

def glCopyTexImage2D(*argv):
	'''no string'''

def glCreateProgram(*argv):
	'''no string'''

def glCreateShader(*argv):
	'''no string'''

def glCullFace(*argv):
	'''no string'''

def glDeleteLists(*argv):
	'''no string'''

def glDeleteProgram(*argv):
	'''no string'''

def glDeleteShader(*argv):
	'''no string'''

def glDeleteTextures(*argv):
	'''no string'''

def glDepthFunc(*argv):
	'''no string'''

def glDepthMask(*argv):
	'''no string'''

def glDepthRange(*argv):
	'''no string'''

def glDetachShader(*argv):
	'''no string'''

def glDisable(*argv):
	'''no string'''

def glDrawBuffer(*argv):
	'''no string'''

def glDrawPixels(*argv):
	'''no string'''

def glEdgeFlag(*argv):
	'''no string'''

def glEdgeFlagv(*argv):
	'''no string'''

def glEnable(*argv):
	'''no string'''

def glEnd(*argv):
	'''no string'''

def glEndList(*argv):
	'''no string'''

def glEvalCoord1d(*argv):
	'''no string'''

def glEvalCoord1dv(*argv):
	'''no string'''

def glEvalCoord1f(*argv):
	'''no string'''

def glEvalCoord1fv(*argv):
	'''no string'''

def glEvalCoord2d(*argv):
	'''no string'''

def glEvalCoord2dv(*argv):
	'''no string'''

def glEvalCoord2f(*argv):
	'''no string'''

def glEvalCoord2fv(*argv):
	'''no string'''

def glEvalMesh1(*argv):
	'''no string'''

def glEvalMesh2(*argv):
	'''no string'''

def glEvalPoint1(*argv):
	'''no string'''

def glEvalPoint2(*argv):
	'''no string'''

def glFeedbackBuffer(*argv):
	'''no string'''

def glFinish(*argv):
	'''no string'''

def glFlush(*argv):
	'''no string'''

def glFogf(*argv):
	'''no string'''

def glFogfv(*argv):
	'''no string'''

def glFogi(*argv):
	'''no string'''

def glFogiv(*argv):
	'''no string'''

def glFrontFace(*argv):
	'''no string'''

def glFrustum(*argv):
	'''no string'''

def glGenLists(*argv):
	'''no string'''

def glGenTextures(*argv):
	'''no string'''

def glGetAttachedShaders(*argv):
	'''no string'''

def glGetBooleanv(*argv):
	'''no string'''

def glGetClipPlane(*argv):
	'''no string'''

def glGetDoublev(*argv):
	'''no string'''

def glGetError(*argv):
	'''no string'''

def glGetFloatv(*argv):
	'''no string'''

def glGetIntegerv(*argv):
	'''no string'''

def glGetLightfv(*argv):
	'''no string'''

def glGetLightiv(*argv):
	'''no string'''

def glGetMapdv(*argv):
	'''no string'''

def glGetMapfv(*argv):
	'''no string'''

def glGetMapiv(*argv):
	'''no string'''

def glGetMaterialfv(*argv):
	'''no string'''

def glGetMaterialiv(*argv):
	'''no string'''

def glGetPixelMapfv(*argv):
	'''no string'''

def glGetPixelMapuiv(*argv):
	'''no string'''

def glGetPixelMapusv(*argv):
	'''no string'''

def glGetPolygonStipple(*argv):
	'''no string'''

def glGetProgramInfoLog(*argv):
	'''no string'''

def glGetProgramiv(*argv):
	'''no string'''

def glGetShaderInfoLog(*argv):
	'''no string'''

def glGetShaderSource(*argv):
	'''no string'''

def glGetShaderiv(*argv):
	'''no string'''

def glGetString(*argv):
	'''no string'''

def glGetTexEnvfv(*argv):
	'''no string'''

def glGetTexEnviv(*argv):
	'''no string'''

def glGetTexGendv(*argv):
	'''no string'''

def glGetTexGenfv(*argv):
	'''no string'''

def glGetTexGeniv(*argv):
	'''no string'''

def glGetTexImage(*argv):
	'''no string'''

def glGetTexLevelParameterfv(*argv):
	'''no string'''

def glGetTexLevelParameteriv(*argv):
	'''no string'''

def glGetTexParameterfv(*argv):
	'''no string'''

def glGetTexParameteriv(*argv):
	'''no string'''

def glGetUniformLocation(*argv):
	'''no string'''

def glHint(*argv):
	'''no string'''

def glIndexMask(*argv):
	'''no string'''

def glIndexd(*argv):
	'''no string'''

def glIndexdv(*argv):
	'''no string'''

def glIndexf(*argv):
	'''no string'''

def glIndexfv(*argv):
	'''no string'''

def glIndexi(*argv):
	'''no string'''

def glIndexiv(*argv):
	'''no string'''

def glIndexs(*argv):
	'''no string'''

def glIndexsv(*argv):
	'''no string'''

def glInitNames(*argv):
	'''no string'''

def glIsEnabled(*argv):
	'''no string'''

def glIsList(*argv):
	'''no string'''

def glIsProgram(*argv):
	'''no string'''

def glIsShader(*argv):
	'''no string'''

def glIsTexture(*argv):
	'''no string'''

def glLightModelf(*argv):
	'''no string'''

def glLightModelfv(*argv):
	'''no string'''

def glLightModeli(*argv):
	'''no string'''

def glLightModeliv(*argv):
	'''no string'''

def glLightf(*argv):
	'''no string'''

def glLightfv(*argv):
	'''no string'''

def glLighti(*argv):
	'''no string'''

def glLightiv(*argv):
	'''no string'''

def glLineStipple(*argv):
	'''no string'''

def glLineWidth(*argv):
	'''no string'''

def glLinkProgram(*argv):
	'''no string'''

def glListBase(*argv):
	'''no string'''

def glLoadIdentity(*argv):
	'''no string'''

def glLoadMatrixd(*argv):
	'''no string'''

def glLoadMatrixf(*argv):
	'''no string'''

def glLoadName(*argv):
	'''no string'''

def glLogicOp(*argv):
	'''no string'''

def glMap1d(*argv):
	'''no string'''

def glMap1f(*argv):
	'''no string'''

def glMap2d(*argv):
	'''no string'''

def glMap2f(*argv):
	'''no string'''

def glMapGrid1d(*argv):
	'''no string'''

def glMapGrid1f(*argv):
	'''no string'''

def glMapGrid2d(*argv):
	'''no string'''

def glMapGrid2f(*argv):
	'''no string'''

def glMaterialf(*argv):
	'''no string'''

def glMaterialfv(*argv):
	'''no string'''

def glMateriali(*argv):
	'''no string'''

def glMaterialiv(*argv):
	'''no string'''

def glMatrixMode(*argv):
	'''no string'''

def glMultMatrixd(*argv):
	'''no string'''

def glMultMatrixf(*argv):
	'''no string'''

def glNewList(*argv):
	'''no string'''

def glNormal3b(*argv):
	'''no string'''

def glNormal3bv(*argv):
	'''no string'''

def glNormal3d(*argv):
	'''no string'''

def glNormal3dv(*argv):
	'''no string'''

def glNormal3f(*argv):
	'''no string'''

def glNormal3fv(*argv):
	'''no string'''

def glNormal3i(*argv):
	'''no string'''

def glNormal3iv(*argv):
	'''no string'''

def glNormal3s(*argv):
	'''no string'''

def glNormal3sv(*argv):
	'''no string'''

def glOrtho(*argv):
	'''no string'''

def glPassThrough(*argv):
	'''no string'''

def glPixelMapfv(*argv):
	'''no string'''

def glPixelMapuiv(*argv):
	'''no string'''

def glPixelMapusv(*argv):
	'''no string'''

def glPixelStoref(*argv):
	'''no string'''

def glPixelStorei(*argv):
	'''no string'''

def glPixelTransferf(*argv):
	'''no string'''

def glPixelTransferi(*argv):
	'''no string'''

def glPixelZoom(*argv):
	'''no string'''

def glPointSize(*argv):
	'''no string'''

def glPolygonMode(*argv):
	'''no string'''

def glPolygonOffset(*argv):
	'''no string'''

def glPolygonStipple(*argv):
	'''no string'''

def glPopAttrib(*argv):
	'''no string'''

def glPopClientAttrib(*argv):
	'''no string'''

def glPopMatrix(*argv):
	'''no string'''

def glPopName(*argv):
	'''no string'''

def glPrioritizeTextures(*argv):
	'''no string'''

def glPushAttrib(*argv):
	'''no string'''

def glPushClientAttrib(*argv):
	'''no string'''

def glPushMatrix(*argv):
	'''no string'''

def glPushName(*argv):
	'''no string'''

def glRasterPos2d(*argv):
	'''no string'''

def glRasterPos2dv(*argv):
	'''no string'''

def glRasterPos2f(*argv):
	'''no string'''

def glRasterPos2fv(*argv):
	'''no string'''

def glRasterPos2i(*argv):
	'''no string'''

def glRasterPos2iv(*argv):
	'''no string'''

def glRasterPos2s(*argv):
	'''no string'''

def glRasterPos2sv(*argv):
	'''no string'''

def glRasterPos3d(*argv):
	'''no string'''

def glRasterPos3dv(*argv):
	'''no string'''

def glRasterPos3f(*argv):
	'''no string'''

def glRasterPos3fv(*argv):
	'''no string'''

def glRasterPos3i(*argv):
	'''no string'''

def glRasterPos3iv(*argv):
	'''no string'''

def glRasterPos3s(*argv):
	'''no string'''

def glRasterPos3sv(*argv):
	'''no string'''

def glRasterPos4d(*argv):
	'''no string'''

def glRasterPos4dv(*argv):
	'''no string'''

def glRasterPos4f(*argv):
	'''no string'''

def glRasterPos4fv(*argv):
	'''no string'''

def glRasterPos4i(*argv):
	'''no string'''

def glRasterPos4iv(*argv):
	'''no string'''

def glRasterPos4s(*argv):
	'''no string'''

def glRasterPos4sv(*argv):
	'''no string'''

def glReadBuffer(*argv):
	'''no string'''

def glReadPixels(*argv):
	'''no string'''

def glRectd(*argv):
	'''no string'''

def glRectdv(*argv):
	'''no string'''

def glRectf(*argv):
	'''no string'''

def glRectfv(*argv):
	'''no string'''

def glRecti(*argv):
	'''no string'''

def glRectiv(*argv):
	'''no string'''

def glRects(*argv):
	'''no string'''

def glRectsv(*argv):
	'''no string'''

def glRenderMode(*argv):
	'''no string'''

def glRotated(*argv):
	'''no string'''

def glRotatef(*argv):
	'''no string'''

def glScaled(*argv):
	'''no string'''

def glScalef(*argv):
	'''no string'''

def glScissor(*argv):
	'''no string'''

def glSelectBuffer(*argv):
	'''no string'''

def glShadeModel(*argv):
	'''no string'''

def glShaderSource(*argv):
	'''no string'''

def glStencilFunc(*argv):
	'''no string'''

def glStencilMask(*argv):
	'''no string'''

def glStencilOp(*argv):
	'''no string'''

def glTexCoord1d(*argv):
	'''no string'''

def glTexCoord1dv(*argv):
	'''no string'''

def glTexCoord1f(*argv):
	'''no string'''

def glTexCoord1fv(*argv):
	'''no string'''

def glTexCoord1i(*argv):
	'''no string'''

def glTexCoord1iv(*argv):
	'''no string'''

def glTexCoord1s(*argv):
	'''no string'''

def glTexCoord1sv(*argv):
	'''no string'''

def glTexCoord2d(*argv):
	'''no string'''

def glTexCoord2dv(*argv):
	'''no string'''

def glTexCoord2f(*argv):
	'''no string'''

def glTexCoord2fv(*argv):
	'''no string'''

def glTexCoord2i(*argv):
	'''no string'''

def glTexCoord2iv(*argv):
	'''no string'''

def glTexCoord2s(*argv):
	'''no string'''

def glTexCoord2sv(*argv):
	'''no string'''

def glTexCoord3d(*argv):
	'''no string'''

def glTexCoord3dv(*argv):
	'''no string'''

def glTexCoord3f(*argv):
	'''no string'''

def glTexCoord3fv(*argv):
	'''no string'''

def glTexCoord3i(*argv):
	'''no string'''

def glTexCoord3iv(*argv):
	'''no string'''

def glTexCoord3s(*argv):
	'''no string'''

def glTexCoord3sv(*argv):
	'''no string'''

def glTexCoord4d(*argv):
	'''no string'''

def glTexCoord4dv(*argv):
	'''no string'''

def glTexCoord4f(*argv):
	'''no string'''

def glTexCoord4fv(*argv):
	'''no string'''

def glTexCoord4i(*argv):
	'''no string'''

def glTexCoord4iv(*argv):
	'''no string'''

def glTexCoord4s(*argv):
	'''no string'''

def glTexCoord4sv(*argv):
	'''no string'''

def glTexEnvf(*argv):
	'''no string'''

def glTexEnvfv(*argv):
	'''no string'''

def glTexEnvi(*argv):
	'''no string'''

def glTexEnviv(*argv):
	'''no string'''

def glTexGend(*argv):
	'''no string'''

def glTexGendv(*argv):
	'''no string'''

def glTexGenf(*argv):
	'''no string'''

def glTexGenfv(*argv):
	'''no string'''

def glTexGeni(*argv):
	'''no string'''

def glTexGeniv(*argv):
	'''no string'''

def glTexImage1D(*argv):
	'''no string'''

def glTexImage2D(*argv):
	'''no string'''

def glTexParameterf(*argv):
	'''no string'''

def glTexParameterfv(*argv):
	'''no string'''

def glTexParameteri(*argv):
	'''no string'''

def glTexParameteriv(*argv):
	'''no string'''

def glTranslated(*argv):
	'''no string'''

def glTranslatef(*argv):
	'''no string'''

def glUniform1f(*argv):
	'''no string'''

def glUniform1fv(*argv):
	'''no string'''

def glUniform1i(*argv):
	'''no string'''

def glUniform1iv(*argv):
	'''no string'''

def glUniform2f(*argv):
	'''no string'''

def glUniform2fv(*argv):
	'''no string'''

def glUniform2i(*argv):
	'''no string'''

def glUniform2iv(*argv):
	'''no string'''

def glUniform3f(*argv):
	'''no string'''

def glUniform3fv(*argv):
	'''no string'''

def glUniform3i(*argv):
	'''no string'''

def glUniform3iv(*argv):
	'''no string'''

def glUniform4f(*argv):
	'''no string'''

def glUniform4fv(*argv):
	'''no string'''

def glUniform4i(*argv):
	'''no string'''

def glUniform4iv(*argv):
	'''no string'''

def glUniformMatrix2fv(*argv):
	'''no string'''

def glUniformMatrix2x3fv(*argv):
	'''no string'''

def glUniformMatrix2x4fv(*argv):
	'''no string'''

def glUniformMatrix3fv(*argv):
	'''no string'''

def glUniformMatrix3x2fv(*argv):
	'''no string'''

def glUniformMatrix3x4fv(*argv):
	'''no string'''

def glUniformMatrix4fv(*argv):
	'''no string'''

def glUniformMatrix4x2fv(*argv):
	'''no string'''

def glUniformMatrix4x3fv(*argv):
	'''no string'''

def glUseProgram(*argv):
	'''no string'''

def glValidateProgram(*argv):
	'''no string'''

def glVertex2d(*argv):
	'''no string'''

def glVertex2dv(*argv):
	'''no string'''

def glVertex2f(*argv):
	'''no string'''

def glVertex2fv(*argv):
	'''no string'''

def glVertex2i(*argv):
	'''no string'''

def glVertex2iv(*argv):
	'''no string'''

def glVertex2s(*argv):
	'''no string'''

def glVertex2sv(*argv):
	'''no string'''

def glVertex3d(*argv):
	'''no string'''

def glVertex3dv(*argv):
	'''no string'''

def glVertex3f(*argv):
	'''no string'''

def glVertex3fv(*argv):
	'''no string'''

def glVertex3i(*argv):
	'''no string'''

def glVertex3iv(*argv):
	'''no string'''

def glVertex3s(*argv):
	'''no string'''

def glVertex3sv(*argv):
	'''no string'''

def glVertex4d(*argv):
	'''no string'''

def glVertex4dv(*argv):
	'''no string'''

def glVertex4f(*argv):
	'''no string'''

def glVertex4fv(*argv):
	'''no string'''

def glVertex4i(*argv):
	'''no string'''

def glVertex4iv(*argv):
	'''no string'''

def glVertex4s(*argv):
	'''no string'''

def glVertex4sv(*argv):
	'''no string'''

def glViewport(*argv):
	'''no string'''

def gluLookAt(*argv):
	'''no string'''

def gluOrtho2D(*argv):
	'''no string'''

def gluPerspective(*argv):
	'''no string'''

def gluPickMatrix(*argv):
	'''no string'''

def gluProject(*argv):
	'''no string'''

def gluUnProject(*argv):
	'''no string'''


