def celsius_to(*, unit, value):
    #check for aberrant values
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if unit not in ["c", "f", "k"]:
        raise ValueError("L'unité doit être 'c' (Celsius), 'f' (Fahrenheit) ou 'k' (Kelvin)")
    if value < -273.15:
        raise ValueError("La température en Celsius ne peut pas être inférieure à -273.15°C")
    
    case = {
        "c": value,
        "f": (value * 9.0/5.0) + 32,
        "k": value + 273.15,
    }
    
    return case[unit]

def fahrenheit_to(*, unit, value):
    #check for aberrant values
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if unit not in ["c", "f", "k"]:
        raise ValueError("L'unité doit être 'c' (Celsius), 'f' (Fahrenheit) ou 'k' (Kelvin)")
    if value < -459.67:
        raise ValueError("La température en Fahrenheit ne peut pas être inférieure à -459.67°F")
    
    case = {
        "c": (value - 32) * 5.0/9.0,
        "f": value,
        "k": (value - 32) * 5.0/9.0 + 273.15,
    }
    
    return case[unit]

def kelvin_to(*, unit, value):
    #check for aberrant values
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if unit not in ["c", "f", "k"]:
        raise ValueError("L'unité doit être 'c' (Celsius), 'f' (Fahrenheit) ou 'k' (Kelvin)")
    if value < 0:
        raise ValueError("La température en Kelvin ne peut pas être inférieure à 0K")
    
    case = {
        "c": value - 273.15,
        "f": (value - 273.15) * 9.0/5.0 + 32,
        "k": value,
    }
    
    return case[unit]


if __name__ == "__main__":
    #Tests unitaires
    import math

    assert celsius_to(unit="f", value=0) == 32
    assert celsius_to(unit="k", value=0) == 273.15

    assert math.isclose(fahrenheit_to(unit="c", value=0), -17.77777777777778, rel_tol=1e-9)
    assert math.isclose(fahrenheit_to(unit="k", value=0), 255.3722222222222, rel_tol=1e-9)

    assert math.isclose(kelvin_to(unit="c", value=0), -273.15, rel_tol=1e-9)
    assert math.isclose(kelvin_to(unit="f", value=0), -459.67, rel_tol=1e-9)

    print("Tests passés avec succès")
