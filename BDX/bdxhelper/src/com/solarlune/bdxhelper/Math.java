package com.solarlune.bdxhelper;

import java.util.ArrayList;

import javax.vecmath.Vector2f;
import javax.vecmath.Vector3f;

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
		
	public static float oscillateSin(float oscRate, float oscRange){
	    	
    	return (float) java.lang.Math.sin(Bdx.time * java.lang.Math.PI * oscRate) * oscRange;
    	
    }
	
	public static float lerp(float valueOne, float valueTwo, float percent){
		return valueOne + percent * (valueTwo - valueOne);
	}
	
}
