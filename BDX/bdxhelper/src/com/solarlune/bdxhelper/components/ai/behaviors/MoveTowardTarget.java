package com.solarlune.bdxhelper.components.ai.behaviors;

import com.nilunder.bdx.GameObject;
import com.solarlune.bdxhelper.components.ai.Behavior;

import javax.vecmath.Vector3f;

public class MoveTowardTarget extends Behavior {

    public GameObject targetObject;
    public Vector3f targetPosition;
    public float acceleration;
    public float maxSpeed;
    public float minDistance;
    public float maxDistance;
    public String moveAxes;

    public MoveTowardTarget(GameObject g, GameObject target){
        this(g, target, 0.1f, 4.0f, 0, 0);
    }

    public MoveTowardTarget(GameObject g, GameObject target, float acceleration, float maxSpeed, float minDistance, float maxDistance) {
        super(g);
        this.targetObject = target;
        this.acceleration = acceleration;
        this.maxSpeed = maxSpeed;
        this.minDistance = minDistance;
        this.maxDistance = maxDistance;
        targetPosition = new Vector3f(0, 0, 0);
        moveAxes = "xyz";
    }

    public void main(){

        Vector3f targetPosition = null;
        String axes = moveAxes.toLowerCase();

        if (targetObject != null)
            targetPosition = targetObject.position();
        else
            targetPosition = this.targetPosition;

        if (targetPosition != null) {

            Vector3f vect = new Vector3f();

            if (targetPosition.minus(g.position()).length() > maxDistance)
                vect.set(targetPosition.minus(g.position()));

            if (targetPosition.minus(g.position()).length() < minDistance)
                vect.set(g.position().minus(targetPosition));

            if (!axes.contains("x"))
                vect.x = 0;
            if (!axes.contains("y"))
                vect.y = 0;
            if (!axes.contains("z"))
                vect.z = 0;

            if (vect.length() > 0)
                vect.length(maxSpeed);

            vect = g.velocity().plus(vect.minus(g.velocity()).mul(acceleration));

            if (!axes.contains("x"))
                vect.x = 0;
            if (!axes.contains("y"))
                vect.y = 0;
            if (!axes.contains("z"))
                vect.z = 0;

            if (vect.length() > 0)
                vect.length(Math.min(vect.length(), maxSpeed));

            if (!axes.contains("z"))
                vect.z = g.velocity().z;

            g.velocity(vect);

        }

    }

    public boolean tooFar(){
        Vector3f targetPos;
        if (targetObject != null)
            targetPos = targetObject.position();
        else
            targetPos = targetPosition;
        return targetPos.minus(g.position()).length() > maxDistance;
    }

    public boolean tooClose(){
        Vector3f targetPos;
        if (targetObject != null)
            targetPos = targetObject.position();
        else
            targetPos = targetPosition;
        return targetPos.minus(g.position()).length() < minDistance;
    }

}
