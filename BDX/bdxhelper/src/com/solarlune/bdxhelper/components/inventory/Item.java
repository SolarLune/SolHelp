package com.solarlune.bdxhelper.components.inventory;

import com.nilunder.bdx.Bdx;
import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.Scene;

import java.util.ArrayList;
import java.util.HashMap;

/**
 * Created by solarlune on 8/2/16.
 */
public class Item extends Component<GameObject> {

    public String name;                             // Name of the item; defaults to name of the owner GameObject
    public String id;                               // ID; used for stacking (determining if two items are basically the same); defaults to name
    public String description;                      // Description, if you so choose to have one
    public HashMap<String, Float> stats = new HashMap<String, Float>(); // Used to store basic statistics about the item (attack, defense, durability, rarity, elements, cost, etc)

    public float creationTimestamp = Bdx.time;      // When the Item was instantiated
    public float collectionTimestamp;               // When the Item was last collected
    public float dropTimestamp;                     // When the Item was last dropped

    public GameObject owner;
    public boolean canBeCollected = true;
    public boolean canBeDropped = true;
    public int quantity = 1;                        // How many of the item there are in this "stack" (i.e. you might have hundreds of Gold Pieces in a single "Item")
    public int stackLimit = 99999999;

    public Item(GameObject g, String name, int quantity){
        super(g);
        owner = g;
        this.name = name;
        this.id = name;
        this.quantity = quantity;
        logicFrequency = 0;
    }

    public Item(GameObject g){
        this(g, g.getClass().getSimpleName(), 1);
    }

    public boolean collect(){
        if (canBeCollected) {
            owner.end();
            collectionTimestamp = Bdx.time;
            return true;
        }
        return false;
    }

    public GameObject drop(Scene scene){
        if (canBeDropped) {
            GameObject o = scene.add(owner.name);
            dropTimestamp = Bdx.time;
            if (o.components.get("Item") != null)
                o.components.remove("Item");        // Clear whatever item usually "spawns" in with the GameObject
            o.components.add(this);                 // Put yourself back there
            owner = o;
            return owner;
        }
        return null;
    }

    public String toString(){
        return name + ": " + quantity;
    }

}
