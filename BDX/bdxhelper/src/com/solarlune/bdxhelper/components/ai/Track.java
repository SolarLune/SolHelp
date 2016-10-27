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
    private int prevBehaviorIndex;
    private boolean justChanged = true;
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
                justChanged = true;
            }

            justChanged = false;

            currentBehavior.main();

            if (currentBehavior.done()) {

                prevBehaviorIndex = behaviorIndex;

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
                justChanged = true;

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

    public Behavior next() {
        if (behaviorPlayRate > 0) {
            if (behaviorIndex + behaviorPlayRate < size())
                return get(behaviorIndex + behaviorPlayRate);
            else
                return get(behaviorIndex + behaviorPlayRate - size());
        } else {
            if (behaviorIndex + behaviorPlayRate > 0)
                return get(behaviorIndex + behaviorPlayRate);
            else
                return get(behaviorIndex + behaviorPlayRate + size());
        }
    }

    public Behavior prev() {
        if (behaviorPlayRate > 0) {
            if (behaviorIndex - behaviorPlayRate > 0)
                return get(behaviorIndex - behaviorPlayRate);
            else
                return get(behaviorIndex - behaviorPlayRate + size());
        } else {
            if (behaviorIndex - behaviorPlayRate < size())
                return get(behaviorIndex - behaviorPlayRate);
            else
                return get(behaviorIndex - behaviorPlayRate - size());
        }
    }

    public boolean justChanged(){
        return justChanged;
    }

    public boolean atEnd(){
        return behaviorIndex >= size() - 1;
    }

}
