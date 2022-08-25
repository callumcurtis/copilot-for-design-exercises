# Question 1
Your team is designing the software for the dashboard of your company's latest gas-powered car. The next feature to be
implemented is the logic behind the “low gas” indicator. The indicator is implemented inside
[`LowGasIndicator`](low_gas_indicator.py) and can be toggled on/off by setting/clearing the `on` flag. The gas tank
level is tracked by [`GasTank`](gas_tank.py) and can be accessed using `remaining()`. While
[`LowGasIndicator`](low_gas_indicator.py) is the first feature to depend on the remaining gas in
[`GasTank`](gas_tank.py), your team expects that future indicators could also depend on it. Your task is to ensure that
the [`LowGasIndicator`](low_gas_indicator.py) is toggled on if and only if there is less than `threshold` liters
of gas remaining in the tank. Make sure to consider how future indicators could be added to also depend on the remaining
gas in [`GasTank`](gas_tank.py). Add or modify files as you see fit.