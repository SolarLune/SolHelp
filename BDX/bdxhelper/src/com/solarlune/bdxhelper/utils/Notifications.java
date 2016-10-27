package com.solarlune.bdxhelper.utils;

import com.nilunder.bdx.Bdx;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.utils.Named;

import javax.vecmath.Vector3f;
import java.util.ArrayList;
import java.util.HashMap;

public class Notifications {

    static public class Note implements Named {

        public String name;
        public float timestamp;
        public Object data;

        public Note (String name) {
            this.name = name;
            timestamp = Bdx.time;
        }
        public Note (String name, Object data) {
            this(name);
            this.data = data;
        }

        public String toString(){
            return name;
        }

        public String name(){
            return name;
        }

    }

    static public class Notifier {
        public void onNote(Note note){};
    }

    public HashMap<String, ArrayList<Notifier>> registered;

    public Notifications(){
        registered = new HashMap<String, ArrayList<Notifier>>();
    }

    public void broadcast(Note note, String groupName){
        if (registered.containsKey(groupName)) {
            for (Notifier n : new ArrayList<Notifier>(registered.get(groupName))) {
                n.onNote(note);
            }
        }
    }

    public void broadcast(Note note) {
        for (String groupName : registered.keySet()) {
            broadcast(note, groupName);
        }
    }

    public void broadcast(String noteName) {
        broadcast(new Note(noteName));
    }

    public void register(Notifier n, String groupName) {
        if (!registered.containsKey(groupName))
            registered.put(groupName, new ArrayList<Notifier>());
        registered.get(groupName).add(n);
    }

    public void register(Notifier n) {
        register(n, "default");
    }

    public void unregister(Notifier n, String groupName) {
        if (!registered.containsKey(groupName))
            registered.put(groupName, new ArrayList<Notifier>());
        if (registered.get(groupName) != null)
            registered.get(groupName).remove(n);
    }

    public void unregister(Notifier n){
        unregister(n, "default");
    }

}

