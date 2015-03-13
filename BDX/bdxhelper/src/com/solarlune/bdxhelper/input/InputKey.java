package com.solarlune.bdxhelper.input;

import com.nilunder.bdx.Bdx;

/**
 * Created by SolarLune on 1/9/2015.
 */
public class InputKey extends InputBase {

    public String keyName;

    public InputKey(String keyName){
        this.keyName = keyName;
    }

    public void poll(){

        active = 0;

        if (Bdx.keyboard.keyDown(keyName))
            active = scalar;

		super.poll();

    }

}
