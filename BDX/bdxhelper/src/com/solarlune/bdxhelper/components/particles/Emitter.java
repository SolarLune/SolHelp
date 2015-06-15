package com.solarlune.bdxhelper.components.particles;

import java.util.ArrayList;

import javax.vecmath.Vector3f;
import javax.vecmath.Vector4f;

import com.nilunder.bdx.Component;
import com.nilunder.bdx.GameObject;
import com.nilunder.bdx.State;
import com.nilunder.bdx.components.Halo;
import com.nilunder.bdx.utils.Random;
import com.nilunder.bdx.utils.Timer;

public class Emitter extends Component<GameObject> {

	public ArrayList<GameObject> particles;
	private ArrayList<String> particleTemplates;	// Names of particles that are randomly chosen for the particles to spawn
	public Vector3f windDirection;					// Wind (constant force) direction
	public Vector3f gravityDirection;				// Gravity (additive force) direction
	public Vector3f spawnOffset;					// Spawn position offset
	public Vector3f spawnRandom;					// Random range in which particles can spawn
	public Vector3f startingVelocity;				// Starting velocity for particles
	public float friction;							// Linear friction applied as particles move
	private float spawnWait;						// In seconds
	public float minLife;							// Minimum lifetime for particles in seconds
	public float maxLife;							// Max lifetime
	public float minSize;							// Minimum size for particles (scaling is uniform)
	public float maxSize;							// Maximum size
	public int spawnNum;							// Number of particles to spawn at a time
	public int maxNumParticles;						// Maximum number of particles that can exist
	public boolean halo;							// If the particles should face the camera
	
	public ArrayList<Vector4f> colorStages;			// Color stages
	
	private Timer spawnTimer;
	
	public Emitter(GameObject g) {
		
		super(g);
		
		particles = new ArrayList<GameObject>();
		particleTemplates = new ArrayList<String>();
		
		windDirection = new Vector3f();
		gravityDirection = new Vector3f();
		spawnOffset = new Vector3f();
		spawnRandom = new Vector3f();
		startingVelocity = new Vector3f();
		
		colorStages = new ArrayList<Vector4f>();
		
		friction = 0;
		minLife = 1;
		maxLife = 1;
		minSize = 1;
		maxSize = 1;
		maxNumParticles = Integer.MAX_VALUE;
		spawnNum = 1;
		halo = true;
		
		spawnTimer = new Timer();
		spawnTime(0.01f);		
		spawnTimer.done(true);
		
		state = mainState;
		
	}
	
	public void addTemplate(String partName){		
		particleTemplates.add(partName);
	}
	
	State mainState = new State(){
		
		public void main(){
			
			if (spawnTimer.done()) {
				spawnTimer.restart();
				
				for (int i = 0; i < spawnNum; i++) {
					
					if ((particleTemplates.size() > 0) && (particles.size() < maxNumParticles)) {
					
						String choice = Random.choice(particleTemplates);
						
						GameObject part = g.scene.add(choice);
						
						part.position(g.position().plus(spawnOffset));
						part.move(Random.direction().mul(spawnRandom));
						if (halo)
							part.components.add(new Halo(part));
						part.scale(Random.random(minSize, maxSize));
						
						Particle partComp = new Particle(part, Emitter.this, Random.random(minLife, maxLife));
						partComp.velocity = new Vector3f(startingVelocity);
						part.components.add(partComp);	
						
						particles.add(part);
						part.parent(g);			// Could cause problems later; I'll let it lie here for now, though
						
					}
				
				}
				
			}
			
		}
		
	};
	
	public void spawnTime(float spawnTime){
		spawnWait = spawnTime;
		spawnTimer.set(spawnWait);
		spawnTimer.restart();
	}
	
}
