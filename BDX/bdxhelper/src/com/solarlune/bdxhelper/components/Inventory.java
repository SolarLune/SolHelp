package com.solarlune.bdxhelper.components;

import java.util.HashMap;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;

public class Inventory extends Component<GameObject> {

	HashMap<String, Object> container = new HashMap<String, Object>();
	
	public Inventory(GameObject g) {
		super(g);
	}

}
