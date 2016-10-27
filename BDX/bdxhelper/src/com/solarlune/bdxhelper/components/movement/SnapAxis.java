package com.solarlune.bdxhelper.components.movement;

import javax.vecmath.Vector3f;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;

public class SnapAxis extends Component<GameObject> {

    int axis;
    float snapTo;

    public SnapAxis(GameObject g, int axis, float snapTo) {
        super(g);
        state = mainState;
        this.axis = axis;
        this.snapTo = snapTo;
    }

    State mainState = new State(){

        public void main(){

            Vector3f pos = g.position();

            if (axis == 0)
                pos.x = snapTo;
            else if (axis == 1)
                pos.y = snapTo;
            else
                pos.z = snapTo;

            g.position(pos);

        }

    };

}
