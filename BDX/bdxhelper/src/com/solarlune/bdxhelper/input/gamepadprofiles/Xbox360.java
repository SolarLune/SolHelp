package com.solarlune.bdxhelper.input.gamepadprofiles;

import com.badlogic.gdx.controllers.PovDirection;

/**
 * Created by SolarLune on 1/16/2015.
 */

public class Xbox360 extends GPProfile {

    public Xbox360(){

        buttons.put("a", 0);
        buttons.put("b", 1);
        buttons.put("x", 2);
        buttons.put("y", 3);
        buttons.put("lb", 4);
        buttons.put("rb", 5);
        buttons.put("back", 6);
        buttons.put("start", 7);
        buttons.put("ls", 8);
        buttons.put("rs", 9);

        axes.put("leftHori", 1);
        axes.put("leftVert", 0);
        axes.put("rightHori", 2);
        axes.put("rightVert", 3);
        axes.put("triggers", 4);

        hats.put("upRight", PovDirection.northEast.ordinal());
        hats.put("right", PovDirection.east.ordinal());
        hats.put("downRight", PovDirection.southEast.ordinal());
        hats.put("down", PovDirection.south.ordinal());
        hats.put("downLeft", PovDirection.southWest.ordinal());
        hats.put("left", PovDirection.west.ordinal());
        hats.put("upLeft", PovDirection.northWest.ordinal());
        hats.put("up", PovDirection.north.ordinal());

    }

}
