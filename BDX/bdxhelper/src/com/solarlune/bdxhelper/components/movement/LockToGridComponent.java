package com.solarlune.bdxhelper.components.movement;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;

import javax.vecmath.Vector3f;

/**
 * Created by solarlune on 7/30/16.
 */
public class LockToGridComponent extends Component<GameObject> {

    public GameObject parent;
    public float gridSize = 1;

    public LockToGridComponent(GameObject g) {
        super(g);
        state(mainState);
    }

    State mainState = new State(){

        public void main(){

            Vector3f pos;

            if (parent != null)
                pos = parent.position();
            else
                pos = g.position();

            pos.x = Math.round(pos.x * gridSize) / gridSize;
            pos.y = Math.round(pos.y * gridSize) / gridSize;
            pos.z = Math.round(pos.z * gridSize) / gridSize;
            g.position(pos);
        }

    };

}
