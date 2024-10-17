def mg_to(*, unit, value):
    #check for aberrant values
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["mg", "g", "kg", "t", "livre", "once"]:
        raise ValueError("L'unité doit être 'mg', 'g', 'kg', 't', 'livre' ou 'once'")
    
    case = {
        "mg": value,
        "g": value / 1000,
        "kg": value / 1000000,
        "t": value / 1000000000,
        "livre": value * 0.00000220462,
        "once": value * 0.000035274,
    }

    return case[unit]

def g_to(*, unit, value):
    #check for aberrant values
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["mg", "g", "kg", "t", "livre", "once"]:
        raise ValueError("L'unité doit être 'mg', 'g', 'kg', 't', 'livre' ou 'once'")

    case = {
        "mg": value * 1000,
        "g": value,
        "kg": value / 1000,
        "t": value / 1000000,
        "livre": value * 0.00220462,
        "once": value * 0.035274,
    }

    return case[unit]

def Kg_to(*, unit, value):
    #check for aberrant values
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["mg", "g", "kg", "t", "livre", "once"]:
        raise ValueError("L'unité doit être 'mg', 'g', 'kg', 't', 'livre' ou 'once'")

    case = {
        "mg": value * 1000000,
        "g": value * 1000,
        "kg": value,
        "t": value / 1000,
        "livre": value * 2.20462,
        "once": value * 35.274,
    }

    return case[unit]

def T_to(*, unit, value):
    #check for aberrant values
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["mg", "g", "kg", "t", "livre", "once"]:
        raise ValueError("L'unité doit être 'mg', 'g', 'kg', 't', 'livre' ou 'once'")
    
    case = {
        "mg": value * 1000000000,
        "g": value * 1000000,
        "kg": value * 1000,
        "t": value,
        "livre": value * 2204.62,
        "once": value * 35274,
    }
    
    return case[unit]

def livre_to(*, unit, value):
    #check for aberrant values
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["mg", "g", "kg", "t", "livre", "once"]:
        raise ValueError("L'unité doit être 'mg', 'g', 'kg', 't', 'livre' ou 'once'")

    case = {
        "mg": value * 453592,
        "g": value * 453.592,
        "kg": value * 0.453592,
        "t": value * 0.000453592,
        "livre": value,
        "once": value * 16,
    }

    return case[unit]

def once_to(*, unit, value):
    #check for aberrant values
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["mg", "g", "kg", "t", "livre", "once"]:
        raise ValueError("L'unité doit être 'mg', 'g', 'kg', 't', 'livre' ou 'once'")
    
    case = {
        "mg": value * 28349.5,
        "g": value * 28.3495,
        "kg": value * 0.0283495,
        "t": value * 0.0000283495,
        "livre": value * 0.0625,
        "once": value,
    }

    return case[unit]
     

if __name__ == "__main__":
    # Test unitaire
    import math

    assert mg_to(unit="mg", value=5) == 5
    assert mg_to(unit="g", value=5) == 0.005
    assert mg_to(unit="kg", value=5) == 0.000005
    assert mg_to(unit="t", value=5) == 0.000000005
    assert math.isclose(mg_to(unit="livre", value=5), 0.0000110231, rel_tol=1e-9)
    assert math.isclose(mg_to(unit="once", value=5), 0.00017637, rel_tol=1e-9)

    assert g_to(unit="mg", value=5) == 5000
    assert g_to(unit="g", value=5) == 5
    assert g_to(unit="kg", value=5) == 0.005
    assert g_to(unit="t", value=5) == 0.000005
    assert math.isclose(g_to(unit="livre", value=5), 0.0110231, rel_tol=1e-9)
    assert math.isclose(g_to(unit="once", value=5), 0.17637, rel_tol=1e-9)

    assert Kg_to(unit="mg", value=5) == 5000000
    assert Kg_to(unit="g", value=5) == 5000
    assert Kg_to(unit="kg", value=5) == 5
    assert Kg_to(unit="t", value=5) == 0.005
    assert math.isclose(Kg_to(unit="livre", value=5), 11.0231, rel_tol=1e-9)
    assert math.isclose(Kg_to(unit="once", value=5), 176.37, rel_tol=1e-9)

    assert T_to(unit="mg", value=5) == 5000000000
    assert T_to(unit="g", value=5) == 5000000
    assert T_to(unit="kg", value=5) == 5000
    assert T_to(unit="t", value=5) == 5
    assert math.isclose(T_to(unit="livre", value=5), 11023.1, rel_tol=1e-9)
    assert math.isclose(T_to(unit="once", value=5), 176370, rel_tol=1e-9)

    assert livre_to(unit="mg", value=5) == 2267960
    assert livre_to(unit="g", value=5) == 2267.96
    assert livre_to(unit="kg", value=5) == 2.26796
    assert livre_to(unit="t", value=5) == 0.00226796
    assert livre_to(unit="livre", value=5) == 5
    assert livre_to(unit="once", value=5) == 80

    assert once_to(unit="mg", value=5) == 141747.5
    assert once_to(unit="g", value=5) == 141.7475
    assert once_to(unit="kg", value=5) == 0.1417475
    assert once_to(unit="t", value=5) == 0.0001417475
    assert once_to(unit="livre", value=5) == 0.3125
    assert once_to(unit="once", value=5) == 5


    print(g_to(unit="mg", value=5))
    print("Les tests ont réussi")    