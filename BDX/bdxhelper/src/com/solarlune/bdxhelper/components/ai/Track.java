package com.solarlune.bdxhelper.components.ai;

import com.nilunder.bdx.utils.Named;
import com.nilunder.bdx.utils.Random;

import java.util.ArrayList;

/**
 * Created by SolarLuneNew on 4/1/2016.
 */
public class Track extends ArrayList<Behavior> implements Named {

	public enum TrackPlay {
		NORMAL,
		CHOOSE
	}

	public enum TrackEnd {
		LOOP,
		PINGPONG,
		STOP
	}

	public int behaviorIndex;
	public TrackPlay playMode = TrackPlay.NORMAL;
	public TrackEnd onEnd = TrackEnd.LOOP;
	public int behaviorPlayRate = 1;
	public boolean playing = true;
	public boolean active = true;
	public String name;

	public Behavior currentBehavior;

	public boolean add(Behavior... behaviors){
		for (Behavior b : behaviors)
			add(b);
		return true;
	}

	public Track(String name){
		this.name = name;
	}

	public Track(){
		this("default");
	}

	public void main(){

		if (size() > 0 && playing) {

			if (currentBehavior != this.get(behaviorIndex)) {
				currentBehavior = this.get(behaviorIndex);
				currentBehavior.enter();
			}

			currentBehavior.main();

			if (currentBehavior.done()) {

				if (playMode == TrackPlay.NORMAL)
					behaviorIndex += behaviorPlayRate;
				else if (playMode == TrackPlay.CHOOSE)
					behaviorIndex = (int) Random.random(0, size());

				currentBehavior.exit();

				if (onEnd == TrackEnd.LOOP) {
					loopIndex();
				}
				else if (onEnd == TrackEnd.PINGPONG) {
					capIndex();
					if (behaviorIndex >= size() || behaviorIndex < 0)
						behaviorPlayRate = -behaviorPlayRate;
				}
				else if (onEnd == TrackEnd.STOP) {
					capIndex();
					playing = false;
				}

				currentBehavior = this.get(behaviorIndex);
				currentBehavior.enter();

			}

		}

	}

	private void loopIndex(){
		while (behaviorIndex >= size())
			behaviorIndex -= size();
		while (behaviorIndex < 0)
			behaviorIndex += size();
	}

	private void capIndex(){
		behaviorIndex = Math.max(0, Math.min(size() - 1, behaviorIndex));
	}

	public String name(){
		return name;
	}

}
