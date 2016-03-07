package com.solarlune.bdxhelper.components.properties;

import com.nilunder.bdx.Bdx;
import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;

public class Gauge extends Component<GameObject> {

	public enum Adjust {  	// What happens if you adjust the maximum value (e.g. when MAX was 10, but now = 20, and VAL = 5)
		NONE,    			// Don't do anything (M = 20, V = 5)
		RATIO,  			// Push value to maintain ratio (M = 20, V = 10)
		VALUE,  			// Push value to maintain value difference (M = 20, V = 15)
	}
	
	private float value;
	private float maxValue;
	private float prevValue;
	public boolean invulnerable;
	public float regenRate;				// Percentage of the max to regen a second
	public Adjust onMaxAdjust;				// What to do when the max is adjusted
	public boolean allowNegatives;
	
	public Gauge(GameObject g, float value, String name) {
		
		super(g);
		setMax(value);
		set(value);
		invulnerable = false;
		regenRate = 0;
		state = stateMain;
		this.name = name;
		onMaxAdjust = Adjust.NONE;
		allowNegatives = false;
		
	}
	
	public Gauge(GameObject g) {
		this(g, 10, "Gauge");
	}
	
	public void add(float value){
		set(get() + value);
	}
	
	public void sub(float value){
		if (!invulnerable)
			set(get() - value);
	}

	public void mul(float value) {
		set(get() * value);
	}

	public void set(float value){
		if (allowNegatives)
			this.value = Math.min(value, getMax());
		else
			this.value = Math.max(Math.min(value, getMax()), 0);
	}
	
	public void setMax(float value) {
		readjustStrat(value);
		this.maxValue = value;
	}
		
	public float get() {
		return value;
	}
	
	public float getAsPercentage(){
		return get() / getMax();
	}
	
	public float getMax(){
		return maxValue;
	}
			
	private void readjustStrat(float newMax){
		if (onMaxAdjust == Adjust.RATIO){
			float ratio = newMax / maxValue;
			value *= ratio;
		}
		else if (onMaxAdjust == Adjust.VALUE) {
			float diff = newMax - maxValue;
			value += diff;
		}
	}
	
	public void refill(){
		set(getMax());
	}

	State stateMain = new State(){
		
		public void main() {
			if (regenRate != 0) 
				add((maxValue / regenRate) * Bdx.TICK_TIME);

			prevValue = value;
		};
		
	};

}
