package com.solarlune.bdxhelper;

import java.util.ArrayList;

import javax.vecmath.Vector2f;

import com.nilunder.bdx.utils.Random;

import java.lang.Math;

public class RandomRoom extends ArrayList<ArrayList<Integer>> {
	
	public enum Wrap {
		
		NONE,
		CLAMP,
		LOOP;
		
	}
	
	public enum ConnectionMode {
		
		ALL,
		HUB,
		ONE,
		
	}
		
	public Wrap wrapBehavior = Wrap.CLAMP;
	
	public long seed = 0;
	
	public RandomRoom(int sizeX, int sizeY) {
		
		resize(sizeX, sizeY);
		
	}
	
	public void resize(int sizeX, int sizeY) {
		
		clear();
		
		for (int i = 0; i < sizeY; i++) {
			
			add(new ArrayList<Integer>());
			
			for (int j = 0; j < sizeX; j++) {
				
				get(i).add(0);
				
			}
			
		}
		
	}
	
	public void fill(ArrayList<Integer> numbers) {
		
		// Fills the room with one of a random assortment of zero elements.
		
		for (ArrayList<Integer> row : this) {
			
			for (int i = 0; i < row.size(); i++) {
				
				row.set(i, Random.choice(numbers));
				
			}
			
		}
		
	}
	
	public void fill(){
		fill(new ArrayList<Integer>(0));			
	}
	
	public int get(int x, int y) {
	
		int fy = (int) getCoords(x, y).y;
		int fx = (int) getCoords(x, y).x;
		
		return get(fy).get(fx);

	}
	
	public int get(Vector2f pos) {
		
		int fy = (int) getCoords(pos).y;
		int fx = (int) getCoords(pos).x;
		
		return get(fy).get(fx);

	}
	
	public Vector2f getCoords(int posX, int posY){
		
		Vector2f p = new Vector2f(posX, posY);
		
		if (wrapBehavior == Wrap.CLAMP) {
			
			p.y = Math.max(Math.min(posY, size() - 1), 0);
			p.x = Math.max(Math.min(posX, get((int) p.y).size() - 1), 0);
		}
		
		else if (wrapBehavior == Wrap.LOOP) {
			
			p.y = posY;
			while (p.y >= size())
				p.y -= size();
			while (p.y < 0)
				p.y += size();
			
			int rowSize = get((int) p.y).size();
			p.x = posX;
			
			while (p.x >= rowSize)
				p.x -= rowSize;
			while (p.x < 0)
				p.x += rowSize;

		}
				
		return p;
		
	}
	
	public Vector2f getCoords(Vector2f pos) {
		return getCoords(Math.round(pos.x), Math.round(pos.y));
	}
	
	public void set(int x, int y, int value) {
		
		int fx = (int) getCoords(x, y).x;
		int fy = (int) getCoords(x, y).y;
		
		get(fy).set(fx, value);
		
	}
	
	public void set(Vector2f pos, int value) {
		set(Math.round(pos.x), Math.round(pos.y), value);
	}
	
	public Vector2f getMiddleCoords(){
		
		return new Vector2f((int) size() / 2, (int) get(0).size() / 2);
		
	}

	public void setLine(Vector2f start, Vector2f end, int value) {
		
		Vector2f pos = new Vector2f(start);
		
		boolean axisX = false;
		
		set(pos, value);
		
		Vector2f dir = end.minus(start);
		dir.normalize();
		
		int rPX = Math.round(pos.x);
		int rPY = Math.round(pos.y);
				
		while (rPX != Math.round(end.x) || rPY != Math.round(end.y)) {
									
			if (axisX)
				pos.x += dir.x;
			else
				pos.y += dir.y;
			
			axisX = !axisX;
			
			rPX = Math.round(pos.x);
			rPY = Math.round(pos.y);
						
			set(pos, value);
				
		}
		
	}
	
	public void generateNodes(int[] nodeValues, int[] hallValues, ConnectionMode connectionMode, boolean connectOnce) {
	
		final ArrayList<Integer> nodeVals = new ArrayList<Integer>();
		for (Integer i : nodeValues)
			nodeVals.add(i);
		
		final ArrayList<Integer> hallVals = new ArrayList<Integer>();
		for (Integer i : hallValues)
			hallVals.add(i);
		
		final class Node {
			
			Vector2f position;
			ArrayList<Node> connections;
			ArrayList<Node> connectionsInitiated;
			
			public Node(int x, int y){
				position = new Vector2f(x, y);
				connections = new ArrayList<Node>();
				connectionsInitiated = new ArrayList<Node>();
			}
			
			public Node(Vector2f coords) {
				this(Math.round(coords.x), Math.round(coords.y));
			}
			
			public void connect(Node other){
				
				if (other != this) {
					
					setLine(position, other.position, Random.choice(hallVals));
					connections.add(other);
					connectionsInitiated.add(other);
					other.connections.add(this);
					
				}
				
			}
			
		}
		
		if (seed != 0)
			Random.seed(seed);
		
		int nodeCount = 6;
		
		ArrayList<Node> nodes = new ArrayList<Node>();
		
		for (int n = 0; n < nodeCount; n++) {
			nodes.add(new Node(getRandomCoords()));
		}
		
		if (connectionMode == ConnectionMode.HUB) {
			
			Node hub = Random.choice(nodes);
			
			for (Node node : nodes) {
				
				node.connect(hub);
				
			}
			
		}
		
		else if (connectionMode == ConnectionMode.ALL) {
			
			for (Node node : nodes) {
				
				for (Node other : nodes) {
					
					node.connect(other);
					
				}
				
			}
			
		}
		
		else if (connectionMode == ConnectionMode.ONE) {
			
			ArrayList<Node> unconnectedNodes = new ArrayList<Node>(nodes);
			
			for (Node node : nodes) { 
				
				if (unconnectedNodes.size() > 0) {
				
					Node other = Random.choice(unconnectedNodes);
					
					if (unconnectedNodes.size() > 1 && other == node) {
						
						while(other == node) {
							other = Random.choice(unconnectedNodes);
						}
						
					}
					
					node.connect(other);
					
					if (other != node)
						unconnectedNodes.remove(node);
				
				}
				
			}
			
		}
		
		for (Node n : nodes) {
			set(n.position, Random.choice(nodeVals));  // Setting the lines messes this up
		}
		
	}
	
//	public void generateTurnAlgo(int[] values){
//		
//		if (seed != 0)
//			Random.seed(seed);
//		
//		Vector2f pos = getRandomCoords();
//		
//		Vector2f direction = new Vector2f(Random.direction().x, Random.direction().y);
//		direction.normalize();
//				
//		ArrayList<Integer> vals = new ArrayList<Integer>();
//		
//		for (Integer i : values)
//			vals.add(i);
//		
//		int turnCount = 3; // Should be an argument, perhaps two (between x and y numbers of turns)
//		
//		for (int t = 0; t < turnCount; t++) {
//			
//			float d = Random.random(1, size());
//			
//			Vector2f end = pos.plus(direction.mul(d));
//			
//			end.x = Math.round(end.x);
//			end.y = Math.round(end.y);
//			
//			setLine(pos, end, Random.choice(vals));
//			
//			if (Random.random() > 0.5f) {	// Right hand turn
//				float temp = -direction.x;
//				direction.x = direction.y;
//				direction.y = temp;
//			}
//			else {
//				float temp = -direction.y;
//				direction.y = direction.x;
//				direction.x = temp;
//			}
//			
//			end = getCoords(end);
//			
//			System.out.println(pos);
//			
//			pos = end;
//			
//			System.out.println(pos);
//				
//		}
//				
//	}
	
	public Vector2f getRandomCoords(){
				
		return new Vector2f( (int) Random.random(0, size()), (int) Random.random(0, get(0).size()));
		
	}
	
	public String toString(){
		
		String out = "";
		
		for (ArrayList<Integer> row : this) {
			out += row.toString();
			out += "\n";
		}
		
		return out;
	}
	
}
