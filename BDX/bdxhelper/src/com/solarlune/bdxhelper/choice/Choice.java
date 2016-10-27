package com.solarlune.bdxhelper.choice;

import com.nilunder.bdx.utils.Named;

import javax.vecmath.Vector3f;

/**
 * Created by solarlune on 8/7/16.
 */
public class Choice implements Named {

    private String name;
    public Screen screen;
    public Vector3f position = new Vector3f();

    private Choice up;
    private Choice down;
    private Choice left;
    private Choice right;

    public Choice(String name){
        name(name);
    }

    public void name(String name){
        this.name = name;
    }

    public String name(){
        return name;
    }

    public void right(Choice choice){
        right = choice;
        if (choice.left == null)
            choice.left = this;
    }

    public void right(String choiceName){
        right(screen.choices.get(choiceName));
    }

    public Choice right(){
        return right;
    }

    public void clearRight(){
        right = null;
    }

    public void left(Choice choice) {
        left = choice;
        if (choice.right == null)
            choice.right = this;
    }

    public void left(String choiceName) {
        left(screen.choices.get(choiceName));
    }

    public Choice left(){
        return left;
    }

    public void clearLeft(){
        left = null;
    }

    public void up(Choice choice) {
        up = choice;
        if (choice.down == null)
            choice.down = this;
    }

    public void up(String choiceName) {
        up(screen.choices.get(choiceName));
    }

    public Choice up(){
        return up;
    }

    public void clearUp(){
        up = null;
    }

    public void down(Choice choice) {
        down = choice;
        if (choice.up == null)
            choice.up = this;
    }

    public void down(String choiceName) {
        down(screen.choices.get(choiceName));
    }

    public Choice down(){
        return down;
    }

    public void clearDown(){
        down = null;
    }

    public void clearNeighbors(){
        clearUp();
        clearRight();
        clearDown();
        clearLeft();
    }

    public String toString(){
        return "Choice: " + name();
    }

}
