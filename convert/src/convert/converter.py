from convert.errors import UnknownUnitError, IncompatibleUnitsError


CONVERSIONS = {
    "distance": {
        "km": "miles",
        "miles": "km",
        "factor": 0.621371,
    },
    "mass": {
        "kg": "lbs",
        "lbs": "kg",
        "factor": 2.20462,
    },
    "temperature": {
        "celsius": "fahrenheit",
        "fahrenheit": "celsius",
    },
}

UNIT_TO_CATEGORY = {
    "km": "distance",
    "miles": "distance",
    "kg": "mass",
    "lbs": "mass",
    "celsius": "temperature",
    "fahrenheit": "temperature",
}


def convert(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in UNIT_TO_CATEGORY:
        raise UnknownUnitError(f"Unknown unit: {from_unit}")
    if to_unit not in UNIT_TO_CATEGORY:
        raise UnknownUnitError(f"Unknown unit: {to_unit}")

    from_cat = UNIT_TO_CATEGORY[from_unit]
    to_cat = UNIT_TO_CATEGORY[to_unit]

    if from_cat != to_cat:
        raise IncompatibleUnitsError(
            f"Cannot convert {from_unit} ({from_cat}) to {to_unit} ({to_cat})"
        )

    if from_cat == "distance":
        factor = CONVERSIONS["distance"]["factor"]
        if from_unit == "km" and to_unit == "miles":
            return value * factor
        elif from_unit == "miles" and to_unit == "km":
            return value / factor
    elif from_cat == "mass":
        factor = CONVERSIONS["mass"]["factor"]
        if from_unit == "kg" and to_unit == "lbs":
            return value * factor
        elif from_unit == "lbs" and to_unit == "kg":
            return value / factor
    elif from_cat == "temperature":
        if from_unit == "celsius" and to_unit == "fahrenheit":
            return value * 9 / 5 + 32
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            return (value - 32) * 5 / 9

    return value
