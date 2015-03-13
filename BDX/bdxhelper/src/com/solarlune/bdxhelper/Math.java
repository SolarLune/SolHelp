package com.solarlune.bdxhelper;

import javax.vecmath.Vector3f;

/**
 * Created by SolarLune on 1/9/2015.
 */
public final class Math {

    public static Vector3f snapVectToGrid(Vector3f vect, float snapTo){

        vect.x = java.lang.Math.round(vect.x * snapTo) / snapTo;
        vect.y = java.lang.Math.round(vect.y * snapTo) / snapTo;
        vect.z = java.lang.Math.round(vect.z * snapTo) / snapTo;

        return vect;
    }

}
