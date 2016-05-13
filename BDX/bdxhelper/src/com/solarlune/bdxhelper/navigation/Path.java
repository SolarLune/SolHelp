package com.solarlune.bdxhelper.navigation;

import java.util.Collections;
import java.util.LinkedList;

import javax.vecmath.Vector3f;

/**
 * Created by SolarLune on 1/14/2015.
 */

public class Path extends LinkedList<Vector3f>{

    public int nodeIndex = 0;
    public boolean reversed = false;
    public boolean reachedEnd = false;

    public Path(LinkedList<Vector3f> path) {
    	super(path);
	}

	public Vector3f get(int index){
    	int value = Math.max(Math.min(index, size() - 1), 0);
    	return super.get(value);
    }
    
    public Vector3f getCurrentStep(){
    	return get(nodeIndex);
    }
    
    public Vector3f getNextStep(){
    	return get(nodeIndex + 1);
    }
    
    public Vector3f getPreviousStep(){
    	return get(nodeIndex - 1);
    }
    
    public void gotoNextStep(){
    	gotoStep(nodeIndex + 1);
    }
    
    public void gotoPreviousStep(){
    	gotoStep(nodeIndex - 1);
    }
    
    public void gotoStep(int step){
    	    	
    	if (step >= size() - 1) {
    		reachedEnd = true;
    	}
    	else {
    		nodeIndex = step;
    		reachedEnd = false;
    	}
    	
    }

    public boolean atCurrentStep(Vector3f position, float margin){
    	return position.minus(getCurrentStep()).length() < margin;
    }
    
    public boolean atCurrentStep(Vector3f position){
    	return atCurrentStep(position, 0.01f);
    }
    
    public void reverse(){
    	Collections.reverse(this);
    	reversed = !reversed;
    }

    public void resetPath(){
        if (reversed)
        	Collections.reverse(this);
        reversed = false;
        gotoStep(0);
    }
    
}
