package com.solarlune.bdxhelper.input;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by SolarLune on 1/7/2015.
 */

public final class InputMap {

    static public HashMap<String, ArrayList<InputBase>> bindings = new HashMap<String, ArrayList<InputBase>>();
    static public HashMap<String, ArrayList<Float>> results = new HashMap<String, ArrayList<Float>>();

    private InputMap(){
    }

    static public void addBinding(String bindingName, InputBase inputBase){

        if (!bindings.containsKey(bindingName))
            bindings.put(bindingName, new ArrayList<InputBase>());

		ArrayList<Float> ar = new ArrayList<Float>();

		ar.add(0.0f);  // For current and past value
		ar.add(0.0f);

		results.put(bindingName, ar);

        bindings.get(bindingName).add(inputBase);

    }

    static public void removeBinding(String bindingName){

        if (bindings.containsKey(bindingName)) {
			bindings.remove(bindingName);
		}
		if (results.containsKey(bindingName)) {
			results.remove(bindingName);
		}
    }

    static public void clear(){
        bindings.clear();
		results.clear();
    }

    static public float bindDown(String bindName){

        if (results.containsKey(bindName)){

			return results.get(bindName).get(1);

        }

        return 0;
    }

    static public boolean bd(String bindName){

        return bindDown(bindName) != 0;

    }

    static public float bindPressed(String bindName){

        if (results.containsKey(bindName)){

            ArrayList<Float> res = results.get(bindName);

			if (res.get(1) != 0 && res.get(0) == 0)
				return res.get(1);
        }

        return 0;
    }

    static public boolean bp(String bindName){

        return bindPressed(bindName) != 0;

    }

    static public float bindReleased(String bindName) {

        if (results.containsKey(bindName)){

			ArrayList<Float> res = results.get(bindName);

			if (res.get(1) == 0 && res.get(0) != 0)

				return res.get(1);

        }

        return 0;
    }

    static public boolean br(String bindName){

        return bindReleased(bindName) != 0;

    }

    static public void poll(){

        for (String binding : bindings.keySet() ) {
            poll(binding);
        }

    }

    static public void poll(String bindingName) {

        for (InputBase ik : bindings.get(bindingName)) {

            ik.poll();

			results.get(bindingName).remove(0);
			results.get(bindingName).add(ik.active);

        }

    }

    static public void set(String bindingName, float value) {

		results.get(bindingName).set(1, value);

    }

	static public void discard(String bindingName, boolean pastFrame) {

		if (pastFrame)
			results.get(bindingName).set(0, results.get(bindingName).get(1));
		else
			results.get(bindingName).set(1, results.get(bindingName).get(0));

	}

	static public void discard(String bindingName) {
		discard(bindingName, true);
	}

}
