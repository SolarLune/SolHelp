package com.solarlune.bdxhelper.utils;

import java.util.ArrayList;

import javax.vecmath.Vector2f;
import javax.vecmath.Vector3f;
import javax.vecmath.Vector4f;

import com.nilunder.bdx.Bdx;
import com.nilunder.bdx.utils.Random;

/**
 * Created by SolarLune on 1/9/2015.
 */
public final class BDXHMath {

    public static Vector3f snapVectToGrid(Vector3f vect, float gridSpacesPerUnit){

        vect.x = Math.round(vect.x * gridSpacesPerUnit) / gridSpacesPerUnit;
        vect.y = Math.round(vect.y * gridSpacesPerUnit) / gridSpacesPerUnit;
        vect.z = Math.round(vect.z * gridSpacesPerUnit) / gridSpacesPerUnit;

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

    public static float clamp(float value, float min, float max){
        return Math.min(Math.max(value, min), max);
    }

    public static float clamp(float value, float maximums) {
        return clamp(value, -maximums, maximums);
    }

    public static Vector2f roundVector(Vector2f vec){
        Vector2f out = new Vector2f(Math.round(vec.x),
                Math.round(vec.y));
        return out;
    }

    public static Vector3f roundVector(Vector3f vec){
        Vector3f out = new Vector3f(Math.round(vec.x),
                Math.round(vec.y),
                Math.round(vec.z));
        return out;
    }

    public static Vector4f roundVector(Vector4f vec){
        Vector4f out = new Vector4f(Math.round(vec.x),
                Math.round(vec.y),
                Math.round(vec.z),
                Math.round(vec.w));
        return out;
    }

    public static float oscillateSin(float oscRate, float oscRange, boolean baseOffset, float timeOffset){

        float value = (float) Math.sin((Bdx.time + timeOffset) * (Math.PI * 2) * oscRate) * oscRange;

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
