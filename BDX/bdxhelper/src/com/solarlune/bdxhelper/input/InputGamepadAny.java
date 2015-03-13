package com.solarlune.bdxhelper.input;

import com.badlogic.gdx.controllers.PovDirection;

import static com.badlogic.gdx.controllers.Controllers.getControllers;

/**
 * Created by SolarLune on 1/28/2015.
 */
public class InputGamepadAny extends InputBase {

    public float deadzone;
    public int inputType = -1;
    public int inputNum = -1;

    public int IT_AXIS = 0;
    public int IT_BUTTON = 1;
    public int IT_HAT = 2;

    public InputGamepadAny(float deadzone, float scalar){

        this.deadzone = deadzone;
        this.scalar = scalar;

    }

    public InputGamepadAny(){

        this(0.1f, 1);

    }

	/*
	polls the InputGamepadAny() object for changes. Note that this is specifically set up to use direct access to variables
	instead of getters and setters.
	inputType = the input type of the gamepad input. IT_AXIS is for axes changes, IT_BUTTON for buttons, and IT_HAT for hats.
	inputNum = the axis number, button number, or hat number of the input.
	active = whether the input is active or not, of course. If this is not 0, then the input is active. If it's an axis,
	it can vary according to the range that the axis is pushed, as well as being able to go into negatives (for both directions
	an axis can go).
	 */
    public void poll(){

        for (int c = 0; c < getControllers().size; c++) {

            setGamepadIndex(c);

            for (int a = 0; a < 32; a++) { // For some bizarre reason, there's no method to get information from controllers
                // in LibGDX other than just asking directly for it; so, I'm defaulting to 32 checks of EVERYTHING...

                float result = controller.getAxis(a);
                inputType = IT_AXIS;
                inputNum = a;

                active = 0;

                if (Math.abs(result) >= deadzone)
                    active = result * scalar;

                if (active == 0) {
                    if (controller.getButton(a)) {
                        active = scalar;
                        inputType = IT_BUTTON;
                    } else
                        active = 0;
                }

                if (active == 0) {
                    if (controller.getPov(a) != PovDirection.center) {
						active = scalar;
						inputType = IT_HAT;
						inputNum = controller.getPov(a).ordinal();
					}
                    else
                        active = 0;
                }

                if (active != 0)
                    break;

                inputType = -1;
                inputNum = -1;

            }

            if (active != 0)
                break;

        }

		super.poll();

    }


}
