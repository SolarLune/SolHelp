package com.solarlune.bdxhelper.input;

import com.badlogic.gdx.controllers.PovDirection;

/**
 * Created by SolarLune on 1/9/2015.
 */
public class InputGamepadHat extends InputBase {

    public int hatNumber;

    public InputGamepadHat(int povDirection, int hatNumber, int gamepadIndex, float scalar){

        this.hatNumber = hatNumber;
        this.povDirection = povDirection;
        this.scalar = scalar;
        this.setGamepadIndex(gamepadIndex);
    }

    public InputGamepadHat(int povDirection){

        this(povDirection, 0, 0, 1);
    }

    public void poll(){

        active = 0;

        if (controller.getPov(hatNumber).ordinal() == povDirection)
            active = scalar;

        super.poll();

    }

}
