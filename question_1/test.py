"""
Tests the participant's solution to question 1

Note that these tests are provided here for illustrative purposes only and would not
be provided to participants during the study.
"""

import pytest

from question_1.gas_tank import GasTank
from question_1.low_gas_indicator import LowGasIndicator


class Test:
    INITIAL_TANK_FILL = 50

    @pytest.fixture()
    def tank(self) -> GasTank:
        return GasTank(self.INITIAL_TANK_FILL)

    def test_indicator_off_for_initial_gas_above_threshold(self, tank: GasTank):
        indicator = LowGasIndicator(tank, 50)
        assert not indicator.on

    def test_indicator_on_for_initial_gas_below_threshold(self, tank: GasTank):
        indicator = LowGasIndicator(tank, 51)
        assert indicator.on

    def test_gas_consumption_past_threshold_sets_indicator(self, tank: GasTank):
        indicator = LowGasIndicator(tank, 30)
        tank.consume(21)
        assert indicator.on

    def test_gas_consumption_above_threshold_does_not_set_indicator(self, tank: GasTank):
        indicator = LowGasIndicator(tank, 30)
        tank.consume(20)
        assert not indicator.on
