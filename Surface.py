# Conversion de surfaces
def m2_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m²", "km²", "hectare", "acre", "p²"]:
        raise ValueError("L'unité doit être 'm²', 'km²', 'hectare', 'acre' ou 'p²'")
    
    case = {
        "m²": value,
        "km²": value / 1_000_000,
        "hectare": value / 10_000,
        "acre": value / 4046.86,
        "p²": value * 10.7639,
    }
    
    return case[unit]


def km2_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m²", "km²", "hectare", "acre", "p²"]:
        raise ValueError("L'unité doit être 'm²', 'km²', 'hectare', 'acre' ou 'p²'")
    
    case = {
        "m²": value * 1_000_000,
        "km²": value,
        "hectare": value * 100,
        "acre": value * 247.105,
        "p²": value * 1.076e+7,
    }
    
    return case[unit]


def hectare_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m²", "km²", "hectare", "acre", "p²"]:
        raise ValueError("L'unité doit être 'm²', 'km²', 'hectare', 'acre' ou 'p²'")
    
    case = {
        "m²": value * 10_000,
        "km²": value / 100,
        "hectare": value,
        "acre": value * 2.47105,
        "p²": value * 107639,
    }
    
    return case[unit]


def acre_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m²", "km²", "hectare", "acre", "p²"]:
        raise ValueError("L'unité doit être 'm²', 'km²', 'hectare', 'acre' ou 'p²'")
    
    case = {
        "m²": value * 4046.86,
        "km²": value / 247.105,
        "hectare": value / 2.47105,
        "acre": value,
        "p²": value * 43560,
    }
    
    return case[unit]


def p2_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m²", "km²", "hectare", "acre", "p²"]:
        raise ValueError("L'unité doit être 'm²', 'km²', 'hectare', 'acre' ou 'p²'")
    
    case = {
        "m²": value / 10.7639,
        "km²": value / 1.076e+7,
        "hectare": value / 107639,
        "acre": value / 43560,
        "p²": value,
    }
    
    return case[unit]


# Tests unitaires pour les conversions de surface
if __name__ == "__main__":
    import math

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
    assert math.isclose(p2_to(unit="acre", value=43560), 1, rel_tol=1e-2)

    print("Tous les tests ont réussi !")
