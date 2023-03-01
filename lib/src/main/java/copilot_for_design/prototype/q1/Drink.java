package copilot_for_design.prototype.q1;

import java.math.BigDecimal;
import java.util.Set;

public class Drink {
    // Required fields
    private final float volume;
    private final float temperature;
    private final String flavor;
    private final BigDecimal price;

    // Optional fields
    private final String topping;
    private final boolean isSeasonal;
    private final Set<String> countriesWhereAvailable;

    /**
     * Create a Drink instance with provided required and optional fields
     * <p>
     * TODO: allow creating a Drink using any combination of optional parameters
     * 
     * @param volume                  the volume of the drink when it is served
     * @param temperature             the temperature of the drink when it is served
     * @param flavor                  the drink's flavor
     * @param price                   the price of the drink
     * @param topping                 the name of the drink topping
     * @param isSeasonal              true iff drink is available only in specific seasons
     * @param countriesWhereAvailable set of country names where the drink is available
     */
    public Drink(
        float volume,
        float temperature,
        String flavor,
        BigDecimal price,
        String topping,
        boolean isSeasonal,
        Set<String> countriesWhereAvailable
    ) {
        this.volume = volume;
        this.temperature = temperature;
        this.flavor = flavor;
        this.price = price;
        this.topping = topping;
        this.isSeasonal = isSeasonal;
        this.countriesWhereAvailable = countriesWhereAvailable;
    }

    public float getVolume() {
        return volume;
    }

    public float getTemperature() {
        return temperature;
    }

    public String getFlavor() {
        return flavor;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public String getTopping() {
        return topping;
    }

    public boolean isSeasonal() {
        return isSeasonal;
    }

    public Set<String> getCountriesWhereAvailable() {
        return countriesWhereAvailable;
    }

    public String toString() {
        return String.format(
            "Drink: volume=%f, temperature=%f, flavor=%s, price=%s, topping=%s, isSeasonal=%b, countriesWhereAvailable=%s",
            volume,
            temperature,
            flavor,
            price,
            topping,
            isSeasonal,
            countriesWhereAvailable
        );
    }
}
