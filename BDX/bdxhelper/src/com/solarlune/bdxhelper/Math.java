package com.solarlune.bdxhelper;

import java.util.ArrayList;

import javax.vecmath.Vector2f;
import javax.vecmath.Vector3f;
import javax.vecmath.Vector4f;

import com.nilunder.bdx.Bdx;
import com.nilunder.bdx.utils.Random;

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
    
    public static Vector2f rotR(Vector2f in){

        Vector2f v = new Vector2f(in);

        float temp = v.x;
        v.x = v.y;
        v.y = -temp;

        return v;

    }
    
    public static Vector2f rotL(Vector2f in){

        Vector2f v = new Vector2f(in);

        float temp = v.x;
        v.x = -v.y;
        v.y = temp;

        return v;

    }

    public static Vector2f randomCardinalVector2f(){

        ArrayList<Vector2f> d = new ArrayList<Vector2f>();

        d.add(new Vector2f(1, 0));
        d.add(new Vector2f(-1, 0));
        d.add(new Vector2f(0, 1));
        d.add(new Vector2f(0, -1));

        return Random.choice(d);

    }

    public static Vector2f roundVector(Vector2f vec){
        Vector2f out = new Vector2f(java.lang.Math.round(vec.x),
                java.lang.Math.round(vec.y));
        return out;
    }

    public static Vector3f roundVector(Vector3f vec){
        Vector3f out = new Vector3f(java.lang.Math.round(vec.x),
                java.lang.Math.round(vec.y),
                java.lang.Math.round(vec.z));
        return out;
    }

    public static Vector4f roundVector(Vector4f vec){
        Vector4f out = new Vector4f(java.lang.Math.round(vec.x),
                java.lang.Math.round(vec.y),
                java.lang.Math.round(vec.z),
                java.lang.Math.round(vec.w));
        return out;
    }

    public static float oscillateSin(float oscRate, float oscRange, boolean baseOffset, float timeOffset){

        float value = (float) java.lang.Math.sin((Bdx.time + timeOffset) * (java.lang.Math.PI * 2) * oscRate) * oscRange;

        if (baseOffset) {
            value /= 2.0f;
            value += oscRange / 2;
        }

        return value;

    }

    public static float oscillateSin(float oscRate, float oscRange, boolean baseOffset){
        return oscillateSin(oscRate, oscRange, baseOffset, 0);
    }

    public static float lerp(float valueOne, float valueTwo, float percent){
        return valueOne + percent * (valueTwo - valueOne);
    }

}
