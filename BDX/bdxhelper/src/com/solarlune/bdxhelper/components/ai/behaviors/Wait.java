package com.solarlune.bdxhelper.components.ai.behaviors;

import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.utils.Timer;
import com.solarlune.bdxhelper.components.ai.Behavior;

/**
 * Created by SolarLuneNew on 4/1/2016.
 */
public class Wait extends Behavior {

	public Timer waitTimer;

	public Wait(GameObject g) {
		this(g, 1);
	}

	public Wait(GameObject g, float waitTime) {
		super(g);
		waitTimer = new Timer(waitTime);
	}

	public void enter(){
		waitTimer.restart();
	}

	public boolean done(){
		return waitTimer.tick();
	}

}
