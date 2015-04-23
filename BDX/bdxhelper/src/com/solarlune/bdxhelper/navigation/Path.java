package com.solarlune.bdxhelper.navigation;

import java.util.Collections;
import java.util.LinkedList;

import javax.vecmath.Vector3f;

/**
 * Created by SolarLune on 1/14/2015.
 */

public class Path {

    LinkedList<Node> points;
    int nodeIndex = 0;
    public boolean reversed = false;
    public boolean reachedEnd = false;

    public Path(LinkedList<Node> points){
        this.points = new LinkedList<Node>(points);
    }

    public Vector3f currentStep(){
    	if (nodeIndex < points.size() && nodeIndex > -1)
    		return points.get(nodeIndex).getPosition();
    	    	
    	return null;
    	
    }
    
    public void gotoNextStep(){
    	gotoStep(nodeIndex + 1);
    }
    
    public void gotoStep(int step){
    	
    	if (step >= points.size()) {
    		reachedEnd = true;
    	}
    	else {
    		nodeIndex = step;
    		reachedEnd = false;
    	}
    	
    }
    
    public void reverse(){
    	Collections.reverse(points);
    	reversed = !reversed;
    }

    public void resetPath(){
        if (reversed)
        	Collections.reverse(points);
        reversed = false;
        gotoStep(0);
    }
    
    public String toString(){
    	return this.points.toString();	
    }

}
