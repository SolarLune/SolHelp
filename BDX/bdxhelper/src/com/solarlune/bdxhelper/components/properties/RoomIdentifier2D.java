package com.solarlune.bdxhelper.components.properties;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.RayHit;
import com.nilunder.bdx.State;

import javax.vecmath.Vector3f;

public class RoomIdentifier2D extends Component<GameObject> {

	public GameObject currentRoom;
	public GameObject pastRoom;
	
	public RoomIdentifier2D(GameObject g) {
		super(g);
		state = mainState;
	}
	
	State mainState = new State(){
		
		public void main(){
            check();
		}
		
	};

    public void check(){
        pastRoom = currentRoom;

        RayHit ray = g.scene.ray(g.position().plus(new Vector3f(0, -50, 0)), new Vector3f(0, 100, 0));

        if (ray != null && ray.object.props.containsKey("room"))
            currentRoom = ray.object;
    }
	
	public boolean changedRooms(){
		return currentRoom != pastRoom;
	}

}
