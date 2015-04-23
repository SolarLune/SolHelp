package com.solarlune.bdxhelper;

import java.util.ArrayList;

import com.nilunder.bdx.GameObject;

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

}
