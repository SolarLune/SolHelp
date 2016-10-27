package com.solarlune.bdxhelper.components.properties;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;
import com.nilunder.bdx.utils.Timer;

/**
 * Created by SolarLuneNew on 3/23/2016.
 */
public class TimedEnd extends Component<GameObject> {

    public Timer timer;

    public TimedEnd(GameObject g, float time){
        super(g);
        timer = new Timer(time);
        state = main;
    }

    State main = new State(){
        public void main(){
            if (timer.done())
                g.end();
        }
    };

}
