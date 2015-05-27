package com.solarlune.bdxhelper.components;

import java.util.ArrayList;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;

public class AIDirector extends Component<GameObject> {
		
	public ArrayList<AIDirection<GameObject>> directions = new ArrayList<AIDirection<GameObject>>();
	
	public int currentDirection = 0;
	
	public AIDirector(GameObject g) {
		super(g);
		state = mainState;
	}
	
	State mainState = new State(){
		
		public void main(){
			
			if (currentDirection < directions.size()) {
				
				AIDirection<GameObject> current = directions.get(currentDirection);
				
				current.state.main();
								
				if (current.done()) {
					current.done(false);
					currentDirection++;
					if (currentDirection < directions.size())
						directions.get(currentDirection).restart();
				}
				
			}
			else {
				currentDirection = 0;
				
				if (currentDirection < directions.size())
					directions.get(currentDirection).restart();
			}
			
		}
		
	};
	
	public String getCurrentDirectionName(){
		
		AIDirection<GameObject> current = directions.get(currentDirection);
		
		if (current != null) {
			return current.name();		
		}
		
		return null;
		
	}
	
	public AIDirection<GameObject> getCurrentDirection(){
		return directions.get(currentDirection);
	}

}
