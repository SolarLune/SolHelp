package com.solarlune.bdxhelper.components;

import com.nilunder.bdx.Bdx;
import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;

import javax.vecmath.Vector4f;

/**
 * Created by SolarLune on 2/2/2015.
 */
public class Flash extends Component {

	Vector4f firstColor;
	Vector4f secondColor;
	float flashTime;

	public Flash(GameObject g, Vector4f firstColor, Vector4f secondColor, float flashTime){

		super(g);
		state = main;

		this.firstColor = firstColor;
		this.secondColor = secondColor;
		this.flashTime = flashTime;

	}

	public Flash(GameObject g, Vector4f secondColor){

		this(g, new Vector4f(1, 1, 1, 1), secondColor, 1);

	}

	public State main = new State(){
		public void main() {

			Vector4f c = g.color();

			float t = 0.5f + (float) Math.sin((Bdx.time * Math.PI) * flashTime) * 0.5f;

			c.x = firstColor.x + ((secondColor.x - firstColor.x) * t); // R
			c.y = firstColor.y + ((secondColor.y - firstColor.y) * t); // G
			c.z = firstColor.z + ((secondColor.z - firstColor.z) * t); // B
			c.w = firstColor.w + ((secondColor.w - firstColor.w) * t); // A

			g.color(c);

		}
	};

}
