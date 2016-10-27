package com.solarlune.bdxhelper.components.movement;

import com.nilunder.bdx.Bdx;
import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;

import javax.vecmath.Vector3f;

/**
 * Created by solarlune on 5/7/16.
 */
public class ConstantMotion extends Component<GameObject> {

    Vector3f motion = new Vector3f();

    public ConstantMotion (GameObject g, Vector3f motion) {
        super(g);
        state = main;
        this.motion.set(motion);
    }

    State main = new State(){

        public void main(){
            g.move(motion.mul(Bdx.TICK_TIME));
        }

    };

}
