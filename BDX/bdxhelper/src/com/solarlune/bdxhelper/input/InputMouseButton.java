package com.solarlune.bdxhelper.input;

import com.badlogic.gdx.Gdx;
import com.nilunder.bdx.Bdx;

/**
 * Created by SolarLune on 1/9/2015.
 */
public class InputMouseButton extends InputBase {

    String buttonName;

    public InputMouseButton(String buttonName, float scalar){
        this.buttonName = buttonName;
        this.scalar = scalar;
    }

    public InputMouseButton(String buttonName){
        this(buttonName, 1);
    }

    public void poll(){

        active = 0;

        if (Bdx.mouse.btnDown(buttonName))
            active = scalar;

        super.poll();

    }

}
