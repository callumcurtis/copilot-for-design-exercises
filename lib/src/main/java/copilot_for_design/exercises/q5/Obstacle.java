package copilot_for_design.exercises.q5;

import org.apache.commons.math3.util.Pair;

public class Obstacle {
    private Pair<Double, Double> velocity;
    private Pair<Double, Double> position;
    private final double mass;
    private final Mesh mesh;

    public Obstacle(Pair<Double, Double> position, double mass, Mesh mesh) {
        this.velocity = new Pair<Double, Double>(0.0, 0.0);
        this.position = position;
        this.mass = mass;
        this.mesh = mesh;
    }

    /**
     * Called by the simulation loop to update the state of the obstacle each frame.
     * Updates the position of the obstacle according to its current velocity.
     * 
     * @param secondsElapsed number of seconds elapsed in the simulation since the last frame/update
     */
    public void onUpdate(float secondsElapsed) {
        Pair<Double, Double> deltaPos = new Pair<Double, Double>(
            velocity.getFirst() * secondsElapsed,
            velocity.getSecond() * secondsElapsed);
        position = new Pair<Double, Double>(
            position.getFirst() + deltaPos.getFirst(),
            position.getSecond() + deltaPos.getSecond());
    }

    public Pair<Double, Double> getVelocity() {
        return velocity;
    }

    public void setVelocity(Pair<Double, Double> velocity) {
        this.velocity = velocity;
    }

    public Pair<Double, Double> getPosition() {
        return position;
    }

    public double getMass() {
        return mass;
    }

    public Mesh getMesh() {
        return mesh;
    }
}
