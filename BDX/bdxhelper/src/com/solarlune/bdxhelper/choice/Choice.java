package com.solarlune.bdxhelper.choice;

import com.nilunder.bdx.Text;

/**
 * Created by SolarLune on 1/28/2015.
 */
public class Choice {

    private String name;
	public Screen screen;
	public Text textmesh;

    public Choice(String name){
        setName(name);
    }

	public void setScreen(Screen screen){
		this.screen = screen;
	}

	public Text getTextMesh(){
		return textmesh;
	}

	public void setTextMesh(Text mesh){
		textmesh = mesh;
		setName(name);
	}

	public void setName(String name){

		this.name = name;

		if (textmesh != null && !textmesh.valid())
			textmesh = null;

		if (textmesh != null){
			textmesh.set(name); // Update text
		}

	}

	public String getName(){
		return name;
	}

}
