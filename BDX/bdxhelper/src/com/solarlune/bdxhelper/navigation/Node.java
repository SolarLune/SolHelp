package com.solarlune.bdxhelper.navigation;

import com.nilunder.bdx.GameObject;

import javax.vecmath.Vector3f;

import java.util.ArrayList;

/**
 * Created by SolarLune on 1/14/2015.
 */
public class Node {

    public GameObject gameObject;
    public ArrayList<Node> neighbors;
    public Node parent;
    public float cost = 0;
    public float gCost = 0;
    
    public Node(GameObject owner){
        neighbors = new ArrayList<Node>();
        gameObject = owner;
        //position = owner.position();
        parent = null;
    }

    public Vector3f getPosition(){
        return gameObject.position();
    }
    
    @Override
    public String toString() {
    	return "Node: " + getPosition().toString();
    }

}
