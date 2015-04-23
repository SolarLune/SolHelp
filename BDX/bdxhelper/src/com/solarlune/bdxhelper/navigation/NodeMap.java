package com.solarlune.bdxhelper.navigation;

import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.RayHit;
import com.nilunder.bdx.Scene;
import com.solarlune.bdxhelper.API;

import javax.vecmath.Vector3f;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;

/**
 * Created by SolarLune on 1/14/2015.
 */
public class NodeMap {

    ArrayList<Node> nodes = new ArrayList<Node>();

    public NodeMap(){
    }

    public void addNode(Node node){

        nodes.add(node);

    }

    public void removeNode(Node node){

        nodes.remove(node);

    }

    public void updateNeighbors(float minDist, float maxDist, boolean onlyStraight, boolean rayTest){

        ArrayList<Node> evaluated = new ArrayList<Node>();

        for (Node n : nodes){

            for (Node m : nodes){

                if (n != m && !evaluated.contains(m)){

                    float dist = (n.getPosition().minus(m.getPosition())).length();

                    if ((maxDist >= dist || maxDist == 0) && dist >= minDist){

                        float tooClose = 0.001f;

                        boolean xg = Math.abs(m.getPosition().x - n.getPosition().x) < tooClose;
                        boolean yg = Math.abs(m.getPosition().y - n.getPosition().y) < tooClose;
                        boolean zg = Math.abs(m.getPosition().z - n.getPosition().z) < tooClose;

                        if (!onlyStraight || (onlyStraight && API.atLeastBooleans(2, xg, yg, zg))) {
                        	
                        	Scene scene = n.gameObject.scene;
                        	
                            RayHit ray;

                            if (rayTest)
                                ray = scene.ray(n.getPosition(), m.getPosition().minus(n.getPosition()));
                            else
                                ray = null;

                            if (ray == null) {

                            	m.neighbors.add(n);
                            	n.neighbors.add(m);
                               
                            }
                        }

                    }

                }

            }

            evaluated.add(n);

        }

    }

    public void updateNeighbors() {
    	
    	updateNeighbors(0, 0, false, true);
    	
    }
    
    public Node getClosestNode(final Vector3f position, boolean rayTest){

        ArrayList<Node> sorted = new ArrayList<Node>(nodes);

        Collections.sort(sorted, new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2){
            	
            	if (o1.getPosition().minus(position).length() < o2.getPosition().minus(position).length())
            		return -1;
            	return 1;
            }
        });
 
        Node closest;
        
        if (rayTest) {

	        closest = null;
	        
	        System.out.println("yes");
	
	        for (Node n : sorted){
	        	
	        	Scene scene = n.gameObject.scene;
	
	            RayHit ray = scene.ray(position, n.getPosition().minus(position));
	
	            if (ray == null){
	
	                closest = n;
	                break;
	
	            }
	
	        }
        
        }
        
        else
        	
        	closest = sorted.get(0);

        return closest;

    }
    
    public Node getClosestNode(final Vector3f position){
    	
    	return getClosestNode(position, true);
    	
    }

    public Path getPathTo(Vector3f endingPoint, Vector3f startingPoint, int maxCheckNum, boolean rayNodeCheck){
    	    	
    	final Node goal = getClosestNode(endingPoint, rayNodeCheck);
    	
    	final Node start = getClosestNode(startingPoint, rayNodeCheck);
    	
    	if (goal == null) {
    		System.out.println("GOAL point can't be reached from any node on the Nodemap.");
    		return null;
    	}
    	
    	else if (start == null) {
    		System.out.println("START point can't be reached from any node on the Nodemap.");
    		return null;
    	}
    	    	
    	LinkedList<Node> openList = new LinkedList<Node>();
    	openList.add(start);
    	
    	LinkedList<Node> closedList = new LinkedList<Node>();
    	
    	boolean exitLoop = false;
    	boolean pathFound = false;
    	
    	for (Node n : nodes) {
    		n.gCost = 0;
    	}
    	
    	for (int i = 0; i < maxCheckNum; i++) {
    		
    		openList.sort(new Comparator<Node>() {
    			@Override
    			public int compare(Node n1, Node n2) {
    				//float n1Dist = start.getPosition().minus(n1.getPosition()).length() + n1.getPosition().minus(goal.getPosition()).length() + n2.cost;
    				//float n2Dist = start.getPosition().minus(n2.getPosition()).length() + n2.getPosition().minus(goal.getPosition()).length() + n1.cost;
    				float n1Dist = n1.gCost + n1.getPosition().minus(goal.getPosition()).length() - n2.cost;
    				float n2Dist = n2.gCost + n2.getPosition().minus(goal.getPosition()).length() - n1.cost;
    				
    				System.out.println(n1.cost);
    				System.out.println(n2.cost);
    	
    				if (n1Dist < n2Dist)
    					return -1;
    				return 1;
    			}
    		});
    	
    		if (openList.size() > 0) {
    		
	    		Node current = openList.pop();
	    		
	    		closedList.push(current);
	    		
	    		for (Node neighbor : current.neighbors) {
	    			
	    			if (closedList.contains(neighbor))
	    				continue;
	    			
	    			if (!openList.contains(neighbor)) {
	    				
	    				neighbor.parent = current;
	    				
	    				neighbor.gCost = current.gCost + (neighbor.getPosition().minus(current.getPosition()).length());

	    				openList.add(neighbor);
	        				
	    				if (neighbor.equals(goal)) {
	    					
	    					exitLoop = true;
	    					pathFound = true;
	    				    					
	    					break;
	    					
	    				}
	    				
	    			}
	    			
	    		}
    		
    		}
    		
    		else {
    			
    			exitLoop = true;
    			pathFound = false;
    			System.out.println("Can't get to goal; are all nodes in node-map connected?");
    		}
    		
    		if (exitLoop)
    			break;
    		    		
    	}
    	
    	if (pathFound) {
    	
	    	LinkedList<Node> path = new LinkedList<Node>();
			
			Node targetSquare = goal;
			
			for (int x = 0; x < maxCheckNum; x++) {
				
				path.add(targetSquare);
				
				if (targetSquare.equals(start))
					
					break;
				
				targetSquare = targetSquare.parent;
				
			}
			
			Collections.reverse(path);
				
			if (path.size() > 0)
				return new Path(path);
			else
				pathFound = false;
    	}
		
    	if (!pathFound)
			System.out.println("No path found. :<");
    	
    	return null;
    	
    }
    
    public Path getPathTo(Vector3f endingPoint, Vector3f startingPoint) {
    	return getPathTo(endingPoint, startingPoint, 1000, true);    	
    }
    
    public void debugDraw(Scene scene){

        for (Node n : nodes) {

            for (Node m : n.neighbors) {

                GameObject c = scene.add("Cube");

                c.position(n.getPosition());

                c.alignAxisToVec(1, m.getPosition().minus(n.getPosition()));

                c.scale(1, n.getPosition().minus(m.getPosition()).length(), 1);

            }

        }

    }

}
