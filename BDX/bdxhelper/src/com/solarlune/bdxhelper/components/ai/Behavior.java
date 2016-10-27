package com.solarlune.bdxhelper.components.ai;

import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;

/**
 * Created by SolarLuneNew on 4/1/2016.
 */

public class Behavior extends State {

    public GameObject g;

    public Behavior(GameObject g){
        this.g = g;
    }

    public boolean done(){
        return true;
    }

    public String name(){
        return this.getClass().getSimpleName();
    }

}