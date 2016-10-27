package com.solarlune.bdxhelper.components.particles;

import javax.vecmath.Vector3f;

import com.nilunder.bdx.Bdx;
import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;
import com.nilunder.bdx.utils.Color;
import com.nilunder.bdx.utils.Timer;
import com.solarlune.bdxhelper.utils.BDXHMath;

public class Particle extends Component<GameObject> {

    public Emitter system;

    public Vector3f velocity;

    public float lifeTime;

    private Timer lifeTimer;

    public Particle(GameObject g, Emitter s, float lifeTime) {
        super(g);
        system = s;
        state = mainState;
        this.lifeTime = lifeTime;
        lifeTimer = new Timer(lifeTime);
        velocity = new Vector3f();
    }

    State mainState = new State(){

        public void main(){

            velocity.add(system.gravityDirection.mul(Bdx.TICK_TIME));

            if (velocity.length() > system.friction) {
                Vector3f neg = velocity.negated();
                velocity.add(neg.mul(system.friction));
            }
            else
                velocity.length(0);

            Vector3f vel = new Vector3f(velocity);
            vel.add(system.windDirection);

            g.move(vel.mul(Bdx.TICK_TIME));

            if (lifeTimer.done()) {
                g.end();
                system.particles.remove(g);
            }
            else {

                float lifePercent = (lifeTime - lifeTimer.timeLeft()) / lifeTime;

                if (system.colorStages.size() > 0) {

                    int stageNum = system.colorStages.size() - 1;
                    int currentStage = java.lang.Math.min((int) java.lang.Math.floor(stageNum * lifePercent), system.colorStages.size() - 1);

                    Color currentColor = system.colorStages.get(currentStage);
                    Color nextColor = currentColor;

                    float stagePercent = (lifePercent * stageNum) - currentStage;

                    if (system.colorStages.size() > currentStage + 1)
                        nextColor = system.colorStages.get(currentStage + 1);

                    Color c = new Color();
                    c.a = BDXHMath.lerp(currentColor.a, nextColor.a, stagePercent);
                    c.r = BDXHMath.lerp(currentColor.r, nextColor.r, stagePercent);
                    c.g = BDXHMath.lerp(currentColor.g, nextColor.g, stagePercent);
                    c.b = BDXHMath.lerp(currentColor.b, nextColor.b, stagePercent);

                    g.mesh().materials.color(c);

                }

            }

        }

    };

}
