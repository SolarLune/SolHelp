package com.solarlune.bdxhelper.components.properties;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;

public class Health extends Component<GameObject> {

	private float value;
	private float maxValue;
	public boolean invulnerable;
	
	public Health(GameObject g) {
		this(g, 10);
	}
	
	public Health(GameObject g, float value) {
		super(g);
		setMax(value);
		set(value);
		invulnerable = false;
	}
	
	public void add(float value){
		set(get() + value);
	}
	public void sub(float value){
		if (!invulnerable)
			set(get() - value);
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
