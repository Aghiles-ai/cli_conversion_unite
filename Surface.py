# Conversion des surfaces
def m2_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m²", "km²", "hectare", "acre", "p²", "mile²", "pouce²"]:
        raise ValueError("L'unité doit être 'm²', 'km²', 'hectare', 'acre', 'p²', 'mile²', ou 'pouce²'")
    
    case = {
        "m²": value,
        "km²": value / 1_000_000,
        "hectare": value / 10_000,
        "acre": value / 4046.86,
        "p²": value * 10.7639,
        "mile²": value / 2_589_988.11,
        "pouce²": value * 1550.0031,
    }
    
    return case[unit]


def km2_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m²", "km²", "hectare", "acre", "p²", "mile²", "pouce²"]:
        raise ValueError("L'unité doit être 'm²', 'km²', 'hectare', 'acre', 'p²', 'mile²', ou 'pouce²'")
    
    case = {
        "m²": value * 1_000_000,
        "km²": value,
        "hectare": value * 100,
        "acre": value * 247.105,
        "p²": value * 1.076e+7,
        "mile²": value / 2.58999,
        "pouce²": value * 1.55e+9,
    }
    
    return case[unit]


def hectare_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m²", "km²", "hectare", "acre", "p²", "mile²", "pouce²"]:
        raise ValueError("L'unité doit être 'm²', 'km²', 'hectare', 'acre', 'p²', 'mile²', ou 'pouce²'")
    
    case = {
        "m²": value * 10_000,
        "km²": value / 100,
        "hectare": value,
        "acre": value * 2.47105,
        "p²": value * 107_639,
        "mile²": value / 258.998811,
        "pouce²": value * 1.55e+7,
    }
    
    return case[unit]


def acre_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m²", "km²", "hectare", "acre", "p²", "mile²", "pouce²"]:
        raise ValueError("L'unité doit être 'm²', 'km²', 'hectare', 'acre', 'p²', 'mile²', ou 'pouce²'")
    
    case = {
        "m²": value * 4046.86,
        "km²": value / 247.105,
        "hectare": value / 2.47105,
        "acre": value,
        "p²": value * 43_560,
        "mile²": value / 640,
        "pouce²": value * 6.273e+6,
    }
    
    return case[unit]


def p2_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m²", "km²", "hectare", "acre", "p²", "mile²", "pouce²"]:
        raise ValueError("L'unité doit être 'm²', 'km²', 'hectare', 'acre', 'p²', 'mile²', ou 'pouce²'")
    
    case = {
        "m²": value / 10.7639,
        "km²": value / 1.076e+7,
        "hectare": value / 107_639,
        "acre": value / 43_560,
        "p²": value,
        "mile²": value / 27_878_400,
        "pouce²": value * 144,
    }
    
    return case[unit]
def pouce2_to(*, unit, value):
    # Vérification des valeurs aberrantes
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m²", "km²", "hectare", "acre", "p²", "mile²", "pouce²"]:
        raise ValueError("L'unité doit être 'm²', 'km²', 'hectare', 'acre', 'p²', 'mile²', ou 'pouce²'")

    case = {
        "m²": value * 0.00064516,
        "km²": value * 6.4516e-10,
        "hectare": value * 6.4516e-8,
        "acre": value * 1.59423e-7,
        "p²": value * 0.00694444,
        "mile²": value * 2.49098e-10,
        "pouce²": value,
    }

    return case[unit]
def mile2_to(*, unit, value):
    # Vérification des valeurs aberrantes
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m²", "km²", "hectare", "acre", "p²", "mile²", "pouce²"]:
        raise ValueError("L'unité doit être 'm²', 'km²', 'hectare', 'acre', 'p²', 'mile²', ou 'pouce²'")

    case = {
        "m²": value * 2_589_988.11,
        "km²": value * 2.58999,
        "hectare": value * 258.998811,
        "acre": value * 640,
        "p²": value * 27_878_400,
        "mile²": value,
        "pouce²": value * 4_014_489_600,
    }

    return case[unit]
if __name__ == "__main__":
    import math
    
    # Tests pour mile2_to
    assert math.isclose(mile2_to(unit="m²", value=1), 2_589_988.11, rel_tol=1e-2)
    assert math.isclose(mile2_to(unit="p²", value=1), 27_878_400, rel_tol=1e-2)
    assert math.isclose(mile2_to(unit="pouce²", value=1), 4_014_489_600, rel_tol=1e-2)

    # Tests pour pouce2_to
    assert math.isclose(pouce2_to(unit="m²", value=1), 0.00064516, rel_tol=1e-2)
    assert math.isclose(pouce2_to(unit="p²", value=1), 0.00694444, rel_tol=1e-2)
    assert math.isclose(pouce2_to(unit="mile²", value=1), 2.49098e-10, rel_tol=1e-2)

    # Tests pour m2_to
    assert m2_to(unit="km²", value=1_000_000) == 1
    assert math.isclose(m2_to(unit="acre", value=4046.86), 1, rel_tol=1e-2)
    assert math.isclose(m2_to(unit="p²", value=1), 10.76, rel_tol=1e-2)

    # Tests pour km2_to
    assert km2_to(unit="m²", value=1) == 1_000_000
    assert math.isclose(km2_to(unit="acre", value=1), 247.105, rel_tol=1e-2)

    # Tests pour hectare_to
    assert hectare_to(unit="m²", value=1) == 10_000
    assert math.isclose(hectare_to(unit="acre", value=1), 2.47105, rel_tol=1e-2)

    # Tests pour acre_to
    assert acre_to(unit="m²", value=1) == 4046.86
    assert math.isclose(acre_to(unit="hectare", value=1), 0.404686, rel_tol=1e-2)

    # Tests pour p2_to
    assert p2_to(unit="m²", value=10.7639) == 1
    assert math.isclose(p2_to(unit="acre", value=43_560), 1, rel_tol=1e-2)

    print("Tous les tests ont réussi !")
