package com.solarlune.bdxhelper.navigation;

import javax.vecmath.Vector3f;

import java.util.ArrayList;

/**
 * Created by SolarLune on 1/14/2015.
 */
public class Node {

	private Vector3f position;
    public ArrayList<Node> neighbors;
    public Node parent;
    public float gCost;
    private float cost;
    
    public Node(Vector3f position){
        neighbors = new ArrayList<Node>();
        this.position = position;
        parent = null;
    }
    
    public Vector3f position(){
    	return position;
    }
    
    public void position(Vector3f pos){
    	position = pos;
    }
    
    @Override
    public String toString() {
    	return "Node: " + position.toString();
    }
    
    public void cost(float value){
    	cost = value;
    }
    public float cost(){
    	return cost;
    }

}
