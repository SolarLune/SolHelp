package com.solarlune.bdxhelper.components.movement;

import java.util.ArrayList;

import javax.vecmath.Vector3f;

import com.nilunder.bdx.Bdx;
import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.RayHit;
import com.nilunder.bdx.State;
import com.nilunder.bdx.utils.Color;

public class GroundRay extends Component<GameObject> {

	class RayResults {
		ArrayList<RayHit> results = new ArrayList<RayHit>();
		Vector3f offset = new Vector3f();
		Vector3f startPos = new Vector3f();
	}

	public float groundOffset;
	public float rayExtraDistance;
	public boolean snapToGround = true;
	public boolean alignToGround = false;
	public ArrayList<String> ignoredProperties;
	public ArrayList<String> checkedProperties;

	public GameObject hitObject;
	public GameObject lastHitObject;
	public Vector3f hitPosition;
	public Vector3f lastHitPosition;
	public Vector3f hitNormal;
	public Vector3f lastHitNormal;
	public Vector3f down = new Vector3f(0, 0, -1);
	public float minimumEscapeSpeed = 1;
	public boolean debugOn = false;
    public ArrayList<GameObject> castPoints;

	public GroundRay(GameObject g) {
		this(g, 0.05f, 0.05f);
	}
	
	public GroundRay(GameObject g, float rayExtra, float groundOffset) {
		super(g);
		state = main;
		this.rayExtraDistance = rayExtra;
		this.groundOffset = groundOffset;
		ignoredProperties = new ArrayList<String>();
		checkedProperties = new ArrayList<String>();
		ignoredProperties.add("notGround");
        castPoints = new ArrayList<GameObject>();
	}

	State main = new State(){

		public void main() {

			boolean childCasters = false;

			lastHitObject = hitObject;
			lastHitNormal = hitNormal;
			lastHitPosition = hitPosition;

			hitObject = null;

			Vector3f size = g.dimensions();

			float height = size.z / 2;

			float rayDist = rayExtraDistance + (Math.abs(g.velocityLocal().z) * Bdx.TICK_TIME);

			ArrayList<RayResults> allResults = new ArrayList<RayResults>();

			if (castPoints.size() == 0) {
				RayResults r = new RayResults();
				r.startPos = g.position().plus(down.mul(height));
				r.results.addAll(g.scene.xray(g.position().plus(down.mul(height)), down.mul(rayDist)));
				allResults.add(r);
			}
			else {
				childCasters = true;
				for (GameObject castPoint : castPoints){
                    RayResults r = new RayResults();
                    r.startPos = castPoint.position();
                    r.results.addAll(g.scene.xray(castPoint.position(), down.mul(rayDist)));
                    r.offset = g.position().minus(castPoint.position());
                    allResults.add(r);
				}
			}

			g.alignAxisToVec(2, down.negated());

			hitPosition = null;
			hitObject = null;
			hitNormal = null;

			for (RayResults result : allResults) {

				if (debugOn)
					g.scene.drawLine(result.startPos, result.startPos.plus(down.mul(rayDist)), new Color(1, 0, 0, 1));

				for (RayHit ray : result.results) {

					boolean skip = false;

					if (checkedProperties.size() > 0) {
						skip = true;
						for (String propName : checkedProperties)
							if (ray.object.props.containsKey(propName))
								skip = false;
					}
					for (String propName : ignoredProperties){
						if (ray.object.props.containsKey(propName))
							skip = true;
					}
					if (ray.object == g)
						skip = true;

					if (skip)
						continue;

					// Success!

					if (debugOn)
						g.scene.drawLine(result.startPos, result.startPos.plus(down), new Color(0, 1, 0, 1));

					hitObject = ray.object;
					hitPosition = ray.position;
					hitNormal = ray.normal;

					if (g.velocityLocal().z < minimumEscapeSpeed) {

						if (alignToGround)
							g.alignAxisToVec(2, ray.normal);

						if (snapToGround) {
							g.position(ray.position);
							if (childCasters) {
								g.move(result.offset);
								g.move(down.negated().mul(groundOffset));
							} else
								g.move(down.negated().mul(height + groundOffset));
							Vector3f vel = g.velocityLocal();
							vel.z = 0;
							g.velocityLocal(vel);
						}

					}

					break;

				}

				if (hitObject != null)
					break;

			}

		}

	};
	
	public boolean justLanded(){
		return hitObject != null && lastHitObject == null;
	}
	
	public boolean justJumped(){
		return hitObject == null && lastHitObject != null;
	}
	
	public boolean onGround(){
		return hitObject != null;
	}

}
