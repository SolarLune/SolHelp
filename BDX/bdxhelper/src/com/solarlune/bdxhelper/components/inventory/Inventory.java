package com.solarlune.bdxhelper.components.inventory;

import java.util.ArrayList;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;

public class Inventory extends Component<GameObject> {

    GameObject g;
    public int maxNumberOfSlots = 999;
    public ArrayList<Item> data = new ArrayList<Item>();

    public Inventory(GameObject g){
        super(g);
        logicFrequency = 0;
    }

    public boolean add(int index, Item item) {

        if (item.canBeCollected) {

            boolean stack = false;

            for (Item x : data) {

                if (x.id.equals(item.id) && x.quantity + item.quantity < x.stackLimit) {
                    x.quantity += item.quantity;
                    stack = true;
                }
            }

            if (!stack) {
                if (data.size() < maxNumberOfSlots)
                    data.add(index, item);
            }

            item.collect();

            return true;
        }

        return false;
    }

    public boolean add(Item item) {
        return add(data.size(), item);
    }

    public Item get(int index) {
        return data.get(index);
    }

    public Item drop(int index) {
        if (data.size() > index && data.get(index).canBeDropped) {
            Item i = data.remove(index);
            i.drop(g.scene);
            return i;
        }
        return null;
    }

    public void drop(Item item) {
        if (data.contains(item) && item.canBeDropped) {
            data.remove(item);
            item.drop(g.scene);
        }
    }

    public int size(){
        return data.size();
    }

    public void empty(){
        for (Item i : data) {
            i.drop(g.scene);
        }
        data.clear();
    }

    public String toString(){
        return data.toString();
    }

}
