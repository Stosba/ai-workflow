import pytest
from convert.converter import convert
from convert.errors import UnknownUnitError, IncompatibleUnitsError


class TestConverter:
    def test_km_to_miles(self):
        assert convert(1, "km", "miles") == 1 * 0.621371

    def test_miles_to_km(self):
        assert convert(1, "miles", "km") == 1 / 0.621371

    def test_kg_to_lbs(self):
        assert convert(1, "kg", "lbs") == 1 * 2.20462

    def test_lbs_to_kg(self):
        assert convert(1, "lbs", "kg") == 1 / 2.20462

    def test_celsius_to_fahrenheit(self):
        assert convert(0, "celsius", "fahrenheit") == 32
        assert convert(100, "celsius", "fahrenheit") == 212

    def test_fahrenheit_to_celsius(self):
        assert convert(32, "fahrenheit", "celsius") == 0
        assert convert(212, "fahrenheit", "celsius") == 100

    def test_zero_value(self):
        assert convert(0, "km", "miles") == 0
        assert convert(0, "kg", "lbs") == 0
        assert convert(0, "celsius", "fahrenheit") == 32

    def test_unknown_unit(self):
        with pytest.raises(UnknownUnitError):
            convert(1, "km", "parsec")

    def test_incompatible_units(self):
        with pytest.raises(IncompatibleUnitsError):
            convert(1, "km", "kg")
