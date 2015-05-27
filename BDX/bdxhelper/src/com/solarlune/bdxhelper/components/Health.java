package com.solarlune.bdxhelper.components;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;

public class Health extends Component<GameObject> {

	public float value;
	public float maxValue;
	
	public Health(GameObject g) {
		this(g, 10);
	}
	
	public Health(GameObject g, float value) {
		super(g);
		setMax(value);
		set(value);
	}
	
	public void set(float value){
		this.value = Math.min(value, getMax());
	}
	
	public void setMax(float value) {
		this.maxValue = value;
	}
	
	public float get() {
		return value;
	}
	
	public float getMax(){
		return maxValue;
	}

}
