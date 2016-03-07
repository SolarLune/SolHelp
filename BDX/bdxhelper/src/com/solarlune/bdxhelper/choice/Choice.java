package com.solarlune.bdxhelper.choice;

import com.nilunder.bdx.Text;

/**
 * Created by SolarLune on 1/28/2015.
 */
public class Choice {

    private String name;
	public Screen screen;
	public Text textMesh;

    public Choice(String name){
        setName(name);
    }

	public void setScreen(Screen screen){
		this.screen = screen;
	}

	public Text getTextMesh(){
		return textMesh;
	}

	public void setTextMesh(Text mesh){
		textMesh = mesh;
		setName(name);
	}

	public void setName(String name){

		this.name = name;

		if (textMesh != null){
			if (!textMesh.valid())
				textMesh = null;
			else
				textMesh.text(name); // Update text
		}

	}

	public String getName(){
		return name;
	}

}
