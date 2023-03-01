# Question 1

## Description

Starbuzz is having difficulty implementing the drink creation system in its new mobile app. You have been hired as a contractor to clean up the creation process for instances of their `Drink` class by designing and implementing a new builder class that allows `Drink` to be instantiated using any combination of optional parameters (`topping`, `isSeasonal`, and `countriesWhereAvailable`). In other words, a `Drink` should be able to be created without any optional arguments provided, with all optional arguments provided, or with any other subset of optional arguments provided.

## Criteria

Add a main method to your builder class demonstrating the creation of a `Drink` with the following fields:

* volume: 243.8
* temperature: 34.6
* flavor: "coffee"
* price: 5.78
* topping: \<not provided\>
* isSeasonal: true
* countriesWhereAvailable: \<not provided\>

Any non-provided fields should default to sensible values.