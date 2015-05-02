package com.solarlune.bdxhelper.input;


/**
 * Created by SolarLune on 1/9/2015.
 */
public class InputMouseAxis extends InputBase {

    int axisIndex;
    int axisDirection;

    public InputMouseAxis(int axisIndex, int axisDirection, float scalar){

        this.axisIndex = axisIndex;
        this.axisDirection = axisDirection;
        this.scalar = scalar;
    }

    public InputMouseAxis(int axisIndex, int axisDirection){

        this(axisIndex, axisDirection, 1);

    }

    public void poll(){

        // Mouse Axis Checking

        //Vector4f v = Bdx.mouse.clipCoords();

//        if ((axisIndex == 0) && (Math.signum(v.x)) == Math.signum(v.x))
//
//            active = v.x;
//
//        else
//
//            active = 0

        super.poll();

    }

}
