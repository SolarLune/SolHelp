package com.solarlune.bdxhelper.components.mesh;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;

import javax.vecmath.Matrix3f;
import javax.vecmath.Vector3f;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;

/**
 * Created by solarlune on 5/10/16.
 */
public class Trail extends Component<GameObject> {

    private class VertexCollection {

        public float position;
        public ArrayList<Integer> indices;

        public VertexCollection(float position){
            this.position = position;
            indices = new ArrayList<Integer>();
        }

    }

    private class PosOriPair {

        Vector3f position;
        Matrix3f orientation;

        public PosOriPair(Vector3f position, Matrix3f orientation){
            this.position = position;
            this.orientation = orientation;
        }

        public String toString(){
            return position.toString();
        }

    }

    HashMap<Integer, Vector3f> vertOffsets;
    ArrayList<VertexCollection> vertPairs;
    ArrayList<PosOriPair> targetPositions;

    public boolean stretch = false;                  // If the trail should stretch (difference between a lightcycle trail and a cape)
    public int spacing = 3;                         // Number of frames between the movement and the vertex update
    public boolean reverse = false;                 // If the trail should reverse its movements (i.e. when a sword swings left, the trail swings left too)
    public String axis = "y";                       // The axis the vertices align on
    public boolean updateOnlyWhenMoving = false;    // If the trail should only update if its owning object moves
    public GameObject target = null;                // What object the trail follows. The trail should not be parented to this object.
    public int materialIndex = 0;

    Vector3f targetPastPos = new Vector3f();
    Matrix3f targetPastOri = new Matrix3f();

    public Trail(GameObject g, GameObject target, String axis){
        super(g);
        this.axis = axis;
        this.target = target;
        state(main);

    }

    State main = new State(){

        public void enter(){

            vertOffsets = new HashMap<Integer, Vector3f>();

            for (int i = 0; i < g.mesh.getVertexCount(materialIndex); i++)
                vertOffsets.put(i, g.mesh.vertPos(materialIndex, i));

            vertPairs = new ArrayList<VertexCollection>();

            HashMap<Float, ArrayList<Integer>> vp = new HashMap<Float, ArrayList<Integer>>();

            for (int i = 0; i < g.mesh.getVertexCount(materialIndex); i++) {
                float vertPos;
                if (axis.toLowerCase().equals("x"))
                    vertPos = Math.round(g.mesh.vertPos(materialIndex, i).x * 100.0f) / 100.0f;
                else if (axis.toLowerCase().equals("y"))
                    vertPos = Math.round(g.mesh.vertPos(materialIndex, i).y * 100.0f) / 100.0f;
                else
                    vertPos = Math.round(g.mesh.vertPos(materialIndex, i).z * 100.0f) / 100.0f;

                if (!vp.containsKey(vertPos))
                    vp.put(vertPos, new ArrayList<Integer>());

                vp.get(vertPos).add(i);

            }

            for (float axisValue : vp.keySet()){
                VertexCollection ax = new VertexCollection(axisValue);
                ax.indices.addAll(vp.get(axisValue));
                vertPairs.add(ax);
            }

            vertPairs.sort(new Comparator<VertexCollection>() {
                @Override
                public int compare(VertexCollection o1, VertexCollection o2) {
                    if (o1.position > o2.position)
                        return -1;
                    else
                        return 1;
                }
            });

            Collections.reverse(vertPairs);

            targetPositions = new ArrayList<PosOriPair>();

            for (int x = 0; x < vertPairs.size() * spacing; x++)
                targetPositions.add(new PosOriPair(g.position(), g.orientation()));

        }

        public void main(){

            if (g.parent() != target) {
                g.position(target.position());
                g.orientation(target.orientation());
            }

            boolean insert = false;

            if (!updateOnlyWhenMoving)
                insert = true;
            else {
                float posDiff = target.position().minus(targetPastPos).length();
                Matrix3f ori = target.orientation();
                ori.sub(targetPastOri);
                float oriDiff = ori.getScale();
                float thresh = 0.0001f;
                if (posDiff > thresh || oriDiff > thresh)
                    insert = true;
            }

            if (insert)
                targetPositions.add(new PosOriPair(new Vector3f(target.position()), new Matrix3f(target.orientation())));

            if (targetPositions.size() > vertPairs.size() * spacing)
                targetPositions.remove(0);

            Vector3f diff;
            Matrix3f invTargetOri = new Matrix3f(target.orientation());
            invTargetOri.invert();

            for (int x = 0; x < vertPairs.size(); x++) {

                ArrayList<Integer> verts = vertPairs.get(x).indices;

                if (targetPositions.size() > x * spacing){

                    Vector3f pos = targetPositions.get(x * spacing).position;
                    Matrix3f ori = targetPositions.get(x * spacing).orientation;
                    Matrix3f oriInverted = new Matrix3f(ori);
                    oriInverted.invert();

                    for (int v : verts) {

                        if (!reverse) {

                            if (stretch) {
                                diff = ori.mult(pos.minus(target.position()));
                                g.mesh.vertPos(materialIndex, v, target.orientation().mult(vertOffsets.get(v).plus(diff)));
                            }
                            else
                                g.mesh.vertPos(materialIndex, v, target.orientation().mult(vertOffsets.get(v)));

                            Vector3f vPos = g.mesh.vertPos(materialIndex, v);
                            g.mesh.vertPos(materialIndex, v, oriInverted.mult(vPos));

                        }
                        else {

                            if (stretch) {
                                diff = ori.mult(pos.minus(target.position()));
                                g.mesh.vertPos(materialIndex, v, invTargetOri.mult(vertOffsets.get(v).plus(diff)));
                            }
                            else
                                g.mesh.vertPos(materialIndex, v, invTargetOri.mult(vertOffsets.get(v)));

                            Vector3f vPos = g.mesh.vertPos(materialIndex, v);
                            g.mesh.vertPos(materialIndex, v, ori.mult(vPos));

                        }

                    }

                }

            }

            targetPastOri = new Matrix3f(target.orientation());
            targetPastPos = new Vector3f(target.position());

        }

    };



}


