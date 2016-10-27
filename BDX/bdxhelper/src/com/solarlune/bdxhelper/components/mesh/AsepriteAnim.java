package com.solarlune.bdxhelper.components.mesh;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.graphics.GLTexture;
import com.badlogic.gdx.graphics.Mesh;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g3d.Model;
import com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute;
import com.badlogic.gdx.math.Matrix3;
import com.badlogic.gdx.utils.JsonReader;
import com.badlogic.gdx.utils.JsonValue;
import com.nilunder.bdx.Bdx;
import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;
import com.nilunder.bdx.utils.Timer;

import javax.vecmath.Vector2f;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

/**
 * Created by solarlune on 10/26/16.
 */

public class AsepriteAnim extends Component<GameObject> {

    public static class Frame extends Vector2f {
        public int index;
        public int sequence;
        public float duration;
        public Frame(Vector2f v){
            super(v);
        }
    }

    public static class Animation extends ArrayList<Frame>{

        public String name;
        public boolean looping;

        public int playHead;
        public int playDir;
        public Frame current;

        public Animation(String name, boolean looping){
            this.name = name;
            this.looping = looping;
            playHead = 0;
            playDir = 1;
        }

        public Frame nextFrame(){
            if (onLastFrame()){
                if (looping)
                    reset();
                else
                    playHead -= playDir;
            }

            Frame frame = get(playHead);

            current = frame;

            playHead += playDir;

            return frame;
        }

        public boolean onLastFrame(){
            return playHead == size() || playHead == -1;
        }

        public void reset(){
            if (playDir > 0)
                playHead = 0;
            else
                playHead = size() - 1;
        }

    }

    public static class Tag {

        public int start;
        public int end;
        public String name;

    }

    public float speed;
    public HashMap<String, Animation> animations;
    public Animation active;
    public HashMap<String, Tag> tags;

    private int prevFrame;
    private Timer ticker;
    private Matrix3 uvScale;
    private boolean rowBased;
    private Vector2f baseFrame;
    private Vector2f frameDim;
    private HashSet<Tag> prevTouchingTags;
    private HashSet<Tag> touchingTags;

    public AsepriteAnim(GameObject g, int frameWidth, int frameHeight, boolean rowBased, boolean uniqueModel){
        super(g);
        if (uniqueModel)
            g.mesh(g.mesh().copy());
        this.rowBased = rowBased;
        animations = new HashMap<String, Animation>();
        ticker = new Timer();
        uvScale = new Matrix3();
        uvScale.idt();
        speed = 1;
        state = play;

        // initially displayed frame
        HashMap<Model,Vector2f> modelToFrame = g.scene.modelToFrame;

        baseFrame = modelToFrame.get(g.modelInstance.model);
        if (baseFrame == null){
            baseFrame = uvFrame();
            modelToFrame.put(g.modelInstance.model, baseFrame);
        }

        // frameDim
        TextureAttribute ta = (TextureAttribute)g.modelInstance.materials.get(0).get(TextureAttribute.Diffuse);
        GLTexture t = ta.textureDescription.texture;
        float u = 1f / t.getWidth();
        float v = 1f / t.getHeight();

        frameDim = new Vector2f(u * frameWidth, v * frameHeight);

        tags = new HashMap<String, Tag>();
        touchingTags = new HashSet<Tag>();
        prevTouchingTags = new HashSet<Tag>();
    }

    public AsepriteAnim(GameObject g, int frameWidth, int frameHeight){
        this(g, frameWidth, frameHeight, true, true);
    }

    public void add(String name, int index, int[] frames){
        add(name, index, frames, 12, true);
    }

    public void add(String name, int sequence, int[] frames, float fps, boolean looping){

        Animation anim = new Animation(name, looping);

        for (int i : frames){
            Vector2f f = new Vector2f(baseFrame);
            if (rowBased){
                f.x += i * frameDim.x;
                f.y += sequence * frameDim.y;
            }else{
                f.x += sequence * frameDim.x;
                f.y += i * frameDim.y;
            }
            Frame frame = new Frame(f);
            frame.index = i;
            frame.sequence = sequence;
            frame.duration = 1 / fps;
            anim.add(frame);
        }

        anim.current = anim.get(0);

        animations.put(anim.name, anim);

    }

    public void load(FileHandle jsonFilePath, boolean importTagsAsAnimations){

        JsonReader reader = new JsonReader();
        JsonValue data = reader.parse(jsonFilePath);
        JsonValue frames = data.get("frames");

        boolean rowBased = false;

        if (frames.size > 1) {
            if (frames.get(1).get("frame").get("y").asFloat() > frames.get(0).get("frame").get("y").asFloat())
                rowBased = true;
        }

        for (JsonValue t : data.get("meta").get("frameTags")) {
            Tag tag = new Tag();
            tag.name = t.get("name").asString();
            tag.start = t.get("from").asInt();
            tag.end = t.get("to").asInt();
            tags.put(tag.name, tag);
        }

        importAnim("All", rowBased, frames, 0, frames.size - 1);

        if (importTagsAsAnimations) {

            for (String tagName : tags.keySet())
                importAnim(tagName, rowBased, frames, tags.get(tagName).start, tags.get(tagName).end);

        }

    }

    public void load(){

        // Auto-loads using what should be the texture's proposed path

        Texture t = g.mesh().materials.get(0).currentTexture;
        String texName = "";
        for (String s : g.scene.textures.keySet()) {
            if (g.scene.textures.get(s) == t) {
                texName = s;
                break;
            }
        }

        String sub = texName;

        if (texName.lastIndexOf(".") > -1)
            sub = texName.substring(0, texName.lastIndexOf("."));

        FileHandle f = Gdx.files.internal("bdx/textures/" + sub + ".json");

        load(f, true);

    }

    private Animation importAnim(String animName, boolean rowBased, JsonValue frames, int start, int end){

        Animation a = new Animation(animName, true);

        for (int i = start; i <= end; i++) {

            JsonValue frameData = frames.get(i);

            Vector2f f = new Vector2f(baseFrame);

            if (rowBased){
                f.y += i * frameDim.y;
            }else{
                f.x += i * frameDim.x;
            }

            Frame frame = new Frame(f);
            frame.index = i;
            frame.sequence = 0;
            frame.duration = frameData.get("duration").asFloat() / 1000f;
            a.add(frame);

        }

        a.current = a.get(0);

        animations.put(a.name, a);

        return a;

    }

    public ArrayList<String> animationNames(){
        return new ArrayList<String>(animations.keySet());
    }

    public void uvScaleX(float s){
        uvScale(s, uvScaleY());
    }

    public void uvScaleY(float s){
        uvScale(uvScaleX(), s);
    }

    public float uvScaleX(){
        return uvScale.val[Matrix3.M00];
    }

    public float uvScaleY(){
        return uvScale.val[Matrix3.M11];
    }

    public void play(String name){
        Animation next = animations.get(name);

        if (active != next){
            active = next;
            active.playDir = speed < 0 ? -1 : 1;
            active.reset();
            ticker.done(true); // immediate play
        }

        if (!active.looping && active.onLastFrame()){
            active.playDir = speed < 0 ? -1 : 1;
            active.reset();
            ticker.done(true);
        }

    }

    public void showNextFrame() {
        active.playDir = speed < 0 ? -1 : 1;
        uvFrame(active.nextFrame());
    }

    public void frame(int frame){
        active.playHead = frame; // Set the frame, and
        ticker.done(true); // Update the sprite immediately
    }

    public int frame(){
        return active.playHead - active.playDir;
    }

    public boolean frameChanged(){
        return prevFrame != frame();
    }

    private State play = new State(){
        private float nz(float n){
            return n <= 0 ? 0.000001f : n;
        }

        public void main(){

            prevTouchingTags = touchingTags;
            touchingTags = touchingTags();

            if (active == null)
                return;

            prevFrame = frame();

            ticker.interval = nz(Math.abs(active.current.duration) / Math.abs(speed));

            if (ticker.tick()){
                showNextFrame();
            }

        }
    };

    private void uvFrame(Vector2f frame){
        Matrix3 trans = new Matrix3();
        Vector2f df = uvFrame();
        trans.setToTranslation(frame.x - df.x, frame.y - df.y);

        Mesh mesh = g.modelInstance.model.meshes.first();
        mesh.transformUV(trans);

    }

    private Vector2f uvFrame(){
        Mesh mesh = g.modelInstance.model.meshes.first();
        int n = mesh.getNumVertices();
        float[] verts = new float[n*Bdx.VERT_STRIDE];
        mesh.getVertices(0, verts.length, verts);

        Vector2f frame = new Vector2f(0, 0);

        int uvStart = Bdx.VERT_STRIDE - 2;
        for (int v = 0; v < n; ++v){
            int i = v * Bdx.VERT_STRIDE;
            frame.x += verts[i + uvStart];
            frame.y += verts[i + uvStart + 1];
        }

        frame.x /= n;
        frame.y /= n;

        return frame;
    }

    private void scaleUV(Matrix3 scale){
        Matrix3 trans = new Matrix3(); trans.idt();
        Vector2f df = uvFrame();
        trans.setToTranslation(df.x, df.y);

        Matrix3 toOrigin = new Matrix3(trans);
        toOrigin.inv();

        trans.mul(scale);
        trans.mul(toOrigin);

        Mesh mesh = g.modelInstance.model.meshes.first();
        mesh.transformUV(trans);
    }

    private void uvScale(float x, float y){
        if (uvScaleX() == x && uvScaleY() == y)
            return;

        // back to unit scale
        uvScale.inv();
        scaleUV(uvScale);

        // set new scale
        uvScale.idt();
        uvScale.scale(x, y);
        scaleUV(uvScale);
    }

    public HashSet<Tag> touchingTags(){
        HashSet<Tag> a = new HashSet<Tag>();
        for (String t : tags.keySet()) {
            Tag tag = tags.get(t);
            if (tag.start <= active.current.index && active.current.index <= tag.end)
                a.add(tag);

        }
        return a;
    }

    public HashSet<Tag> hitTags(){
        HashSet<Tag> result = new HashSet<Tag>(touchingTags);
        result.removeAll(prevTouchingTags);
        return result;
    }

    public HashSet<Tag> leftTags(){
        HashSet<Tag> result = new HashSet<Tag>(prevTouchingTags);
        result.removeAll(touchingTags);
        return result;
    }

}
