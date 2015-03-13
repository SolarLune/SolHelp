package com.solarlune.bdxhelper.navigation;

import java.util.Collections;
import java.util.Stack;

/**
 * Created by SolarLune on 1/14/2015.
 */

public class Path {

    Stack<Node> points;
    Stack<Node> tempPoints;

    public Path(){
        points = new Stack<Node>();
        tempPoints = new Stack<Node>();
    }

    public void onReachedEnd(){}

    public void navigate(){
    }

    public void resetPath(){
        Collections.copy(tempPoints, points);
    }

}
