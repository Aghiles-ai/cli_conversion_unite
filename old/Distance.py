# Conversion de distances
def mm_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m", "km", "dm", "cm", "mm", "pouce", "pied", "mile"]:
        raise ValueError("L'unité doit être 'm', 'km', 'dm', 'cm', 'mm', 'pouce', 'pied' ou 'mile'")

    case = {
        "m": value / 1000,
        "km": value / 1000000,
        "dm": value / 100,
        "cm": value / 10,
        "mm": value,
        "pouce": value * 0.0393701,
        "pied": value * 0.00328084,
        "mile": value * 0.000000621371,
    }

    return case[unit]


def dm_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m", "km", "dm", "cm", "mm", "pouce", "pied", "mile"]:
        raise ValueError("L'unité doit être 'm', 'km', 'dm', 'cm', 'mm', 'pouce', 'pied' ou 'mile'")

    case = {
        "m": value / 10,
        "km": value / 10000,
        "dm": value,
        "cm": value * 10,
        "mm": value * 100,
        "pouce": value * 3.93701,
        "pied": value * 0.328084,
        "mile": value * 0.0000621371,
    }

    return case[unit]


def pouce_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m", "km", "dm", "cm", "mm", "pouce", "pied", "mile"]:
        raise ValueError("L'unité doit être 'm', 'km', 'dm', 'cm', 'mm', 'pouce', 'pied' ou 'mile'")

    case = {
        "m": value * 0.0254,
        "km": value * 0.0000254,
        "dm": value * 0.254,
        "cm": value * 2.54,
        "mm": value * 25.4,
        "pouce": value,
        "pied": value * 0.0833333,
        "mile": value * 0.0000157828,
    }

    return case[unit]


def pied_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m", "km", "dm", "cm", "mm", "pouce", "pied", "mile"]:
        raise ValueError("L'unité doit être 'm', 'km', 'dm', 'cm', 'mm', 'pouce', 'pied' ou 'mile'")

    case = {
        "m": value * 0.3048,
        "km": value * 0.0003048,
        "dm": value * 3.048,
        "cm": value * 30.48,
        "mm": value * 304.8,
        "pouce": value * 12,
        "pied": value,
        "mile": value * 0.000189394,
    }

    return case[unit]

def m_to(*, unit, value):
    # Vérification des valeurs aberrantes
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m", "km", "dm", "cm", "mm", "pouce", "pied", "mile"]:
        raise ValueError("L'unité doit être 'm', 'km', 'dm', 'cm', 'mm', 'pouce', 'pied' ou 'mile'")

    case = {
        "m": value,
        "km": value / 1000,
        "dm": value * 10,
        "cm": value * 100,
        "mm": value * 1000,
        "pouce": value * 39.3701,
        "pied": value * 3.28084,
        "mile": value * 0.000621371,
    }

    return case[unit]

def km_to(*, unit, value):
    # Vérification des valeurs aberrantes
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m", "km", "dm", "cm", "mm", "pouce", "pied", "mile"]:
        raise ValueError("L'unité doit être 'm', 'km', 'dm', 'cm', 'mm', 'pouce', 'pied' ou 'mile'")

    case = {
        "m": value * 1000,
        "km": value,
        "dm": value * 10000,
        "cm": value * 100000,
        "mm": value * 1000000,
        "pouce": value * 39370.1,
        "pied": value * 3280.84,
        "mile": value * 0.621371,
    }

    return case[unit]

def cm_to(*, unit, value):
    # Vérification des valeurs aberrantes
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m", "km", "dm", "cm", "mm", "pouce", "pied", "mile"]:
        raise ValueError("L'unité doit être 'm', 'km', 'dm', 'cm', 'mm', 'pouce', 'pied' ou 'mile'")

    case = {
        "m": value / 100,
        "km": value / 100000,
        "dm": value / 10,
        "cm": value,
        "mm": value * 10,
        "pouce": value * 0.393701,
        "pied": value * 0.0328084,
        "mile": value * 0.0000062137,
    }

    return case[unit]

def mile_to(*, unit, value):
    # Vérification des valeurs aberrantes
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["m", "km", "dm", "cm", "mm", "pouce", "pied", "mile"]:
        raise ValueError("L'unité doit être 'm', 'km', 'dm', 'cm', 'mm', 'pouce', 'pied' ou 'mile'")

    case = {
        "m": value * 1609.34,
        "km": value * 1.60934,
        "dm": value * 16093.4,
        "cm": value * 160934,
        "mm": value * 1609340,
        "pouce": value * 63360,
        "pied": value * 5280,
        "mile": value,
    }

    return case[unit]

if __name__ == "__main__":
    # Test unitaire pour m_to, km_to, cm_to, mile_to (déjà existants)
    import math

    # Tests pour m_to
    assert m_to(unit="m", value=5) == 5
    assert m_to(unit="km", value=5) == 0.005
    assert math.isclose(m_to(unit="pied", value=5), 16.4042, rel_tol=1e-2)

    # Tests pour km_to
    assert km_to(unit="m", value=5) == 5000
    assert math.isclose(km_to(unit="mile", value=5), 3.10686, rel_tol=1e-2)

    # Tests pour cm_to
    assert cm_to(unit="mm", value=5) == 50
    assert math.isclose(cm_to(unit="pouce", value=5), 1.968505, rel_tol=1e-2)

    # Tests pour mile_to
    assert math.isclose(mile_to(unit="km", value=5), 8.0467, rel_tol=1e-2)

    # Tests pour mm_to
    assert mm_to(unit="m", value=5) == 0.005
    assert mm_to(unit="cm", value=5) == 0.5
    assert math.isclose(mm_to(unit="pouce", value=5), 0.19685, rel_tol=1e-2)

    # Tests pour dm_to
    assert dm_to(unit="m", value=5) == 0.5
    assert dm_to(unit="km", value=5) == 0.0005
    assert math.isclose(dm_to(unit="pouce", value=5), 19.685, rel_tol=1e-2)

    # Tests pour pouce_to
    assert pouce_to(unit="m", value=5) == 0.127
    assert pouce_to(unit="cm", value=5) == 12.7
    assert math.isclose(pouce_to(unit="mile", value=5), 0.000078914, rel_tol=1e-2)

    # Tests pour pied_to
    assert pied_to(unit="m", value=5) == 1.524
    assert pied_to(unit="cm", value=5) == 152.4
    assert math.isclose(pied_to(unit="mile", value=5), 0.00094697, rel_tol=1e-2)

    print("Tous les tests ont réussi !")

