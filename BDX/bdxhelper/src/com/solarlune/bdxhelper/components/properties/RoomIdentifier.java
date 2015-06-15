package com.solarlune.bdxhelper.components.properties;

import java.util.ArrayList;

import javax.vecmath.Vector3f;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.RayHit;
import com.nilunder.bdx.State;
import com.solarlune.nmsgamejam.GlobalGame;

public class RoomIdentifier extends Component<GameObject> {

	public GameObject room;
	public GameObject pastRoom;
	
	public RoomIdentifier(GameObject g) {
		super(g);
		state = mainState;
	}
	
	State mainState = new State(){
		
		public void main(){
			
			pastRoom = room;
			
			ArrayList<RayHit> rays = g.scene.xray(g.position(), g.scene.gravity().mul(100));
			
			for (RayHit ray : rays) {
			
				if (ray.object.props.containsKey("room")) {
					room = ray.object;
					break;
				}
				
			}

		}
		
	};
	
	public boolean changedRooms(){
		return room != pastRoom;
	}

}
