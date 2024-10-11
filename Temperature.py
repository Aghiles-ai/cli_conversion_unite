def celsius_to(*, unit, value):
    #check for aberrant values
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if unit not in ["C", "F", "K"]:
        raise ValueError("L'unité doit être 'C' (Celsius), 'F' (Fahrenheit) ou 'K' (Kelvin)")
    if value < -273.15:
        raise ValueError("La température en Celsius ne peut pas être inférieure à -273.15°C")
    
    case = {
        "C": value,
        "F": (value * 9.0/5.0) + 32,
        "K": value + 273.15,
    }
    
    return case[unit]

def fahrenheit_to(*, unit, value):
    #check for aberrant values
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if unit not in ["C", "F", "K"]:
        raise ValueError("L'unité doit être 'C' (Celsius), 'F' (Fahrenheit) ou 'K' (Kelvin)")
    if value < -459.67:
        raise ValueError("La température en Fahrenheit ne peut pas être inférieure à -459.67°F")
    
    case = {
        "C": (value - 32) * 5.0/9.0,
        "F": value,
        "K": (value - 32) * 5.0/9.0 + 273.15,
    }
    
    return case[unit]

def kelvin_to(*, unit, value):
    #check for aberrant values
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if unit not in ["C", "F", "K"]:
        raise ValueError("L'unité doit être 'C' (Celsius), 'F' (Fahrenheit) ou 'K' (Kelvin)")
    if value < 0:
        raise ValueError("La température en Kelvin ne peut pas être inférieure à 0K")
    
    case = {
        "C": value - 273.15,
        "F": (value - 273.15) * 9.0/5.0 + 32,
        "K": value,
    }
    
    return case[unit]


if __name__ == "__main__":
    #Tests unitaires
    import math

    assert celsius_to(unit="F", value=0) == 32
    assert celsius_to(unit="K", value=0) == 273.15

    assert math.isclose(fahrenheit_to(unit="C", value=0), -17.77777777777778, rel_tol=1e-9)
    assert math.isclose(fahrenheit_to(unit="K", value=0), 255.3722222222222, rel_tol=1e-9)

    assert math.isclose(kelvin_to(unit="C", value=0), -273.15, rel_tol=1e-9)
    assert math.isclose(kelvin_to(unit="F", value=0), -459.67, rel_tol=1e-9)

    print("Tests passés avec succès")
