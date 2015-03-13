package com.solarlune.bdxhelper.input;

/**
 * Created by SolarLune on 1/9/2015.
 */
public class InputGamepadAxis extends InputBase {

    public int axisIndex;
    public int axisDirection;
    float deadzone;

    public InputGamepadAxis(int axisIndex, int axisDirection, int gamepadIndex, float deadzone, float scalar){

        this.axisIndex = axisIndex;
        this.axisDirection = axisDirection;
        this.deadzone = deadzone;
        this.scalar = scalar;
        this.setGamepadIndex(gamepadIndex);

    }

    public InputGamepadAxis(int axisIndex, int axisDirection){

        this(axisIndex, axisDirection, 0, 0.1f, 1);

    }

    public void poll(){

        float axis = controller.getAxis(axisIndex);

        active = 0;

        if ((Math.signum(axis) == axisDirection) && (Math.abs(axis) >= deadzone))
            active = Math.abs(axis * scalar);

		super.poll();

    }

}
