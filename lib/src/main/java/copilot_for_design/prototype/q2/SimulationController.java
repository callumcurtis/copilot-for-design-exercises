package copilot_for_design.prototype.q2;

import org.apache.commons.math3.util.Pair;

/**
 * Represents your robot simulation code.
 * Methods in this library accept imperial units.
 */
public class SimulationController {
    private final float SPEED_TOLERANCE = 0.01f;  // margin of error for speed in ft/s
    private final ThirdPartyLibrary lib;
    private final Pair<Float, Float> goal;

    /**
     * Create a controller for simulating the robot.
     * 
     * @param lib  third-party library
     * @param goal 2D goal point (x, y), where x and y are in units of feet
     */
    public SimulationController(ThirdPartyLibrary lib, Pair<Float, Float> goal) {
        this.lib = lib;
        this.goal = goal;
    }

    /**
     * Execute the simulation by navigating to the goal point
     */
    public void executeSimulation() {
        // TODO: fix this calculation by converting the result of calculateCurrentSpeed()
        //  to ft/s using the adapter pattern
        if(lib.calculateCurrentSpeed() < 0 + SPEED_TOLERANCE) {
            throw new IllegalStateException("The robot must be unmoving at the start of execution.");
        }

        // TODO: fix this call to moveToPoint() by adapting its interface to
        //  accept goal (a Pair of floats in units of feet)
        // lib.moveToPoint(goal);
    }

    /**
     * Main method that creates an instance of SimulationController and calls executeSimulation
     */
    public static void main(String[] args) {
        // TODO
    }
}
