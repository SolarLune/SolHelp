package com.solarlune.bdxhelper.navigation;

import com.nilunder.bdx.RayHit;
import com.nilunder.bdx.Scene;
import com.nilunder.bdx.utils.*;
import com.solarlune.bdxhelper.utils.API;

import javax.vecmath.Vector3f;

import java.util.*;

/**
 * Created by SolarLune on 1/14/2015.
 */
public class NodeMap {

    public class Path extends ArrayList<Node>{

        public int index = 0;
        public int prevIndex = 0;
        public boolean reversed = false;

        public Path(ArrayList<Node> path) {
            super(path);
        }

        public Node get(int index){
            return super.get(enforceEdges(index));
        }

        public Node current(){
            return get(index);
        }

        public void setNext(){
            set(index + 1);
        }

        public void setPrev(){
            set(index - 1);
        }

        public Node next(){
            return get(index + 1);
        }

        public Node prev(){
            return get(index - 1);
        }

        public void set(int step){
            prevIndex = index;
            index = enforceEdges(step);
        }

        public int enforceEdges(int i){
            return Math.max(Math.min(i, size() - 1), 0);
        }

        public boolean atEnd(){
            return (index >= size() - 1 && !reversed) || (index == 0 && reversed);
        }

        public boolean atStep(Vector3f position, int step, Vector3f margins){

            Vector3f diff = position.minus(get(step).position());
            diff.x = Math.abs(diff.x);
            diff.y = Math.abs(diff.y);
            diff.z = Math.abs(diff.z);

            return diff.x < margins.x && diff.y < margins.y && diff.z < margins.z;
        }

        public boolean atStep(Vector3f position, float margin){
            return atStep(position, index, new Vector3f(margin, margin, margin));
        }

        public boolean atStep(Vector3f position, Vector3f margins){
            return atStep(position, index, margins);
        }

        public void addCost(int cost){
            for (Node n : this)
                n.cost(n.cost() + cost);
        }

        public void setCost(int cost){
            for (Node n : this)
                n.cost(cost);
        }

        public void resetCost(){
            for (Node n : this)
                n.cost(0);
        }

        public void reverse(){
            Collections.reverse(this);
            reversed = !reversed;
        }

        public void resetPath(){
            if (reversed)
                Collections.reverse(this);
            reversed = false;
            set(0);
        }

        public void debugDraw(){

            for (int i = 0; i < size(); i++) {

                Node point = get(i);
                Node nextPoint = get(i + 1);

                Vector3f[] xy = new Vector3f[]{
                        new Vector3f(-0.25f, 0, 0),
                        new Vector3f(0, 0.25f, 0),
                        new Vector3f(0.25f, 0, 0),
                        new Vector3f(0, -0.25f, 0),
                        new Vector3f(0, 0, 0.25f),
                        new Vector3f(0, 0, -0.25f)};

                for (Vector3f v : xy)
                    scene.drawLine(point.position(), point.position().plus(v), new Color(0, 0, 1, 1));

                if (nextPoint != null)
                    scene.drawLine(point.position(), nextPoint.position(), new Color(0, 1, 0, 1));

            }

        }

    }

    public class Node {

        public ArrayList<Node> neighbors;
        public Node parent;
        public float gCost;
        public HashMap<String, String> tags;

        private Vector3f position;
        private float cost = 0;

        public Node(Vector3f position){
            neighbors = new ArrayList<Node>();
            this.position = position;
            parent = null;
            tags = new HashMap<String, String>();
        }

        public Vector3f position(){
            return position;
        }
        public void position(Vector3f pos){
            position = pos;
        }
        public String toString() {
            return "Node: " + position.toString() + ":" + String.valueOf(hashCode());
        }
        public void cost(float value){
            cost = value;
        }
        public float cost(){
            return cost;
        }

    }

    public class Options {

        public float minDist;
        public float maxDist;
        public boolean onlyStraight;
        public String[] rayBlockingProperties;
        public String[] ignoreTags;

        public Options(float minDist, float maxDist, boolean onlyStraight, String[] rayBlockingProperties, String[] ignoreTags){
            this.minDist = minDist;
            this.maxDist = maxDist;
            this.onlyStraight = onlyStraight;
            this.rayBlockingProperties = rayBlockingProperties;
            this.ignoreTags = ignoreTags;
        }

        public Options(){
            this(0, 0, false, new String[]{}, new String[]{});
        }

    }

    public ArrayList<Node> nodes = new ArrayList<Node>();
    public boolean dirty = false;       // If the node map has been altered since neighbors have been calculated
    public Options defaultOptions = new Options();

    private Scene scene;                 // Which scene the NodeMap belongs to
    private Color debugLineColor = new Color(0, 0, 1, 1);
    private Color debugNodeColor = new Color(0, 1, 0, 1);

    public NodeMap(Scene scene){
        this.scene = scene;
    }

    public Scene scene(){
        return scene;
    }

    public void addNode(Node node) {
        nodes.add(node);
        dirty = true;
    }

    public Node addNode(Vector3f position){
        Node n = new Node(position);
        addNode(n);
        return n;
    }

    public void removeNode(Node node){
        nodes.remove(node);
        dirty = true;
    }

    public void removeNode(Vector3f position){
        Node n = null;
        for (Node n2 : nodes) {
            if (n2.position() == position) {
                n = n2;
                break;
            }
        }
        if (n != null)
            removeNode(n);
        else
            System.out.println("Couldn't find node at position: " + position);
    }
    
    public Node getNode(Vector3f position){

        Node ret = null;

        for (Node n : nodes) {

            if (n.position().equals(position))

                ret = n;

        }

        return ret;

    }

    public ArrayList<Node> getNodesByTag(ArrayList<Node> nodes, String tagName){

        ArrayList<Node> newList = new ArrayList<Node>();

        for (Node n : nodes) {
            if (n.tags.containsKey(tagName))
                newList.add(n);
        }

        return newList;

    }

    public ArrayList<Node> getNodesByTag(String tagName){
        return getNodesByTag(nodes, tagName);
    }

    public void clearNeighbors(ArrayList<Node> nodes){
        for (Node n : nodes)
            n.neighbors.clear();
    }

    public void clearNeighbors(){
        clearNeighbors(nodes);
    }

    public void updateNeighbors(ArrayList<Node> nodeList, Options options){

        // Updates the neighbor relationships for each node in the NodeMap. Sets the dirty flag to be false, indicating
        // The NodeMap is up-to-date.

        // minDist = The minimum distance Nodes have to be in order to be neighbors. Too close, and they won't be.

        // maxDist = The maximum distance away Nodes have to be in order to be neighbors.

        // onlyStraight = Whether Nodes only can lie on a straight line to be neighbors. Useful for grid-based layouts.

        // rayBlockingProperties... By default, nodes are considered neighbors by simply their location. If you supply a string (or series of strings),
        // the function will cast rays to determine if obstructing objects lie on the path between nodes.
        // Whatever the strings you supply, objects must have a property of one of those names and be between nodes to be considered obstructing.
        // If the string is an asterisk ("*"), then any hits are valid, and the objects don't have to have any particular properties.

        dirty = false;

        ArrayList<Node> evaluated = new ArrayList<Node>();

        for (Node n : nodeList){

            for (Node m : nodeList){

                if (n != m && !evaluated.contains(m)){

                    float dist = (n.position().minus(m.position())).length();

                    if ((options.maxDist >= dist || options.maxDist == 0) && dist >= options.minDist){

                        float tooClose = 0.001f;

                        boolean xg = Math.abs(m.position().x - n.position().x) < tooClose;
                        boolean yg = Math.abs(m.position().y - n.position().y) < tooClose;
                        boolean zg = Math.abs(m.position().z - n.position().z) < tooClose;

                        if (!options.onlyStraight || API.atLeastBooleans(2, xg, yg, zg)) {   // The nodes lie on a straight line from each other

                            boolean blocked = false;
                            
                            if (options.rayBlockingProperties.length > 0) {
                                
                                ArrayList<RayHit> rays = scene.xray(n.position(), m.position().minus(n.position()));

                                for (RayHit ray : rays) {

                                    for (String p : options.rayBlockingProperties) {
                                        if (ray.object.props.containsKey(p) || p.equals("*")) {
                                            blocked = true;
                                            break;
                                        }
                                    }

                                }
                                
                            }
             
                            if (!blocked) {

                                m.neighbors.add(n);
                                n.neighbors.add(m);
                               
                            }

                        }

                    }

                }

            }

            evaluated.add(n);

        }

    }

    public void updateNeighbors() {
        updateNeighbors(nodes, defaultOptions);
    }

    private Node nc(final Vector3f position, final int gcn, final Options options){

        // Compares the nodes in the map to find the closest or furthest one from to the position (depending on gcn's value, whether positive or negative),
        // And casts rays to determine if the nodes found, if given properties other than "". "*" is a wildcard property name (any property can trigger this)
        //

        ArrayList<Node> sorted = new ArrayList<Node>(nodes);

        Collections.sort(sorted, new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2){

                for (String t : options.ignoreTags){
                    if (o1.tags.containsKey(t))        // Adding in tag searching (closest node of "X" tag)
                        return gcn;
                }

                if (o1.position().minus(position).length() < o2.position().minus(position).length())
                    return -gcn;        // Determines if you're looking for the closest node, or furthest node from a point
                return gcn;             // gcn of 1 = closest node, gcn of -1 = furthest node
                                        // 10/2016 SolarLune: I think gcn stands for "get closest node". Poor name.
            }
        });
 
        Node closest;
        
        if (options.rayBlockingProperties.length > 0) {

            closest = null;

            for (Node n : sorted){

                ArrayList<RayHit> rays = scene.xray(position, n.position().minus(position));

                closest = n;

                if (rays.size() == 0)
                    break;

                boolean blocked = false;

                for (RayHit r : rays) {

                    for (String p : options.rayBlockingProperties) {

                        if (r.object.props.containsKey(p) || (p.equals("*"))) {

                            closest = null;
                            blocked = true;
                            break;

                        }

                    }

                    if (blocked)
                        break;

                }

                if (blocked)
                    break;

            }
        
        }
        
        else

            closest = sorted.get(0);

        return closest;

    }

    public Node getClosestNode(final Vector3f position, Options options) {
        return nc(position, 1, options);
    }

    public Node getClosestNode(final Vector3f position){
        return getClosestNode(position, defaultOptions);
    }

    public Node getFurthestNode(final Vector3f position, Options options) {
        return nc(position, -1, options);
    }

    public Node getFurthestNode(final Vector3f position){
        return getFurthestNode(position, defaultOptions);
    }

    public Path getPathTo(final Node goal, final Node start, int maxCheckNum){

        ArrayList<Node> openList = new ArrayList<Node>();       // Moving to basic ArrayLists because LinkedLists aren't supported by GWT (?)
        openList.add(start);

        ArrayList<Node> closedList = new ArrayList<Node>();

        boolean exitLoop = false;
        boolean pathFound = false;

        for (Node n : nodes)
            n.gCost = 0;

        if (goal == start) {
            pathFound = true;
            exitLoop = true;
        }

        for (int i = 0; i < maxCheckNum; i++) {

            Collections.sort(openList, new Comparator<Node>() {
                @Override
                public int compare(Node n1, Node n2) {
                    float n1Dist = n1.gCost + n1.position().minus(goal.position()).length() - n2.cost();
                    float n2Dist = n2.gCost + n2.position().minus(goal.position()).length() - n1.cost();

                    if (n1Dist < n2Dist)
                        return -1;
                    return 1;
                }
            });

            if (openList.size() > 0) {

                Node current = openList.remove(0);

                closedList.add(current);

                for (Node neighbor : current.neighbors) {

                    if (closedList.contains(neighbor))
                        continue;

                    if (!openList.contains(neighbor)) {

                        neighbor.parent = current;

                        neighbor.gCost = current.gCost + (neighbor.position().minus(current.position()).length());

                        openList.add(neighbor);

                        if (neighbor.equals(goal)) {

                            exitLoop = true;
                            pathFound = true;

                            break;

                        }

                    }

                }

            }

            else {

                exitLoop = true;
                pathFound = false;
                //System.out.println("PATHFINDING ERROR: Can't get to goal. Are all nodes in node-map connected?");
            }

            if (exitLoop)
                break;

        }

        if (pathFound) {

            ArrayList<Node> path = new ArrayList<Node>();

            Node targetSquare = goal;

            for (int x = 0; x < maxCheckNum; x++) {

                path.add(targetSquare);

                if (targetSquare.equals(start))

                    break;

                targetSquare = targetSquare.parent;

            }

            Collections.reverse(path);

            if (path.size() > 0) {
                Path p = new Path(path);
                return p;
            }
            else
                pathFound = false;
        }

//    	if (!pathFound)
//			System.out.println("No path found. :<");

        return null;

    }
    
    public Path getPathTo(Node goal, Node start) {
        return getPathTo(goal, start, 1000);
    }

    public void debugDraw(){

        for (Node n : nodes) {

            Vector3f[] xy = new Vector3f[]{
                    new Vector3f(-0.25f, 0, 0),
                    new Vector3f(0, 0.25f, 0),
                    new Vector3f(0.25f, 0, 0),
                    new Vector3f(0, -0.25f, 0),
                    new Vector3f(0, 0, 0.25f),
                    new Vector3f(0, 0, -0.25f)};

            for (Vector3f v : xy)
                scene.drawLine(n.position(), n.position().plus(v), debugNodeColor);

            for (Node m : n.neighbors)
                scene.drawLine(n.position(), m.position(), debugLineColor);
        }

    }

    public void clean(){
        // Remove nodes that have no neighbors
        for (Node n : new ArrayList<Node>(nodes)) {
            if (n.neighbors.size() == 0)
                nodes.remove(n);
        }
    }

    public boolean allConnected(){
        // If every node on the map is connected to each other.
        boolean allConnected = false;

        if (nodes.size() == 0)
            return false;

        ArrayList<Node> checked = new ArrayList<Node>();
        Stack<Node> toCheck = new Stack<Node>();

        toCheck.push(nodes.get(0));

        while (toCheck.size() > 0) {
            Node n = toCheck.pop();
            checked.add(n);
            for (Node n2 : n.neighbors) {
                if (!checked.contains(n2))
                toCheck.push(n2);
            }
        }

        return checked.size() == nodes.size();

    }

}
