import pytest

from copilot_for_design.exercises.q1.gas_tank import GasTank
from copilot_for_design.exercises.q1.low_gas_indicator import LowGasIndicator


class TestQ1:
    INITIAL_TANK_FILL = 50

    @pytest.fixture
    def tank(self) -> GasTank:
        return GasTank(self.INITIAL_TANK_FILL)

    def test_indicator_off_for_initial_gas_above_threshold(self, tank: GasTank):
        indicator = LowGasIndicator(tank, 50)
        assert not indicator.on

    def test_indicator_on_for_initial_gas_below_threshold(self, tank: GasTank):
        indicator = LowGasIndicator(tank, 51)
        assert indicator.on

    def test_consuming_gas_past_threshold_sets_indicator(self, tank: GasTank):
        indicator = LowGasIndicator(tank, 30)
        tank.consume(21)
        assert indicator.on

    def test_consuming_gas_above_threshold_does_not_set_indicator(self, tank: GasTank):
        indicator = LowGasIndicator(tank, 30)
        tank.consume(20)
        assert not indicator.on

    def test_filling_tank_past_threshold_clears_indicator(self, tank: GasTank):
        indicator = LowGasIndicator(tank, 60)
        tank.fill(10)
        assert not indicator.on

    def test_filling_tank_below_threshold_does_not_clear_indicator(self, tank: GasTank):
        indicator = LowGasIndicator(tank, 60)
        tank.fill(9)
        assert indicator.on
