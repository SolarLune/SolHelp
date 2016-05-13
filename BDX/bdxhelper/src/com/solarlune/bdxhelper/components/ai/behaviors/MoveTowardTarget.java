package com.solarlune.bdxhelper.components.ai.behaviors;

import com.nilunder.bdx.GameObject;
import com.solarlune.bdxhelper.components.ai.Behavior;

import javax.vecmath.Vector3f;

/**
 * Created by SolarLuneNew on 4/1/2016.
 */
public class MoveTowardTarget extends Behavior {

	public GameObject target;
	public float acceleration;
	public float maxSpeed;
	public float minDistance;
	public float maxDistance;

	public MoveTowardTarget(GameObject g, GameObject target){
		this(g, target, 0.1f, 4.0f, 0, 0);
	}

	public MoveTowardTarget(GameObject g, GameObject target, float acceleration, float maxSpeed, float minDistance, float maxDistance) {
		super(g);
		this.target = target;
		this.acceleration = acceleration;
		this.maxSpeed = maxSpeed;
		this.minDistance = minDistance;
		this.maxDistance = maxDistance;
	}

	public void main(){

		if (target != null) {

			Vector3f vect = new Vector3f();

			if (target.position().minus(g.position()).length() > maxDistance)
				vect.set(target.position().minus(g.position()));

			if (target.position().minus(g.position()).length() < minDistance)
				vect.set(g.position().minus(target.position()));

			vect.z = 0;

			vect.length(maxSpeed);

			vect = g.velocity().plus(vect.minus(g.velocity()).mul(acceleration));
			vect.z = 0;
			vect.length(Math.min(vect.length(), maxSpeed));
			vect.z = g.velocity().z;

			g.velocity(vect);

		}
	}

}
