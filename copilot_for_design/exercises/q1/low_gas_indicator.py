from copilot_for_design.exercises.q1.gas_tank import GasTank


class LowGasIndicator:
    def __init__(self, gas_tank: GasTank, threshold: int):
        assert threshold >= 0
        self._gas_tank = gas_tank
        self._threshold = threshold
        self.on = gas_tank.remaining() < threshold
