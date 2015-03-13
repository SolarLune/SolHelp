class constraints:
	def createConstraint(physicsid, physicsid2, constrainttype, pivotX, pivotY, pivotZ, axisX, axisY, axisZ, flag):
		'''
	   Creates a constraint.
	
	   :arg physicsid: the physics id of the first object in constraint
	   :type physicsid: int
	
	   :arg physicsid2: the physics id of the second object in constraint
	   :type physicsid2: int
	
	   :arg constrainttype: the type of the constraint. The constraint types are:
	
	   - :class:`POINTTOPOINT_CONSTRAINT`
	   - :class:`LINEHINGE_CONSTRAINT`
	   - :class:`ANGULAR_CONSTRAINT`
	   - :class:`CONETWIST_CONSTRAINT`
	   - :class:`VEHICLE_CONSTRAINT`
	
	   :type constrainttype: int
	
	   :arg pivotX: pivot X position
	   :type pivotX: float
	
	   :arg pivotY: pivot Y position
	   :type pivotY: float
	
	   :arg pivotZ: pivot Z position
	   :type pivotZ: float
	
	   :arg axisX: X axis
	   :type axisX: float
	
	   :arg axisY: Y axis
	   :type axisY: float
	
	   :arg axisZ: Z axis
	   :type axisZ: float
	
	   :arg flag: .. to do
	   :type flag: int
	
		'''
		pass

	def exportBulletFile(filename):
		'''
	   export a .bullet file
	
	   :arg filename: File name
	   :type filename: string
	
		'''
		pass

	def getAppliedImpulse(constraintId):
		'''
	   :arg constraintId: The id of the constraint.
	   :type constraintId: int
	
	   :return: the most recent applied impulse.
	   :rtype: float
	
		'''
		pass

	def getVehicleConstraint(constraintId):
		'''
	   :arg constraintId: The id of the vehicle constraint.
	   :type constraintId: int
	
	   :return: a vehicle constraint object.
	   :rtype: :class:`bge.types.KX_VehicleWrapper`
	
		'''
		pass

	def getCharacter(gameobj):
		'''
	   :arg gameobj: The game object with the character physics.
	   :type gameobj: :class:`bge.types.KX_GameObject`
	
	   :return: character wrapper
	   :rtype: :class:`bge.types.KX_CharacterWrapper`
	
		'''
		pass

	def removeConstraint(constraintId):
		'''
	   Removes a constraint.
	
	   :arg constraintId: The id of the constraint to be removed.
	   :type constraintId: int
	
		'''
		pass

	def setCcdMode(ccdMode):
		'''
	   .. note::
	      Very experimental, not recommended
	
	   Sets the CCD (Continous Colision Detection) mode in the Physics Environment.
	
	   :arg ccdMode: The new CCD mode.
	   :type ccdMode: int
	
		'''
		pass

	def setContactBreakingTreshold(breakingTreshold):
		'''
	   .. note::
	      Reasonable default is 0.02 (if units are meters)
	
	   Sets tresholds to do with contact point management.
	
	   :arg breakingTreshold: The new contact breaking treshold.
	   :type breakingTreshold: float
	
		'''
		pass

	def setDeactivationAngularTreshold(angularTreshold):
		'''
	   Sets the angular velocity treshold.
	
	   :arg angularTreshold: New deactivation angular treshold.
	   :type angularTreshold: float
	
		'''
		pass

	def setDeactivationLinearTreshold(linearTreshold):
		'''
	   Sets the linear velocity treshold.
	
	   :arg linearTreshold: New deactivation linear treshold.
	   :type linearTreshold: float
	
		'''
		pass

	def setDeactivationTime(time):
		'''
	   Sets the time after which a resting rigidbody gets deactived.
	
	   :arg time: The deactivation time.
	   :type time: float
	
		'''
		pass

	def setDebugMode(mode):
		'''
	   Sets the debug mode.
	
	   Debug modes:
	      - :class:`DBG_NODEBUG`
	      - :class:`DBG_DRAWWIREFRAME`
	      - :class:`DBG_DRAWAABB`
	      - :class:`DBG_DRAWFREATURESTEXT`
	      - :class:`DBG_DRAWCONTACTPOINTS`
	      - :class:`DBG_NOHELPTEXT`
	      - :class:`DBG_DRAWTEXT`
	      - :class:`DBG_PROFILETIMINGS`
	      - :class:`DBG_ENABLESATCOMPARISION`
	      - :class:`DBG_DISABLEBULLETLCP`
	      - :class:`DBG_ENABLECCD`
	      - :class:`DBG_DRAWCONSTRAINTS`
	      - :class:`DBG_DRAWCONSTRAINTLIMITS`
	      - :class:`DBG_FASTWIREFRAME`
	
	   :arg mode: The new debug mode.
	   :type mode: int
	
		'''
		pass

	def setGravity(x, y, z):
		'''
	   Sets the gravity force.
	
	   :arg x: Gravity X force.
	   :type x: float
	
	   :arg y: Gravity Y force.
	   :type y: float
	
	   :arg z: Gravity Z force.
	   :type z: float
	
		'''
		pass

	def setLinearAirDamping(damping):
		'''
	   .. note::
	      Not implemented.
	
	   Sets the linear air damping for rigidbodies.
	
		'''
		pass

	def setNumIterations(numiter):
		'''
	   Sets the number of iterations for an iterative constraint solver.
	
	   :arg numiter: New number of iterations.
	   :type numiter: int
	
		'''
		pass

	def setNumTimeSubSteps(numsubstep):
		'''
	   Sets the number of substeps for each physics proceed. Tradeoff quality for performance.
	
	   :arg numsubstep: New number of substeps.
	   :type numsubstep: int
	
		'''
		pass

	def setSolverDamping(damping):
		'''
	   .. note::
	      Very experimental, not recommended
	
	   Sets the damper constant of a penalty based solver.
	
	   :arg damping: New damping for the solver.
	   :type damping: float
	
		'''
		pass

	def setSolverTau(tau):
		'''
	   .. note::
	      Very experimental, not recommended
	
	   Sets the spring constant of a penalty based solver.
	
	   :arg tau: New tau for the solver.
	   :type tau: float
	
		'''
		pass

	def setSolverType(solverType):
		'''
	   .. note::
	      Very experimental, not recommended
	
	   Sets the solver type.
	
	   :arg solverType: The new type of the solver.
	   :type solverType: int
	
		'''
		pass

	def setSorConstant(sor):
		'''
	   .. note::
	      Very experimental, not recommended
	
	   Sets the successive overrelaxation constant.
	
	   :arg sor: New sor value.
	   :type sor: float
	
		'''
		pass

	def setUseEpa(epa):
		'''
	   Not implemented.
	
		'''
		pass

	error = None
	'''
	   Simbolic constant string that indicates error.
	
	'''

	DBG_NODEBUG = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   No debug.
	
	'''

	DBG_DRAWWIREFRAME = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   Draw wireframe in debug.
	
	'''

	DBG_DRAWAABB = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   Draw Axis Aligned Bounding Box in debug.
	
	'''

	DBG_DRAWFREATURESTEXT = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   Draw freatures text in debug.
	
	'''

	DBG_DRAWCONTACTPOINTS = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   Draw contact points in debug.
	
	'''

	DBG_NOHELPTEXT = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   Debug without help text.
	
	'''

	DBG_DRAWTEXT = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   Draw text in debug.
	
	'''

	DBG_PROFILETIMINGS = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   Draw profile timings in debug.
	
	'''

	DBG_ENABLESATCOMPARISION = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   Enable sat comparision in debug.
	
	'''

	DBG_DISABLEBULLETLCP = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   Disable Bullet LCP.
	
	'''

	DBG_ENABLECCD = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   Enable Continous Colision Detection in debug.
	
	'''

	DBG_DRAWCONSTRAINTS = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   Draw constraints in debug.
	
	'''

	DBG_DRAWCONSTRAINTLIMITS = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   Draw constraint limits in debug.
	
	'''

	DBG_FASTWIREFRAME = None
	'''
	   .. note::
	      Debug mode to be used with function :class:`setDebugMode`
	
	   Draw a fast wireframe in debug.
	
	'''

	POINTTOPOINT_CONSTRAINT = None
	'''
	   .. note::
	      Constraint type to be used with function :class:`createConstraint`
	
	   .. to do
	
	'''

	LINEHINGE_CONSTRAINT = None
	'''
	   .. note::
	      Constraint type to be used with function :class:`createConstraint`
	
	   .. to do
	
	'''

	ANGULAR_CONSTRAINT = None
	'''
	   .. note::
	      Constraint type to be used with function :class:`createConstraint`
	
	   .. to do
	
	'''

	CONETWIST_CONSTRAINT = None
	'''
	   .. note::
	       Constraint type to be used with function :class:`createConstraint`
	
	   .. to do
	
	'''

	VEHICLE_CONSTRAINT = None
	'''
	   .. note::
	      Constraint type to be used with function :class:`createConstraint`
	
	   .. to do
	'''

class events:
	def EventToString(event):
		'''
	   Return the string name of a key event. Will raise a ValueError error if its invalid.
	
	   :arg event: key event constant from :mod:`bge.events` or the keyboard sensor.
	   :type event: int
	   :rtype: string
	
		'''
		pass

	def EventToCharacter(event, shift):
		'''
	   Return the string name of a key event. Returns an empty string if the event cant be represented as a character.
	
	   :type event: int
	   :arg event: key event constant from :mod:`bge.events` or the keyboard sensor.
	   :type shift: bool
	   :arg shift: set to true if shift is held.
	   :rtype: string
	
		'''
		pass

	LEFTMOUSE = None
	MIDDLEMOUSE = None
	RIGHTMOUSE = None
	WHEELUPMOUSE = None
	WHEELDOWNMOUSE = None
	MOUSEX = None
	MOUSEY = None
	AKEY = None
	BKEY = None
	CKEY = None
	DKEY = None
	EKEY = None
	FKEY = None
	GKEY = None
	HKEY = None
	IKEY = None
	JKEY = None
	KKEY = None
	LKEY = None
	MKEY = None
	NKEY = None
	OKEY = None
	PKEY = None
	QKEY = None
	RKEY = None
	SKEY = None
	TKEY = None
	UKEY = None
	VKEY = None
	WKEY = None
	XKEY = None
	YKEY = None
	ZKEY = None
	ZEROKEY = None
	ONEKEY = None
	TWOKEY = None
	THREEKEY = None
	FOURKEY = None
	FIVEKEY = None
	SIXKEY = None
	SEVENKEY = None
	EIGHTKEY = None
	NINEKEY = None
	CAPSLOCKKEY = None
	LEFTCTRLKEY = None
	LEFTALTKEY = None
	RIGHTALTKEY = None
	RIGHTCTRLKEY = None
	RIGHTSHIFTKEY = None
	LEFTSHIFTKEY = None
	LEFTARROWKEY = None
	DOWNARROWKEY = None
	RIGHTARROWKEY = None
	UPARROWKEY = None
	PAD0 = None
	PAD1 = None
	PAD2 = None
	PAD3 = None
	PAD4 = None
	PAD5 = None
	PAD6 = None
	PAD7 = None
	PAD8 = None
	PAD9 = None
	PADPERIOD = None
	PADSLASHKEY = None
	PADASTERKEY = None
	PADMINUS = None
	PADENTER = None
	PADPLUSKEY = None
	F1KEY = None
	F2KEY = None
	F3KEY = None
	F4KEY = None
	F5KEY = None
	F6KEY = None
	F7KEY = None
	F8KEY = None
	F9KEY = None
	F10KEY = None
	F11KEY = None
	F12KEY = None
	F13KEY = None
	F14KEY = None
	F15KEY = None
	F16KEY = None
	F17KEY = None
	F18KEY = None
	F19KEY = None
	ACCENTGRAVEKEY = None
	BACKSLASHKEY = None
	BACKSPACEKEY = None
	COMMAKEY = None
	DELKEY = None
	ENDKEY = None
	EQUALKEY = None
	ESCKEY = None
	HOMEKEY = None
	INSERTKEY = None
	LEFTBRACKETKEY = None
	LINEFEEDKEY = None
	MINUSKEY = None
	PAGEDOWNKEY = None
	PAGEUPKEY = None
	PAUSEKEY = None
	PERIODKEY = None
	QUOTEKEY = None
	RIGHTBRACKETKEY = None
	ENTERKEY = None
	SEMICOLONKEY = None
	SLASHKEY = None
	SPACEKEY = None
	TABKEY = None
class logic:
	def getCurrentController():
		'''
	   Gets the Python controller associated with this Python script.
	   
	   :rtype: :class:`bge.types.SCA_PythonController`
	
		'''
		pass

	def getCurrentScene():
		'''
	   Gets the current Scene.
	   
	   :rtype: :class:`bge.types.KX_Scene`
	
		'''
		pass

	def getSceneList():
		'''
	   Gets a list of the current scenes loaded in the game engine.
	   
	   :rtype: list of :class:`bge.types.KX_Scene`
	   
	   .. note:: Scenes in your blend file that have not been converted wont be in this list. This list will only contain scenes such as overlays scenes.
	
		'''
		pass

	def loadGlobalDict():
		'''
	   Loads bge.logic.globalDict from a file.
	
		'''
		pass

	def saveGlobalDict():
		'''
	   Saves bge.logic.globalDict to a file.
	
		'''
		pass

	def startGame(blend):
		'''
	   Loads the blend file.
	   
	   :arg blend: The name of the blend file
	   :type blend: string
	
		'''
		pass

	def endGame():
		'''
	   Ends the current game.
	
		'''
		pass

	def restartGame():
		'''
	   Restarts the current game by reloading the .blend file (the last saved version, not what is currently running).
	   
		'''
		pass

	def LibLoad(blend, type, data, load_actions=False, verbose=False, load_scripts=True, async=False):
		'''   
	   Converts the all of the datablocks of the given type from the given blend.
	   
	   :arg blend: The path to the blend file (or the name to use for the library if data is supplied)
	   :type blend: string
	   :arg type: The datablock type (currently only "Action", "Mesh" and "Scene" are supported)
	   :type type: string
	   :arg data: Binary data from a blend file (optional)
	   :type data: bytes
	   :arg load_actions: Search for and load all actions in a given Scene and not just the "active" actions (Scene type only)
	   :type load_actions: bool
	   :arg verbose: Whether or not to print debugging information (e.g., "SceneName: Scene")
	   :type verbose: bool
	   :arg load_scripts: Whether or not to load text datablocks as well (can be disabled for some extra security)
	   :type load_scripts: bool   
	   :arg async: Whether or not to do the loading asynchronously (in another thread). Only the "Scene" type is currently supported for this feature.
	   :type async: bool
	   
	   :rtype: :class:`bge.types.KX_LibLoadStatus`
	
	   .. note:: Asynchronously loaded libraries will not be available immediately after LibLoad() returns. Use the returned KX_LibLoadStatus to figure out when the libraries are ready.
	   
		'''
		pass

	def LibNew(name, type, data):
		'''
	   Uses existing datablock data and loads in as a new library.
	   
	   :arg name: A unique library name used for removal later
	   :type name: string
	   :arg type: The datablock type (currently only "Mesh" is supported)
	   :type type: string
	   :arg data: A list of names of the datablocks to load
	   :type data: list of strings
	   
		'''
		pass

	def LibFree(name):
		'''
	   Frees a library, removing all objects and meshes from the currently active scenes.
	
	   :arg name: The name of the library to free (the name used in LibNew)
	   :type name: string
	   
		'''
		pass

	def LibList():
		'''
	   Returns a list of currently loaded libraries.
	   
	   :rtype: list [str]
	
		'''
		pass

	def addScene(name, overlay=1):
		'''
	   Loads a scene into the game engine.
	
	   .. note::
	
	      This function is not effective immediately, the scene is queued
	      and added on the next logic cycle where it will be available
	      from `getSceneList`
	
	   :arg name: The name of the scene
	   :type name: string
	   :arg overlay: Overlay or underlay (optional)
	   :type overlay: integer
	
		'''
		pass

	def sendMessage(subject, body="", to="", message_from=""):
		'''
	   Sends a message to sensors in any active scene.
	   
	   :arg subject: The subject of the message
	   :type subject: string
	   :arg body: The body of the message (optional)
	   :type body: string
	   :arg to: The name of the object to send the message to (optional)
	   :type to: string
	   :arg message_from: The name of the object that the message is coming from (optional)
	   :type message_from: string
	
		'''
		pass

	def setGravity(gravity):
		'''
	   Sets the world gravity.
	   
	   :type gravity: list [fx, fy, fz]
	
		'''
		pass

	def getSpectrum():
		'''
	   Returns a 512 point list from the sound card.
	   This only works if the fmod sound driver is being used.
	   
	   :rtype: list [float], len(getSpectrum()) == 512
	
		'''
		pass

	def getMaxLogicFrame():
		'''
	   Gets the maximum number of logic frames per render frame.
	   
	   :return: The maximum number of logic frames per render frame
	   :rtype: integer
	
		'''
		pass

	def setMaxLogicFrame(maxlogic):
		'''
	   Sets the maximum number of logic frames that are executed per render frame.
	   This does not affect the physic system that still runs at full frame rate.   
	    
	   :arg maxlogic: The new maximum number of logic frames per render frame. Valid values: 1..5
	   :type maxlogic: integer
	
		'''
		pass

	def getMaxPhysicsFrame():
		'''
	   Gets the maximum number of physics frames per render frame.
	   
	   :return: The maximum number of physics frames per render frame
	   :rtype: integer
	
		'''
		pass

	def setMaxPhysicsFrame(maxphysics):
		'''
	   Sets the maximum number of physics timestep that are executed per render frame.
	   Higher value allows physics to keep up with realtime even if graphics slows down the game.
	   Physics timestep is fixed and equal to 1/tickrate (see setLogicTicRate)
	   maxphysics/ticrate is the maximum delay of the renderer that physics can compensate.
	    
	   :arg maxphysics: The new maximum number of physics timestep per render frame. Valid values: 1..5.
	   :type maxphysics: integer
	
		'''
		pass

	def getLogicTicRate():
		'''
	   Gets the logic update frequency.
	   
	   :return: The logic frequency in Hz
	   :rtype: float
	
		'''
		pass

	def setLogicTicRate(ticrate):
		'''
	   Sets the logic update frequency.
	   
	   The logic update frequency is the number of times logic bricks are executed every second.
	   The default is 60 Hz.
	   
	   :arg ticrate: The new logic update frequency (in Hz).
	   :type ticrate: float
	
		'''
		pass

	def getPhysicsTicRate():
		'''
	   Gets the physics update frequency
	   
	   :return: The physics update frequency in Hz
	   :rtype: float
	   
	   .. warning: Not implimented yet
	
		'''
		pass

	def setPhysicsTicRate(ticrate):
		'''
	   Sets the physics update frequency
	   
	   The physics update frequency is the number of times the physics system is executed every second.
	   The default is 60 Hz.
	   
	   :arg ticrate: The new update frequency (in Hz).
	   :type ticrate: float
	
	   .. warning: Not implimented yet
	
		'''
		pass

	def getExitKey():
		'''
	   Gets the key used to exit the game engine
	
	   :return: The key (defaults to :mod:`bge.events.ESCKEY`)
	   :rtype: int
	
		'''
		pass

	def setExitKey(key):
		'''
	   Sets the key used to exit the game engine
	
	   :arg key: A key constant from :mod:`bge.events`
	   :type key: int
	
		'''
		pass

	def NextFrame():
		'''
	   Render next frame (if Python has control)
	
		'''
		pass

	def expandPath(path):
		'''
	   Converts a blender internal path into a proper file system path.
	
	   Use / as directory separator in path
	   You can use '//' at the start of the string to define a relative path;
	   Blender replaces that string by the directory of the current .blend or runtime file
	   to make a full path name. The function also converts the directory separator to
	   the local file system format.
	
	   :arg path: The path string to be converted/expanded.
	   :type path: string
	   :return: The converted string
	   :rtype: string
	
		'''
		pass

	def getAverageFrameRate():
		'''
	   Gets the estimated/average framerate for all the active scenes, not only the current scene.
	
	   :return: The estimated average framerate in frames per second
	   :rtype: float
	
		'''
		pass

	def getBlendFileList(path = "//"):
		'''
	   Returns a list of blend files in the same directory as the open blend file, or from using the option argument.
	
	   :arg path: Optional directory argument, will be expanded (like expandPath) into the full path.
	   :type path: string
	   :return: A list of filenames, with no directory prefix
	   :rtype: list
	
		'''
		pass

	def getRandomFloat():
		'''
	   Returns a random floating point value in the range [0 - 1)
	
		'''
		pass

	def PrintGLInfo():
		'''
	   Prints GL Extension Info into the console
	
		'''
		pass

	def PrintMemInfo():
		'''
	   Prints engine statistics into the console
	
		'''
		pass

	def getProfileInfo():
		'''
	   Returns a Python dictionary that contains the same information as the on screen profiler. The keys are the profiler categories and the values are tuples with the first element being time taken (in ms) and the second element being the percentage of total time.
	   
		'''
		pass

	globalDict = None
	'''
	   A dictionary that is saved between loading blend files so you can use it to store inventory and other variables you want to store between scenes and blend files.
	   It can also be written to a file and loaded later on with the game load/save actuators.
	
	   .. note:: only python built in types such as int/string/bool/float/tuples/lists can be saved, GameObjects, Actuators etc will not work as expected.
	
	'''

	keyboard = None
	'''
	   The current keyboard wrapped in an :class:`~bge.types.SCA_PythonKeyboard` object.
	
	'''

	mouse = None
	'''
	   The current mouse wrapped in an :class:`~bge.types.SCA_PythonMouse` object.
	
	'''

	joysticks = None
	'''
	   A list of attached :class:`~bge.types.SCA_PythonJoystick`.
	   The list size is the maximum number of supported joysticks.
	   If no joystick is available for a given slot, the slot is set to None.
	
	'''

	KX_TRUE = None
	'''
	   True value used by some modules.
	
	'''

	KX_FALSE = None
	'''
	   False value used by some modules.
	
	'''

	KX_SENSOR_INACTIVE = None
	KX_SENSOR_JUST_ACTIVATED = None
	KX_SENSOR_ACTIVE = None
	KX_SENSOR_JUST_DEACTIVATED = None
	KX_ARMSENSOR_STATE_CHANGED = None
	'''
	  Detect that the constraint is changing state (active/inactive)
	
	  :value: 0
	  
	'''

	KX_ARMSENSOR_LIN_ERROR_BELOW = None
	'''
	  Detect that the constraint linear error is above a threshold
	  
	  :value: 1
	  
	'''

	KX_ARMSENSOR_LIN_ERROR_ABOVE = None
	'''
	  Detect that the constraint linear error is below a threshold
	
	  :value: 2
	  
	'''

	KX_ARMSENSOR_ROT_ERROR_BELOW = None
	'''
	  Detect that the constraint rotation error is above a threshold
	  
	  :value: 3
	  
	'''

	KX_ARMSENSOR_ROT_ERROR_ABOVE = None
	'''
	  Detect that the constraint rotation error is below a threshold
	  
	  :value: 4
	  
	
	'''

	KX_PROPSENSOR_EQUAL = None
	'''
	   Activate when the property is equal to the sensor value.
	
	   :value: 1
	
	'''

	KX_PROPSENSOR_NOTEQUAL = None
	'''
	   Activate when the property is not equal to the sensor value.
	   
	   :value: 2
	
	'''

	KX_PROPSENSOR_INTERVAL = None
	'''
	   Activate when the property is between the specified limits.
	   
	   :value: 3
	   
	'''

	KX_PROPSENSOR_CHANGED = None
	'''
	   Activate when the property changes   
	
	   :value: 4
	
	'''

	KX_PROPSENSOR_EXPRESSION = None
	'''
	   Activate when the expression matches
	   
	   :value: 5
	
	'''

	KX_RADAR_AXIS_POS_X = None
	KX_RADAR_AXIS_POS_Y = None
	KX_RADAR_AXIS_POS_Z = None
	KX_RADAR_AXIS_NEG_X = None
	KX_RADAR_AXIS_NEG_Y = None
	KX_RADAR_AXIS_NEG_Z = None
	KX_RAY_AXIS_POS_X = None
	KX_RAY_AXIS_POS_Y = None
	KX_RAY_AXIS_POS_Z = None
	KX_RAY_AXIS_NEG_X = None
	KX_RAY_AXIS_NEG_Y = None
	KX_RAY_AXIS_NEG_Z = None
	KX_ACTIONACT_PLAY = None
	KX_ACTIONACT_PINGPONG = None
	KX_ACTIONACT_FLIPPER = None
	KX_ACTIONACT_LOOPSTOP = None
	KX_ACTIONACT_LOOPEND = None
	KX_ACTIONACT_PROPERTY = None
	KX_ACT_ARMATURE_RUN = None
	'''
	  Just make sure the armature will be updated on the next graphic frame.
	  This is the only persistent mode of the actuator:
	  it executes automatically once per frame until stopped by a controller
	  
	  :value: 0
	
	'''

	KX_ACT_ARMATURE_ENABLE = None
	'''
	  Enable the constraint.
	
	  :value: 1
	
	'''

	KX_ACT_ARMATURE_DISABLE = None
	'''
	  Disable the constraint (runtime constraint values are not updated).
	
	  :value: 2
	
	'''

	KX_ACT_ARMATURE_SETTARGET = None
	'''
	  Change target and subtarget of constraint.
	  
	  :value: 3
	
	'''

	KX_ACT_ARMATURE_SETWEIGHT = None
	'''
	  Change weight of constraint (IK only).
	
	  :value: 4
	
	'''

	KX_ACT_ARMATURE_SETINFLUENCE = None
	'''
	  Change influence of constraint.
	
	  :value: 5
	
	'''

	KX_CONSTRAINTACT_NORMAL = None
	'''
	     Activate alignment to surface
	   
	'''

	KX_CONSTRAINTACT_DISTANCE = None
	'''
	     Activate distance control
	
	'''

	KX_CONSTRAINTACT_LOCAL = None
	'''
	     Direction of the ray is along the local axis
	
	'''

	KX_CONSTRAINTACT_DOROTFH = None
	'''
	     Force field act on rotation as well
	
	'''

	KX_CONSTRAINTACT_MATERIAL = None
	'''
	     Detect material rather than property
	   
	'''

	KX_CONSTRAINTACT_PERMANENT = None
	'''
	     No deactivation if ray does not hit target
	
	'''

	KX_CONSTRAINTACT_LOCX = None
	'''
	   Limit X coord.
	   
	'''

	KX_CONSTRAINTACT_LOCY = None
	'''
	   Limit Y coord
	
	'''

	KX_CONSTRAINTACT_LOCZ = None
	'''
	   Limit Z coord
	   
	'''

	KX_CONSTRAINTACT_ROTX = None
	'''
	   Limit X rotation
	
	'''

	KX_CONSTRAINTACT_ROTY = None
	'''
	   Limit Y rotation
	   
	'''

	KX_CONSTRAINTACT_ROTZ = None
	'''
	   Limit Z rotation
	   
	'''

	KX_CONSTRAINTACT_DIRNX = None
	'''
	   Set distance along negative X axis
	
	'''

	KX_CONSTRAINTACT_DIRNY = None
	'''
	   Set distance along negative Y axis
	   
	'''

	KX_CONSTRAINTACT_DIRNZ = None
	'''
	   Set distance along negative Z axis
	   
	'''

	KX_CONSTRAINTACT_DIRPX = None
	'''
	   Set distance along positive X axis
	
	'''

	KX_CONSTRAINTACT_DIRPY = None
	'''
	   Set distance along positive Y axis
	   
	'''

	KX_CONSTRAINTACT_DIRPZ = None
	'''
	   Set distance along positive Z axis
	   
	'''

	KX_CONSTRAINTACT_ORIX = None
	'''
	   Set orientation of X axis
	   
	'''

	KX_CONSTRAINTACT_ORIY = None
	'''
	   Set orientation of Y axis
	   
	'''

	KX_CONSTRAINTACT_ORIZ = None
	'''
	   Set orientation of Z axis
	   
	'''

	KX_CONSTRAINTACT_FHNX = None
	'''
	   Set force field along negative X axis
	   
	'''

	KX_CONSTRAINTACT_FHNY = None
	'''
	   Set force field along negative Y axis
	   
	'''

	KX_CONSTRAINTACT_FHNZ = None
	'''
	   Set force field along negative Z axis
	   
	'''

	KX_CONSTRAINTACT_FHPX = None
	'''
	   Set force field along positive X axis
	
	'''

	KX_CONSTRAINTACT_FHPY = None
	'''
	   Set force field along positive Y axis
	   
	'''

	KX_CONSTRAINTACT_FHPZ = None
	'''
	   Set force field along positive Z axis
	
	'''

	KX_DYN_RESTORE_DYNAMICS = None
	KX_DYN_DISABLE_DYNAMICS = None
	KX_DYN_ENABLE_RIGID_BODY = None
	KX_DYN_DISABLE_RIGID_BODY = None
	KX_DYN_SET_MASS = None
	KX_GAME_LOAD = None
	KX_GAME_START = None
	KX_GAME_RESTART = None
	KX_GAME_QUIT = None
	KX_GAME_SAVECFG = None
	KX_GAME_LOADCFG = None
	KX_PARENT_REMOVE = None
	KX_PARENT_SET = None
	KX_RANDOMACT_BOOL_CONST = None
	KX_RANDOMACT_BOOL_UNIFORM = None
	KX_RANDOMACT_BOOL_BERNOUILLI = None
	KX_RANDOMACT_INT_CONST = None
	KX_RANDOMACT_INT_UNIFORM = None
	KX_RANDOMACT_INT_POISSON = None
	KX_RANDOMACT_FLOAT_CONST = None
	KX_RANDOMACT_FLOAT_UNIFORM = None
	KX_RANDOMACT_FLOAT_NORMAL = None
	KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL = None
	KX_SCENE_RESTART = None
	KX_SCENE_SET_SCENE = None
	KX_SCENE_SET_CAMERA = None
	KX_SCENE_ADD_FRONT_SCENE = None
	KX_SCENE_ADD_BACK_SCENE = None
	KX_SCENE_REMOVE_SCENE = None
	KX_SCENE_SUSPEND = None
	KX_SCENE_RESUME = None
	KX_SOUNDACT_PLAYSTOP = None
	'''
	   :value: 1
	   
	'''

	KX_SOUNDACT_PLAYEND = None
	'''
	   :value: 2
	   
	'''

	KX_SOUNDACT_LOOPSTOP = None
	'''
	   :value: 3
	   
	'''

	KX_SOUNDACT_LOOPEND = None
	'''
	   :value: 4
	   
	'''

	KX_SOUNDACT_LOOPBIDIRECTIONAL = None
	'''
	   :value: 5
	   
	'''

	KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP = None
	'''
	   :value: 6
	
	'''

	KX_STEERING_SEEK = None
	'''
	   :value: 1
	
	'''

	KX_STEERING_FLEE = None
	'''
	   :value: 2
	
	'''

	KX_STEERING_PATHFOLLOWING = None
	'''
	   :value: 3
	
	
	'''

	RAS_2DFILTER_BLUR = None
	'''
	   :value: 2
	   
	'''

	RAS_2DFILTER_CUSTOMFILTER = None
	'''
	   Customer filter, the code code is set via shaderText property.
	   
	   :value: 12
	   
	'''

	RAS_2DFILTER_DILATION = None
	'''
	   :value: 4
	   
	'''

	RAS_2DFILTER_DISABLED = None
	'''
	   Disable the filter that is currently active
	
	   :value: -1
	   
	'''

	RAS_2DFILTER_ENABLED = None
	'''
	   Enable the filter that was previously disabled
	
	   :value: -2
	   
	'''

	RAS_2DFILTER_EROSION = None
	'''
	   :value: 5
	   
	'''

	RAS_2DFILTER_GRAYSCALE = None
	'''
	   :value: 9
	   
	'''

	RAS_2DFILTER_INVERT = None
	'''
	   :value: 11
	   
	'''

	RAS_2DFILTER_LAPLACIAN = None
	'''
	   :value: 6
	   
	'''

	RAS_2DFILTER_MOTIONBLUR = None
	'''
	   Create and enable preset filters
	
	   :value: 1
	   
	'''

	RAS_2DFILTER_NOFILTER = None
	'''
	   Disable and destroy the filter that is currently active
	
	   :value: 0
	   
	'''

	RAS_2DFILTER_PREWITT = None
	'''
	   :value: 8
	   
	'''

	RAS_2DFILTER_SEPIA = None
	'''
	   :value: 10
	   
	'''

	RAS_2DFILTER_SHARPEN = None
	'''
	   :value: 3
	   
	'''

	RAS_2DFILTER_SOBEL = None
	'''
	   :value: 7
	
	'''

	ROT_MODE_QUAT = None
	'''
	  Use quaternion in rotation attribute to update bone rotation.
	
	  :value: 0
	
	'''

	ROT_MODE_XYZ = None
	'''
	  Use euler_rotation and apply angles on bone's Z, Y, X axis successively.
	
	  :value: 1
	
	'''

	ROT_MODE_XZY = None
	'''
	  Use euler_rotation and apply angles on bone's Y, Z, X axis successively.
	
	  :value: 2
	
	'''

	ROT_MODE_YXZ = None
	'''
	  Use euler_rotation and apply angles on bone's Z, X, Y axis successively.
	
	  :value: 3
	
	'''

	ROT_MODE_YZX = None
	'''
	  Use euler_rotation and apply angles on bone's X, Z, Y axis successively.
	
	  :value: 4
	
	'''

	ROT_MODE_ZXY = None
	'''
	  Use euler_rotation and apply angles on bone's Y, X, Z axis successively.
	
	  :value: 5
	
	'''

	ROT_MODE_ZYX = None
	'''
	  Use euler_rotation and apply angles on bone's X, Y, Z axis successively.
	
	  :value: 6
	
	
	'''

	CONSTRAINT_TYPE_TRACKTO = None
	CONSTRAINT_TYPE_KINEMATIC = None
	CONSTRAINT_TYPE_ROTLIKE = None
	CONSTRAINT_TYPE_LOCLIKE = None
	CONSTRAINT_TYPE_MINMAX = None
	CONSTRAINT_TYPE_SIZELIKE = None
	CONSTRAINT_TYPE_LOCKTRACK = None
	CONSTRAINT_TYPE_STRETCHTO = None
	CONSTRAINT_TYPE_CLAMPTO = None
	CONSTRAINT_TYPE_TRANSFORM = None
	CONSTRAINT_TYPE_DISTLIMIT = None
	CONSTRAINT_IK_COPYPOSE = None
	'''
	   constraint is trying to match the position and eventually the rotation of the target.
	
	   :value: 0
	
	'''

	CONSTRAINT_IK_DISTANCE = None
	'''
	   Constraint is maintaining a certain distance to target subject to ik_mode
	
	   :value: 1
	
	'''

	CONSTRAINT_IK_FLAG_TIP = None
	'''
	   Set when the constraint operates on the head of the bone and not the tail
	
	   :value: 1
	
	'''

	CONSTRAINT_IK_FLAG_ROT = None
	'''
	   Set when the constraint tries to match the orientation of the target
	
	   :value: 2
	
	'''

	CONSTRAINT_IK_FLAG_STRETCH = None
	'''
	   Set when the armature is allowed to stretch (only the bones with stretch factor > 0.0)
	
	   :value: 16
	   
	'''

	CONSTRAINT_IK_FLAG_POS = None
	'''
	   Set when the constraint tries to match the position of the target.
	
	   :value: 32
	
	'''

	CONSTRAINT_IK_MODE_INSIDE = None
	'''
	   The constraint tries to keep the bone within ik_dist of target
	
	   :value: 0
	
	'''

	CONSTRAINT_IK_MODE_OUTSIDE = None
	'''
	   The constraint tries to keep the bone outside ik_dist of the target
	
	   :value: 1
	   
	'''

	CONSTRAINT_IK_MODE_ONSURFACE = None
	'''
	   The constraint tries to keep the bone exactly at ik_dist of the target.
	
	   :value: 2
	
	'''

	BL_DST_ALPHA = None
	BL_DST_COLOR = None
	BL_ONE = None
	BL_ONE_MINUS_DST_ALPHA = None
	BL_ONE_MINUS_DST_COLOR = None
	BL_ONE_MINUS_SRC_ALPHA = None
	BL_ONE_MINUS_SRC_COLOR = None
	BL_SRC_ALPHA = None
	BL_SRC_ALPHA_SATURATE = None
	BL_SRC_COLOR = None
	BL_ZERO = None
	KX_INPUT_NONE = None
	KX_INPUT_JUST_ACTIVATED = None
	KX_INPUT_ACTIVE = None
	KX_INPUT_JUST_RELEASED = None
	KX_ACTION_MODE_PLAY = None
	'''
	   Play the action once.
	   
	   :value: 0
	
	'''

	KX_ACTION_MODE_LOOP = None
	'''
	   Loop the action (repeat it).
	   
	   :value: 1
	
	'''

	KX_ACTION_MODE_PING_PONG = None
	'''
	   Play the action one direct then back the other way when it has completed.
	   
	   :value: 2
	
	'''

	KX_ACTION_BLEND_BLEND = None
	'''
	   Blend layers using linear interpolation
	
	   :value: 0
	
	'''

	KX_ACTION_BLEND_ADD = None
	'''
	   Adds the layers together
	
	   :value: 1
	
	'''

	KX_MOUSE_BUT_LEFT = None
	KX_MOUSE_BUT_MIDDLE = None
	KX_MOUSE_BUT_RIGHT = None
	RM_WALLS = None
	'''
	   Draw only the walls.
	
	'''

	RM_POLYS = None
	'''
	   Draw only polygons.
	 
	'''

	RM_TRIS = None
	'''
	   Draw triangle mesh.
	   
	'''

	VIEWMATRIX = None
	VIEWMATRIX_INVERSE = None
	VIEWMATRIX_INVERSETRANSPOSE = None
	VIEWMATRIX_TRANSPOSE = None
	MODELMATRIX = None
	MODELMATRIX_INVERSE = None
	MODELMATRIX_INVERSETRANSPOSE = None
	MODELMATRIX_TRANSPOSE = None
	MODELVIEWMATRIX = None
	MODELVIEWMATRIX_INVERSE = None
	MODELVIEWMATRIX_INVERSETRANSPOSE = None
	MODELVIEWMATRIX_TRANSPOSE = None
	CAM_POS = None
	'''
	   Current camera position
	
	'''

	CONSTANT_TIMER = None
	'''
	   User a timer for the uniform value.
	
	'''

	SHD_TANGENT = None
	KX_STATE1 = None
	KX_STATE2 = None
	KX_STATE3 = None
	KX_STATE4 = None
	KX_STATE5 = None
	KX_STATE6 = None
	KX_STATE7 = None
	KX_STATE8 = None
	KX_STATE9 = None
	KX_STATE10 = None
	KX_STATE11 = None
	KX_STATE12 = None
	KX_STATE13 = None
	KX_STATE14 = None
	KX_STATE15 = None
	KX_STATE16 = None
	KX_STATE17 = None
	KX_STATE18 = None
	KX_STATE19 = None
	KX_STATE20 = None
	KX_STATE21 = None
	KX_STATE22 = None
	KX_STATE23 = None
	KX_STATE24 = None
	KX_STATE25 = None
	KX_STATE26 = None
	KX_STATE27 = None
	KX_STATE28 = None
	KX_STATE29 = None
	KX_STATE30 = None
	KX_STATE_OP_CLR = None
	'''
	   Substract bits to state mask
	
	   :value: 0
	
	'''

	KX_STATE_OP_CPY = None
	'''
	   Copy state mask
	
	   :value: 1
	   
	'''

	KX_STATE_OP_NEG = None
	'''
	   Invert bits to state mask
	
	   :value: 2
	
	'''

	KX_STATE_OP_SET = None
	'''
	   Add bits to state mask
	
	   :value: 3
	
	'''

class render:
	def getWindowWidth():
		'''
	   Gets the width of the window (in pixels)
	   
	   :rtype: integer
	
		'''
		pass

	def getWindowHeight():
		'''
	   Gets the height of the window (in pixels)
	   
	   :rtype: integer
	
		'''
		pass

	def setWindowSize(width, height):
		'''
	   Set the width and height of the window (in pixels). This also works for fullscreen applications.
	   
	   :type width: integer
	   :type height: integer
	
		'''
		pass

	def setFullScreen(enable):
		'''
	   Set whether or not the window should be fullscreen.
	   
	   :type enable: bool
	
		'''
		pass

	def getFullScreen():
		'''
	   Returns whether or not the window is fullscreen.
	   
	   :rtype: bool
	
		'''
		pass

	def makeScreenshot(filename):
		'''
	   Writes a screenshot to the given filename.
	   
	   If filename starts with // the image will be saved relative to the current directory.
	   If the filename contains # it will be replaced with the frame number.
	   
	   The standalone player saves .png files. It does not support color space conversion 
	   or gamma correction.
	   
	   When run from Blender, makeScreenshot supports all Blender image file formats like PNG, TGA, Jpeg and OpenEXR.
	   Gamma, Colorspace conversion and Jpeg compression are taken from the Render settings panels.
	   
	   :type filename: string
	
	
		'''
		pass

	def enableVisibility(visible):
		'''
	   Doesn't really do anything...
	
	
		'''
		pass

	def showMouse(visible):
		'''
	   Enables or disables the operating system mouse cursor.
	   
	   :type visible: boolean
	
	
		'''
		pass

	def setMousePosition(x, y):
		'''
	   Sets the mouse cursor position.
	   
	   :type x: integer
	   :type y: integer
	
	
		'''
		pass

	def setBackgroundColor(rgba):
		'''
	   Sets the window background color.
	   
	   :type rgba: list [r, g, b, a]
	
	
		'''
		pass

	def setMistColor(rgb):
		'''
	   Sets the mist color.
	   
	   :type rgb: list [r, g, b]
	
	   
		'''
		pass

	def setAmbientColor(rgb):
		'''
	   Sets the color of ambient light.
	   
	   :type rgb: list [r, g, b]
	
	
		'''
		pass

	def setMistStart(start):
		'''
	   Sets the mist start value.  Objects further away than start will have mist applied to them.
	   
	   :type start: float
	
	
		'''
		pass

	def setMistEnd(end):
		'''
	   Sets the mist end value.  Objects further away from this will be colored solid with
	   the color set by setMistColor().
	   
	   :type end: float
	
	   
		'''
		pass

	def disableMist():
		'''
	   Disables mist.
	   
	   .. note:: Set any of the mist properties to enable mist.
	
	   
		'''
		pass

	def setEyeSeparation(eyesep):
		'''
	   Sets the eye separation for stereo mode. Usually Focal Length/30 provides a confortable value.
	   
	   :arg eyesep: The distance between the left and right eye.
	   :type eyesep: float
	
	
		'''
		pass

	def getEyeSeparation():
		'''
	   Gets the current eye separation for stereo mode.
	   
	   :rtype: float
	
	   
		'''
		pass

	def setFocalLength(focallength):
		'''
	   Sets the focal length for stereo mode. It uses the current camera focal length as initial value.
	   
	   :arg focallength: The focal length.  
	   :type focallength: float
	
		'''
		pass

	def getFocalLength():
		'''
	   Gets the current focal length for stereo mode.
	   
	   :rtype: float
	
		'''
		pass

	def setMaterialMode(mode):
		'''
	   Set the material mode to use for OpenGL rendering.
	   
	   :type mode: KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL
	
	   .. note:: Changes will only affect newly created scenes.
	
	
		'''
		pass

	def getMaterialMode(mode):
		'''
	   Get the material mode to use for OpenGL rendering.
	   
	   :rtype: KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL
	
	
		'''
		pass

	def setGLSLMaterialSetting(setting, enable):
		'''
	   Enables or disables a GLSL material setting.
	   
	   :type setting: string (lights, shaders, shadows, ramps, nodes, extra_textures)
	   :type enable: boolean
	
	
		'''
		pass

	def getGLSLMaterialSetting(setting, enable):
		'''
	   Get the state of a GLSL material setting.
	   
	   :type setting: string (lights, shaders, shadows, ramps, nodes, extra_textures)
	   :rtype: boolean
	
		'''
		pass

	def setAnisotropicFiltering(level):
		'''
	   Set the anisotropic filtering level for textures.
	   
	   :arg level: The new anisotropic filtering level to use
	   :type level: integer (must be one of 1, 2, 4, 8, 16)
	   
	   .. note:: Changing this value can cause all textures to be recreated, which can be slow.
	   
		'''
		pass

	def getAnisotropicFiltering():
		'''
	   Get the anisotropic filtering level used for textures.
	   
	   :rtype: integer (one of 1, 2, 4, 8, 16)
	
		'''
		pass

	def setMipmapping(value):
		'''
	   Change how to use mipmapping.
	   
	   :type value: RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR
	   
	   .. note:: Changing this value can cause all textures to be recreated, which can be slow.
	
		'''
		pass

	def getMipmapping():
		'''
	   Get the current mipmapping setting.
	   
	   :rtype: RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR
	   
		'''
		pass

	def drawLine(fromVec,toVec,color):
		'''
	   Draw a line in the 3D scene.
	   
	   :arg fromVec: the origin of the line
	   :type fromVec: list [x, y, z]
	   :arg toVec: the end of the line
	   :type toVec: list [x, y, z]
	   :arg color: the color of the line
	   :type color: list [r, g, b]
	
	
		'''
		pass

	def enableMotionBlur(factor):
		'''
	   Enable the motion blur effect.
	   
	   :arg factor: the ammount of motion blur to display.
	   :type factor: float [0.0 - 1.0]
	
	
		'''
		pass

	def disableMotionBlur():
		'''
	   Disable the motion blur effect.
	
		'''
		pass

	def setVsync(value):
		'''
	   Set the vsync value
	
	   :arg value: One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE
	   :type value: integer
	
		'''
		pass

	def getVsync():
		'''
	   Get the current vsync value
	
	   :rtype: One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE
		'''
		pass

	KX_TEXFACE_MATERIAL = None
	'''
	   Materials as defined by the texture face settings.
	
	'''

	KX_BLENDER_MULTITEX_MATERIAL = None
	'''
	   Materials approximating blender materials with multitexturing.
	
	'''

	KX_BLENDER_GLSL_MATERIAL = None
	'''
	   Materials approximating blender materials with GLSL.
	   
	'''

class texture:
	def getLastError():
		'''
	   Last error that occurred in a bge.texture function.
	
	   :return: the description of the last error occurred in a bge.texture function.
	   :rtype: string
	
		'''
		pass

	def imageToArray(image,mode):
		'''
	   Returns a :class:`~bgl.buffer` corresponding to the current image stored in a texture source object.
	
	   :arg image: Image source object.
	   :type image: object of type :class:`VideoFFmpeg`, :class:`ImageFFmpeg`, :class:`ImageBuff`, :class:`ImageMix`, :class:`ImageRender`, :class:`ImageMirror` or :class:`ImageViewport`
	   :arg mode: optional argument representing the pixel format.
	      You can use the characters R, G, B for the 3 color channels, A for the alpha channel,
	      0 to force a fixed 0 color channel and 1 to force a fixed 255 color channel.
	      Example: "BGR" will return 3 bytes per pixel with the Blue, Green and Red channels in that order.
	      "RGB1" will return 4 bytes per pixel with the Red, Green, Blue channels in that order and the alpha channel forced to 255.
	      A special mode "F" allows to return the image as an array of float. This mode should only be used to retrieve
	      the depth buffer of the ImageViewport and ImageRender object.
	      The default mode is "RGBA".
	          
	
	   :type mode: string
	   :rtype: :class:`~bgl.buffer`
	   :return: A object representing the image as one dimensional array of bytes of size (pixel_size*width*height),
	      line by line starting from the bottom of the image. The pixel size and format is determined by the mode
	      parameter. For mode 'F', the array is a one dimensional array of float of size (width*height).
	
		'''
		pass

	def materialID(object,name):
		'''
	   Returns a numeric value that can be used in :class:`Texture` to create a dynamic texture.
	
	   The value corresponds to an internal material number that uses the texture identified
	   by name. name is a string representing a texture name with IM prefix if you want to
	   identify the texture directly.    This method works for basic tex face and for material,
	   provided the material has a texture channel using that particular texture in first
	   position of the texture stack.    name can also have MA prefix if you want to identify
	   the texture by material. In that case the material must have a texture channel in first
	   position.
	
	   If the object has no material that matches name, it generates a runtime error. Use try/except to catch the exception.
	
	   Ex: bge.texture.materialID(obj, 'IMvideo.png')
	
	   :arg object: the game object that uses the texture you want to make dynamic
	   :type object: game object
	   :arg name: name of the texture/material you want to make dynamic.
	   :type name: string
	   :rtype: integer
	
		'''
		pass

	def setLogFile(filename):
		'''
	   Sets the name of a text file in which runtime error messages will be written, in addition to the printing
	   of the messages on the Python console. Only the runtime errors specific to the VideoTexture module
	   are written in that file, ordinary runtime time errors are not written.
	
	   :arg filename: name of error log file
	   :type filename: string
	   :rtype: integer
		'''
		pass

	class VideoFFmpeg:
		'''   FFmpeg video source
		'''

		def play():
			'''
	      Play (restart) video
	
			'''
			pass

		def pause():
			'''
	      pause video
	
			'''
			pass

		def stop():
			'''
	      stop video (play will replay it from start)
	
			'''
			pass

		status = None
		'''
	      video status
	
		'''

		range = None
		'''
	      replay range
	
		'''

		repeat = None
		'''
	      repeat count, -1 for infinite repeat
	
	      :type: int
	
		'''

		framerate = None
		'''
	      frame rate
	
	      :type: float
	
		'''

		valid = None
		'''
	      Tells if an image is available
	
	      :type: bool
	
		'''

		image = None
		'''
	      image data
	
		'''

		size = None
		'''
	      image size
	
		'''

		scale = None
		'''
	      fast scale of image (near neighbour)
	
		'''

		flip = None
		'''
	      flip image vertically
	
		'''

		filter = None
		'''
	      pixel filter
	
		'''

		preseek = None
		'''
	      number of frames of preseek
	
	      :type: int
	
		'''

		deinterlace = None
		'''
	      deinterlace image
	
	      :type: bool
	
		'''

	class ImageFFmpeg:
		'''   FFmpeg image source
		'''

		def refresh():
			'''
	      Refresh image, i.e. load it
	
			'''
			pass

		status = None
		'''
	      video status
	
		'''

		valid = None
		'''
	      Tells if an image is available
	
	      :type: bool
	
		'''

		image = None
		'''
	      image data
	
		'''

		size = None
		'''
	      image size
	
		'''

		scale = None
		'''
	      fast scale of image (near neighbour)
	
		'''

		flip = None
		'''
	      flip image vertically
	
		'''

		filter = None
		'''
	      pixel filter
	
		'''

	class ImageBuff:
		'''   Image source from image buffer
		'''

		def load(imageBuffer, width, height):
			'''
	      Load image from buffer
	
			'''
			pass

		def plot(imageBuffer, width, height, positionX, positionY):
			'''
	      update image buffer
	
			'''
			pass

		filter = None
		'''
	      pixel filter
	
		'''

		flip = None
		'''
	      flip image vertically
	
		'''

		image = None
		'''
	      image data
	
		'''

		scale = None
		'''
	      fast scale of image (near neighbour)
	
		'''

		size = None
		'''
	      image size
	
		'''

	class ImageMirror:
		'''   Image source from mirror
		'''

		def refresh(imageMirror):
			'''
	      Refresh image - invalidate its current content
	
			'''
			pass

		alpha = None
		'''
	      use alpha in texture
	
		'''

		background = None
		'''
	      background color
	
		'''

		capsize = None
		'''
	      size of render area
	
		'''

		clip = None
		'''
	      clipping distance
	
		'''

		filter = None
		'''
	      pixel filter
	
		'''

		flip = None
		'''
	      flip image vertically
	
		'''

		image = None
		'''
	      image data
	
		'''

		scale = None
		'''
	      fast scale of image (near neighbour)
	
		'''

		size = None
		'''
	      image size
	
		'''

		valid = None
		'''
	      bool to tell if an image is available
	
		'''

	class ImageMix:
		'''   Image mixer
		'''

		def getSource(imageMix):
			'''
	      get image source
	
			'''
			pass

		def getWeight(imageMix):
			'''
	      get image source weight
	
	
			'''
			pass

		def refresh(imageMix):
			'''
	      Refresh image - invalidate its current content
	
			'''
			pass

		def setSource(imageMix):
			'''
	      set image source
	
			'''
			pass

		def setWeight(imageMix):
			'''
	      set image source weight
	
			'''
			pass

		filter = None
		'''
	      pixel filter
	
		'''

		flip = None
		'''
	      flip image vertically
	
		'''

		image = None
		'''
	      image data
	
		'''

		scale = None
		'''
	      fast scale of image (near neighbour)
	
		'''

	class ImageRender:
		'''   Image source from render
		'''

		def refresh(imageRender):
			'''
	      Refresh image - invalidate its current content
	
			'''
			pass

		alpha = None
		'''
	      use alpha in texture
	
		'''

		background = None
		'''
	      background color
	
		'''

		capsize = None
		'''
	      size of render area
	
		'''

		filter = None
		'''
	      pixel filter
	
		'''

		flip = None
		'''
	      flip image vertically
	
		'''

		image = None
		'''
	      image data
	
		'''

		scale = None
		'''
	      fast scale of image (near neighbour)
	
		'''

		size = None
		'''
	      image size
	
		'''

		valid = None
		'''
	      bool to tell if an image is available
	
		'''

		whole = None
		'''
	      use whole viewport to render
	
		'''

		depth = None
		'''
	      use depth component of render as array of float -  not suitable for texture source,
	      should only be used with bge.texture.imageToArray(mode='F')
	
		'''

	class ImageViewport:
		'''   Image source from viewport
		'''

		def refresh(imageViewport):
			'''
	      Refresh image - invalidate its current content
	
			'''
			pass

		alpha = None
		'''
	      use alpha in texture
	
		'''

		capsize = None
		'''
	      size of viewport area being captured
	
		'''

		filter = None
		'''
	      pixel filter
	
		'''

		flip = None
		'''
	      flip image vertically
	
		'''

		image = None
		'''
	      image data
	
		'''

		position = None
		'''
	      upper left corner of captured area
	
		'''

		scale = None
		'''
	      fast scale of image (near neighbour)
	
		'''

		size = None
		'''
	      image size
	
		'''

		valid = None
		'''
	      bool to tell if an image is available
	
		'''

		whole = None
		'''
	      use whole viewport to capture
	
		'''

		depth = None
		'''
	      use depth component of viewport as array of float -  not suitable for texture source,
	      should only be used with bge.texture.imageToArray(mode='F')
	
		'''

	class Texture:
		'''   Texture objects
		'''

		def close(texture):
			'''
	      Close dynamic texture and restore original
	
			'''
			pass

		def refresh(texture):
			'''
	      Refresh texture from source
	
			'''
			pass

		bindId = None
		'''
	      OpenGL Bind Name
	
		'''

		mipmap = None
		'''
	      mipmap texture
	
		'''

	class FilterBGR24:
		'''   Source filter BGR24 objects
		'''

	class FilterBlueScreen:
		'''   Filter for Blue Screen objects
		'''

		color = None
		'''
	      blue screen color
	
		'''

		limits = None
		'''
	      blue screen color limits
	
		'''

	class FilterColor:
		'''   Filter for color calculations
		'''

		matrix = None
		'''
	      matrix [4][5] for color calculation
	
		'''

	class FilterGray:
		'''   Filter for gray scale effect
		'''

	class FilterLevel:
		'''   Filter for levels calculations
		'''

		levels = None
		'''
	      levels matrix [4] (min, max)
	
		'''

	class FilterNormal:
		'''   Filter for Blue Screen objects
		'''

		colorIdx = None
		'''
	      index of color used to calculate normal (0 - red, 1 - green, 2 - blue)
	
		'''

		depth = None
		'''
	      depth of relief
	
		'''

	class FilterRGB24:
		'''   Returns a new input filter object to be used with :class:`ImageBuff` object when the image passed
	   to the ImageBuff.load() function has the 3-bytes pixel format BGR.
		'''

	class FilterRGBA32:
		'''   Source filter RGBA32 objects
		'''

class types:
	class KX_TrackToActuator:
		'''   Edit Object actuator in Track To mode.
		'''

		object = None
		'''
	      the object this actuator tracks.
	
	      :type: :class:`KX_GameObject` or None
	
		'''

		time = None
		'''
	      the time in frames with which to delay the tracking motion.
	
	      :type: integer
	
		'''

	class KX_ObjectActuator:
		'''   The object actuator ("Motion Actuator") applies force, torque, displacement, angular displacement, 
	   velocity, or angular velocity to an object.
	   Servo control allows to regulate force to achieve a certain speed target.
		'''

		force = None
		'''
	      The force applied by the actuator.
	
	      :type: list [x, y, z]
	
		'''

		useLocalForce = None
		'''
	      A flag specifying if the force is local.
	
	      :type: boolean
	
		'''

		torque = None
		'''
	      The torque applied by the actuator.
	
	      :type: list [x, y, z]
	
		'''

		useLocalTorque = None
		'''
	      A flag specifying if the torque is local.
	
	      :type: boolean
	
		'''

		dLoc = None
		'''
	      The displacement vector applied by the actuator.
	
	      :type: list [x, y, z]
	
		'''

		useLocalDLoc = None
		'''
	      A flag specifying if the dLoc is local.
	
	      :type: boolean
	
		'''

		dRot = None
		'''
	      The angular displacement vector applied by the actuator
	
	      :type: list [x, y, z]
	      
	      .. note::
	      
	         Since the displacement is applied every frame, you must adjust the displacement based on the frame rate, or you game experience will depend on the player's computer speed.
	
		'''

		useLocalDRot = None
		'''
	      A flag specifying if the dRot is local.
	
	      :type: boolean
	
		'''

		linV = None
		'''
	      The linear velocity applied by the actuator.
	
	      :type: list [x, y, z]
	
		'''

		useLocalLinV = None
		'''
	      A flag specifying if the linear velocity is local.
	
	      :type: boolean
	      
	      .. note::
	      
	         This is the target speed for servo controllers.
	
		'''

		angV = None
		'''
	      The angular velocity applied by the actuator.
	
	      :type: list [x, y, z]
	
		'''

		useLocalAngV = None
		'''
	      A flag specifying if the angular velocity is local.
	
	      :type: boolean
	
		'''

		damping = None
		'''
	      The damping parameter of the servo controller.
	
	      :type: short
	
		'''

		forceLimitX = None
		'''
	      The min/max force limit along the X axis and activates or deactivates the limits in the servo controller.
	
	      :type: list [min(float), max(float), bool]
	
		'''

		forceLimitY = None
		'''
	      The min/max force limit along the Y axis and activates or deactivates the limits in the servo controller.
	
	      :type: list [min(float), max(float), bool]
	
		'''

		forceLimitZ = None
		'''
	      The min/max force limit along the Z axis and activates or deactivates the limits in the servo controller.
	
	      :type: list [min(float), max(float), bool]
	
		'''

		pid = None
		'''
	      The PID coefficients of the servo controller.
	
	      :type: list of floats [proportional, integral, derivate]
	
		'''

	class CListValue:
		'''   This is a list like object used in the game engine internally that behaves similar to a python list in most ways.
		'''

		def append(val):
			'''
	      Add an item to the list (like pythons append)
	
	      .. warning::
	      
	         Appending values to the list can cause crashes when the list is used internally by the game engine.
	
			'''
			pass

		def count(val):
			'''
	      Count the number of instances of a value in the list.
	
	      :return: number of instances
	      :rtype: integer
	
			'''
			pass

		def index(val):
			'''
	      Return the index of a value in the list.
	
	      :return: The index of the value in the list.
	      :rtype: integer
	
			'''
			pass

		def reverse():
			'''
	      Reverse the order of the list.
	
			'''
			pass

		def get(key, default=None):
			'''
	      Return the value matching key, or the default value if its not found.
	
	      :return: The key value or a default.
	
			'''
			pass

	class KX_NavMeshObject:
		'''   Python interface for using and controlling navigation meshes. 
		'''

		def findPath(start, goal):
			'''
	      Finds the path from start to goal points.
	
	      :arg start: the start point
	      :arg start: 3D Vector
	      :arg goal: the goal point
	      :arg start: 3D Vector
	      :return: a path as a list of points
	      :rtype: list of points
	
			'''
			pass

		def raycast(start, goal):
			'''
	      Raycast from start to goal points.
	
	      :arg start: the start point
	      :arg start: 3D Vector
	      :arg goal: the goal point
	      :arg start: 3D Vector
	      :return: the hit factor
	      :rtype: float
	
			'''
			pass

		def draw(mode):
			'''
	      Draws a debug mesh for the navigation mesh.
	
	      :arg mode: the drawing mode (one of :ref:`these constants <navmesh-draw-mode>`)
	      :arg mode: integer
	      :return: None
	
			'''
			pass

	class SCA_RandomActuator:
		'''   Random Actuator
		'''

		def setBoolConst(value):
			'''
	      Sets this generator to produce a constant boolean value.
	
	      :arg value: The value to return.
	      :type value: boolean
	
			'''
			pass

		def setBoolUniform():
			'''
	      Sets this generator to produce a uniform boolean distribution.
	
	      The generator will generate True or False with 50% chance.
	
			'''
			pass

		def setBoolBernouilli(value):
			'''
	      Sets this generator to produce a Bernouilli distribution.
	
	      :arg value: Specifies the proportion of False values to produce.
	
	         * 0.0: Always generate True
	         * 1.0: Always generate False
	      :type value: float
	
			'''
			pass

		def setIntConst(value):
			'''
	      Sets this generator to always produce the given value.
	
	      :arg value: the value this generator produces.
	      :type value: integer
	
			'''
			pass

		def setIntUniform(lower_bound, upper_bound):
			'''
	      Sets this generator to produce a random value between the given lower and
	      upper bounds (inclusive).
	
	      :type lower_bound: integer
	      :type upper_bound: integer
	
			'''
			pass

		def setIntPoisson(value):
			'''
	      Generate a Poisson-distributed number.
	
	      This performs a series of Bernouilli tests with parameter value.
	      It returns the number of tries needed to achieve succes.
	
	      :type value: float
	
			'''
			pass

		def setFloatConst(value):
			'''
	      Always generate the given value.
	
	      :type value: float
	
			'''
			pass

		def setFloatUniform(lower_bound, upper_bound):
			'''
	      Generates a random float between lower_bound and upper_bound with a
	      uniform distribution.
	
	      :type lower_bound: float
	      :type upper_bound: float
	
			'''
			pass

		def setFloatNormal(mean, standard_deviation):
			'''
	      Generates a random float from the given normal distribution.
	
	      :arg mean: The mean (average) value of the generated numbers
	      :type mean: float
	      :arg standard_deviation: The standard deviation of the generated numbers.
	      :type standard_deviation: float
	
			'''
			pass

		seed = None
		'''
	      Seed of the random number generator.
	
	      :type: integer.
	
	      Equal seeds produce equal series. If the seed is 0, the generator will produce the same value on every call.
	
		'''

		para1 = None
		'''
	      the first parameter of the active distribution.
	
	      :type: float, read-only.
	
	      Refer to the documentation of the generator types for the meaning of this value. 
	
		'''

		para2 = None
		'''
	      the second parameter of the active distribution.
	
	      :type: float, read-only
	
	      Refer to the documentation of the generator types for the meaning of this value.
	
		'''

		distribution = None
		'''
	      Distribution type. (read-only). Can be one of :ref:`these constants <logic-random-distributions>`
	
	      :type: integer
	
		'''

		propName = None
		'''
	      the name of the property to set with the random value.
	
	      :type: string
	
	      If the generator and property types do not match, the assignment is ignored.
	
		'''

	class KX_GameActuator:
		'''   The game actuator loads a new .blend file, restarts the current .blend file or quits the game.
		'''

		fileName = None
		'''
	      the new .blend file to load.
	
	      :type: string
	
		'''

	class SCA_PythonController:
		'''   A Python controller uses a Python script to activate it's actuators, 
	   based on it's sensors.
		'''

		def activate(actuator):
			'''
	      Activates an actuator attached to this controller.
	
	      :arg actuator: The actuator to operate on.
	      :type actuator: actuator or the actuator name as a string
	
			'''
			pass

		owner = None
		'''
	      The object the controller is attached to.
	
	      :type: :class:`KX_GameObject`
	
		'''

		script = None
		'''
	      The value of this variable depends on the execution methid.
	
	      * When 'Script' execution mode is set this value contains the entire python script as a single string (not the script name as you might expect) which can be modified to run different scripts.
	      * When 'Module' execution mode is set this value will contain a single line string - module name and function "module.func" or "package.modile.func" where the module names are python textblocks or external scripts.
	
	      :type: string
	      
	      .. note::
	      
	         Once this is set the script name given for warnings will remain unchanged.
	
		'''

		mode = None
		'''
	      the execution mode for this controller (read-only).
	
	      * Script: 0, Execite the :data:`script` as a python code.
	      * Module: 1, Execite the :data:`script` as a module and function.
	
	      :type: integer
	
		'''

	class KX_RaySensor:
		'''   A ray sensor detects the first object in a given direction.
		'''

		propName = None
		'''
	      The property the ray is looking for.
	
	      :type: string
	
		'''

		range = None
		'''
	      The distance of the ray.
	
	      :type: float
	
		'''

		useMaterial = None
		'''
	      Whether or not to look for a material (false = property).
	
	      :type: boolean
	
		'''

		useXRay = None
		'''
	      Whether or not to use XRay.
	
	      :type: boolean
	
		'''

		hitObject = None
		'''
	      The game object that was hit by the ray. (read-only).
	
	      :type: :class:`KX_GameObject`
	
		'''

		hitPosition = None
		'''
	      The position (in worldcoordinates) where the object was hit by the ray. (read-only).
	
	      :type: list [x, y, z]
	
		'''

		hitNormal = None
		'''
	      The normal (in worldcoordinates) of the object at the location where the object was hit by the ray. (read-only).
	
	      :type: list [x, y, z]
	
		'''

		hitMaterial = None
		'''
	      The material of the object in the face hit by the ray. (read-only).
	
	      :type: string
	
		'''

		rayDirection = None
		'''
	      The direction from the ray (in worldcoordinates). (read-only).
	
	      :type: list [x, y, z]
	
		'''

	class SCA_ActuatorSensor:
		'''   Actuator sensor detect change in actuator state of the parent object.
	   It generates a positive pulse if the corresponding actuator is activated
	   and a negative pulse if the actuator is deactivated.
		'''

	class KX_BlenderMaterial:
		'''   KX_BlenderMaterial
		'''

		def getShader():
			'''
	      Returns the material's shader.
	
	      :return: the material's shader
	      :rtype: :class:`BL_Shader`
	
			'''
			pass

		def setBlending(src, dest):
			'''
	      Set the pixel color arithmetic functions.
	
	      :arg src: Specifies how the red, green, blue, and alpha source blending factors are computed.
	      :type src: Value in...
	
	         * GL_ZERO,
	         * GL_ONE, 
	         * GL_SRC_COLOR, 
	         * GL_ONE_MINUS_SRC_COLOR, 
	         * GL_DST_COLOR, 
	         * GL_ONE_MINUS_DST_COLOR, 
	         * GL_SRC_ALPHA, 
	         * GL_ONE_MINUS_SRC_ALPHA, 
	         * GL_DST_ALPHA, 
	         * GL_ONE_MINUS_DST_ALPHA, 
	         * GL_SRC_ALPHA_SATURATE
	
	      :arg dest: Specifies how the red, green, blue, and alpha destination blending factors are computed.
	      :type dest: Value in...
	
	         * GL_ZERO
	         * GL_ONE
	         * GL_SRC_COLOR
	         * GL_ONE_MINUS_SRC_COLOR
	         * GL_DST_COLOR
	         * GL_ONE_MINUS_DST_COLOR
	         * GL_SRC_ALPHA
	         * GL_ONE_MINUS_SRC_ALPHA
	         * GL_DST_ALPHA
	         * GL_ONE_MINUS_DST_ALPHA
	         * GL_SRC_ALPHA_SATURATE
	
			'''
			pass

		shader = None
		'''
	      The materials shader.
	
	      :type: :class:`BL_Shader`
	
		'''

		blending = None
		'''
	      Ints used for pixel blending, (src, dst), matching the setBlending method.
	
	      :type: (integer, integer)
	
		'''

		material_index = None
		'''
	      The material's index.
	
	      :type: integer
	
		'''

	class SCA_IController:
		'''   Base class for all controller logic bricks.
		'''

		state = None
		'''
	      The controllers state bitmask. This can be used with the GameObject's state to test if the controller is active.
	      
	      :type: int bitmask
	
		'''

		sensors = None
		'''
	      A list of sensors linked to this controller.
	      
	      :type: sequence supporting index/string lookups and iteration.
	
	      .. note::
	
	         The sensors are not necessarily owned by the same object.
	
	      .. note::
	         
	         When objects are instanced in dupligroups links may be lost from objects outside the dupligroup.
	
		'''

		actuators = None
		'''
	      A list of actuators linked to this controller.
	      
	      :type: sequence supporting index/string lookups and iteration.
	
	      .. note::
	
	         The sensors are not necessarily owned by the same object.
	
	      .. note::
	         
	         When objects are instanced in dupligroups links may be lost from objects outside the dupligroup.
	
		'''

	class SCA_NANDController:
		'''   An NAND controller activates when all linked sensors are not active.
		'''

	class KX_ConstraintWrapper:
		'''   KX_ConstraintWrapper
		'''

	class KX_GameObject:
		'''   All game objects are derived from this class.
		'''

		def endObject():
			'''
	      Delete this object, can be used in place of the EndObject Actuator.
	
	      The actual removal of the object from the scene is delayed.
	
			'''
			pass

		def replaceMesh(mesh, useDisplayMesh=True, usePhysicsMesh=False):
			'''
	      Replace the mesh of this object with a new mesh. This works the same was as the actuator.
	
	      :arg mesh: mesh to replace or the meshes name.
	      :type mesh: :class:`MeshProxy` or string
	      :arg useDisplayMesh: when enabled the display mesh will be replaced (optional argument).
	      :type useDisplayMesh: boolean
	      :arg usePhysicsMesh: when enabled the physics mesh will be replaced (optional argument).
	      :type usePhysicsMesh: boolean
	
			'''
			pass

		def setVisible(visible, recursive):
			'''
	      Sets the game object's visible flag.
	
	      :arg visible: the visible state to set.
	      :type visible: boolean
	      :arg recursive: optional argument to set all childrens visibility flag too.
	      :type recursive: boolean
	
			'''
			pass

		def setOcclusion(occlusion, recursive):
			'''
	      Sets the game object's occlusion capability.
	
	      :arg occlusion: the state to set the occlusion to.
	      :type occlusion: boolean
	      :arg recursive: optional argument to set all childrens occlusion flag too.
	      :type recursive: boolean
	
			'''
			pass

		def alignAxisToVect(vect, axis=2, factor=1.0):
			'''
	      Aligns any of the game object's axis along the given vector.
	
	
	      :arg vect: a vector to align the axis.
	      :type vect: 3D vector
	      :arg axis: The axis you want to align
	
	         * 0: X axis
	         * 1: Y axis
	         * 2: Z axis
	
	      :type axis: integer
	      :arg factor: Only rotate a feaction of the distance to the target vector (0.0 - 1.0)
	      :type factor: float
	
			'''
			pass

		def getAxisVect(vect):
			'''
	      Returns the axis vector rotates by the objects worldspace orientation.
	      This is the equivalent of multiplying the vector by the orientation matrix.
	
	      :arg vect: a vector to align the axis.
	      :type vect: 3D Vector
	      :return: The vector in relation to the objects rotation.
	      :rtype: 3d vector.
	
			'''
			pass

		def applyMovement(movement, local=False):
			'''
	      Sets the game object's movement.
	
	      :arg movement: movement vector.
	      :type movement: 3D Vector
	      :arg local:
	         * False: you get the "global" movement ie: relative to world orientation.
	         * True: you get the "local" movement ie: relative to object orientation.
	      :arg local: boolean
	
			'''
			pass

		def applyRotation(rotation, local=False):
			'''
	      Sets the game object's rotation.
	
	      :arg rotation: rotation vector.
	      :type rotation: 3D Vector
	      :arg local:
	         * False: you get the "global" rotation ie: relative to world orientation.
	         * True: you get the "local" rotation ie: relative to object orientation.
	      :arg local: boolean
	
			'''
			pass

		def applyForce(force, local=False):
			'''
	      Sets the game object's force.
	
	      This requires a dynamic object.
	
	      :arg force: force vector.
	      :type force: 3D Vector
	      :arg local:
	         * False: you get the "global" force ie: relative to world orientation.
	         * True: you get the "local" force ie: relative to object orientation.
	      :type local: boolean
	
			'''
			pass

		def applyTorque(torque, local=False):
			'''
	      Sets the game object's torque.
	
	      This requires a dynamic object.
	
	      :arg torque: torque vector.
	      :type torque: 3D Vector
	      :arg local:
	         * False: you get the "global" torque ie: relative to world orientation.
	         * True: you get the "local" torque ie: relative to object orientation.
	      :type local: boolean
	
			'''
			pass

		def getLinearVelocity(local=False):
			'''
	      Gets the game object's linear velocity.
	
	      This method returns the game object's velocity through it's centre of mass, ie no angular velocity component.
	
	      :arg local:
	         * False: you get the "global" velocity ie: relative to world orientation.
	         * True: you get the "local" velocity ie: relative to object orientation.
	      :type local: boolean
	      :return: the object's linear velocity.
	      :rtype: list [vx, vy, vz]
	
			'''
			pass

		def setLinearVelocity(velocity, local=False):
			'''
	      Sets the game object's linear velocity.
	
	      This method sets game object's velocity through it's centre of mass,
	      ie no angular velocity component.
	
	      This requires a dynamic object.
	
	      :arg velocity: linear velocity vector.
	      :type velocity: 3D Vector
	      :arg local:
	         * False: you get the "global" velocity ie: relative to world orientation.
	         * True: you get the "local" velocity ie: relative to object orientation.
	      :type local: boolean
	
			'''
			pass

		def getAngularVelocity(local=False):
			'''
	      Gets the game object's angular velocity.
	
	      :arg local:
	         * False: you get the "global" velocity ie: relative to world orientation.
	         * True: you get the "local" velocity ie: relative to object orientation.
	      :type local: boolean
	      :return: the object's angular velocity.
	      :rtype: list [vx, vy, vz]
	
			'''
			pass

		def setAngularVelocity(velocity, local=False):
			'''
	      Sets the game object's angular velocity.
	
	      This requires a dynamic object.
	
	      :arg velocity: angular velocity vector.
	      :type velocity: boolean
	      :arg local:
	         * False: you get the "global" velocity ie: relative to world orientation.
	         * True: you get the "local" velocity ie: relative to object orientation.
	
			'''
			pass

		def getVelocity(point=(0, 0, 0)):
			'''
	      Gets the game object's velocity at the specified point.
	
	      Gets the game object's velocity at the specified point, including angular
	      components.
	
	      :arg point: optional point to return the velocity for, in local coordinates.
	      :type point: 3D Vector
	      :return: the velocity at the specified point.
	      :rtype: list [vx, vy, vz]
	
			'''
			pass

		def getReactionForce():
			'''
	      Gets the game object's reaction force.
	
	      The reaction force is the force applied to this object over the last simulation timestep.
	      This also includes impulses, eg from collisions.
	
	      :return: the reaction force of this object.
	      :rtype: list [fx, fy, fz]
	
	      .. note::
	
	         This is not implimented at the moment.
	
			'''
			pass

		def applyImpulse(point, impulse):
			'''
	      Applies an impulse to the game object.
	
	      This will apply the specified impulse to the game object at the specified point.
	      If point != position, applyImpulse will also change the object's angular momentum.
	      Otherwise, only linear momentum will change.
	
	      :arg point: the point to apply the impulse to (in world coordinates)
	      :type point: the point to apply the impulse to (in world coordinates)
	
			'''
			pass

		def suspendDynamics():
			'''
	      Suspends physics for this object.
	
			'''
			pass

		def restoreDynamics():
			'''
	      Resumes physics for this object.
	
	      .. note::
	
	         The objects linear velocity will be applied from when the dynamics were suspended.
	
			'''
			pass

		def enableRigidBody():
			'''
	      Enables rigid body physics for this object.
	
	      Rigid body physics allows the object to roll on collisions.
	
			'''
			pass

		def disableRigidBody():
			'''
	      Disables rigid body physics for this object.
	
			'''
			pass

		def setParent(parent, compound=True, ghost=True):
			'''
	      Sets this object's parent.
	      Control the shape status with the optional compound and ghost parameters:
	
	      In that case you can control if it should be ghost or not:
	
	      :arg parent: new parent object.
	      :type parent: :class:`KX_GameObject`
	      :arg compound: whether the shape should be added to the parent compound shape.
	
	         * True: the object shape should be added to the parent compound shape.
	         * False: the object should keep its individual shape.
	
	      :type compound: boolean
	      :arg ghost: whether the object should be ghost while parented.
	
	         * True: if the object should be made ghost while parented.
	         * False: if the object should be solid while parented.
	
	      :type ghost: boolean
	
	      .. note::
	
	         If the object type is sensor, it stays ghost regardless of ghost parameter
	
			'''
			pass

		def removeParent():
			'''
	      Removes this objects parent.
	
			'''
			pass

		def getPhysicsId():
			'''
	      Returns the user data object associated with this game object's physics controller.
	
			'''
			pass

		def getPropertyNames():
			'''
	      Gets a list of all property names.
	
	      :return: All property names for this object.
	      :rtype: list
	
			'''
			pass

		def getDistanceTo(other):
			'''
	      :arg other: a point or another :class:`KX_GameObject` to measure the distance to.
	      :type other: :class:`KX_GameObject` or list [x, y, z]
	      :return: distance to another object or point.
	      :rtype: float
	
			'''
			pass

		def getVectTo(other):
			'''
	      Returns the vector and the distance to another object or point.
	      The vector is normalized unless the distance is 0, in which a zero length vector is returned.
	
	      :arg other: a point or another :class:`KX_GameObject` to get the vector and distance to.
	      :type other: :class:`KX_GameObject` or list [x, y, z]
	      :return: (distance, globalVector(3), localVector(3))
	      :rtype: 3-tuple (float, 3-tuple (x, y, z), 3-tuple (x, y, z))
	
			'''
			pass

		def rayCastTo(other, dist, prop):
			'''
	      Look towards another point/object and find first object hit within dist that matches prop.
	
	      The ray is always casted from the center of the object, ignoring the object itself.
	      The ray is casted towards the center of another object or an explicit [x, y, z] point.
	      Use rayCast() if you need to retrieve the hit point
	
	      :arg other: [x, y, z] or object towards which the ray is casted
	      :type other: :class:`KX_GameObject` or 3-tuple
	      :arg dist: max distance to look (can be negative => look behind); 0 or omitted => detect up to other
	      :type dist: float
	      :arg prop: property name that object must have; can be omitted => detect any object
	      :type prop: string
	      :return: the first object hit or None if no object or object does not match prop
	      :rtype: :class:`KX_GameObject`
	
			'''
			pass

		def rayCast(objto, objfrom, dist, prop, face, xray, poly):
			'''
	      Look from a point/object to another point/object and find first object hit within dist that matches prop.
	      if poly is 0, returns a 3-tuple with object reference, hit point and hit normal or (None, None, None) if no hit.
	      if poly is 1, returns a 4-tuple with in addition a :class:`KX_PolyProxy` as 4th element.
	      if poly is 2, returns a 5-tuple with in addition a 2D vector with the UV mapping of the hit point as 5th element.
	
	      .. code-block:: python
	
	         # shoot along the axis gun-gunAim (gunAim should be collision-free)
	         obj, point, normal = gun.rayCast(gunAim, None, 50)
	         if obj:
	            # do something
	            pass
	
	      The face paremeter determines the orientation of the normal.
	
	      * 0 => hit normal is always oriented towards the ray origin (as if you casted the ray from outside)
	      * 1 => hit normal is the real face normal (only for mesh object, otherwise face has no effect)
	
	      The ray has X-Ray capability if xray parameter is 1, otherwise the first object hit (other than self object) stops the ray.
	      The prop and xray parameters interact as follow.
	
	      * prop off, xray off: return closest hit or no hit if there is no object on the full extend of the ray.
	      * prop off, xray on : idem.
	      * prop on, xray off: return closest hit if it matches prop, no hit otherwise.
	      * prop on, xray on : return closest hit matching prop or no hit if there is no object matching prop on the full extend of the ray.
	
	      The :class:`KX_PolyProxy` 4th element of the return tuple when poly=1 allows to retrieve information on the polygon hit by the ray.
	      If there is no hit or the hit object is not a static mesh, None is returned as 4th element.
	
	      The ray ignores collision-free objects and faces that dont have the collision flag enabled, you can however use ghost objects.
	
	      :arg objto: [x, y, z] or object to which the ray is casted
	      :type objto: :class:`KX_GameObject` or 3-tuple
	      :arg objfrom: [x, y, z] or object from which the ray is casted; None or omitted => use self object center
	      :type objfrom: :class:`KX_GameObject` or 3-tuple or None
	      :arg dist: max distance to look (can be negative => look behind); 0 or omitted => detect up to to
	      :type dist: float
	      :arg prop: property name that object must have; can be omitted or "" => detect any object
	      :type prop: string
	      :arg face: normal option: 1=>return face normal; 0 or omitted => normal is oriented towards origin
	      :type face: integer
	      :arg xray: X-ray option: 1=>skip objects that don't match prop; 0 or omitted => stop on first object
	      :type xray: integer
	      :arg poly: polygon option: 0, 1 or 2 to return a 3-, 4- or 5-tuple with information on the face hit.
	
	         * 0 or omitted: return value is a 3-tuple (object, hitpoint, hitnormal) or (None, None, None) if no hit
	         * 1: return value is a 4-tuple and the 4th element is a :class:`KX_PolyProxy` or None if no hit or the object doesn't use a mesh collision shape.
	         * 2: return value is a 5-tuple and the 5th element is a 2-tuple (u, v) with the UV mapping of the hit point or None if no hit, or the object doesn't use a mesh collision shape, or doesn't have a UV mapping.
	
	      :type poly: integer
	      :return: (object, hitpoint, hitnormal) or (object, hitpoint, hitnormal, polygon) or (object, hitpoint, hitnormal, polygon, hituv).
	
	         * object, hitpoint and hitnormal are None if no hit.
	         * polygon is valid only if the object is valid and is a static object, a dynamic object using mesh collision shape or a soft body object, otherwise it is None
	         * hituv is valid only if polygon is valid and the object has a UV mapping, otherwise it is None
	
	      :rtype:
	
	         * 3-tuple (:class:`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz))
	         * or 4-tuple (:class:`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), :class:`KX_PolyProxy`)
	         * or 5-tuple (:class:`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), :class:`KX_PolyProxy`, 2-tuple (u, v))
	
	      .. note::
	
	         The ray ignores the object on which the method is called. It is casted from/to object center or explicit [x, y, z] points.
	
			'''
			pass

		def setCollisionMargin(margin):
			'''
	      Set the objects collision margin.
	
	      :arg margin: the collision margin distance in blender units.
	      :type margin: float
	
	      .. note::
	
	         If this object has no physics controller (a physics ID of zero), this function will raise RuntimeError.
	
			'''
			pass

		def sendMessage(subject, body="", to=""):
			'''
	      Sends a message.
	
	      :arg subject: The subject of the message
	      :type subject: string
	      :arg body: The body of the message (optional)
	      :type body: string
	      :arg to: The name of the object to send the message to (optional)
	      :type to: string
	
			'''
			pass

		def reinstancePhysicsMesh(gameObject, meshObject):
			'''
	      Updates the physics system with the changed mesh.
	
	      If no arguments are given the physics mesh will be re-created from the first mesh assigned to the game object.
	
	      :arg gameObject: optional argument, set the physics shape from this gameObjets mesh.
	      :type gameObject: string, :class:`KX_GameObject` or None
	      :arg meshObject: optional argument, set the physics shape from this mesh.
	      :type meshObject: string, :class:`MeshProxy` or None
	
	      :return: True if reinstance succeeded, False if it failed.
	      :rtype: boolean
	
	      .. note::
	
	         If this object has instances the other instances will be updated too.
	
	      .. note::
	
	         The gameObject argument has an advantage that it can convert from a mesh with modifiers applied (such as subsurf).
	
	      .. warning::
	
	         Only triangle mesh type objects are supported currently (not convex hull)
	
	      .. warning::
	
	         If the object is a part of a combound object it will fail (parent or child)
	
	      .. warning::
	
	         Rebuilding the physics mesh can be slow, running many times per second will give a performance hit.
	
			'''
			pass

		def get(key, default=None):
			'''
	      Return the value matching key, or the default value if its not found.
	      :return: The key value or a default.
	
			'''
			pass

		def playAction(name, start_frame, end_frame, layer=0, priority=0, blendin=0, play_mode=0, layer_weight=0.0, ipo_flags=0, speed=1.0, blend_mode=0):
			'''
	      Plays an action.
	
	      :arg name: the name of the action
	      :type name: string
	      :arg start: the start frame of the action
	      :type start: float
	      :arg end: the end frame of the action
	      :type end: float
	      :arg layer: the layer the action will play in (actions in different layers are added/blended together)
	      :type layer: integer
	      :arg priority: only play this action if there isn't an action currently playing in this layer with a higher (lower number) priority
	      :type priority: integer
	      :arg blendin: the amount of blending between this animation and the previous one on this layer
	      :type blendin: float
	      :arg play_mode: the play mode
	      :type play_mode: one of :ref:`these constants <gameobject-playaction-mode>`
	      :arg layer_weight: how much of the previous layer to use for blending
	      :type layer_weight: float
	      :arg ipo_flags: flags for the old IPO behaviors (force, etc)
	      :type ipo_flags: int bitfield
	      :arg speed: the playback speed of the action as a factor (1.0 = normal speed, 2.0 = 2x speed, etc)
	      :type speed: float
	      :arg blend_mode: how to blend this layer with previous layers
	      :type blend_mode: one of :ref:`these constants <gameobject-playaction-blend>`
	
			'''
			pass

		def stopAction(layer=0):
			'''
	      Stop playing the action on the given layer.
	
	      :arg layer: The layer to stop playing.
	      :type layer: integer
	
			'''
			pass

		def getActionFrame(layer=0):
			'''
	      Gets the current frame of the action playing in the supplied layer.
	
	      :arg layer: The layer that you want to get the frame from.
	      :type layer: integer
	
	      :return: The current frame of the action
	      :rtype: float
	
			'''
			pass

		def setActionFrame(frame, layer=0):
			'''
	      Set the current frame of the action playing in the supplied layer.
	
	      :arg layer: The layer where you want to set the frame
	      :type layer: integer
	      :arg frame: The frame to set the action to
	      :type frame: float
	
			'''
			pass

		name = None
		'''
	      The object's name. (read-only).
	
	      :type: string
	
		'''

		mass = None
		'''
	      The object's mass
	
	      :type: float
	
	      .. note::
	
	         The object must have a physics controller for the mass to be applied, otherwise the mass value will be returned as 0.0.
	
		'''

		linVelocityMin = None
		'''
	      Enforces the object keeps moving at a minimum velocity.
	
	      :type: float
	
	      .. note::
	
	         Applies to dynamic and rigid body objects only.
	
	      .. note::
	
	         A value of 0.0 disables this option.
	
	      .. note::
	
	         While objects are stationary the minimum velocity will not be applied.
	
		'''

		linVelocityMax = None
		'''
	      Clamp the maximum linear velocity to prevent objects moving beyond a set speed.
	
	      :type: float
	
	      .. note::
	
	         Applies to dynamic and rigid body objects only.
	
	      .. note::
	
	         A value of 0.0 disables this option (rather then setting it stationary).
	
		'''

		localInertia = None
		'''
	      the object's inertia vector in local coordinates. Read only.
	
	      :type: list [ix, iy, iz]
	
		'''

		parent = None
		'''
	      The object's parent object. (read-only).
	
	      :type: :class:`KX_GameObject` or None
	
		'''

		groupMembers = None
		'''
	      Returns the list of group members if the object is a group object, otherwise None is returned.
	
	      :type: :class:`CListValue` of :class:`KX_GameObject` or None
	
		'''

		groupObject = None
		'''
	      Returns the group object that the object belongs to or None if the object is not part of a group.
	
	      :type: :class:`KX_GameObject` or None
	
		'''

		collisionCallbacks = None
		'''
	      A list of callables to be run when a collision occurs.
	
	      :type: list
	
		'''

		scene = None
		'''
	      The object's scene. (read-only).
	
	      :type: :class:`KX_Scene` or None
	
		'''

		visible = None
		'''
	      visibility flag.
	
	      :type: boolean
	
	      .. note::
	
	         Game logic will still run for invisible objects.
	
		'''

		record_animation = None
		'''
	      Record animation for this object.
	
	      :type: boolean
	
		'''

		color = None
		'''
	      The object color of the object. [r, g, b, a]
	
	      :type: :class:`mathutils.Vector`
	
		'''

		occlusion = None
		'''
	      occlusion capability flag.
	
	      :type: boolean
	
		'''

		position = None
		'''
	      The object's position. [x, y, z] On write: local position, on read: world position
	
	      .. deprecated:: use :data:`localPosition` and :data:`worldPosition`.
	
	      :type: :class:`mathutils.Vector`
	
		'''

		orientation = None
		'''
	      The object's orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector. On write: local orientation, on read: world orientation
	
	      .. deprecated:: use :data:`localOrientation` and :data:`worldOrientation`.
	
	      :type: :class:`mathutils.Matrix`
	
		'''

		scaling = None
		'''
	      The object's scaling factor. [sx, sy, sz] On write: local scaling, on read: world scaling
	
	      .. deprecated:: use :data:`localScale` and :data:`worldScale`.
	
	      :type: :class:`mathutils.Vector`
	
		'''

		localOrientation = None
		'''
	      The object's local orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector.
	
	      :type: :class:`mathutils.Matrix`
	
		'''

		worldOrientation = None
		'''
	      The object's world orientation. 3x3 Matrix.
	
	      :type: :class:`mathutils.Matrix`
	
		'''

		localScale = None
		'''
	      The object's local scaling factor. [sx, sy, sz]
	
	      :type: :class:`mathutils.Vector`
	
		'''

		worldScale = None
		'''
	      The object's world scaling factor. [sx, sy, sz]
	
	      :type: :class:`mathutils.Vector`
	
		'''

		localPosition = None
		'''
	      The object's local position. [x, y, z]
	
	      :type: :class:`mathutils.Vector`
	
		'''

		worldPosition = None
		'''
	      The object's world position. [x, y, z]
	
	      :type: :class:`mathutils.Vector`
	
		'''

		localTransform = None
		'''
	      The object's local space transform matrix. 4x4 Matrix.
	
	      :type: :class:`mathutils.Matrix`
	
		'''

		worldTransform = None
		'''
	      The object's world space transform matrix. 4x4 Matrix.
	
	      :type: :class:`mathutils.Matrix`
	
		'''

		localLinearVelocity = None
		'''
	      The object's local linear velocity. [x, y, z]
	
	      :type: :class:`mathutils.Vector`
	
		'''

		worldLinearVelocity = None
		'''
	      The object's world linear velocity. [x, y, z]
	
	      :type: :class:`mathutils.Vector`
	
		'''

		localAngularVelocity = None
		'''
	      The object's local angular velocity. [x, y, z]
	
	      :type: :class:`mathutils.Vector`
	
		'''

		worldAngularVelocity = None
		'''
	      The object's world angular velocity. [x, y, z]
	
	      :type: :class:`mathutils.Vector`
	
		'''

		timeOffset = None
		'''
	      adjust the slowparent delay at runtime.
	
	      :type: float
	
		'''

		state = None
		'''
	      the game object's state bitmask, using the first 30 bits, one bit must always be set.
	
	      :type: int
	
		'''

		meshes = None
		'''
	      a list meshes for this object.
	
	      :type: list of :class:`KX_MeshProxy`
	
	      .. note::
	
	         Most objects use only 1 mesh.
	
	      .. note::
	
	         Changes to this list will not update the KX_GameObject.
	
		'''

		sensors = None
		'''
	      a sequence of :class:`SCA_ISensor` objects with string/index lookups and iterator support.
	
	      :type: list
	
	      .. note::
	
	         This attribute is experemental and may be removed (but probably wont be).
	
	      .. note::
	
	         Changes to this list will not update the KX_GameObject.
	
		'''

		controllers = None
		'''
	      a sequence of :class:`SCA_IController` objects with string/index lookups and iterator support.
	
	      :type: list of :class:`SCA_ISensor`
	
	      .. note::
	
	         This attribute is experemental and may be removed (but probably wont be).
	
	      .. note::
	
	         Changes to this list will not update the KX_GameObject.
	
		'''

		actuators = None
		'''
	      a list of :class:`SCA_IActuator` with string/index lookups and iterator support.
	
	      :type: list
	
	      .. note::
	
	         This attribute is experemental and may be removed (but probably wont be).
	
	      .. note::
	
	         Changes to this list will not update the KX_GameObject.
	
		'''

		attrDict = None
		'''
	      get the objects internal python attribute dictionary for direct (faster) access.
	
	      :type: dict
	
		'''

		children = None
		'''
	      direct children of this object, (read-only).
	
	      :type: :class:`CListValue` of :class:`KX_GameObject`'s
	
		'''

		childrenRecursive = None
		'''
	      all children of this object including childrens children, (read-only).
	
	      :type: :class:`CListValue` of :class:`KX_GameObject`'s
	
		'''

		life = None
		'''
	      The number of seconds until the object ends, assumes 50fps.
	      (when added with an add object actuator), (read-only).
	
	      :type: float
	
		'''

	class SCA_PropertyActuator:
		'''   Property Actuator
		'''

		propName = None
		'''
	      the property on which to operate.
	
	      :type: string
	
		'''

		value = None
		'''
	      the value with which the actuator operates.
	
	      :type: string
	
		'''

	class KX_SCA_EndObjectActuator:
		'''   Edit Object Actuator (in End Object mode)
		'''

	class SCA_ORController:
		'''   An OR controller activates when any connected sensor activates.
		'''

	class KX_VisibilityActuator:
		'''   Visibility Actuator.
		'''

		visibility = None
		'''
	      whether the actuator makes its parent object visible or invisible.
	
	      :type: boolean
	
		'''

		useOcclusion = None
		'''
	      whether the actuator makes its parent object an occluder or not.
	
	      :type: boolean
	
		'''

	class KX_StateActuator:
		'''   State actuator changes the state mask of parent object.
		'''

		operation = None
		'''
	      Type of bit operation to be applied on object state mask.
	      
	      You can use one of :ref:`these constants <state-actuator-operation>`
	
	      :type: integer
	
		'''

	class SCA_IObject:
		'''   This class has no python functions
		'''

	class KX_SceneActuator:
		'''   Scene Actuator logic brick.
		'''

		scene = None
		'''
	      the name of the scene to change to/overlay/underlay/remove/suspend/resume.
	
	      :type: string
	
		'''

		camera = None
		'''
	      the camera to change to.
	
	      :type: :class:`KX_Camera` on read, string or :class:`KX_Camera` on write
	      
	      .. note::
	         
	         When setting the attribute, you can use either a :class:`KX_Camera` or the name of the camera.
	
		'''

		useRestart = None
		'''
	      Set flag to True to restart the sene.
	
	      :type: boolean
	
		'''

	class BL_ArmatureBone:
		'''   Proxy to Blender bone structure. All fields are read-only and comply to RNA names.
	   All space attribute correspond to the rest pose.
		'''

		name = None
		'''
	      bone name.
	
	      :type: string
	
		'''

		connected = None
		'''
	      true when the bone head is struck to the parent's tail.
	
	      :type: boolean
	
		'''

		hinge = None
		'''
	      true when bone doesn't inherit rotation or scale from parent bone.
	
	      :type: boolean
	
		'''

		inherit_scale = None
		'''
	      true when bone inherits scaling from parent bone.
	
	      :type: boolean
	
		'''

		bbone_segments = None
		'''
	      number of B-bone segments.
	
	      :type: integer
	
		'''

		roll = None
		'''
	      bone rotation around head-tail axis.
	
	      :type: float
	
		'''

		head = None
		'''
	      location of head end of the bone in parent bone space.
	
	      :type: vector [x, y, z]
	
		'''

		tail = None
		'''
	      location of head end of the bone in parent bone space.
	
	      :type: vector [x, y, z]
	
		'''

		length = None
		'''
	      bone length.
	
	      :type: float
	
		'''

		arm_head = None
		'''
	      location of head end of the bone in armature space.
	
	      :type: vector [x, y, z]
	
		'''

		arm_tail = None
		'''
	      location of tail end of the bone in armature space.
	
	      :type: vector [x, y, z]
	
		'''

		arm_mat = None
		'''
	      matrix of the bone head in armature space.
	
	      :type: matrix [4][4]
	
	      .. note::
	      
	         This matrix has no scale part. 
	
		'''

		bone_mat = None
		'''
	      rotation matrix of the bone in parent bone space.
	
	      :type: matrix [3][3]
	
		'''

		parent = None
		'''
	      parent bone, or None for root bone.
	
	      :type: :class:`BL_ArmatureBone`
	
		'''

	class KX_NetworkMessageSensor:
		'''   The Message Sensor logic brick.
		'''

		subject = None
		'''
	      The subject the sensor is looking for.
	
	      :type: string
	
		'''

		frameMessageCount = None
		'''
	      The number of messages received since the last frame. (read-only).
	
	      :type: integer
	
		'''

		subjects = None
		'''
	      The list of message subjects received. (read-only).
	
	      :type: list of strings
	
		'''

	class SCA_IActuator:
		'''   Base class for all actuator logic bricks.
		'''

	class SCA_DelaySensor:
		'''   The Delay sensor generates positive and negative triggers at precise time, 
	   expressed in number of frames. The delay parameter defines the length of the initial OFF period. A positive trigger is generated at the end of this period.
		'''

		delay = None
		'''
	      length of the initial OFF period as number of frame, 0 for immediate trigger.
	
	      :type: integer.
	
		'''

		duration = None
		'''
	      length of the ON period in number of frame after the initial OFF period.
	
	      If duration is greater than 0, a negative trigger is sent at the end of the ON pulse.
	
	      :type: integer
	
		'''

	class KX_SCA_ReplaceMeshActuator:
		'''   Edit Object actuator, in Replace Mesh mode.
		'''

		mesh = None
		'''
	      :class:`MeshProxy` or the name of the mesh that will replace the current one.
	   
	      Set to None to disable actuator.
	
	      :type: :class:`MeshProxy` or None if no mesh is set
	
		'''

		useDisplayMesh = None
		'''
	      when true the displayed mesh is replaced.
	
	      :type: boolean
	
		'''

		usePhysicsMesh = None
		'''
	      when true the physics mesh is replaced.
	
	      :type: boolean
	
		'''

	class KX_SoundActuator:
		'''   Sound Actuator.
		'''

		def startSound():
			'''
	      Starts the sound.
	
	      :return: None
	
			'''
			pass

		def pauseSound():
			'''
	      Pauses the sound.
	
	      :return: None
	
			'''
			pass

		volume = None
		'''
	      The volume (gain) of the sound.
	
	      :type: float
	
		'''

		time = None
		'''
	      The current position in the audio stream (in seconds).
	
	      :type: float
	
		'''

		pitch = None
		'''
	      The pitch of the sound.
	
	      :type: float
	
		'''

		mode = None
		'''
	      The operation mode of the actuator. Can be one of :ref:`these constants<logic-sound-actuator>`
	
	      :type: integer
	
		'''

		sound = None
		'''
	      The sound the actuator should play.
	
	      :type: Audaspace factory
	
		'''

		is3D = None
		'''
	      Whether or not the actuator should be using 3D sound. (read-only)
	
	      :type: boolean
	
		'''

		volume_maximum = None
		'''
	      The maximum gain of the sound, no matter how near it is.
	
	      :type: float
	
		'''

		volume_minimum = None
		'''
	      The minimum gain of the sound, no matter how far it is away.
	
	      :type: float
	
		'''

		distance_reference = None
		'''
	      The distance where the sound has a gain of 1.0.
	
	      :type: float
	
		'''

		distance_maximum = None
		'''
	      The maximum distance at which you can hear the sound.
	
	      :type: float
	
		'''

		attenuation = None
		'''
	      The influence factor on volume depending on distance.
	
	      :type: float
	
		'''

		cone_angle_inner = None
		'''
	      The angle of the inner cone.
	
	      :type: float
	
		'''

		cone_angle_outer = None
		'''
	      The angle of the outer cone.
	
	      :type: float
	
		'''

		cone_volume_outer = None
		'''
	      The gain outside the outer cone (the gain in the outer cone will be interpolated between this value and the normal gain in the inner cone).
	
	      :type: float
	
		'''

	class BL_ActionActuator:
		'''   Action Actuators apply an action to an actor.
		'''

		action = None
		'''
	      The name of the action to set as the current action.
	
	      :type: string
	
		'''

		frameStart = None
		'''
	      Specifies the starting frame of the animation.
	
	      :type: float
	
		'''

		frameEnd = None
		'''
	      Specifies the ending frame of the animation.
	
	      :type: float
	
		'''

		blendIn = None
		'''
	      Specifies the number of frames of animation to generate when making transitions between actions.
	
	      :type: float
	
		'''

		priority = None
		'''
	      Sets the priority of this actuator. Actuators will lower priority numbers will override actuators with higher numbers.
	
	      :type: integer
	
		'''

		frame = None
		'''
	      Sets the current frame for the animation.
	
	      :type: float
	
		'''

		propName = None
		'''
	      Sets the property to be used in FromProp playback mode.
	
	      :type: string
	
		'''

		blendTime = None
		'''
	      Sets the internal frame timer. This property must be in the range from 0.0 to blendIn.
	
	      :type: float
	
		'''

		mode = None
		'''
	      The operation mode of the actuator. Can be one of :ref:`these constants<action-actuator>`.
	
	      :type: integer
	
		'''

		useContinue = None
		'''
	      The actions continue option, True or False. When True, the action will always play from where last left off,
	      otherwise negative events to this actuator will reset it to its start frame.
	
	      :type: boolean
	
		'''

	class KX_RadarSensor:
		'''   Radar sensor is a near sensor with a conical sensor object.
		'''

		coneOrigin = None
		'''
	      The origin of the cone with which to test. The origin is in the middle of the cone. (read-only).
	
	      :type: list of floats [x, y, z]
	
		'''

		coneTarget = None
		'''
	      The center of the bottom face of the cone with which to test. (read-only).
	
	      :type: list of floats [x, y, z]
	
		'''

		distance = None
		'''
	      The height of the cone with which to test.
	
	      :type: float
	
		'''

		angle = None
		'''
	      The angle of the cone (in degrees) with which to test.
	
	      :type: float
	
		'''

	class SCA_MouseSensor:
		'''   Mouse Sensor logic brick.
		'''

		position = None
		'''
	      current [x, y] coordinates of the mouse, in frame coordinates (pixels).
	
	      :type: [integer, interger]
	
		'''

		mode = None
		'''
	      sensor mode.
	
	      :type: integer
	
	         * KX_MOUSESENSORMODE_LEFTBUTTON(1)
	         * KX_MOUSESENSORMODE_MIDDLEBUTTON(2)
	         * KX_MOUSESENSORMODE_RIGHTBUTTON(3)
	         * KX_MOUSESENSORMODE_WHEELUP(4)
	         * KX_MOUSESENSORMODE_WHEELDOWN(5)
	         * KX_MOUSESENSORMODE_MOVEMENT(6)
	
		'''

	class BL_Shader:
		'''   BL_Shader GLSL shaders.
		'''

		def setUniformfv(name, fList):
			'''
	      Set a uniform with a list of float values
	
	      :arg name: the uniform name
	      :type name: string
	      :arg fList: a list (2, 3 or 4 elements) of float values
	      :type fList: list[float]
	
			'''
			pass

		def delSource():
			'''
	      Clear the shader. Use this method before the source is changed with :data:`setSource`.
	
			'''
			pass

		def getFragmentProg():
			'''
	      Returns the fragment program.
	
	      :return: The fragment program.
	      :rtype: string
	
			'''
			pass

		def getVertexProg():
			'''
	      Get the vertex program.
	
	      :return: The vertex program.
	      :rtype: string
	
			'''
			pass

		def isValid():
			'''
	      Check if the shader is valid.
	
	      :return: True if the shader is valid
	      :rtype: boolean
	
			'''
			pass

		def setAttrib(enum):
			'''
	      Set attribute location. (The parameter is ignored a.t.m. and the value of "tangent" is always used.)
	
	      :arg enum: attribute location value
	      :type enum: integer
	
			'''
			pass

		def setNumberOfPasses( max_pass ):
			'''
	      Set the maximum number of passes. Not used a.t.m.
	
	      :arg max_pass: the maximum number of passes
	      :type max_pass: integer
	
			'''
			pass

		def setSampler(name, index):
			'''
	      Set uniform texture sample index.
	
	      :arg name: Uniform name
	      :type name: string
	      :arg index: Texture sample index.
	      :type index: integer
	
			'''
			pass

		def setSource(vertexProgram, fragmentProgram):
			'''
	      Set the vertex and fragment programs
	
	      :arg vertexProgram: Vertex program
	      :type vertexProgram: string
	      :arg fragmentProgram: Fragment program
	      :type fragmentProgram: string
	
			'''
			pass

		def setUniform1f(name, fx):
			'''
	      Set a uniform with 1 float value.
	
	      :arg name: the uniform name
	      :type name: string
	      :arg fx: Uniform value
	      :type fx: float
	
			'''
			pass

		def setUniform1i(name, ix):
			'''
	      Set a uniform with an integer value.
	
	      :arg name: the uniform name
	      :type name: string
	      :arg ix: the uniform value
	      :type ix: integer
	
			'''
			pass

		def setUniform2f(name, fx, fy):
			'''
	      Set a uniform with 2 float values
	
	      :arg name: the uniform name
	      :type name: string
	      :arg fx: first float value
	      :type fx: float
	
	      :arg fy: second float value
	      :type fy: float
	
			'''
			pass

		def setUniform2i(name, ix, iy):
			'''
	      Set a uniform with 2 integer values
	
	      :arg name: the uniform name
	      :type name: string
	      :arg ix: first integer value
	      :type ix: integer
	      :arg iy: second integer value
	      :type iy: integer
	
			'''
			pass

		def setUniform3f(name, fx, fy, fz):
			'''
	      Set a uniform with 3 float values.
	
	      :arg name: the uniform name
	      :type name: string
	      :arg fx: first float value
	      :type fx: float
	      :arg fy: second float value
	      :type fy: float
	      :arg fz: third float value
	      :type fz: float
	
			'''
			pass

		def setUniform3i(name, ix, iy, iz):
			'''
	      Set a uniform with 3 integer values
	
	      :arg name: the uniform name
	      :type name: string
	      :arg ix: first integer value
	      :type ix: integer
	      :arg iy: second integer value
	      :type iy: integer
	      :arg iz: third integer value
	      :type iz: integer
	
			'''
			pass

		def setUniform4f(name, fx, fy, fz, fw):
			'''
	      Set a uniform with 4 float values.
	
	      :arg name: the uniform name
	      :type name: string
	      :arg fx: first float value
	      :type fx: float
	      :arg fy: second float value
	      :type fy: float
	      :arg fz: third float value
	      :type fz: float
	      :arg fw: fourth float value
	      :type fw: float
	
			'''
			pass

		def setUniform4i(name, ix, iy, iz, iw):
			'''
	      Set a uniform with 4 integer values
	
	      :arg name: the uniform name
	      :type name: string
	      :arg ix: first integer value
	      :type ix: integer
	      :arg iy: second integer value
	      :type iy: integer
	      :arg iz: third integer value
	      :type iz: integer
	      :arg iw: fourth integer value
	      :type iw: integer
	
			'''
			pass

		def setUniformDef(name, type):
			'''
	      Define a new uniform
	
	      :arg name: the uniform name
	      :type name: string
	      :arg type: uniform type
	      :type type: UNI_NONE, UNI_INT, UNI_FLOAT, UNI_INT2, UNI_FLOAT2, UNI_INT3, UNI_FLOAT3, UNI_INT4, UNI_FLOAT4, UNI_MAT3, UNI_MAT4, UNI_MAX
	
			'''
			pass

		def setUniformMatrix3(name, mat, transpose):
			'''
	      Set a uniform with a 3x3 matrix value
	
	      :arg name: the uniform name
	      :type name: string
	      :arg mat: A 3x3 matrix [[f, f, f], [f, f, f], [f, f, f]]
	      :type mat: 3x3 matrix
	      :arg transpose: set to True to transpose the matrix
	      :type transpose: boolean
	
			'''
			pass

		def setUniformMatrix4(name, mat, transpose):
			'''
	      Set a uniform with a 4x4 matrix value
	
	      :arg name: the uniform name
	      :type name: string
	      :arg mat: A 4x4 matrix [[f, f, f, f], [f, f, f, f], [f, f, f, f], [f, f, f, f]]
	      :type mat: 4x4 matrix
	      :arg transpose: set to True to transpose the matrix
	      :type transpose: boolean
	
			'''
			pass

		def setUniformiv(name, iList):
			'''
	      Set a uniform with a list of integer values
	
	      :arg name: the uniform name
	      :type name: string
	      :arg iList: a list (2, 3 or 4 elements) of integer values
	      :type iList: list[integer]
	
			'''
			pass

	class KX_SCA_AddObjectActuator:
		'''   Edit Object Actuator (in Add Object Mode)
		'''

		object = None
		'''
	      the object this actuator adds.
	
	      :type: :class:`KX_GameObject` or None
	
		'''

		objectLastCreated = None
		'''
	      the last added object from this actuator (read-only).
	
	      :type: :class:`KX_GameObject` or None
	
		'''

		time = None
		'''
	      the lifetime of added objects, in frames. Set to 0 to disable automatic deletion.
	
	      :type: integer
	
		'''

		linearVelocity = None
		'''
	      the initial linear velocity of added objects.
	
	      :type: list [vx, vy, vz]
	
		'''

		angularVelocity = None
		'''
	      the initial angular velocity of added objects.
	
	      :type: list [vx, vy, vz]
	
		'''

	class SCA_NORController:
		'''   An NOR controller activates only when all linked sensors are de-activated.
		'''

	class KX_SteeringActuator:
		'''   Steering Actuator for navigation.
		'''

		behavior = None
		'''
	      The steering behavior to use.
	
	      :type: one of :ref:`these constants <logic-steering-actuator>`
	
		'''

		velocity = None
		'''
	      Velocity magnitude
	
	      :type: float
	
		'''

		acceleration = None
		'''
	      Max acceleration
	
	      :type: float
	
		'''

		turnspeed = None
		'''
	      Max turn speed
	
	      :type: float
	
		'''

		distance = None
		'''
	      Relax distance
	
	      :type: float
	
		'''

		target = None
		'''
	      Target object
	
	      :type: :class:`KX_GameObject`
	
		'''

		navmesh = None
		'''
	      Navigation mesh
	
	      :type: :class:`KX_GameObject`
	
		'''

		selfterminated = None
		'''
	      Terminate when target is reached
	
	      :type: boolean
	
		'''

		enableVisualization = None
		'''
	      Enable debug visualization
	
	      :type: boolean
	
		'''

	class BL_ShapeActionActuator:
		'''   ShapeAction Actuators apply an shape action to an mesh object.
		'''

		action = None
		'''
	      The name of the action to set as the current shape action.
	
	      :type: string
	
		'''

		frameStart = None
		'''
	      Specifies the starting frame of the shape animation.
	
	      :type: float
	
		'''

		frameEnd = None
		'''
	      Specifies the ending frame of the shape animation.
	
	      :type: float
	
		'''

		blendIn = None
		'''
	      Specifies the number of frames of animation to generate when making transitions between actions.
	
	      :type: float
	
		'''

		priority = None
		'''
	      Sets the priority of this actuator. Actuators will lower priority numbers will override actuators with higher numbers.
	
	      :type: integer
	
		'''

		frame = None
		'''
	      Sets the current frame for the animation.
	
	      :type: float
	
		'''

		propName = None
		'''
	      Sets the property to be used in FromProp playback mode.
	
	      :type: string
	
		'''

		blendTime = None
		'''
	      Sets the internal frame timer. This property must be in the range from 0.0 to blendin.
	
	      :type: float
	
		'''

		mode = None
		'''
	      The operation mode of the actuator. Can be one of :ref:`these constants<shape-action-actuator>`.
	
	      :type: integer
	
		'''

	class KX_PolygonMaterial:
		'''   This is the interface to materials in the game engine.
		'''

		def updateTexture(tface, rasty):
			'''
	      Updates a realtime animation.
	
	      :arg tface: Texture face (eg mat.tface)
	      :type tface: CObject
	      :arg rasty: Rasterizer
	      :type rasty: CObject
	
			'''
			pass

		def setTexture(tface):
			'''
	      Sets texture render state.
	
	      :arg tface: Texture face
	      :type tface: CObject
	
	      .. code-block:: python
	
	         mat.setTexture(mat.tface)
	         
			'''
			pass

		def activate(rasty, cachingInfo):
			'''
	      Sets material parameters for this object for rendering.
	
	      Material Parameters set:
	
	      #. Texture
	      #. Backface culling
	      #. Line drawing
	      #. Specular Colour
	      #. Shininess
	      #. Diffuse Colour
	      #. Polygon Offset.
	
	      :arg rasty: Rasterizer instance.
	      :type rasty: CObject
	      :arg cachingInfo: Material cache instance.
	      :type cachingInfo: CObject
	
			'''
			pass

		texture = None
		'''
	      Texture name.
	
	      :type: string (read-only)
	
		'''

		gl_texture = None
		'''
	      OpenGL texture handle (eg for glBindTexture(GL_TEXTURE_2D, gl_texture).
	
	      :type: integer (read-only)
	
		'''

		material = None
		'''
	      Material name.
	
	      :type: string (read-only)
	
		'''

		tface = None
		'''
	      Texture face properties.
	
	      :type: CObject (read-only)
	
		'''

		tile = None
		'''
	      Texture is tiling.
	
	      :type: boolean
	
		'''

		tilexrep = None
		'''
	      Number of tile repetitions in x direction.
	
	      :type: integer
	
		'''

		tileyrep = None
		'''
	      Number of tile repetitions in y direction.
	
	      :type: integer
	
		'''

		drawingmode = None
		'''
	      Drawing mode for the material.
	      - 2  (drawingmode & 4)     Textured
	      - 4  (drawingmode & 16)    Light
	      - 14 (drawingmode & 16384) 3d Polygon Text.
	
	      :type: bitfield
	
		'''

		transparent = None
		'''
	      This material is transparent. All meshes with this
	      material will be rendered after non transparent meshes from back
	      to front.
	
	      :type: boolean
	
		'''

		zsort = None
		'''
	      Transparent polygons in meshes with this material will be sorted back to
	      front before rendering.
	      Non-Transparent polygons will be sorted front to back before rendering.
	
	      :type: boolean
	
		'''

		diffuse = None
		'''
	      The diffuse color of the material. black = [0.0, 0.0, 0.0] white = [1.0, 1.0, 1.0].
	
	      :type: list [r, g, b]
	
		'''

		specular = None
		'''
	      The specular color of the material. black = [0.0, 0.0, 0.0] white = [1.0, 1.0, 1.0].
	
	      :type: list [r, g, b]
	
		'''

		shininess = None
		'''
	      The shininess (specular exponent) of the material. 0.0 <= shininess <= 128.0.
	
	      :type: float
	
		'''

		specularity = None
		'''
	      The amount of specular of the material. 0.0 <= specularity <= 1.0.
	
	      :type: float
	
		'''

	class KX_Scene:
		'''   An active scene that gives access to objects, cameras, lights and scene attributes.
		'''

		def addObject(object, other, time=0):
			'''
	      Adds an object to the scene like the Add Object Actuator would.
	
	      :arg object: The object to add
	      :type object: :class:`KX_GameObject` or string
	      :arg other: The object's center to use when adding the object
	      :type other: :class:`KX_GameObject` or string
	      :arg time: The lifetime of the added object, in frames. A time of 0 means the object will last forever.
	      :type time: integer
	      :return: The newly added object.
	      :rtype: :class:`KX_GameObject`
	
			'''
			pass

		def end():
			'''
	      Removes the scene from the game.
	
			'''
			pass

		def restart():
			'''
	      Restarts the scene.
	
			'''
			pass

		def replace(scene):
			'''
	      Replaces this scene with another one.
	
	      :arg scene: The name of the scene to replace this scene with.
	      :type scene: string
	
			'''
			pass

		def suspend():
			'''
	      Suspends this scene.
	
			'''
			pass

		def resume():
			'''
	      Resume this scene.
	
			'''
			pass

		def get(key, default=None):
			'''
	      Return the value matching key, or the default value if its not found.
	      :return: The key value or a default.
	
			'''
			pass

		name = None
		'''
	      The scene's name, (read-only).
	
	      :type: string
	
		'''

		objects = None
		'''
	      A list of objects in the scene, (read-only).
	
	      :type: :class:`CListValue` of :class:`KX_GameObject`
	
		'''

		objectsInactive = None
		'''
	      A list of objects on background layers (used for the addObject actuator), (read-only).
	
	      :type: :class:`CListValue` of :class:`KX_GameObject`
	
		'''

		lights = None
		'''
	      A list of lights in the scene, (read-only).
	
	      :type: :class:`CListValue` of :class:`KX_LightObject`
	
		'''

		cameras = None
		'''
	      A list of cameras in the scene, (read-only).
	
	      :type: :class:`CListValue` of :class:`KX_Camera`
	
		'''

		active_camera = None
		'''
	      The current active camera.
	
	      :type: :class:`KX_Camera`
	      
	      .. note::
	         
	         This can be set directly from python to avoid using the :class:`KX_SceneActuator`.
	
		'''

		suspended = None
		'''
	      True if the scene is suspended, (read-only).
	
	      :type: boolean
	
		'''

		activity_culling = None
		'''
	      True if the scene is activity culling.
	
	      :type: boolean
	
		'''

		activity_culling_radius = None
		'''
	      The distance outside which to do activity culling. Measured in manhattan distance.
	
	      :type: float
	
		'''

		dbvt_culling = None
		'''
	      True when Dynamic Bounding box Volume Tree is set (read-only).
	
	      :type: boolean
	
		'''

		pre_draw = None
		'''
	      A list of callables to be run before the render step.
	
	      :type: list
	
		'''

		post_draw = None
		'''
	      A list of callables to be run after the render step.
	
	      :type: list
	
		'''

		gravity = None
		'''
	      The scene gravity using the world x, y and z axis.
	
	      :type: list [fx, fy, fz]
	
		'''

	class KX_CameraActuator:
		'''   Applies changes to a camera.
		'''

		damping = None
		'''
	      strength of of the camera following movement.
	
	      :type: float
	
		'''

		axis = None
		'''
	      The camera axis (0, 1, 2) for positive ``XYZ``, (3, 4, 5) for negative ``XYZ``.
	
	      :type: int
	
		'''

		min = None
		'''
	      minimum distance to the target object maintained by the actuator.
	
	      :type: float
	
		'''

		max = None
		'''
	      maximum distance to stay from the target object.
	
	      :type: float
	
		'''

		height = None
		'''
	      height to stay above the target object.
	
	      :type: float
	
		'''

	class KX_MeshProxy:
		'''   A mesh object.
		'''

		def getMaterialName(matid):
			'''
	      Gets the name of the specified material.
	
	      :arg matid: the specified material.
	      :type matid: integer
	      :return: the attached material name.
	      :rtype: string
	
			'''
			pass

		def getTextureName(matid):
			'''
	      Gets the name of the specified material's texture.
	
	      :arg matid: the specified material
	      :type matid: integer
	      :return: the attached material's texture name.
	      :rtype: string
	
			'''
			pass

		def getVertexArrayLength(matid):
			'''
	      Gets the length of the vertex array associated with the specified material.
	
	      There is one vertex array for each material.
	
	      :arg matid: the specified material
	      :type matid: integer
	      :return: the number of verticies in the vertex array.
	      :rtype: integer
	
			'''
			pass

		def getVertex(matid, index):
			'''
	      Gets the specified vertex from the mesh object.
	
	      :arg matid: the specified material
	      :type matid: integer
	      :arg index: the index into the vertex array.
	      :type index: integer
	      :return: a vertex object.
	      :rtype: :class:`KX_VertexProxy`
	
			'''
			pass

		def getPolygon(index):
			'''
	      Gets the specified polygon from the mesh.
	
	      :arg index: polygon number
	      :type index: integer
	      :return: a polygon object.
	      :rtype: :class:`KX_PolyProxy`
	
			'''
			pass

		def transform(matid, matrix):
			'''
	      Transforms the vertices of a mesh.
	
	      :arg matid: material index, -1 transforms all.
	      :type matid: integer
	      :arg matrix: transformation matrix.
	      :type matrix: 4x4 matrix [[float]]
	
			'''
			pass

		materials = None
		'''
	      :type: list of :class:`KX_BlenderMaterial` or :class:`KX_PolygonMaterial` types
	
		'''

		numPolygons = None
		'''
	      :type: integer
	
		'''

		numMaterials = None
		'''
	      :type: integer
	
		'''

	class SCA_KeyboardSensor:
		'''   A keyboard sensor detects player key presses.
		'''

		key = None
		'''
	      The key code this sensor is looking for.
	
	      :type: keycode from :mod:`bge.events` module
	
		'''

		hold1 = None
		'''
	      The key code for the first modifier this sensor is looking for.
	
	      :type: keycode from :mod:`bge.events` module
	
		'''

		hold2 = None
		'''
	      The key code for the second modifier this sensor is looking for.
	
	      :type: keycode from :mod:`bge.events` module
	
		'''

		toggleProperty = None
		'''
	      The name of the property that indicates whether or not to log keystrokes as a string.
	
	      :type: string
	
		'''

		targetProperty = None
		'''
	      The name of the property that receives keystrokes in case in case a string is logged.
	
	      :type: string
	
		'''

		useAllKeys = None
		'''
	      Flag to determine whether or not to accept all keys.
	
	      :type: boolean
	
		'''

		events = None
		'''
	      a list of pressed keys that have either been pressed, or just released, or are active this frame. (read-only).
	
	      :type: list [[:ref:`keycode<keyboard-keys>`, :ref:`status<input-status>`], ...]
	
		'''

	class SCA_PythonMouse:
		'''   The current mouse.
		'''

		events = None
		'''
	      a dictionary containing the status of each mouse event. (read-only).
	
	      :type: dictionary {:ref:`keycode<mouse-keys>`::ref:`status<input-status>`, ...}
	
		'''

		active_events = None
		'''
	      a dictionary containing the status of only the active mouse events. (read-only).
	
	      :type: dictionary {:ref:`keycode<mouse-keys>`::ref:`status<input-status>`, ...}
	      
		'''

		position = None
		'''
	      The normalized x and y position of the mouse cursor.
	
	      :type: list [x, y]
	
		'''

	class KX_MouseFocusSensor:
		'''   The mouse focus sensor detects when the mouse is over the current game object.
		'''

		raySource = None
		'''
	      The worldspace source of the ray (the view position).
	
	      :type: list (vector of 3 floats)
	
		'''

		rayTarget = None
		'''
	      The worldspace target of the ray.
	
	      :type: list (vector of 3 floats)
	
		'''

		rayDirection = None
		'''
	      The :data:`rayTarget` - :class:`raySource` normalized.
	
	      :type: list (normalized vector of 3 floats)
	
		'''

		hitObject = None
		'''
	      the last object the mouse was over.
	
	      :type: :class:`KX_GameObject` or None
	
		'''

		hitPosition = None
		'''
	      The worldspace position of the ray intersecton.
	
	      :type: list (vector of 3 floats)
	
		'''

		hitNormal = None
		'''
	      the worldspace normal from the face at point of intersection.
	
	      :type: list (normalized vector of 3 floats)
	
		'''

		hitUV = None
		'''
	      the UV coordinates at the point of intersection.
	
	      :type: list (vector of 2 floats)
	
	      If the object has no UV mapping, it returns [0, 0].
	
	      The UV coordinates are not normalized, they can be < 0 or > 1 depending on the UV mapping.
	
		'''

	class BL_ArmatureConstraint:
		'''   Proxy to Armature Constraint. Allows to change constraint on the fly.
	   Obtained through :class:`BL_ArmatureObject`.constraints.
		'''

		type = None
		'''
	      Type of constraint, (read-only).
	
	      Use one of :ref:`these constants<armatureconstraint-constants-type>`.
	      
	      :type: integer, one of CONSTRAINT_TYPE_* constants
	
		'''

		name = None
		'''
	      Name of constraint constructed as <bone_name>:<constraint_name>. constraints list.
	
	      :type: string
	
	      This name is also the key subscript on :class:`BL_ArmatureObject`.
	
		'''

		enforce = None
		'''
	      fraction of constraint effect that is enforced. Between 0 and 1.
	
	      :type: float
	
		'''

		headtail = None
		'''
	      Position of target between head and tail of the target bone: 0=head, 1=tail.
	
	      :type: float.
	
	      .. note::
	      
	         Only used if the target is a bone (i.e target object is an armature.
	
		'''

		lin_error = None
		'''
	      runtime linear error (in Blender units) on constraint at the current frame.
	
	      This is a runtime value updated on each frame by the IK solver. Only available on IK constraint and iTaSC solver.
	
	      :type: float
	
		'''

		rot_error = None
		'''
	      Runtime rotation error (in radiant) on constraint at the current frame.
	
	      :type: float.
	
	      This is a runtime value updated on each frame by the IK solver. Only available on IK constraint and iTaSC solver.
	
	      It is only set if the constraint has a rotation part, for example, a CopyPose+Rotation IK constraint.
	
		'''

		target = None
		'''
	      Primary target object for the constraint. The position of this object in the GE will be used as target for the constraint.
	
	      :type: :class:`KX_GameObject`.
	
		'''

		subtarget = None
		'''
	      Secondary target object for the constraint. The position of this object in the GE will be used as secondary target for the constraint.
	
	      :type: :class:`KX_GameObject`.
	
	      Currently this is only used for pole target on IK constraint.
	
		'''

		active = None
		'''
	      True if the constraint is active.
	
	      :type: boolean
	      
	      .. note::
	      
	         An inactive constraint does not update lin_error and rot_error.
	
		'''

		ik_weight = None
		'''
	      Weight of the IK constraint between 0 and 1.
	
	      Only defined for IK constraint.
	
	      :type: float
	
		'''

		ik_type = None
		'''
	      Type of IK constraint, (read-only).
	
	      Use one of :ref:`these constants<armatureconstraint-constants-ik-type>`.
	      
	      :type: integer.
	
		'''

		ik_flag = None
		'''
	      Combination of IK constraint option flags, read-only.
	      
	      Use one of :ref:`these constants<armatureconstraint-constants-ik-flag>`.
	
	      :type: integer
	
		'''

		ik_dist = None
		'''
	      Distance the constraint is trying to maintain with target, only used when ik_type=CONSTRAINT_IK_DISTANCE.
	
	      :type: float
	
		'''

	class PyObjectPlus:
		'''   PyObjectPlus base class of most other types in the Game Engine.
		'''

	class SCA_PropertySensor:
		'''   Activates when the game object property matches.
		'''

		mode = None
		'''
	      Type of check on the property. Can be one of :ref:`these constants <logic-property-sensor>`
	
	      :type: integer.
	
		'''

		propName = None
		'''
	      the property the sensor operates.
	
	      :type: string
	
		'''

		value = None
		'''
	      the value with which the sensor compares to the value of the property.
	
	      :type: string
	
		'''

		min = None
		'''
	      the minimum value of the range used to evaluate the property when in interval mode.
	
	      :type: string
	
		'''

	class SCA_ISensor:
		'''   Base class for all sensor logic bricks.
		'''

		usePosPulseMode = None
		'''
	      Flag to turn positive pulse mode on and off.
	      
	      :type: boolean
	
		'''

		useNegPulseMode = None
		'''
	      Flag to turn negative pulse mode on and off.
	      
	      :type: boolean
	
		'''

		frequency = None
		'''
	      The frequency for pulse mode sensors.
	      
	      :type: integer
	
		'''

		level = None
		'''
	      level Option whether to detect level or edge transition when entering a state.
	      It makes a difference only in case of logic state transition (state actuator).
	      A level detector will immediately generate a pulse, negative or positive
	      depending on the sensor condition, as soon as the state is activated.
	      A edge detector will wait for a state change before generating a pulse.
	      note: mutually exclusive with :data:`tap`, enabling will disable :data:`tap`.
	
	      :type: boolean
	
		'''

		tap = None
		'''
	      When enabled only sensors that are just activated will send a positive event, 
	      after this they will be detected as negative by the controllers.
	      This will make a key thats held act as if its only tapped for an instant.
	      note: mutually exclusive with :data:`level`, enabling will disable :data:`level`.
	
	      :type: boolean
	
		'''

		invert = None
		'''
	      Flag to set if this sensor activates on positive or negative events.
	      
	      :type: boolean
	
		'''

		triggered = None
		'''
	      True if this sensor brick is in a positive state. (read-only).
	     
	      :type: boolean
	
		'''

		positive = None
		'''
	      True if this sensor brick is in a positive state. (read-only).
	      
	      :type: boolean
	
		'''

		pos_ticks = None
		'''
	      The number of ticks since the last positive pulse (read-only).
	      
	      :type: int
	
		'''

		neg_ticks = None
		'''
	      The number of ticks since the last negative pulse (read-only).
	      
	      :type: int
	
		'''

		status = None
		'''
	      The status of the sensor (read-only): can be one of :ref:`these constants<sensor-status>`.
	
	      :type: int
	
	      .. note::
	      
	         This convenient attribute combines the values of triggered and positive attributes.
	
		'''

	class KX_CharacterWrapper:
		'''   A wrapper to expose character physics options.
		'''

		onGround = None
		'''
	      Whether or not the character is on the ground. (read-only)
	
	      :type: boolean
	
		'''

		gravity = None
		'''
	      The gravity value used for the character.
	
	      :type: float
	
		'''

		maxJumps = None
		'''
	      The maximum number of jumps a character can perform before having to touch the ground. By default this is set to 1. 2 allows for a double jump, etc.
	
	      :type: int
	
		'''

		jumpCount = None
		'''
	      The current jump count. This can be used to have different logic for a single jump versus a double jump. For example, a different animation for the second jump.
	
	      :type: int
	
		'''

		walkDirection = None
		'''
	      The speed and direction the character is traveling in using world coordinates. This should be used instead of applyMovement() to properly move the character.
	
	      :type: list [x, y, z]
	
		'''

	class KX_ParentActuator:
		'''   The parent actuator can set or remove an objects parent object.
		'''

		object = None
		'''
	      the object this actuator sets the parent too.
	
	      :type: :class:`KX_GameObject` or None
	
		'''

		mode = None
		'''
	      The mode of this actuator.
	
	      :type: integer from 0 to 1.
	
		'''

		compound = None
		'''
	      Whether the object shape should be added to the parent compound shape when parenting.
	
	      Effective only if the parent is already a compound shape.
	
	      :type: boolean
	
		'''

	class KX_ConstraintActuator:
		'''   A constraint actuator limits the position, rotation, distance or orientation of an object.
		'''

		damp = None
		'''
	      Time constant of the constraint expressed in frame (not use by Force field constraint).
	
	      :type: integer
	
		'''

		rotDamp = None
		'''
	      Time constant for the rotation expressed in frame (only for the distance constraint), 0 = use damp for rotation as well.
	
	      :type: integer
	
		'''

		direction = None
		'''
	      The reference direction in world coordinate for the orientation constraint.
	
	      :type: 3-tuple of float: (x, y, z)
	
		'''

		option = None
		'''
	      Binary combination of :ref:`these constants <constraint-actuator-option>`
	
	      :type: integer
	
		'''

		time = None
		'''
	      activation time of the actuator. The actuator disables itself after this many frame. If set to 0, the actuator is not limited in time.
	
	      :type: integer
	
		'''

		propName = None
		'''
	      the name of the property or material for the ray detection of the distance constraint.
	
	      :type: string
	
		'''

		min = None
		'''
	      The lower bound of the constraint. For the rotation and orientation constraint, it represents radiant.
	
	      :type: float
	
		'''

		distance = None
		'''
	      the target distance of the distance constraint.
	
	      :type: float
	
		'''

		max = None
		'''
	      the upper bound of the constraint. For rotation and orientation constraints, it represents radiant.
	
	      :type: float
	
		'''

		rayLength = None
		'''
	      the length of the ray of the distance constraint.
	
	      :type: float
	
		'''

	class KX_VertexProxy:
		'''   A vertex holds position, UV, color and normal information.
		'''

		def getXYZ():
			'''
	      Gets the position of this vertex.
	
	      :return: this vertexes position in local coordinates.
	      :rtype: list [x, y, z]
	
			'''
			pass

		def setXYZ(pos):
			'''
	      Sets the position of this vertex.
	
	      :type:  list [x, y, z]
	
	      :arg pos: the new position for this vertex in local coordinates.
	
			'''
			pass

		def getUV():
			'''
	      Gets the UV (texture) coordinates of this vertex.
	
	      :return: this vertexes UV (texture) coordinates.
	      :rtype: list [u, v]
	
			'''
			pass

		def setUV(uv):
			'''
	      Sets the UV (texture) coordinates of this vertex.
	
	      :type:  list [u, v]
	
			'''
			pass

		def getUV2():
			'''
	      Gets the 2nd UV (texture) coordinates of this vertex.
	
	      :return: this vertexes UV (texture) coordinates.
	      :rtype: list [u, v]
	
			'''
			pass

		def setUV2(uv, unit):
			'''
	      Sets the 2nd UV (texture) coordinates of this vertex.
	
	      :type:  list [u, v]
	
	      :arg unit: optional argument, FLAT==1, SECOND_UV==2, defaults to SECOND_UV
	      :arg unit:  integer
	
			'''
			pass

		def getRGBA():
			'''
	      Gets the color of this vertex.
	
	      The color is represented as four bytes packed into an integer value.  The color is
	      packed as RGBA.
	
	      Since Python offers no way to get each byte without shifting, you must use the struct module to
	      access color in an machine independent way.
	
	      Because of this, it is suggested you use the r, g, b and a attributes or the color attribute instead.
	
	      .. code-block:: python
	
	         import struct;
	         col = struct.unpack('4B', struct.pack('I', v.getRGBA()))
	         # col = (r, g, b, a)
	         # black = (  0, 0, 0, 255)
	         # white = (255, 255, 255, 255)
	
	      :return: packed color. 4 byte integer with one byte per color channel in RGBA format.
	      :rtype: integer
	
			'''
			pass

		def setRGBA(col):
			'''
	      Sets the color of this vertex.
	
	      See getRGBA() for the format of col, and its relevant problems.  Use the r, g, b and a attributes
	      or the color attribute instead.
	
	      setRGBA() also accepts a four component list as argument col.  The list represents the color as [r, g, b, a]
	      with black = [0.0, 0.0, 0.0, 1.0] and white = [1.0, 1.0, 1.0, 1.0]
	
	      .. code-block:: python
	
	         v.setRGBA(0xff0000ff) # Red
	         v.setRGBA(0xff00ff00) # Green on little endian, transparent purple on big endian
	         v.setRGBA([1.0, 0.0, 0.0, 1.0]) # Red
	         v.setRGBA([0.0, 1.0, 0.0, 1.0]) # Green on all platforms.
	
	      :arg col: the new color of this vertex in packed RGBA format.
	      :type col: integer or list [r, g, b, a]
	
			'''
			pass

		def getNormal():
			'''
	      Gets the normal vector of this vertex.
	
	      :return: normalized normal vector.
	      :rtype: list [nx, ny, nz]
	
			'''
			pass

		XYZ = None
		'''
	      The position of the vertex.
	
	      :type: list [x, y, z]
	
		'''

		UV = None
		'''
	      The texture coordinates of the vertex.
	
	      :type: list [u, v]
	
		'''

		normal = None
		'''
	      The normal of the vertex.
	
	      :type: list [nx, ny, nz]
	
		'''

		color = None
		'''
	      The color of the vertex.
	
	      :type: list [r, g, b, a]
	
	      Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0]
	
		'''

		x = None
		'''
	      The x coordinate of the vertex.
	
	      :type: float
	
		'''

		y = None
		'''
	      The y coordinate of the vertex.
	
	      :type: float
	
		'''

		z = None
		'''
	      The z coordinate of the vertex.
	
	      :type: float
	
		'''

		u = None
		'''
	      The u texture coordinate of the vertex.
	
	      :type: float
	
		'''

		v = None
		'''
	      The v texture coordinate of the vertex.
	
	      :type: float
	
		'''

		u2 = None
		'''
	      The second u texture coordinate of the vertex.
	
	      :type: float
	
		'''

		v2 = None
		'''
	      The second v texture coordinate of the vertex.
	
	      :type: float
	
		'''

		r = None
		'''
	      The red component of the vertex color. 0.0 <= r <= 1.0.
	
	      :type: float
	
		'''

		g = None
		'''
	      The green component of the vertex color. 0.0 <= g <= 1.0.
	
	      :type: float
	
		'''

		b = None
		'''
	      The blue component of the vertex color. 0.0 <= b <= 1.0.
	
	      :type: float
	
		'''

		a = None
		'''
	      The alpha component of the vertex color. 0.0 <= a <= 1.0.
	
	      :type: float
	
		'''

	class KX_NetworkMessageActuator:
		'''   Message Actuator
		'''

		propName = None
		'''
	      Messages will only be sent to objects with the given property name.
	
	      :type: string
	
		'''

		subject = None
		'''
	      The subject field of the message.
	
	      :type: string
	
		'''

		body = None
		'''
	      The body of the message.
	
	      :type: string
	
		'''

	class KX_NearSensor:
		'''   A near sensor is a specialised form of touch sensor.
		'''

		distance = None
		'''
	      The near sensor activates when an object is within this distance.
	
	      :type: float
	
		'''

	class KX_Camera:
		'''   A Camera object.
		'''

		def sphereInsideFrustum(centre, radius):
			'''
	      Tests the given sphere against the view frustum.
	
	      :arg centre: The centre of the sphere (in world coordinates.)
	      :type centre: list [x, y, z]
	      :arg radius: the radius of the sphere
	      :type radius: float
	      :return: :data:`~bge.types.KX_Camera.INSIDE`, :data:`~bge.types.KX_Camera.OUTSIDE` or :data:`~bge.types.KX_Camera.INTERSECT`
	      :rtype: integer
	
	      .. note::
	
	         When the camera is first initialized the result will be invalid because the projection matrix has not been set.
	
	      .. code-block:: python
	
	         from bge import logic
	         cont = logic.getCurrentController()
	         cam = cont.owner
	         
	         # A sphere of radius 4.0 located at [x, y, z] = [1.0, 1.0, 1.0]
	         if (cam.sphereInsideFrustum([1.0, 1.0, 1.0], 4) != cam.OUTSIDE):
	             # Sphere is inside frustum !
	             # Do something useful !
	         else:
	             # Sphere is outside frustum
	
			'''
			pass

		def boxInsideFrustum(box):
			'''
	      Tests the given box against the view frustum.
	
	      :arg box: Eight (8) corner points of the box (in world coordinates.)
	      :type box: list of lists
	      :return: :data:`~bge.types.KX_Camera.INSIDE`, :data:`~bge.types.KX_Camera.OUTSIDE` or :data:`~bge.types.KX_Camera.INTERSECT`
	
	      .. note::
	      
	         When the camera is first initialized the result will be invalid because the projection matrix has not been set.
	
	      .. code-block:: python
	
	         from bge import logic
	         cont = logic.getCurrentController()
	         cam = cont.owner
	
	         # Box to test...
	         box = []
	         box.append([-1.0, -1.0, -1.0])
	         box.append([-1.0, -1.0,  1.0])
	         box.append([-1.0,  1.0, -1.0])
	         box.append([-1.0,  1.0,  1.0])
	         box.append([ 1.0, -1.0, -1.0])
	         box.append([ 1.0, -1.0,  1.0])
	         box.append([ 1.0,  1.0, -1.0])
	         box.append([ 1.0,  1.0,  1.0])
	         
	         if (cam.boxInsideFrustum(box) != cam.OUTSIDE):
	           # Box is inside/intersects frustum !
	           # Do something useful !
	         else:
	           # Box is outside the frustum !
	           
			'''
			pass

		def pointInsideFrustum(point):
			'''
	      Tests the given point against the view frustum.
	
	      :arg point: The point to test (in world coordinates.)
	      :type point: 3D Vector
	      :return: True if the given point is inside this camera's viewing frustum.
	      :rtype: boolean
	
	      .. note::
	      
	         When the camera is first initialized the result will be invalid because the projection matrix has not been set.
	
	      .. code-block:: python
	
	         from bge import logic
	         cont = logic.getCurrentController()
	         cam = cont.owner
	
	         # Test point [0.0, 0.0, 0.0]
	         if (cam.pointInsideFrustum([0.0, 0.0, 0.0])):
	           # Point is inside frustum !
	           # Do something useful !
	         else:
	           # Box is outside the frustum !
	
			'''
			pass

		def getCameraToWorld():
			'''
	      Returns the camera-to-world transform.
	
	      :return: the camera-to-world transform matrix.
	      :rtype: matrix (4x4 list)
	
			'''
			pass

		def getWorldToCamera():
			'''
	      Returns the world-to-camera transform.
	
	      This returns the inverse matrix of getCameraToWorld().
	
	      :return: the world-to-camera transform matrix.
	      :rtype: matrix (4x4 list)
	
			'''
			pass

		def setOnTop():
			'''
	      Set this cameras viewport ontop of all other viewport.
	
			'''
			pass

		def setViewport(left, bottom, right, top):
			'''
	      Sets the region of this viewport on the screen in pixels.
	
	      Use :data:`bge.render.getWindowHeight` and :data:`bge.render.getWindowWidth` to calculate values relative to the entire display.
	
	      :arg left: left pixel coordinate of this viewport
	      :type left: integer
	      :arg bottom: bottom pixel coordinate of this viewport
	      :type bottom: integer
	      :arg right: right pixel coordinate of this viewport
	      :type right: integer
	      :arg top: top pixel coordinate of this viewport
	      :type top: integer
	
			'''
			pass

		def getScreenPosition(object):
			'''
	      Gets the position of an object projected on screen space.
	
	      .. code-block:: python
	
	         # For an object in the middle of the screen, coord = [0.5, 0.5]
	         coord = camera.getScreenPosition(object)
	
	      :arg object: object name or list [x, y, z]
	      :type object: :class:`KX_GameObject` or 3D Vector
	      :return: the object's position in screen coordinates.
	      :rtype: list [x, y]
	
			'''
			pass

		def getScreenVect(x, y):
			'''
	      Gets the vector from the camera position in the screen coordinate direction.
	
	      :arg x: X Axis
	      :type x: float
	      :arg y: Y Axis
	      :type y: float
	      :rtype: 3D Vector
	      :return: The vector from screen coordinate.
	
	      .. code-block:: python
	
	         # Gets the vector of the camera front direction:
	         m_vect = camera.getScreenVect(0.5, 0.5)
	
			'''
			pass

		INSIDE = None
		'''
	      See :data:`sphereInsideFrustum` and :data:`boxInsideFrustum`
	
		'''

		INTERSECT = None
		'''
	      See :data:`sphereInsideFrustum` and :data:`boxInsideFrustum`
	
		'''

		OUTSIDE = None
		'''
	      See :data:`sphereInsideFrustum` and :data:`boxInsideFrustum`
	
		'''

		lens = None
		'''
	      The camera's lens value.
	
	      :type: float
	
		'''

		fov = None
		'''
	      The camera's field of view value.
	
	      :type: float
	
		'''

		ortho_scale = None
		'''
	      The camera's view scale when in orthographic mode.
	
	      :type: float
	
		'''

		near = None
		'''
	      The camera's near clip distance.
	
	      :type: float
	
		'''

		far = None
		'''
	      The camera's far clip distance.
	
	      :type: float
	
		'''

		perspective = None
		'''
	      True if this camera has a perspective transform, False for an orthographic projection.
	
	      :type: boolean
	
		'''

		frustum_culling = None
		'''
	      True if this camera is frustum culling.
	
	      :type: boolean
	
		'''

		projection_matrix = None
		'''
	      This camera's 4x4 projection matrix.
	
	      .. note::
	      
	         This is the identity matrix prior to rendering the first frame (any Python done on frame 1). 
	
	      :type: 4x4 Matrix [[float]]
	
		'''

		modelview_matrix = None
		'''
	      This camera's 4x4 model view matrix. (read-only).
	
	      :type: 4x4 Matrix [[float]]
	
	      .. note::
	      
	         This matrix is regenerated every frame from the camera's position and orientation. Also, this is the identity matrix prior to rendering the first frame (any Python done on frame 1).
	
		'''

		camera_to_world = None
		'''
	      This camera's camera to world transform. (read-only).
	
	      :type: 4x4 Matrix [[float]]
	
	      .. note::
	      
	         This matrix is regenerated every frame from the camera's position and orientation.
	
		'''

		world_to_camera = None
		'''
	      This camera's world to camera transform. (read-only).
	
	      :type: 4x4 Matrix [[float]]
	
	      .. note::
	         
	         Regenerated every frame from the camera's position and orientation.
	
	      .. note::
	      
	         This is camera_to_world inverted.
	
		'''

		useViewport = None
		'''
	      True when the camera is used as a viewport, set True to enable a viewport for this camera.
	
	      :type: boolean
	
		'''

	class KX_LightObject:
		'''   A Light object.
		'''

		SPOT = None
		'''
	      A spot light source. See attribute :data:`type`
	
		'''

		SUN = None
		'''
	      A point light source with no attenuation. See attribute :data:`type`
	
		'''

		NORMAL = None
		'''
	      A point light source. See attribute :data:`type`
	
		'''

		type = None
		'''
	      The type of light - must be SPOT, SUN or NORMAL
	
		'''

		layer = None
		'''
	      The layer mask that this light affects object on.
	
	      :type: bitfield
	
		'''

		energy = None
		'''
	      The brightness of this light.
	
	      :type: float
	
		'''

		distance = None
		'''
	      The maximum distance this light can illuminate. (SPOT and NORMAL lights only).
	
	      :type: float
	
		'''

		color = None
		'''
	      The color of this light. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].
	
	      :type: list [r, g, b]
	
		'''

		lin_attenuation = None
		'''
	      The linear component of this light's attenuation. (SPOT and NORMAL lights only).
	
	      :type: float
	
		'''

		quad_attenuation = None
		'''
	      The quadratic component of this light's attenuation (SPOT and NORMAL lights only).
	
	      :type: float
	
		'''

		spotsize = None
		'''
	      The cone angle of the spot light, in degrees (SPOT lights only).
	
	      :type: float in [0 - 180].
	
		'''

	class SCA_RandomSensor:
		'''   This sensor activates randomly.
		'''

		lastDraw = None
		'''
	      The seed of the random number generator.
	
	      :type: integer
	
		'''

	class SCA_XNORController:
		'''   An XNOR controller activates when all linked sensors are the same (activated or inative).
		'''

	class SCA_PythonKeyboard:
		'''   The current keyboard.
		'''

		def getClipboard():
			'''
	      Gets the clipboard text.
	
	      :rtype: string
	
			'''
			pass

		events = None
		'''
	      A dictionary containing the status of each keyboard event or key. (read-only).
	
	      :type: dictionary {:ref:`keycode<keyboard-keys>`::ref:`status<input-status>`, ...}
	
		'''

		active_events = None
		'''
	      A dictionary containing the status of only the active keyboard events or keys. (read-only).
	
	      :type: dictionary {:ref:`keycode<keyboard-keys>`::ref:`status<input-status>`, ...}
	
	
		'''

	class KX_FontObject:
		'''   TODO.
		'''

	class KX_SCA_DynamicActuator:
		'''   Dynamic Actuator.
		'''

		mode = None
		'''
	      :type: integer
	
	      the type of operation of the actuator, 0-4
	
	      * KX_DYN_RESTORE_DYNAMICS(0)
	      * KX_DYN_DISABLE_DYNAMICS(1)
	      * KX_DYN_ENABLE_RIGID_BODY(2)
	      * KX_DYN_DISABLE_RIGID_BODY(3)
	      * KX_DYN_SET_MASS(4)
	
		'''

	class CPropValue:
		'''   This class has no python functions
		'''

	class KX_TouchSensor:
		'''   Touch sensor detects collisions between objects.
		'''

		propName = None
		'''
	      The property or material to collide with.
	
	      :type: string
	
		'''

		useMaterial = None
		'''
	      Determines if the sensor is looking for a property or material. KX_True = Find material; KX_False = Find property.
	
	      :type: boolean
	
		'''

		usePulseCollision = None
		'''
	      When enabled, changes to the set of colliding objects generate a pulse.
	
	      :type: boolean
	
		'''

		hitObject = None
		'''
	      The last collided object. (read-only).
	
	      :type: :class:`KX_GameObject` or None
	
		'''

		hitObjectList = None
		'''
	      A list of colliding objects. (read-only).
	
	      :type: :class:`CListValue` of :class:`KX_GameObject`
	
		'''

	class KX_ArmatureSensor:
		'''   Armature sensor detect conditions on armatures.
		'''

		type = None
		'''
	      The type of measurement that the sensor make when it is active.
	      
	      Can be one of :ref:`these constants <armaturesensor-type>`
	
	      :type: integer.
	
		'''

		constraint = None
		'''
	      The constraint object this sensor is watching.
	
	      :type: :class:`BL_ArmatureConstraint`
	
		'''

	class KX_PolyProxy:
		'''   A polygon holds the index of the vertex forming the poylgon.
		'''

		def getMaterialName():
			'''
	      Returns the polygon material name with MA prefix
	
	      :return: material name
	      :rtype: string
	
			'''
			pass

		def getMaterial():
			'''
	      :return: The polygon material
	      :rtype: :class:`KX_PolygonMaterial` or :class:`KX_BlenderMaterial`
	
			'''
			pass

		def getTextureName():
			'''
	      :return: The texture name
	      :rtype: string
	
			'''
			pass

		def getMaterialIndex():
			'''
	      Returns the material bucket index of the polygon.
	      This index and the ones returned by getVertexIndex() are needed to retrieve the vertex proxy from :class:`MeshProxy`.
	
	      :return: the material index in the mesh
	      :rtype: integer
	
			'''
			pass

		def getNumVertex():
			'''
	      Returns the number of vertex of the polygon.
	
	      :return: number of vertex, 3 or 4.
	      :rtype: integer
	
			'''
			pass

		def isVisible():
			'''
	      Returns whether the polygon is visible or not
	
	      :return: 0=invisible, 1=visible
	      :rtype: boolean
	
			'''
			pass

		def isCollider():
			'''
	      Returns whether the polygon is receives collision or not
	
	      :return: 0=collision free, 1=receives collision
	      :rtype: integer
	
			'''
			pass

		def getVertexIndex(vertex):
			'''
	      Returns the mesh vertex index of a polygon vertex
	      This index and the one returned by getMaterialIndex() are needed to retrieve the vertex proxy from :class:`MeshProxy`.
	
	      :arg vertex: index of the vertex in the polygon: 0->3
	      :arg vertex: integer
	      :return: mesh vertex index
	      :rtype: integer
	
			'''
			pass

		material_name = None
		'''
	      The name of polygon material, empty if no material.
	
	      :type: string
	
		'''

		material = None
		'''
	      The material of the polygon.
	
	      :type: :class:`KX_PolygonMaterial` or :class:`KX_BlenderMaterial`
	
		'''

		texture_name = None
		'''
	      The texture name of the polygon.
	
	      :type: string
	
		'''

		material_id = None
		'''
	      The material index of the polygon, use this to retrieve vertex proxy from mesh proxy.
	
	      :type: integer
	
		'''

		v1 = None
		'''
	      vertex index of the first vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.
	
	      :type: integer
	
		'''

		v2 = None
		'''
	      vertex index of the second vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.
	
	      :type: integer
	
		'''

		v3 = None
		'''
	      vertex index of the third vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.
	
	      :type: integer
	
		'''

		v4 = None
		'''
	      Vertex index of the fourth vertex of the polygon, 0 if polygon has only 3 vertex
	      Use this to retrieve vertex proxy from mesh proxy.
	
	      :type: integer
	
		'''

		visible = None
		'''
	      visible state of the polygon: 1=visible, 0=invisible.
	
	      :type: integer
	
		'''

		collide = None
		'''
	      collide state of the polygon: 1=receives collision, 0=collision free.
	
	      :type: integer
	
		'''

	class KX_VehicleWrapper:
		'''   KX_VehicleWrapper
		'''

		def addWheel(wheel, attachPos, attachDir, axleDir, suspensionRestLength, wheelRadius, hasSteering):
			'''
	      Add a wheel to the vehicle
	
	      :arg wheel: The object to use as a wheel.
	      :type wheel: :class:`KX_GameObject` or a KX_GameObject name
	      :arg attachPos: The position that this wheel will attach to.
	      :type attachPos: vector of 3 floats
	      :arg attachDir: The direction this wheel points.
	      :type attachDir: vector of 3 floats
	      :arg axleDir: The direction of this wheels axle.
	      :type axleDir: vector of 3 floats
	      :arg suspensionRestLength: TODO - Description
	      :type suspensionRestLength: float
	      :arg wheelRadius: The size of the wheel.
	      :type wheelRadius: float
	
			'''
			pass

		def applyBraking(force, wheelIndex):
			'''
	      Apply a braking force to the specified wheel
	
	      :arg force: the brake force
	      :type force: float
	
	      :arg wheelIndex: index of the wheel where the force needs to be applied
	      :type wheelIndex: integer
	
			'''
			pass

		def applyEngineForce(force, wheelIndex):
			'''
	      Apply an engine force to the specified wheel
	
	      :arg force: the engine force
	      :type force: float
	
	      :arg wheelIndex: index of the wheel where the force needs to be applied
	      :type wheelIndex: integer
	
			'''
			pass

		def getConstraintId():
			'''
	      Get the constraint ID
	
	      :return: the constraint id
	      :rtype: integer
	
			'''
			pass

		def getConstraintType():
			'''
	      Returns the constraint type.
	
	      :return: constraint type
	      :rtype: integer
	
			'''
			pass

		def getNumWheels():
			'''
	      Returns the number of wheels.
	
	      :return: the number of wheels for this vehicle
	      :rtype: integer
	
			'''
			pass

		def getWheelOrientationQuaternion(wheelIndex):
			'''
	      Returns the wheel orientation as a quaternion.
	
	      :arg wheelIndex: the wheel index
	      :type wheelIndex: integer
	
	      :return: TODO Description
	      :rtype: TODO - type should be quat as per method name but from the code it looks like a matrix
	
			'''
			pass

		def getWheelPosition(wheelIndex):
			'''
	      Returns the position of the specified wheel
	
	      :arg wheelIndex: the wheel index
	      :type wheelIndex: integer
	      :return: position vector
	      :rtype: list[x, y, z]
	
			'''
			pass

		def getWheelRotation(wheelIndex):
			'''
	      Returns the rotation of the specified wheel
	
	      :arg wheelIndex: the wheel index
	      :type wheelIndex: integer
	
	      :return: the wheel rotation
	      :rtype: float
	
			'''
			pass

		def setRollInfluence(rollInfluece, wheelIndex):
			'''
	      Set the specified wheel's roll influence.
	      The higher the roll influence the more the vehicle will tend to roll over in corners.
	
	      :arg rollInfluece: the wheel roll influence
	      :type rollInfluece: float
	
	      :arg wheelIndex: the wheel index
	      :type wheelIndex: integer
	
			'''
			pass

		def setSteeringValue(steering, wheelIndex):
			'''
	      Set the specified wheel's steering
	
	      :arg steering: the wheel steering
	      :type steering: float
	
	      :arg wheelIndex: the wheel index
	      :type wheelIndex: integer
	
			'''
			pass

		def setSuspensionCompression(compression, wheelIndex):
			'''
	      Set the specified wheel's compression
	
	      :arg compression: the wheel compression
	      :type compression: float
	
	      :arg wheelIndex: the wheel index
	      :type wheelIndex: integer
	
			'''
			pass

		def setSuspensionDamping(damping, wheelIndex):
			'''
	      Set the specified wheel's damping
	
	      :arg damping: the wheel damping
	      :type damping: float
	
	      :arg wheelIndex: the wheel index
	      :type wheelIndex: integer
	
			'''
			pass

		def setSuspensionStiffness(stiffness, wheelIndex):
			'''
	      Set the specified wheel's stiffness
	
	      :arg stiffness: the wheel stiffness
	      :type stiffness: float
	
	      :arg wheelIndex: the wheel index
	      :type wheelIndex: integer
	
			'''
			pass

	class BL_ArmatureChannel:
		'''   Proxy to armature pose channel. Allows to read and set armature pose.
	   The attributes are identical to RNA attributes, but mostly in read-only mode.
		'''

		name = None
		'''
	      channel name (=bone name), read-only.
	
	      :type: string
	
		'''

		bone = None
		'''
	      return the bone object corresponding to this pose channel, read-only.
	
	      :type: :class:`BL_ArmatureBone`
	
		'''

		parent = None
		'''
	      return the parent channel object, None if root channel, read-only.
	
	      :type: :class:`BL_ArmatureChannel`
	
		'''

		has_ik = None
		'''
	      true if the bone is part of an active IK chain, read-only.
	      This flag is not set when an IK constraint is defined but not enabled (miss target information for example).
	
	      :type: boolean
	
		'''

		ik_dof_x = None
		'''
	      true if the bone is free to rotation in the X axis, read-only.
	
	      :type: boolean
	
		'''

		ik_dof_y = None
		'''
	      true if the bone is free to rotation in the Y axis, read-only.
	
	      :type: boolean
	
		'''

		ik_dof_z = None
		'''
	      true if the bone is free to rotation in the Z axis, read-only.
	
	      :type: boolean
	
		'''

		ik_limit_x = None
		'''
	      true if a limit is imposed on X rotation, read-only.
	
	      :type: boolean
	
		'''

		ik_limit_y = None
		'''
	      true if a limit is imposed on Y rotation, read-only.
	
	      :type: boolean
	
		'''

		ik_limit_z = None
		'''
	      true if a limit is imposed on Z rotation, read-only.
	
	      :type: boolean
	
		'''

		ik_rot_control = None
		'''
	      true if channel rotation should applied as IK constraint, read-only.
	
	      :type: boolean
	
		'''

		ik_lin_control = None
		'''
	      true if channel size should applied as IK constraint, read-only.
	
	      :type: boolean
	
		'''

		location = None
		'''
	      displacement of the bone head in armature local space, read-write.
	
	      :type: vector [X, Y, Z].
	
	      .. note::
	      
	         You can only move a bone if it is unconnected to its parent. An action playing on the armature may change the value. An IK chain does not update this value, see joint_rotation.
	
	      .. note::
	      
	         Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see :data:`BL_ArmatureObject.update`).
	
		'''

		scale = None
		'''
	      scale of the bone relative to its parent, read-write.
	
	      :type: vector [sizeX, sizeY, sizeZ].
	
	      .. note::
	      
	         An action playing on the armature may change the value.  An IK chain does not update this value, see joint_rotation.
	
	      .. note::
	      
	         Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see :data:`BL_ArmatureObject.update`)
	
		'''

		rotation_quaternion = None
		'''
	      rotation of the bone relative to its parent expressed as a quaternion, read-write.
	
	      :type: vector [qr, qi, qj, qk].
	
	      .. note::
	      
	         This field is only used if rotation_mode is 0. An action playing on the armature may change the value.  An IK chain does not update this value, see joint_rotation.
	
	      .. note::
	      
	         Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see :data:`BL_ArmatureObject.update`)
	
		'''

		rotation_euler = None
		'''
	      rotation of the bone relative to its parent expressed as a set of euler angles, read-write.
	
	      :type: vector [X, Y, Z].
	
	      .. note::
	      
	         This field is only used if rotation_mode is > 0. You must always pass the angles in [X, Y, Z] order; the order of applying the angles to the bone depends on rotation_mode. An action playing on the armature may change this field.  An IK chain does not update this value, see joint_rotation.
	
	      .. note::
	      
	         Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see :data:`BL_ArmatureObject.update`)
	
		'''

		rotation_mode = None
		'''
	      Method of updating the bone rotation, read-write.
	
	      :type: integer (one of :ref:`these constants <armaturechannel-constants-rotation-mode>`)
	
		'''

		channel_matrix = None
		'''
	      pose matrix in bone space (deformation of the bone due to action, constraint, etc), Read-only.
	      This field is updated after the graphic render, it represents the current pose.
	
	      :type: matrix [4][4]
	
		'''

		pose_matrix = None
		'''
	      pose matrix in armature space, read-only, 
	      This field is updated after the graphic render, it represents the current pose.
	
	      :type: matrix [4][4]
	
		'''

		pose_head = None
		'''
	      position of bone head in armature space, read-only.
	
	      :type: vector [x, y, z]
	
		'''

		pose_tail = None
		'''
	      position of bone tail in armature space, read-only.
	
	      :type: vector [x, y, z]
	
		'''

		ik_min_x = None
		'''
	      minimum value of X rotation in degree (<= 0) when X rotation is limited (see ik_limit_x), read-only.
	
	      :type: float
	
		'''

		ik_max_x = None
		'''
	      maximum value of X rotation in degree (>= 0) when X rotation is limited (see ik_limit_x), read-only.
	
	      :type: float
	
		'''

		ik_min_y = None
		'''
	      minimum value of Y rotation in degree (<= 0) when Y rotation is limited (see ik_limit_y), read-only.
	
	      :type: float
	
		'''

		ik_max_y = None
		'''
	      maximum value of Y rotation in degree (>= 0) when Y rotation is limited (see ik_limit_y), read-only.
	
	      :type: float
	
		'''

		ik_min_z = None
		'''
	      minimum value of Z rotation in degree (<= 0) when Z rotation is limited (see ik_limit_z), read-only.
	
	      :type: float
	
		'''

		ik_max_z = None
		'''
	      maximum value of Z rotation in degree (>= 0) when Z rotation is limited (see ik_limit_z), read-only.
	
	      :type: float
	
		'''

		ik_stiffness_x = None
		'''
	      bone rotation stiffness in X axis, read-only.
	
	      :type: float between 0 and 1
	
		'''

		ik_stiffness_y = None
		'''
	      bone rotation stiffness in Y axis, read-only.
	
	      :type: float between 0 and 1
	
		'''

		ik_stiffness_z = None
		'''
	      bone rotation stiffness in Z axis, read-only.
	
	      :type: float between 0 and 1
	
		'''

		ik_stretch = None
		'''
	      ratio of scale change that is allowed, 0=bone can't change size, read-only.
	
	      :type: float
	
		'''

		ik_rot_weight = None
		'''
	      weight of rotation constraint when ik_rot_control is set, read-write.
	
	      :type: float between 0 and 1
	
		'''

		ik_lin_weight = None
		'''
	      weight of size constraint when ik_lin_control is set, read-write.
	
	      :type: float between 0 and 1
	
		'''

	class SCA_2DFilterActuator:
		'''   Create, enable and disable 2D filters
		'''

		shaderText = None
		'''
	      shader source code for custom shader.
	
	      :type: string
	
		'''

		disableMotionBlur = None
		'''
	      action on motion blur: 0=enable, 1=disable.
	
	      :type: integer
	
		'''

		mode = None
		'''
	      Type of 2D filter, use one of :ref:`these constants <Two-D-FilterActuator-mode>`
	
	      :type: integer
	
		'''

		passNumber = None
		'''
	      order number of filter in the stack of 2D filters. Filters are executed in increasing order of passNb.
	
	      Only be one filter can be defined per passNb.
	
	      :type: integer (0-100)
	
		'''

	class SCA_XORController:
		'''   An XOR controller activates when there is the input is mixed, but not when all are on or off.
		'''

	class SCA_PythonJoystick:
		'''   A Python interface to a joystick.
		'''

		name = None
		'''
	      The name assigned to the joystick by the operating system. (read-only)
		  
	      :type: string
	
		'''

		activeButtons = None
		'''
	      A list of active button values. (read-only)
		  
	      :type: list
	
		'''

		axisValues = None
		'''
	      The state of the joysticks axis as a list of values :data:`numAxis` long. (read-only).
	
	      :type: list of ints.
	
	      Each specifying the value of an axis between -1.0 and 1.0 depending on how far the axis is pushed, 0 for nothing.
	      The first 2 values are used by most joysticks and gamepads for directional control. 3rd and 4th values are only on some joysticks and can be used for arbitary controls.
	
	      * left:[-1.0, 0.0, ...]
	      * right:[1.0, 0.0, ...]
	      * up:[0.0, -1.0, ...]
	      * down:[0.0, 1.0, ...]
	
		'''

		hatValues = None
		'''
	      The state of the joysticks hats as a list of values :data:`numHats` long. (read-only).
	
	      :type: list of ints
	
	      Each specifying the direction of the hat from 1 to 12, 0 when inactive.
	
	      Hat directions are as follows...
	
	      * 0:None
	      * 1:Up
	      * 2:Right
	      * 4:Down
	      * 8:Left
	      * 3:Up - Right
	      * 6:Down - Right
	      * 12:Down - Left
	      * 9:Up - Left
	
		'''

		numAxis = None
		'''
	      The number of axes for the joystick at this index. (read-only).
	
	      :type: integer
	
		'''

		numButtons = None
		'''
	      The number of buttons for the joystick at this index. (read-only).
	
	      :type: integer
	
		'''

	class CValue:
		'''   This class is a basis for other classes.
		'''

	class SCA_JoystickSensor:
		'''   This sensor detects player joystick events.
		'''

		def getButtonActiveList():
			'''
	      :return: A list containing the indicies of the currently pressed buttons.
	      :rtype: list
	
			'''
			pass

		axisValues = None
		'''
	      The state of the joysticks axis as a list of values :data:`numAxis` long. (read-only).
	
	      :type: list of ints.
	
	      Each specifying the value of an axis between -32767 and 32767 depending on how far the axis is pushed, 0 for nothing.
	      The first 2 values are used by most joysticks and gamepads for directional control. 3rd and 4th values are only on some joysticks and can be used for arbitary controls.
	
	      * left:[-32767, 0, ...]
	      * right:[32767, 0, ...]
	      * up:[0, -32767, ...]
	      * down:[0, 32767, ...]
	
		'''

		axisSingle = None
		'''
	      like :data:`axisValues` but returns a single axis value that is set by the sensor. (read-only).
	
	      :type: integer
	
	      .. note::
	         
	         Only use this for "Single Axis" type sensors otherwise it will raise an error.
	
		'''

		hatValues = None
		'''
	      The state of the joysticks hats as a list of values :data:`numHats` long. (read-only).
	
	      :type: list of ints
	
	      Each specifying the direction of the hat from 1 to 12, 0 when inactive.
	
	      Hat directions are as follows...
	
	      * 0:None
	      * 1:Up
	      * 2:Right
	      * 4:Down
	      * 8:Left
	      * 3:Up - Right
	      * 6:Down - Right
	      * 12:Down - Left
	      * 9:Up - Left
	
		'''

		hatSingle = None
		'''
	      Like :data:`hatValues` but returns a single hat direction value that is set by the sensor. (read-only).
	
	      :type: integer
	
		'''

		numAxis = None
		'''
	      The number of axes for the joystick at this index. (read-only).
	
	      :type: integer
	
		'''

		numButtons = None
		'''
	      The number of buttons for the joystick at this index. (read-only).
	
	      :type: integer
	
		'''

		numHats = None
		'''
	      The number of hats for the joystick at this index. (read-only).
	
	      :type: integer
	
		'''

		connected = None
		'''
	      True if a joystick is connected at this joysticks index. (read-only).
	
	      :type: boolean
	
		'''

		index = None
		'''
	      The joystick index to use (from 0 to 7). The first joystick is always 0.
	
	      :type: integer
	
		'''

		threshold = None
		'''
	      Axis threshold. Joystick axis motion below this threshold wont trigger an event. Use values between (0 and 32767), lower values are more sensitive.
	
	      :type: integer
	
		'''

		button = None
		'''
	      The button index the sensor reacts to (first button = 0). When the "All Events" toggle is set, this option has no effect.
	
	      :type: integer
	
		'''

		axis = None
		'''
	      The axis this sensor reacts to, as a list of two values [axisIndex, axisDirection]
	
	      * axisIndex: the axis index to use when detecting axis movement, 1=primary directional control, 2=secondary directional control.
	      * axisDirection: 0=right, 1=up, 2=left, 3=down.
	
	      :type: [integer, integer]
	
		'''

		hat = None
		'''
	      The hat the sensor reacts to, as a list of two values: [hatIndex, hatDirection]
	
	      * hatIndex: the hat index to use when detecting hat movement, 1=primary hat, 2=secondary hat (4 max).
	      * hatDirection: 1-12.
	
	      :type: [integer, integer]
	
		'''

	class KX_IpoActuator:
		'''   IPO actuator activates an animation.
		'''

		frameStart = None
		'''
	      Start frame.
	
	      :type: float
	
		'''

		frameEnd = None
		'''
	      End frame.
	
	      :type: float
	
		'''

		propName = None
		'''
	      Use this property to define the Ipo position.
	
	      :type: string
	
		'''

		framePropName = None
		'''
	      Assign this property this action current frame number.
	
	      :type: string
	
		'''

		mode = None
		'''
	      Play mode for the ipo. Can be on of :ref:`these constants <ipo-actuator>`
	
	      :type: integer
	
		'''

		useIpoAsForce = None
		'''
	      Apply Ipo as a global or local force depending on the local option (dynamic objects only).
	
	      :type: boolean
	
		'''

		useIpoAdd = None
		'''
	      Ipo is added to the current loc/rot/scale in global or local coordinate according to Local flag.
	
	      :type: boolean
	
		'''

		useIpoLocal = None
		'''
	      Let the ipo acts in local coordinates, used in Force and Add mode.
	
	      :type: boolean
	
		'''

	class SCA_ANDController:
		'''   An AND controller activates only when all linked sensors are activated.
		'''

	class KX_LibLoadStatus:
		'''   An object providing information about a LibLoad() operation.
		'''

		onFinish = None
		'''
	      A callback that gets called when the lib load is done.
	
	      :type: callable
	
		'''

		progress = None
		'''
	      The current progress of the lib load as a normalized value from 0.0 to 1.0.
	
	      :type: float
	
		'''

		libraryName = None
		'''
	      The name of the library being loaded (the first argument to LibLoad).
	
	      :type: string
	
		'''

	class BL_ArmatureActuator:
		'''   Armature Actuators change constraint condition on armatures.
		'''

		type = None
		'''
	      The type of action that the actuator executes when it is active.
	
	      Can be one of :ref:`these constants <armatureactuator-constants-type>`
	
	      :type: integer
	
		'''

		constraint = None
		'''
	      The constraint object this actuator is controlling.
	
	      :type: :class:`BL_ArmatureConstraint`
	
		'''

		target = None
		'''
	      The object that this actuator will set as primary target to the constraint it controls.
	
	      :type: :class:`KX_GameObject`
	
		'''

		subtarget = None
		'''
	      The object that this actuator will set as secondary target to the constraint it controls.
	
	      :type: :class:`KX_GameObject`.
	      
	      .. note::
	      
	         Currently, the only secondary target is the pole target for IK constraint.
	
		'''

		weight = None
		'''
	      The weight this actuator will set on the constraint it controls.
	
	      :type: float.
	
	      .. note::
	      
	         Currently only the IK constraint has a weight. It must be a value between 0 and 1.
	
	      .. note::
	      
	         A weight of 0 disables a constraint while still updating constraint runtime values (see :class:`BL_ArmatureConstraint`)
	
		'''

	class SCA_AlwaysSensor:
		'''   This sensor is always activated.
		'''

	class BL_ArmatureObject:
		'''   An armature object.
		'''

		constraints = None
		'''
	      The list of armature constraint defined on this armature.
	      Elements of the list can be accessed by index or string.
	      The key format for string access is '<bone_name>:<constraint_name>'.
	
	      :type: list of :class:`BL_ArmatureConstraint`
	
		'''

		channels = None
		'''
	      The list of armature channels.
	      Elements of the list can be accessed by index or name the bone.
	
	      :type: list of :class:`BL_ArmatureChannel`
	
		'''

	class SCA_ILogicBrick:
		'''   Base class for all logic bricks.
		'''

		executePriority = None
		'''
	      This determines the order controllers are evaluated, and actuators are activated (lower priority is executed first).
	
	      :type: executePriority: int
	
		'''

		owner = None
		'''
	      The game object this logic brick is attached to (read-only).
	      
	      :type: :class:`KX_GameObject` or None in exceptional cases.
	
		'''

