package com.solarlune.bdxhelper.components.properties;

import java.util.ArrayList;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;

public class Type extends Component<GameObject> {

	public String value;
	
	public Type(GameObject g, String type) {
		super(g);
		value = type;
	}
	
	
	public ArrayList<GameObject> find(String type, boolean all) {
		
		ArrayList<GameObject> found = new ArrayList<GameObject>();
		
		for (GameObject other : g.scene.objects) {
			
			if (other != g && other.components.get("Type") != null && ( (Type) other.components.get("Type")).value.equals(type)) {
				found.add(other);
				if (!all)
					break;
			}
			
		}
		
		return found;
		
	}

}
