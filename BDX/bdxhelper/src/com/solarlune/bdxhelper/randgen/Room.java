package com.solarlune.bdxhelper.randgen;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

import javax.vecmath.Vector2f;
import javax.vecmath.Vector3f;

import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.Scene;
import com.nilunder.bdx.utils.Random;

import java.lang.Math;

public class Room extends ArrayList<ArrayList<Cell>> {
	
	public enum Wrap {
		
		NONE,
		CLAMP,
		WRAP;
		
	}
	
	public enum ConnectionMode {  // Used for generateNodes algorithm
		
		ALL,
		HUB,
		ONE,
		
	}
		
	public Wrap wrapBehavior = Wrap.CLAMP;
	
	public ArrayList<Cell> openCells = new ArrayList<Cell>();
	
	public long seed = 0;
	
	public Scene scene;
	
	public Room(int sizeX, int sizeY, Scene scene) {
		
		resize(sizeX, sizeY);
		this.scene = scene;
		
	}
	
	public void resize(int sizeX, int sizeY, ArrayList<String> values) {
		
		clear();
		
		openCells.clear();
		
		for (int i = 0; i < sizeY; i++) {
			
			add(new ArrayList<Cell>());
			
			for (int j = 0; j < sizeX; j++) {
				
				Cell c = new Cell(j, i, this);
				
				c.setValue(Random.choice(values));
				
				get(i).add(c);
				
				openCells.add(c);
				
			}
			
		}
		
	}

	public void resize(int sizeX, int sizeY){
		
		ArrayList<String> s = new ArrayList<String>();
		s.add("0");		
		resize(sizeX, sizeY, s);
		
	}
	
	public Cell get(Vector2f pos) {
		
		int fy = (int) getCoords(pos).y;
		int fx = (int) getCoords(pos).x;
		
		return get(fy).get(fx);

	}
	
	public Cell get(int x, int y) {
		
		return get(new Vector2f(x, y));

	}
	
	public Vector2f getCoords(int posX, int posY){
		
		Vector2f p = new Vector2f(posX, posY);
		
		if (wrapBehavior == Wrap.CLAMP) {
			
			p.y = Math.max(Math.min(posY, size() - 1), 0);
			p.x = Math.max(Math.min(posX, get((int) p.y).size() - 1), 0);
		}
		
		else if (wrapBehavior == Wrap.WRAP) {
			
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
	
	public void set(int x, int y, String value) {
		
		int fx = (int) getCoords(x, y).x;
		int fy = (int) getCoords(x, y).y;
		
		get(fy).get(fx).setValue(value);
		
	}
	
	public void set(Vector2f pos, String value) {
		set(Math.round(pos.x), Math.round(pos.y), value);
	}
	
	public Vector2f getMiddleCoords(){
		
		return new Vector2f((int) size() / 2, (int) get(0).size() / 2);
		
	}

	public void setLine(Vector2f start, Vector2f end, String value) {
		
		Vector2f pos = new Vector2f(start);
		
		Vector2f nextPos = new Vector2f(pos);
		
		boolean axisX = false;
		
		Vector2f dir = end.minus(start);
		dir.normalize();
		
		int rPX = Math.round(pos.x);
		int rPY = Math.round(pos.y);
				
		while (rPX != Math.round(end.x) || rPY != Math.round(end.y)) {
									
			if (axisX)
				nextPos.x += dir.x;
			else
				nextPos.y += dir.y;
			
			axisX = !axisX;
			
			rPX = Math.round(nextPos.x);
			rPY = Math.round(nextPos.y);
						
			//set(pos, value);
			//set(nextPos, value);
			
			get(pos).connect(get(nextPos), value);
			
			pos.x = nextPos.x;
			pos.y = nextPos.y;
			
		}
		
	}
		
	public void generateNodesAlgo(String[] nodeValues, String[] hallValues, ConnectionMode connectionMode, boolean connectOnce) {
	
		final ArrayList<String> nodeVals = new ArrayList<String>();
		for (String i : nodeValues)
			nodeVals.add(i);
		
		final ArrayList<String> hallVals = new ArrayList<String>();
		for (String i : hallValues)
			hallVals.add(i);
				
		if (seed != 0)
			Random.seed(seed);
		
		int nodeCount = 6;
		
		ArrayList<Cell> nodes = new ArrayList<Cell>();
		
		for (int n = 0; n < nodeCount; n++) {
			nodes.add(new Cell(getRandomCoords(), this));
		}
		
		if (connectionMode == ConnectionMode.HUB) {
			
			Cell hub = Random.choice(nodes);
			
			for (Cell node : nodes) {
				
				node.connect(hub, Random.choice(hallVals));
				
			}
			
		}
		
		else if (connectionMode == ConnectionMode.ALL) {
			
			for (Cell node : nodes) {
				
				for (Cell other : nodes) {
					
					node.connect(other, Random.choice(hallVals));
					
				}
				
			}
			
		}
		
		else if (connectionMode == ConnectionMode.ONE) {
			
			ArrayList<Cell> unconnectedNodes = new ArrayList<Cell>(nodes);
			
			for (Cell node : nodes) { 
				
				if (unconnectedNodes.size() > 0) {
				
					Cell other = Random.choice(unconnectedNodes);
					
					if (unconnectedNodes.size() > 1 && other == node) {
						
						while(other == node) {
							other = Random.choice(unconnectedNodes);
						}
						
					}
					
					node.connect(other, Random.choice(hallVals));
					
					if (other != node)
						unconnectedNodes.remove(node);
				
				}
				
			}
			
		}
		
		for (Cell n : nodes) {
			set(n.position, Random.choice(nodeVals));  // Setting the lines messes this up
		}
		
	}
	
	public void generateMazeAlgo(int cellNum, int turnLeftWeight, int turnRightWeight, int straightWeight){
		
		if (seed != 0)
			Random.seed(seed);
				
		Vector2f pos = getRandomCoords();
		
		Vector2f direction = new Vector2f(0, -1);
		
		int cN = Math.min(cellNum, size() * get(0).size() - 1);
		
		for (int c = 0; c < cN; c++) {
			
			ArrayList<Vector2f> possibles = new ArrayList<Vector2f>();
						
			Vector2f l = com.solarlune.bdxhelper.Math.rotL(direction);
			Vector2f r = com.solarlune.bdxhelper.Math.rotR(direction);
	
			if (spaceEmpty(pos.plus(l))) {
				for (int i = 0; i < turnLeftWeight; i++)
					possibles.add(l);
			}
			if (spaceEmpty(pos.plus(r))) {
				for (int i = 0; i < turnRightWeight; i++)
					possibles.add(r);
			}
			if (spaceEmpty(pos.plus(direction))) {
				for (int i = 0; i < straightWeight; i++)
					possibles.add(direction);
			}
			
			if (possibles.size() > 0) {
				
				direction = Random.choice(possibles);
				
				get(pos).connect(get(pos.plus(direction)), "x");
				
				pos.add(direction);
								
			}
			else {
				
				Cell nextOne = getRandomCell("x");
				
				while(nextOne.equals(get(pos)))
					nextOne = getRandomCell("x");
				
				pos = new Vector2f(nextOne.position);
				
				c--; // This cell didn't work, basically, so decrease by one  // This is a way to an infinite loop, so bekarful
				
			}
						
		}
				
	}
	
	public void generateMazeAlgo(){
		generateMazeAlgo(Integer.MAX_VALUE, 1, 1, 1);
	}
	
	public boolean spaceEmpty(Vector2f pos) {
		
		Vector2f p = getCoords(pos);
		
		return get(p).getValue().equals("0");
		
	}
		
	public Vector2f getRandomCoords(){
				
		return new Vector2f( (int) Random.random(0, size()), (int) Random.random(0, get(0).size()));
		
	}
	
	public Cell getRandomCell(String value){
		
		Cell c = null;
		
		while (c == null) {
			
			Vector2f r = getRandomCoords();
			
			Cell p = get(r);
			
			if (p.getValue() == value || value == null) 
				c = p;
			
		}
		
		return c;
		
	}
	
	public Cell getRandomOpenCell(String value) {
		
		return null;
		
	}
		
	public String toString(){
		
		String out = "";
		
		for (ArrayList<Cell> row : this) {
			out += row.toString();
			out += "\n";
		}
		
		return out;
	}
	
	public void placeObjects(String[] ends, String[] straights, String[] corners, 
			String[] tEnds, String[] fourWays, String[] empties, Vector3f spawnPosition){
		
		ArrayList<String> endsAL = new ArrayList<String>(Arrays.asList(ends));
		ArrayList<String> straightsAL = new ArrayList<String>(Arrays.asList(straights));
		ArrayList<String> cornersAL = new ArrayList<String>(Arrays.asList(corners));
		ArrayList<String> tEndsAL = new ArrayList<String>(Arrays.asList(tEnds));
		ArrayList<String> fourWaysAL = new ArrayList<String>(Arrays.asList(fourWays));
		ArrayList<String> emptiesAL = new ArrayList<String>(Arrays.asList(empties));
				
		for (int y = 0; y < size(); y++) {
			
			for (int x = 0; x < get(y).size(); x++) {
				
				Cell cell = get(x,y);
				
				GameObject createdCell = null;
				
				HashMap<String, Cell> neighbors = cell.getNeighbors();
				
				float ninety = (float) Math.PI / 2;
				
				if (cell.connections.size() == 0) {
					
					String emptyName = Random.choice(emptiesAL);
										
					if (emptyName != null) {
						
						createdCell = scene.add(Random.choice(emptiesAL));
					
						ArrayList<Vector3f> rots = new ArrayList<Vector3f>();
						
						rots.add(new Vector3f(0, 0, 0));
						rots.add(new Vector3f(0, 0, (float) Math.PI / 2));
						rots.add(new Vector3f(0, 0, (float) Math.PI));
						rots.add(new Vector3f(0, 0, -(float) Math.PI / 2));
						
						//createdCell.rotate(Random.choice(rots));
					
					}
					
				}
				
				else if (cell.connections.size() == 1) {
					createdCell = scene.add(Random.choice(endsAL));
					
					Vector3f rot = new Vector3f(cell.connections.get(0).position.x - cell.position.x, 
							cell.position.y - cell.connections.get(0).position.y, 0);
					
					createdCell.alignAxisToVec(1, rot);
					createdCell.alignAxisToVec(2, new Vector3f(0, 0, 1));
					
				}
				
				else if (cell.connections.size() == 2) {
					if (neighbors.containsKey("left") && neighbors.containsKey("right")) {
						createdCell = scene.add(Random.choice(straightsAL));
						createdCell.rotate(0, 0, ninety);
					}
					else if (neighbors.containsKey("up") && neighbors.containsKey("down")) {
						createdCell = scene.add(Random.choice(straightsAL));
					}
					else {
						
						createdCell = scene.add(Random.choice(cornersAL));
						
						if (neighbors.containsKey("right") && neighbors.containsKey("down"))
							;
						
						if (neighbors.containsKey("left") && neighbors.containsKey("down"))
							createdCell.rotate(0, 0, -ninety);
						
						if (neighbors.containsKey("right") && neighbors.containsKey("up"))
							createdCell.rotate(0, 0, ninety);
						
						if (neighbors.containsKey("left") && neighbors.containsKey("up"))
							createdCell.rotate(0, 0, ninety*2);
					}
				}
				else if (cell.connections.size() == 3) {
					
					createdCell = scene.add(Random.choice(tEndsAL));
					
					if (!neighbors.containsKey("up"))
						;
					if (!neighbors.containsKey("left"))
						createdCell.rotate(0, 0, ninety);
					if (!neighbors.containsKey("down"))
						createdCell.rotate(0, 0, ninety*2);
					if (!neighbors.containsKey("right"))
						createdCell.rotate(0, 0, -ninety);
						
				}
				else if (cell.connections.size() == 4) {
					createdCell = scene.add(Random.choice(fourWaysAL));
				}
				
				if (createdCell != null) {
				
					Vector3f pos;
					
					if (spawnPosition == null)
						pos = new Vector3f();
					else
						pos = new Vector3f(spawnPosition);
					
					Vector3f blockSize = createdCell.dimensions();
					
					pos.y += size() * blockSize.y / 2;
					pos.x -= get(0).size() * blockSize.x / 2;
					
					pos.y -= (y * blockSize.y);
					pos.x += (x * blockSize.x);
										
					createdCell.position(pos);
					
					cell.createdRoom = createdCell;
				
				}
							
			}
			
		}
		
	}
	
	public void placeObjects(String end, String straight, String corner, String tEnd, String fourWays, String empty, Vector3f spawnPosition){
				
		placeObjects(new String[]{end}, new String[]{straight}, new String[]{corner}, 
				new String[]{tEnd}, new String[]{fourWays}, new String[]{empty}, spawnPosition);
		
	}
	
}
