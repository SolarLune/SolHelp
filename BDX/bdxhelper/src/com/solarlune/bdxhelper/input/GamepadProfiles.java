package com.solarlune.bdxhelper.input;

import com.nilunder.bdx.inputs.Gamepad;
import com.nilunder.bdx.inputs.Gamepad.Axis;
import com.nilunder.bdx.inputs.Gamepad.Profile;

import java.util.HashMap;

public class GamepadProfiles {

    static public Profile SNES(){

        Profile p = new Profile("SNES");

        p.btnToCode.put("x", 0);
        p.btnToCode.put("y", 3);
        p.btnToCode.put("a", 1);
        p.btnToCode.put("b", 2);
        p.btnToCode.put("l", 4);
        p.btnToCode.put("r", 5);

        if (System.getProperty("os.name").startsWith("Windows")) {
            p.axes.put("lx", new Axis(1));
            p.axes.put("ly", new Axis(0));
            p.btnToCode.put("start", 10);
            p.btnToCode.put("select", 9);
        }
        else {
            p.axes.put("lx", new Axis(0));		// Linux is different compared to Windows
            p.axes.put("ly", new Axis(1));
            p.btnToCode.put("start", 9);
            p.btnToCode.put("select", 8);
        }

        p.btnToCode.put("left", -200 - p.axes.get("lx").code);
        p.btnToCode.put("right", 200 + p.axes.get("lx").code);
        p.btnToCode.put("up", -200 - p.axes.get("ly").code);
        p.btnToCode.put("down", 200 + p.axes.get("ly").code);

        return p;

    }

}
