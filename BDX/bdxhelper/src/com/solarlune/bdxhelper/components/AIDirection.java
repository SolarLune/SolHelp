package com.solarlune.bdxhelper.components;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;

public class AIDirection <T extends GameObject> extends Component<T> {

	private boolean done;
	
	public AIDirection(T g) {
		super(g);
	}
	
	public boolean done(){
		return done;
	}
	
	public void done(boolean value){
		done = value;
	}
	
	public void restart(){}

}
