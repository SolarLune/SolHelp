package com.solarlune.bdxhelper.components.properties;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;

public class TouchDamage extends Component<GameObject> {

    String targetType;
    float attack;

    public TouchDamage(GameObject g, String t, float attack) {
        super(g);
        targetType = t;
        this.attack = attack;
        state = mainState;
    }

    State mainState = new State(){

        public void main(){

            for (GameObject other : g.touchingObjects) {

                if (targetType == null || other.props.containsKey(targetType)) {

                    Gauge health = (Gauge) other.components.get("Health");

                    if (health != null)
                        health.sub(attack);

                }

            }

        }

    };

}
