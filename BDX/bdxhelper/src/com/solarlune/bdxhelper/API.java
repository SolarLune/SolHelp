package com.solarlune.bdxhelper;

import java.util.ArrayList;

import javax.vecmath.Vector4f;

import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.utils.Random;

/**
 * Created by SolarLune on 1/15/2015.
 */
public final class API {

    static public boolean atLeastBooleans(int reqNum, boolean... checks){

        int numGood = 0;

        for (boolean b : checks){

            if (b)
                numGood += 1;

        }

        return numGood >= reqNum;

    }

    static public boolean atLeastNotBooleans(int reqNum, boolean... checks){

        int numGood = 0;

        for (boolean b : checks){

            if (!b)
                numGood += 1;

        }

        return numGood >= reqNum;

    }
    
    static public ArrayList<GameObject> sortByDistance(GameObject startingObject, ArrayList<GameObject> objectList) {
    	
    	ArrayList<GameObject> sorted = new ArrayList<GameObject>();
    	
    	GameObject closest = objectList.get(0);
    	
    	sorted.add(closest);
    	
    	for (GameObject o : objectList) {
    		
    		if (startingObject.position().minus(o.position()).length() < startingObject.position().minus(closest.position()).length()) {
    			
    			closest = o;
    			
    			sorted.add(0, closest);
    			
    		}
    		
    		else
    			
    			sorted.add(closest);
    		
    	}
    	
    	return sorted;
    	
    }
    
    static public Vector4f randomizeVector4f(Vector4f bottom, Vector4f top){
    	
    	Vector4f vect = new Vector4f(1,1,1,1);
    	
    	vect.x = Random.random(bottom.x, top.x);
    	vect.y = Random.random(bottom.y, top.y);
    	vect.z = Random.random(bottom.z, top.z);
    	vect.w = Random.random(bottom.w, top.w);
    	
    	return vect;
    	
    }
    
    static public Vector4f randomizeVector4f(Vector4f top) {
    	return randomizeVector4f(new Vector4f(0,0,0,0), top);
    }
    
}
