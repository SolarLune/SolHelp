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
	
	public Wrap wrapBehavior = Wrap.LOOP;
	
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
	
	public void fill(ArrayList<Integer> zeroes) {
		
		// Fills the room with one of a random assortment of zero elements.
		
		for (ArrayList<Integer> row : this) {
			
			for (int i = 0; i < row.size(); i++) {
				
				row.set(i, Random.choice(zeroes));
				
			}
			
		}
		
	}
	
	public void fill(){
		fill(new ArrayList<Integer>(0));			
	}
	
	public int get(int x, int y) {
	
		if (wrapBehavior == Wrap.NONE)
			return get(y).get(x);
		else if (wrapBehavior == Wrap.CLAMP) {
			int fy = Math.max(Math.min(y, size() - 1), 0);
			int fx = Math.max(Math.min(x, get(fy).size() - 1), 0);
			return get(fy).get(fx);
		}
		// else if (wrapBehavior == Wrap.LOOP) {
		else {
			
			int fy = y;
			while (fy > size() - 1)
				fy -= size();
			while (fy < 0)
				fy += size();
			
			int rowSize = get(fy).size() - 1;
			int fx = x;
			
			while (fx > rowSize)
				fx -= rowSize;
			while (fx < 0)
				fx += rowSize;
			
			return get(fy).get(fx);
			
		}
			
	}
	
	public int get(Vector2f pos) {
		return get((int) pos.x, (int) pos.y);
	}
	
	public void set(int x, int y, int value) {
		
		if (wrapBehavior == Wrap.NONE)
			get(y).set(x, value);
		else if (wrapBehavior == Wrap.CLAMP) {
			int fy = Math.max(Math.min(y, size() - 1), 0);
			int fx = Math.max(Math.min(x, get(fy).size() - 1), 0);
			get(fy).set(fx, value);
		}
		//else if (wrapBehavior == Wrap.LOOP) {
		else {	
		
			int fy = y;
			while (fy > size() - 1)
				fy -= size();
			while (fy < 0)
				fy += size();
			
			int rowSize = get(fy).size() - 1;
			int fx = x;
			
			while (fx > rowSize)
				fx -= rowSize;
			while (fx < 0)
				fx += rowSize;
			
			get(fy).set(fx, value);
			
		}
	}
	
	public void set(Vector2f pos, int value) {
		set((int) pos.x, (int) pos.y, value);
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
		
		//for (int i = 0; i < 20; i++) {
			
		while (end.minus(pos).length() > 0.1f) {
			
			if (axisX)
				pos.x += dir.x;
			else
				pos.y += dir.y;
			
			set(pos, value);
			
			axisX = !axisX;
						
			//if (end.x - pos.x < 0.5f && end.y - pos.y < 0.5f)
			//if (end.minus(pos).length() < 0.1f)
			//	break;
			
		}
		
	}
	
	public void generateTurnAlgo(int[] values){
		
		// TODO: random seeds
		
		Vector2f pos = getRandomCoords();
		
		Vector2f direction = new Vector2f(Random.direction().x, Random.direction().y);
		direction.normalize();
				
		ArrayList<Integer> vals = new ArrayList<Integer>();
		
		for (Integer i : values)
			vals.add(i);
		
		set(pos, Random.choice(vals));
		
		int turnCount = 1; // Should be an argument
		
		for (int t = 0; t < turnCount; t++) {
		
			
			
//			if (Random.random() > 0.5f) {  // Right turn
//				
//				
//				
//			}
		
		}
				
	}
	
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
