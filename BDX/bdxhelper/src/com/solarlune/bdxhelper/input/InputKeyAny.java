package com.solarlune.bdxhelper.input;

import com.nilunder.bdx.Bdx;

/**
 * Created by SolarLune on 1/9/2015.
 */
public class InputKeyAny extends InputBase {

    public String keyName;

    public InputKeyAny() {}

    public void poll(){

		pastActive = active;
        active = 0;

        if (!Bdx.keyboard.downKeys().isEmpty()) {
            active = scalar;
			keyName = Bdx.keyboard.downKeys().get(0);

			if (keyName.equals("*"))
            	keyName = Bdx.keyboard.downKeys().get(1);
        }

        super.poll();

    }

}
