package com.solarlune.bdxhelper.components.movement;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;

import javax.vecmath.Vector3f;

/**
 * Created by solarlune on 7/13/16.
 */
public class LockMotion extends Component<GameObject> {

    public String axes;
    public Vector3f lockPosition = new Vector3f();
    public Vector3f lockVelocity = new Vector3f();

    public LockMotion(GameObject g, String axes) {
        super(g);
        this.axes = axes;
        state = mainState;
    }

    public LockMotion(GameObject g) {
        this(g, "y");
    }

    State mainState = new State() {

        public void main() {

            Vector3f vec = g.velocity();
            if (axes.toLowerCase().contains("x"))
                vec.x = lockVelocity.x;
            if (axes.toLowerCase().contains("y"))
                vec.y = lockVelocity.y;
            if (axes.toLowerCase().contains("z"))
                vec.z = lockVelocity.z;
            g.velocity(vec);

            vec = g.position();
            if (axes.toLowerCase().contains("x"))
                vec.x = lockPosition.x;
            if (axes.toLowerCase().contains("y"))
                vec.y = lockPosition.y;
            if (axes.toLowerCase().contains("z"))
                vec.z = lockPosition.z;
            g.position(vec);
        }

    };

}
