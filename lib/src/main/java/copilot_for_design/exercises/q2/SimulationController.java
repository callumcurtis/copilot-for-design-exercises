package copilot_for_design.exercises.q2;

import org.apache.commons.math3.util.Pair;

/**
 * Represents your robot simulation code.
 * Methods in this library accept imperial units.
 */
public class SimulationController {
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
        // TODO: call moveToPoint() with the correct units

        // TODO: call calculateCurrentSpeed() with the correct units
        
    }
}
