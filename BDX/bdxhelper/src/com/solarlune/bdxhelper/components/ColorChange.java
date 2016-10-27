package com.solarlune.bdxhelper.components;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;
import com.nilunder.bdx.utils.Color;
import com.nilunder.bdx.utils.Timer;

import java.util.ArrayList;
import java.util.Collections;

/**
 * Created by SolarLune on 2/2/2015.
 */
public class ColorChange extends Component<GameObject> {

    public enum FinishStrategy {
        PING_PONG,       // A > B > A > B > A ...
        END,            // A > B, Turn off
        LOOP,           // A > B, A > B, A > B...
    }

    public ArrayList<Color> colors = new ArrayList<Color>();
    public Timer changeTimer = new Timer();
    public FinishStrategy onFinish = FinishStrategy.PING_PONG;
    public boolean on = false;
    int colorIndex = 0;
    int playDir = 1;
    private boolean completedCycle = false;

    public ColorChange(GameObject g){
        super(g);
        state(mainState);
    }

    State mainState = new State(){

        public void main(){

            completedCycle = false;

            if (on && colors.size() > 1) {

                g.visibleNoChildren(true);

                if (changeTimer.done()) {

                    if (colorIndex + playDir > 1 && colorIndex + playDir < colors.size() - 1) {
                        colorIndex += playDir;
                        changeTimer.restart();
                    } else {

                        if (onFinish == FinishStrategy.LOOP) {
                            changeTimer.restart();
                            colorIndex = 0;
                            completedCycle = true;
                        }
                        else if (onFinish == FinishStrategy.PING_PONG) {
                            colorIndex += playDir;
                            playDir *= -1;
                            changeTimer.restart();
                            if (colorIndex == 0)
                                completedCycle = true;

                        } else if (onFinish == FinishStrategy.END) {
                            on = false;
                            colorIndex = 0;
                            completedCycle = true;
                        }

                    }

                }

                Color startingColor = colors.get(colorIndex);
                Color targetColor = colors.get(colorIndex + playDir);

                Color c = new Color(startingColor);
                c.lerp(targetColor, 1 - (changeTimer.timeLeft() / changeTimer.interval));
                g.mesh().materials.get(0).color(c);

            }

        }

    };

    public void glow(float time, Color... colors){

        this.colors.clear();

        Collections.addAll(this.colors, colors);

        on = true;

        colorIndex = 0;

        changeTimer.set(time);

    }

    public void glow() {
        glow(1, g.mesh().materials.get(0).color(), new Color(1, 1, 1, 1));      // Just a quick default to try
    }

    public void flash(Color targetColor){
        onFinish = FinishStrategy.END;
        glow(1, new Color(), targetColor);
        changeTimer.done(true);
    }

    public void flash(){
        if (g.mesh().materials.get(0).color().a <= 0.5f)
            flash(new Color(1, 1, 1, 1));
        else
            flash(new Color(1, 1, 1, 0));
    }

    public boolean completedCycle(){
        return completedCycle;
    }

}
