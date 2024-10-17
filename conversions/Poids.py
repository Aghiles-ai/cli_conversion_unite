class Poids:
    def __init__(self):
        self.units = ["mg", "g", "kg", "t", "livre", "once"]

    def get_units(self):
        return self.units

    def _validate_input(self, unit, value):
        if not isinstance(value, (int, float)):
            raise TypeError("La valeur doit être un nombre")
        if value < 0:
            raise ValueError("La valeur ne peut pas être négative")
        if unit not in self.units:
            raise ValueError("L'unité doit être 'mg', 'g', 'kg', 't', 'livre' ou 'once'")

    def mg_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "mg": value,
            "g": value / 1000,
            "kg": value / 1000000,
            "t": value / 1000000000,
            "livre": value * 0.00000220462,
            "once": value * 0.000035274,
        }
        return case[unit]

    def g_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "mg": value * 1000,
            "g": value,
            "kg": value / 1000,
            "t": value / 1000000,
            "livre": value * 0.00220462,
            "once": value * 0.035274,
        }
        return case[unit]

    def kg_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "mg": value * 1000000,
            "g": value * 1000,
            "kg": value,
            "t": value / 1000,
            "livre": value * 2.20462,
            "once": value * 35.274,
        }
        return case[unit]

    def t_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "mg": value * 1000000000,
            "g": value * 1000000,
            "kg": value * 1000,
            "t": value,
            "livre": value * 2204.62,
            "once": value * 35274,
        }
        return case[unit]

    def livre_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "mg": value * 453592,
            "g": value * 453.592,
            "kg": value * 0.453592,
            "t": value * 0.000453592,
            "livre": value,
            "once": value * 16,
        }
        return case[unit]

    def once_to(self, unit, value):
        self._validate_input(unit, value)
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
    import math

    poids = Poids()

    assert poids.mg_to("mg", 5) == 5
    assert poids.mg_to("g", 5) == 0.005
    assert poids.mg_to("kg", 5) == 0.000005
    assert poids.mg_to("t", 5) == 0.000000005
    assert math.isclose(poids.mg_to("livre", 5), 0.0000110231, rel_tol=1e-9)
    assert math.isclose(poids.mg_to("once", 5), 0.00017637, rel_tol=1e-9)

    assert poids.g_to("mg", 5) == 5000
    assert poids.g_to("g", 5) == 5
    assert poids.g_to("kg", 5) == 0.005
    assert poids.g_to("t", 5) == 0.000005
    assert math.isclose(poids.g_to("livre", 5), 0.0110231, rel_tol=1e-9)
    assert math.isclose(poids.g_to("once", 5), 0.17637, rel_tol=1e-9)

    assert poids.kg_to("mg", 5) == 5000000
    assert poids.kg_to("g", 5) == 5000
    assert poids.kg_to("kg", 5) == 5
    assert poids.kg_to("t", 5) == 0.005
    assert math.isclose(poids.kg_to("livre", 5), 11.0231, rel_tol=1e-9)
    assert math.isclose(poids.kg_to("once", 5), 176.37, rel_tol=1e-9)

    assert poids.t_to("mg", 5) == 5000000000
    assert poids.t_to("g", 5) == 5000000
    assert poids.t_to("kg", 5) == 5000
    assert poids.t_to("t", 5) == 5
    assert math.isclose(poids.t_to("livre", 5), 11023.1, rel_tol=1e-9)
    assert math.isclose(poids.t_to("once", 5), 176370, rel_tol=1e-9)

    assert poids.livre_to("mg", 5) == 2267960
    assert poids.livre_to("g", 5) == 2267.96
    assert poids.livre_to("kg", 5) == 2.26796
    assert poids.livre_to("t", 5) == 0.00226796
    assert poids.livre_to("livre", 5) == 5
    assert poids.livre_to("once", 5) == 80

    assert poids.once_to("mg", 5) == 141747.5
    assert poids.once_to("g", 5) == 141.7475
    assert poids.once_to("kg", 5) == 0.1417475
    assert poids.once_to("t", 5) == 0.0001417475
    assert poids.once_to("livre", 5) == 0.3125
    assert poids.once_to("once", 5) == 5

    print("Les tests ont réussi")
