package com.solarlune.bdxhelper.components;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;

public class TouchDamage extends Component<GameObject> {

	String targetType;
	float attack;
	
	public TouchDamage(GameObject g, String t, float attack) {
		super(g);
		targetType = t;
		this.attack = attack;
		state = mainState;
	}
	
	State mainState = new State(){
		
		public void main(){
			
			for (GameObject other : g.touchingObjects) {
				
				if (targetType == null || 
						(other.components.get("Type") != null && 
						((Type) other.components.get("Type")).value.equals(targetType))) {
					
					Health health = (Health) other.components.get("Health");
					
					if (health != null)
						health.value -= attack;
					
				}
				
			}
			
		}
		
	};

}
