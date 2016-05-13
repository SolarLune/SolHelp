package com.solarlune.bdxhelper.components.ai.behaviors;

import com.badlogic.gdx.utils.JsonValue;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.utils.Color;
import com.nilunder.bdx.utils.Random;
import com.solarlune.bdxhelper.components.ai.Behavior;

import javax.vecmath.Matrix3f;
import javax.vecmath.Vector3f;

/**
 * Created by SolarLuneNew on 4/1/2016.
 */
public class Shoot extends Behavior {

	public String bulletObject;
	public Vector3f bulletDirection;
	public Vector3f spawnPosition;
	public float bulletSpeed;
	public Color bulletColor;
	public String bulletProp;
	public float bulletDeviance;

	private GameObject spawnedBullet;

	public Shoot(GameObject g, String bullet) {
		this(g, bullet, new Vector3f(0, 1, 0), new Vector3f(), 10, new Color(1, 1, 1, 1), null, 0.05f);
	}

	public Shoot(GameObject g, String bullet, Vector3f bulletDirection, Vector3f spawnOffset, float bulletSpeed, Color bulletColor, String prop, float shotDeviance){
		super(g);
		this.bulletObject = bullet;
		this.bulletDirection = bulletDirection;
		this.bulletSpeed = bulletSpeed;
		this.spawnPosition = spawnOffset;
		if (bulletColor == null)
			this.bulletColor = new Color(1, 1, 1, 1);
		else
			this.bulletColor = bulletColor;
		this.bulletProp = prop;
		this.bulletDeviance = shotDeviance;
	}

	public void main(){
		GameObject b = g.scene.add(bulletObject);
		b.position(g.position().plus(spawnPosition));
		b.materials.color(bulletColor);
		for (GameObject c : b.childrenRecursive())
			c.materials.color(bulletColor);
		if (bulletProp != null)
			b.props.put(bulletProp, new JsonValue(true));
		Vector3f vel = bulletDirection.mul(bulletSpeed);
		vel = Matrix3f.rotation(new Vector3f(0, 1, 0), Random.random(-bulletDeviance, bulletDeviance)).mult(vel);
		b.velocity(vel);
		spawnedBullet = b;
	}

	public GameObject getLastBullet(){
		return spawnedBullet;
	}

}
