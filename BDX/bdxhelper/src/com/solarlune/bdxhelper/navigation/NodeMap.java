package com.solarlune.bdxhelper.navigation;

import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.RayHit;
import com.nilunder.bdx.Scene;
import com.solarlune.bdxhelper.API;

import javax.vecmath.Vector3f;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

/**
 * Created by SolarLune on 1/14/2015.
 */
public class NodeMap {

    ArrayList<Node> nodes = new ArrayList<Node>();
    int costNum;

    public NodeMap(int costNum){
        this.costNum = costNum;
    }

    public NodeMap(){
        this(1);
    }

    public void addNode(Node node){

        node.resetCosts(costNum);
        nodes.add(node);

    }

    public void removeNode(Node node){

        nodes.remove(node);

    }

    public void updateNeighbors(float minDist, float maxDist, int maxConnections, boolean noDiagonals, boolean rayTest, Scene scene){

        ArrayList<Node> evaluated = new ArrayList<Node>();

        for (Node n : nodes){

            for (Node m : nodes){

                if (n != m && !evaluated.contains(m)){

                    float dist = (n.getPosition().minus(m.getPosition())).length();

                    if (maxDist >= dist && dist >= minDist){

                        float tooClose = 0.001f;

                        boolean xg = Math.abs(m.getPosition().x - n.getPosition().x) < tooClose;
                        boolean yg = Math.abs(m.getPosition().y - n.getPosition().y) < tooClose;
                        boolean zg = Math.abs(m.getPosition().z - n.getPosition().z) < tooClose;

                        if (!noDiagonals || (noDiagonals && API.atLeastBooleans(2, xg, yg, zg))) {

                            RayHit ray;

                            if (rayTest)
                                ray = scene.ray(n.getPosition(), m.getPosition().minus(n.getPosition()));
                            else
                                ray = null;

                            if (ray == null) {

                                if (n.neighbors.size() < maxConnections && m.neighbors.size() < maxConnections) {

                                    m.neighbors.add(n);
                                    n.neighbors.add(m);

                                }

                            }
                        }

                    }

                }

            }

            evaluated.add(n);

        }

    }

    public Node getClosestNode(final Vector3f position, Scene scene){

        ArrayList<Node> sorted = new ArrayList<Node>();

        Collections.copy(sorted, nodes);

        Collections.sort(sorted, new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2){
                return (int) ((o1.getPosition().minus(position).length() - o2.getPosition().minus(position).length()) * 100000);
            }
        });

        Node closest = null;

        for (Node n : sorted){

            RayHit ray = scene.ray(position, n.getPosition());

            if (ray == null){

                closest = n;
                break;

            }

        }

        return closest;

        //sorted.sort();

    }

    public void debugDraw(Scene scene){

        for (Node n : nodes) {

            for (Node m : n.neighbors) {

                GameObject c = scene.add("Cube");

                c.position(n.getPosition());

                c.alignAxisToVec(1, m.getPosition().minus(n.getPosition()));

                c.scale(1, n.getPosition().minus(m.getPosition()).length(), 1);

            }

        }

    }

}
