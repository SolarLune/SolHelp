package com.solarlune.bdxhelper.components.ai;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;
import com.nilunder.bdx.utils.ArrayListNamed;

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

}
