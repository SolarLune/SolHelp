package com.solarlune.bdxhelper.components.movement;

import java.util.ArrayList;

import javax.vecmath.Matrix3f;
import javax.vecmath.Vector3f;

import com.nilunder.bdx.Bdx;
import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.RayHit;
import com.nilunder.bdx.State;

public class GroundRay extends Component<GameObject> {

	public GameObject groundObj;
	public GameObject lastGroundObj;
	
	public GroundRay(GameObject g) {
		super(g);
		state = main;
	}
	
	State main = new State(){
		
		public void main(){
		
			lastGroundObj = groundObj;
			groundObj = null;
			Vector3f down = g.scene.gravity();
			down.normalize();
			
			Matrix3f inv = g.orientation();
			inv.negate();
			Vector3f height = inv.mult(g.dimensions());
			height.absolute();
						
			float rayDist = height.z / 2 + 0.1f + (Math.abs(g.velocityLocal().z) * Bdx.TICK_TIME);
						
			ArrayList<RayHit> rays = g.scene.xray(g.position(), down.mul(rayDist));
			
			for (RayHit ray : rays){
			
				if (!ray.object.props.containsKey("noGround")) {
					
					if (g.velocityLocal().z < 1) {
						
						g.position(ray.position);
												
						g.move(down.negated().mul(height.z / 2));
						
						if (ray.object.props.containsKey("ramp"))
							g.move(down.negated().mul(0.05f));
						
						Vector3f vel = g.velocityLocal();
						vel.z = 0;
						g.velocityLocal(vel);
						
						groundObj = ray.object;
											
					}
										
					break;
									
				}
			
			}
			g.alignAxisToVec(2, down.negated());
						
		}
		
	};
	
	public boolean justLanded(){
		return groundObj != null && lastGroundObj == null;
	}
	
	public boolean justJumped(){
		return groundObj == null && lastGroundObj != null;
	}
	
	public boolean onGround(){
		return groundObj != null;
	}
	
}
