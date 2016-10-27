package com.solarlune.bdxhelper.components.ai;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;
import com.nilunder.bdx.utils.ArrayListNamed;

import java.util.ArrayList;

public class Director extends Component<GameObject> {

    public ArrayListNamed<Track> tracks = new ArrayListNamed<Track>();

    public Director(GameObject g){
        super(g);
        state = main;
        tracks.add(new Track());
    }

    State main = new State(){

        public void main(){
            for (Track track : tracks) {
                if (track.active)
                    track.main();
            }
        }

    };

    public Track active(){
        Track t = null;
        if (activeTracks().size() > 0)
            t = activeTracks().get(0);
        return t;
    }

    public ArrayList<Track> activeTracks(){
        ArrayList<Track> actives = new ArrayList<Track>();
        for (Track t : tracks) {
            if (t.active)
                actives.add(t);
        }
        return actives;
    }

}
