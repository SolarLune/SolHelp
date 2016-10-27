package com.solarlune.bdxhelper.components.properties;

import com.nilunder.bdx.Bdx;
import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;

public class Gauge extends Component<GameObject> {

	public enum Adjust {  	// What happens if you adjust the maximum value (e.g. when VAL = 5 and MAX was 10, but MAX changes to 20)
		NONE,    			// Don't do anything (M = 20, V = 5)
		RATIO,  			// Set value to maintain ratio (M = 20, V = 10)
		VALUE,  			// Set value to maintain value difference (M = 20, V = 15)
		REFILL,				// Set value to match the new maximum (M = 20, V = 20)
	}

	public enum Regen {
		VALUE,				// Regen value per second
		PERCENTAGE,			// Regen percentage of max per second
	}
	
	private float value;
	private float maxValue;
	public boolean invulnerable = false;
	public float regenRate = 0;				// Regeneration per second
	public Adjust onMaxAdjust = Adjust.NONE;			// What to do when the max is adjusted
	public Regen regenMode = Regen.PERCENTAGE;				// Regeneration mode
	public boolean allowNegatives = false;
    public boolean bottomedOut = false;
	private boolean prevBottomedOut = false;
    public float bottomOutRelease = 0.2f;   // What percentage to release regen penalty when bottomed out (if atBottom is glow to CUTREGEN)
    public float bottomOutRegenCut = 0.5f;  // What percentage to cut regen by when bottomed out
	public float regenBoostOnPercentage = 0.0f;	// How much regen boost to give according to the percentage remaining

	public Gauge(GameObject g, float value, String name) {
		super(g);
		max(value);
		value(value);
		state = stateMain;
		this.name = name;
	}
	
	public Gauge(GameObject g) {
		this(g, 10, "Gauge");
	}
	
	public void add(float value){
		value(value() + value);
	}
	
	public void sub(float value){
		if (!invulnerable)
			value(value() - value);
	}

	public void mul(float value) {
		value(value() * value);
	}

	public void div(float value) {
		value(value() / value);
	}

	public void value(float value){
		if (allowNegatives)
			this.value = Math.min(value, max());
		else
			this.value = Math.max(Math.min(value, max()), 0);
	}

	public float value() {
		return value;
	}
	
	public float valueAsPercentage(){
		return value() / max();
	}

	public void max(float value) {
		readjustStrat(value);
		this.maxValue = value;
	}
	
	public float max(){
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
		else if (onMaxAdjust == Adjust.REFILL)
			value = newMax;
	}

	public boolean justEmptied(){
		return bottomedOut && !prevBottomedOut;
	}

	State stateMain = new State(){
		
		public void main() {

			prevBottomedOut = bottomedOut;

            float regen = 0;

			if (regenRate != 0) {
				if (regenMode == Regen.PERCENTAGE)
					regen = (maxValue / regenRate) * Bdx.TICK_TIME;
				else
					regen = regenRate * Bdx.TICK_TIME;
			}

            regen += regenBoostOnPercentage * valueAsPercentage() * Bdx.TICK_TIME;

            if (value() <= 0)
                bottomedOut = true;

            if (valueAsPercentage() >= bottomOutRelease)
                bottomedOut = false;

            if (bottomedOut)
                regen *= bottomOutRegenCut;

            add(regen);

        };
		
	};

}
