package com.solarlune.bdxhelper.components;

import com.nilunder.bdx.Bdx;
import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;
import com.nilunder.bdx.utils.Color;

/**
 * Created by SolarLune on 2/2/2015.
 */
public class Flash extends Component<GameObject> {

	public Color firstColor;
	public Color secondColor;
	public float flashDuration;
	public float flashTime;

	public Flash(GameObject g, Color firstColor, Color secondColor, float flashDuration){

		super(g);
		state = main;

		this.firstColor = firstColor;  // First color in flash
		this.secondColor = secondColor;  // Second color in flash
		this.flashDuration = flashDuration;  // How long a single "cycle" takes in a flash

	}

	public Flash(GameObject g, Color secondColor){

		this(g, new Color(1, 1, 1, 1), secondColor, 1);

	}

	public State main = new State(){
		public void main() {

			Color c = g.materials.get(0).color();

			float t = 0.5f + (float) Math.sin((flashTime * Math.PI) / flashDuration) * 0.5f;

			c.r = firstColor.r + ((secondColor.r - firstColor.r) * t); // R
			c.g = firstColor.g + ((secondColor.g - firstColor.g) * t); // G
			c.b = firstColor.b + ((secondColor.b - firstColor.b) * t); // B
			c.a = firstColor.a + ((secondColor.a - firstColor.a) * t); // A

			g.materials.color(c);
			
			flashTime += Bdx.TICK_TIME;

		}
	};

}
