package com.solarlune.bdxhelper.choice;

import com.nilunder.bdx.Scene;
import com.nilunder.bdx.utils.ArrayListNamed;
import com.nilunder.bdx.utils.Named;

import javax.vecmath.Vector3f;

import java.util.ArrayList;

/**
 * Created by SolarLune on 1/28/2015.
 */

public class Screen {

    public enum BoundsMode {
        STOP,
        LOOP,
    }

    public enum AutoNeighborChoice {
        UP,
        RIGHT,
        DOWN,
        LEFT
    }

    public ArrayListNamed<Choice> choices = new ArrayListNamed<Choice>();
    public int loopSize = -1;
    public BoundsMode boundsMode = BoundsMode.STOP;

    public String name;
    public Choice activeChoice;

    Vector3f areaStart = new Vector3f();
    Vector3f areaEnd = new Vector3f();

    public void add(Choice c){
        if (activeChoice == null)
            activeChoice = c;
        choices.add(c);
        c.screen = this;
    }

    public ArrayListNamed<Choice> add(String... choiceNames) {

        ArrayListNamed<Choice> addedChoices = new ArrayListNamed<Choice>();

        for (String s : choiceNames) {
            Choice c = new Choice(s);
            addedChoices.add(c);
            add(c);
        }

        return addedChoices;
    }

    public void autoChoiceScroll(AutoNeighborChoice scrollMode) {

        for (int i = 0; i < choices.size(); i++) {

            Choice c = choices.get(i);

            Choice n = null;
            if (i < choices.size() - 1)
                n = choices.get(i + 1);

            Choice p = null;
            if (i > 0)
                p = choices.get(i - 1);

            if (n == null)      // At the end
                break;

            if (scrollMode == AutoNeighborChoice.UP) {
                c.up(n);
                n.down(c);
            }
            else if (scrollMode == AutoNeighborChoice.RIGHT) {
                c.right(n);
                n.left(c);
            }
            else if (scrollMode == AutoNeighborChoice.DOWN) {
                c.down(n);
                n.up(c);
            }
            else {
                c.left(n);
                n.right(c);
            }

            if (p != null) {
                if (scrollMode == AutoNeighborChoice.UP) {
                    c.down(p);
                    p.up(c);
                }
                else if (scrollMode == AutoNeighborChoice.RIGHT) {
                    c.left(p);
                    p.right(c);
                }
                else if (scrollMode == AutoNeighborChoice.DOWN) {
                    c.up(p);
                    p.down(c);
                }
                else {
                    c.right(p);
                    p.left(c);
                }
            }

        }

    }

    public void autoChoiceScroll(){
        autoChoiceScroll(AutoNeighborChoice.DOWN);
    }

    public void resetChoiceNeighbors(){
        for (Choice c : choices) {
            c.clearNeighbors();
        }
    }

    public void remove(Choice c){
        choices.remove(c);
    }

    public void clearChoices(){
        choices.clear();
    }

    public void up(){
        if (activeChoice.up() != null)
            activeChoice = activeChoice.up();
        else if (boundsMode == BoundsMode.LOOP) {
            Choice n = activeChoice;
            while (n.down() != null) {
                n = n.down();
            }
            activeChoice = n;
        }
    }

    public void right(){
        if (activeChoice.right() != null)
            activeChoice = activeChoice.right();
        else if (boundsMode == BoundsMode.LOOP) {
            Choice n = activeChoice;
            while (n.left() != null) {
                n = n.left();
            }
            activeChoice = n;
        }
    }

    public void down(){
        if (activeChoice.down() != null)
            activeChoice = activeChoice.down();
        else if (boundsMode == BoundsMode.LOOP) {
            Choice n = activeChoice;
            while (n.up() != null) {
                n = n.up();
            }
            activeChoice = n;
        }
    }

    public void left(){
        if (activeChoice.left() != null)
            activeChoice = activeChoice.left();
        else if (boundsMode == BoundsMode.LOOP) {
            Choice n = activeChoice;
            while (n.right() != null) {
                n = n.right();
            }
            activeChoice = n;
        }
    }

    public void autoChoicePosition(Scene scene){
        for (Choice c : choices) {
            if (scene.objects.get(c.name()) != null)
                c.position.set(scene.objects.get(c.name()).position());
        }
    }

//    public Choice setChoice(int index){
//        if (active)
//            currentChoiceIndex = index;
//        enforceBounds();
//        return choices.get(currentChoiceIndex);
//    }
//
//    public Choice skipChoice(int skip){
//        return setChoice(currentChoiceIndex + skip);
//    }

//    public void enforceBounds(){
//
//        if (boundsMode == BoundsMode.LOOP) {
//
//            int skip = loopSize == -1 ? choices.size() : loopSize + 1;
//
//            if (currentChoiceIndex >= choices.size()) {
//                currentChoiceIndex -= skip;
//            }
//            if (currentChoiceIndex < 0) {
//                currentChoiceIndex += skip;
//            }
//
//        }
//        else if (boundsMode == BoundsMode.STOP) {
//            currentChoiceIndex = BDXHMath.max(BDXHMath.min(currentChoiceIndex, choices.size() - 1), 0);
//        }
//
//    }

//    public Choice currentChoice(){
//        enforceBounds();
//        return choices.get(currentChoiceIndex);
//    }

    public void zone(Vector3f start, Vector3f end){
        areaStart.set(start);
        areaEnd.set(end);
    }

    public boolean on(String choiceName) {
        return activeChoice.name().equals(choiceName);
    }

    public int getChoiceIndex(Choice c){
        return choices.indexOf(c);
    }

}
