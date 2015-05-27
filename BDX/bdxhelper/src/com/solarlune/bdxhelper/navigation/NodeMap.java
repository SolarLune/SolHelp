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

    Scene scene;
    
    public NodeMap(Scene scene){
    	this.scene = scene;
    }

    public void addNode(Node node){

        nodes.add(node);

    }

    public void removeNode(Node node){

        nodes.remove(node);

    }

    public void updateNeighbors(float minDist, float maxDist, boolean onlyStraight, String rayBlocker){

        ArrayList<Node> evaluated = new ArrayList<Node>();

        for (Node n : nodes){

            for (Node m : nodes){

                if (n != m && !evaluated.contains(m)){

                    float dist = (n.position().minus(m.position())).length();

                    if ((maxDist >= dist || maxDist == 0) && dist >= minDist){

                        float tooClose = 0.001f;

                        boolean xg = Math.abs(m.position().x - n.position().x) < tooClose;
                        boolean yg = Math.abs(m.position().y - n.position().y) < tooClose;
                        boolean zg = Math.abs(m.position().z - n.position().z) < tooClose;

                        if (!onlyStraight || (onlyStraight && API.atLeastBooleans(2, xg, yg, zg))) {

                            boolean blocked = false;
                            
                            if (rayBlocker != null) {
                                
                            	ArrayList<RayHit> rays = scene.xray(n.position(), m.position().minus(n.position()));
                            	
                            	for (RayHit ray : rays) {
                            		
                            		if (ray.object.props.containsKey(rayBlocker)) {
                            			blocked = true;
                            			break;
                            		}
                            		
                            	}
                                
                            }
             
                            if (!blocked) {

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
    	
    	updateNeighbors(0, 0, false, null);
    	
    }
        
    public Node getClosestNode(final Vector3f position, String rayBlocker){

        ArrayList<Node> sorted = new ArrayList<Node>(nodes);

        Collections.sort(sorted, new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2){
            	
            	if (o1.position().minus(position).length() < o2.position().minus(position).length())
            		return -1;
            	return 1;
            }
        });
 
        Node closest;
        
        if (rayBlocker != null) {

	        closest = null;
	
	        for (Node n : sorted){
	   
	            //RayHit ray = scene.ray(n.position(), position.minus(n.position()));
	            
	        	ArrayList<RayHit> rays = scene.xray(position, n.position().minus(position));
	            
	        	if (rays.size() == 0) {
	        		closest = n;
	        		break;
	        	}
	        	
	        	boolean blocked = false;
	        	
	        	for (RayHit r : rays) {
	        	
		            if (r.object.props.containsKey(rayBlocker)){
		         	
		                closest = null;
		                blocked = true;
		                break;
		
		            }
	            
	        	}
	        	
	        	if (blocked)
	        		continue;
	        	
	        }
        
        }
        
        else
        	
        	closest = sorted.get(0);

        return closest;

    }
    
    public Node getClosestNode(final Vector3f position){
    	
    	return getClosestNode(position, null);
    	
    }

    public Path getPathTo(Vector3f endingPoint, Vector3f startingPoint, int maxCheckNum, String rayBlocker){
    	    	
    	final Node goal = getClosestNode(endingPoint, rayBlocker);
    	
    	final Node start = getClosestNode(startingPoint, rayBlocker);
    	
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
    		Collections.sort(openList, new Comparator<Node>() {
    			@Override
    			public int compare(Node n1, Node n2) {
    				//float n1Dist = start.getPosition().minus(n1.getPosition()).length() + n1.getPosition().minus(goal.getPosition()).length() + n2.cost;
    				//float n2Dist = start.getPosition().minus(n2.getPosition()).length() + n2.getPosition().minus(goal.getPosition()).length() + n1.cost;
    				float n1Dist = n1.gCost + n1.position().minus(goal.position()).length() - n2.cost;
    				float n2Dist = n2.gCost + n2.position().minus(goal.position()).length() - n1.cost;
    	
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
	    				
	    				neighbor.gCost = current.gCost + (neighbor.position().minus(current.position()).length());

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
    	return getPathTo(endingPoint, startingPoint, 1000, null);    	
    }
    
    public void debugDraw(){

        for (Node n : nodes) {

            for (Node m : n.neighbors) {
            	
                GameObject c = scene.add("Cube");

                c.position(n.position());

                c.alignAxisToVec(1, m.position().minus(n.position()));

                c.scale(1, n.position().minus(m.position()).length(), 1);

            }

        }

    }

}
