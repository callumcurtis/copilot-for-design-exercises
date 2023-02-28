package copilot_for_design.prototype.q4;

import java.awt.Color;

public class ColorChangingLightPanels {
    private float brightness;
    private Color color;
    private boolean on;

    /**
     * Represents a color-changing device that can be controlled using Commands.
     * 
     * @param brightness brightness of the light panels; larger is brighter
     * @param color      color of the light panels
     */
    public ColorChangingLightPanels(float brightness, Color color) {
        this.brightness = brightness;
        this.color = color;
        this.on = false;
    }

    public float getBrightness() {
        return brightness;
    }

    public void setBrightness(float brightness) {
        this.brightness = brightness;
    }

    public Color getColor() {
        return color;
    }

    public void setColor(Color color) {
        this.color = color;
    }

    public boolean isOn() {
        return on;
    }

    public void setOn(boolean on) {
        this.on = on;
    }
}
