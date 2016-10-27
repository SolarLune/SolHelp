package com.solarlune.bdxhelper.components.properties;

import com.badlogic.gdx.utils.JsonValue;
import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;

import java.util.ArrayList;
import java.util.HashMap;

/**
 * Created by solarlune on 8/2/16.
 */

public class TeamComponent extends Component<GameObject> {

    static HashMap<String, ArrayList<GameObject>> teamCollection;

    String team;

    public TeamComponent(GameObject g, String team){
        super(g);
        this.team = team;
        if (teamCollection == null)
            teamCollection = new HashMap<String, ArrayList<GameObject>>();
    }

    public State mainState = new State(){

        public void enter() {
            if (!teamCollection.containsKey(team))
                teamCollection.put(team, new ArrayList<GameObject>());
            teamCollection.get(team).add(g);
            g.props.put("team-"+team, new JsonValue(true));
        }

        public void exit() {
            teamCollection.get(team).remove(g);
            g.props.remove("team-"+team);
        }
    };

}
