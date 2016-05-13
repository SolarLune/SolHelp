package com.solarlune.bdxhelper.choice;

import com.nilunder.bdx.Scene;
import com.nilunder.bdx.Text;

import javax.vecmath.Vector3f;

import java.util.ArrayList;

/**
 * Created by SolarLune on 1/28/2015.
 */
public class Screen {

    String name;
    public ArrayList<Choice> choices;
    public boolean active = true;
    int currentChoiceIndex = 0;
	Scene scene;

	Vector3f areaStart = new Vector3f();
	Vector3f areaEnd = new Vector3f();

    public Screen(Scene scene, String name){
        choices = new ArrayList<Choice>();
		this.scene = scene;
    }
    public Screen(Scene scene){
        this(scene, "default");
    }

    public void add(Choice c){
        choices.add(c);
		c.setScreen(this);
    }

	public void setArea(Vector3f startVec, Vector3f endVec){
		areaStart = startVec;
		areaEnd = endVec;
	}

	public void setArea(ArrayList<Vector3f> startAndEnd){
		setArea(startAndEnd.get(0), startAndEnd.get(1));
	}

	public void setArea(float startX, float startY, float startZ, float endX, float endY, float endZ){
		setArea(new Vector3f(startX, startY, startZ), new Vector3f(endX, endY, endZ));
	}

	public void moveArea(Vector3f moveVec){
		areaStart.add(moveVec);
		areaEnd.add(moveVec);
	}

	public ArrayList<Vector3f> getArea(){

		ArrayList<Vector3f> v = new ArrayList<Vector3f>();

		v.add(areaStart);
		v.add(areaEnd);

		return v;

	}

	public void createChoiceText(String textName){

		for (Choice c : choices){

			if (c.getTextMesh() != null){
				c.getTextMesh().end();
				c.setTextMesh(null);
			}

			Text t = (Text) scene.add(textName);

			c.setTextMesh(t);

		}

	}

	public void deleteChoiceText(){

		for (Choice c : choices){

			if (c.getTextMesh() != null) {

				c.getTextMesh().end();
				c.setTextMesh(null);

			}

		}

	}

	public void positionChoiceText(float margin){

		Vector3f areaDiff = areaEnd.minus(areaStart).mul(1.0f / choices.size());

		for (int i = 0; i < choices.size(); i++){

			Choice c = choices.get(i);

			if (c.getTextMesh() != null) {

				Text t = c.getTextMesh();

				if (margin == 0)  // No margin; auto fit
					t.position(areaStart.x + (areaDiff.x * i),
							areaStart.y + (areaDiff.y * i),
							areaStart.z + (areaDiff.z * i));
				else
					t.position(areaStart.x + ((Math.signum(areaDiff.x) * margin) * i),
							areaStart.y + ((Math.signum(areaDiff.y) * margin) * i),
							areaStart.z + ((Math.signum(areaDiff.z) * margin) * i));

			}

		}

	}

	public void positionChoiceText(){
		positionChoiceText(0);
	}


    public void remove(Choice c){
        choices.remove(c);
    }

	public void clearChoices(){
		deleteChoiceText();
		choices.clear();
	}

    public void nextChoice(int skipAhead){
		if (active) {
			currentChoiceIndex += skipAhead;
			enforceBounds();
		}
    }

	public void nextChoice(){
		nextChoice(1);
	}

    public void setChoice(int index){
		if (active) {
			currentChoiceIndex = index;
			enforceBounds();
		}
    }

    public void enforceBounds(){

        if (currentChoiceIndex >= choices.size()){
            currentChoiceIndex -= choices.size();
        }
        if (currentChoiceIndex < 0){
            currentChoiceIndex += choices.size();
        }

    }

    public Choice currentChoice(){
        enforceBounds();
        return choices.get(currentChoiceIndex);
    }

	public int getChoiceIndex(Choice c){
		return choices.indexOf(c);
	}

}
