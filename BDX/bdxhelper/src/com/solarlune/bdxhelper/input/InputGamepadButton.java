package com.solarlune.bdxhelper.input;

/**
 * Created by SolarLune on 1/9/2015.
 */
public class InputGamepadButton extends InputBase {

    public int buttonIndex;

    public InputGamepadButton(int buttonIndex, int gamepadIndex, float scalar){

        this.buttonIndex = buttonIndex;
        this.scalar = scalar;
        this.setGamepadIndex(gamepadIndex);
    }

    public InputGamepadButton(int buttonIndex){

        this(buttonIndex, 0, 1);
    }

    public void poll(){

        active = 0;

        if (controller.getButton(buttonIndex))
            active = scalar;

		super.poll();

    }

}
