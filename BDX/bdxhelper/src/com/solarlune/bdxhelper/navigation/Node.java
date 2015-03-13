package com.solarlune.bdxhelper.navigation;

import com.nilunder.bdx.GameObject;

import javax.vecmath.Vector3f;
import java.util.ArrayList;

/**
 * Created by SolarLune on 1/14/2015.
 */
public class Node {

    //Vector3f position;
    GameObject gameObject;
    ArrayList<Node> neighbors;
    ArrayList<Integer> costs;
    Node parent;

    public Node(GameObject owner){
        neighbors = new ArrayList<Node>();
        costs = new ArrayList<Integer>();
        gameObject = owner;
        //position = owner.position();
        parent = null;
    }

    public void resetCosts(int costNum){
        costs.clear();

        for (int x = 0; x < costs.size(); x += 1){

            costs.add(0);

        }
    }

    public void setCost(int value, int index){
        costs.set(index, value);
    }

    public int getCost(int index){
        return costs.get(index);
    }

    public void addCost(int value, int index){
        costs.set(index, costs.get(index) + value);
    }

    public void subCost(int value, int index){
        costs.set(index, costs.get(index) - value);
    }

    public Vector3f getPosition(){
        return gameObject.position();
    }

}
