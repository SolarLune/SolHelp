package com.solarlune.bdxhelper.input.gamepadprofiles;

import java.util.HashMap;

/**
 * Created by SolarLune on 1/16/2015.
 */
public class GPProfile {

    public HashMap<String, Integer> buttons = new HashMap<String, Integer>();
    public HashMap<String, Integer> axes = new HashMap<String, Integer>();
    public HashMap<String, Integer> hats = new HashMap<String, Integer>();

    public int getAxis(String axisName){
        return axes.get(axisName);
    }
    public String getAxis(int axisIndex){
        for (String name : axes.keySet()){
            if (axes.get(name) == axisIndex)
                return name;
        }
        return null;
    }
    public int getButton(String buttonName){
        return buttons.get(buttonName);
    }
    public String getButton(int buttonIndex){
        for (String name : buttons.keySet()){
            if (buttons.get(name) == buttonIndex)
                return name;
        }
        return null;
    }
    public int getHat(String hatName){
        return hats.get(hatName);
    }
    public String getHat(int hatDir) {
        for (String name : hats.keySet()){
            if (hats.get(name) == hatDir){
                return name;
            }
        }
        return null;
    }

}
