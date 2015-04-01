package com.solarlune.bdxhelper.ai;

import java.util.HashMap;

public class StateMachine {

	State currentState;
	State prevState;
	State globalState;
	
	HashMap<String, State> states = new HashMap<String, State>();
	
	public StateMachine(){
	}
	
	public void changeState(String newState) {
		
		if (currentState != null)
			currentState.exit();
		
		prevState = currentState;
	
		currentState = states.get(newState);
		
		currentState.enter();
		
	}
	
	public void addState(State state) {
		states.put(state.getClass().getSimpleName(), state);
	}
	
	public void setGlobalState(State newState){
		
		if (globalState != null)
			globalState.exit();
		globalState = states.get(newState);
		globalState.enter();
	}
	
	public void main(){
		if (currentState != null)
			currentState.main();
		if (globalState != null)
			globalState.main();
	}
	
	public void sendMessage(String msg){
		currentState.onMessage(msg);
	}
	
	public String getGlobalState(){
		return globalState.getClass().getSimpleName();
	}
	
	public String getCurrentState(){
		return currentState.getClass().getSimpleName();
	}
		
}
