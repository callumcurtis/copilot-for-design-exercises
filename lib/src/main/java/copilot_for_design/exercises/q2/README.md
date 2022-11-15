# Question 2

## Description

Your fresh startup is working on adding simulation capabilities to your web application that lets customers design robots, but the library you are working with ([`ThirdPartyLibrary.java`](ThirdPartyLibrary.java)) does not accept `Pair` instances and only accepts units in metric – while your code ([`SimulationController.java`](SimulationController.java)) handles imperial units. Leverage the adapter pattern to resolve these two discrepancies.

## Additional Constraints

You must not alter any code in [`ThirdPartyLibrary.java`](ThirdPartyLibrary.java).

## Criteria

After your changes, [`SimulationController.java`](SimulationController.java) should provide/recieve values with appropriate units to/from [`ThirdPartyLibrary.java`](ThirdPartyLibrary.java), and [`SimulationController.java`](SimulationController.java) should supply `Pair` instances to its interface (in reality, through the  adapter's interface).