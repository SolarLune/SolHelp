package com.solarlune.bdxhelper.randgen;

import java.util.ArrayList;
import java.util.HashMap;

import javax.vecmath.Vector2f;

import com.nilunder.bdx.GameObject;

public class Cell {

	public Vector2f position;
	public ArrayList<Cell> connections;
	public ArrayList<Cell> connectionsInitiated;
	public Room room;
	private String value;
	public GameObject createdRoom;
	
	public Cell(int x, int y, Room room){
		position = new Vector2f(x, y);
		connections = new ArrayList<Cell>();
		connectionsInitiated = new ArrayList<Cell>();
		setValue("0");
		this.room = room;
	}
	
	public Cell(Vector2f coords, Room room) {
		this((int) room.getCoords(coords).x, (int) room.getCoords(coords).y, room);
	}
	
	public void connect(Cell other, String value){
		
		if (other != this) {
			
			room.set(position, value);
			room.set(other.position, value);
			connections.add(other);
			other.connections.add(this);
			connectionsInitiated.add(other);
			
		}
		
	}
	
	public HashMap<String, Cell> getNeighbors(){
		
		HashMap<String, Cell> hash = new HashMap<String, Cell>();
		
		for (Cell conn : connections) {
						
			if (conn.position.x > position.x + 0.01f)
				hash.put("right", conn);
			else if (conn.position.x < position.x - 0.01f)
				hash.put("left", conn);
			else if (conn.position.y > position.y + 0.01f)
				hash.put("down", conn);
			else if (conn.position.y < position.y - 0.01f)
				hash.put("up", conn);
			
		}
		
		return hash;
		
	}

	public void setValue(String value){
		this.value = value;
	}
	
	public String getValue(){
		return value;
	}
	
	public String toString(){
		return getValue();
	}
	
}