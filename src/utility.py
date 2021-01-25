# @author KOOKIIE


def to_km(value, unit):
    if unit == "mm":
        return value / 1000000
    elif unit == "cm":
        return value / 100000
    elif unit == "m":
        return value / 1000
    elif unit == "km":
        return
    else:
        raise ValueError(f"Invalid unit: {unit}")


def to_mi(value, unit):
    if unit == "ft":
        return value / 5280
    elif unit == "in":
        return value / 63360
    elif unit == "mi":
        return value
    else:
        raise ValueError(f"Invalid unit: {unit}")


def to_kg(value, unit):
    if unit == "g":
        return value / 1000
    elif unit == "kg":
        return value
    else:
        raise ValueError(f"Invalid unit: {unit}")


def to_lbs(value, unit):
    if unit == "oz":
        return value / 16
    elif unit == "lbs":
        return value
    else:
        raise ValueError(f"Invalid unit: {unit}")


def to_ml(value, unit):
    if unit == "l":
        return value / 1000
    elif unit in ("ml", "cc"):
        return value
    else:
        raise ValueError(f"Invalid unit: {unit}")


def to_oz(value, unit):
    if unit == "gallon":
        return value * 128
    elif unit == "pint":
        return value * 16
    elif unit == "oz":
        return value
    else:
        raise ValueError(f"Invalid unit: {unit}")


def c_to_k(value):
    return value + 273.15


def k_to_c(value):
    return value - 273.15


def f_to_k(value):
    return ((value - 32) / 1.8) + 273.15


def k_to_f(value):
    return ((value - 273.15) * 1.8) + 32


SI_UNITS = [
    "km",
    "m",
    "cm",
    "mm",
    "kg",
    "g",
    "l",
    "ml",
    "cc",
]


IMPERIAL_UNITS = [
    "mi",
    "ft",
    "in",
    "lbs",
    "oz",
    "pint",
    "gallon",
]
