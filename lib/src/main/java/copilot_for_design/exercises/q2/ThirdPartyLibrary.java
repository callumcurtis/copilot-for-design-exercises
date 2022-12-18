package copilot_for_design.exercises.q2;

/**
 * Represents a third-party library that helps your application simulate robots.
 * Methods in this library accept metric units. Do not modify this class.
 */
public class ThirdPartyLibrary {
    /**
     * Move the robot to the point (x, y), where x and y are given in meters.
     * 
     * @param x horizontal component of position in meters
     * @param y vertical component of position in meters
     */
    public void moveToPoint(float x, float y) {
        // move to the point (x, y)...
    }

    /**
     * Calculate the current speed of the robot.
     * 
     * @return current speed of the robot in m/s
     */
    public float calculateCurrentSpeed() {
        // calculate the current speed in m/s...
        return (float) Math.random() * 10;
    }
}
