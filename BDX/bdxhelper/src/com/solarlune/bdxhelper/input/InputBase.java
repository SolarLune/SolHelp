package com.solarlune.bdxhelper.input;

import com.badlogic.gdx.controllers.Controller;
import com.badlogic.gdx.controllers.PovDirection;

import static com.badlogic.gdx.controllers.Controllers.getControllers;

/**
 * Created by SolarLune on 1/7/2015.
 */

public class InputBase {

    static public final int IS_UP = 0;
    static public final int IS_PRESSED = 1;
    static public final int IS_DOWN = 2;
    static public final int IS_RELEASED = 3;

    public int inputState = IS_UP;

    public float active = 0;
    public float pastActive = -1; // Begin with -1, to indicate that we don't have a buffer (a previous state for the input)
    public float scalar = 1;

    public int controllerIndex;
    public Controller controller;  // Used for joystick input types; doesn't
    public int povDirection;  // make sense to duplicate this across multiple classes
	// povDirection is now a normal integer because it's easier to deal with across multiple areas.

    public void setGamepadIndex(int index){
        controllerIndex = index;
        this.controller = getControllers().get(index); // For joysticks
    }

    public void poll(){

		if (pastActive == -1)  // When first created, if an Input had a pastActive of 0, then the input being down would
			pastActive = active;  // indicate a press and down, which is bad, since that could just be a person holding down
		// a key, not an actual key press or release

        if (active != 0){ // Is active

            if (pastActive != 0)
                inputState = IS_DOWN;
            else
                inputState = IS_PRESSED;
        }
        else{

            if (pastActive == 0)
                inputState = IS_UP;
            else
                inputState = IS_RELEASED;
        }

        pastActive = active;

    }

}
