class Distance:
    def __init__(self):
        self.units = ["m", "km", "dm", "cm", "mm", "pouce", "pied", "mille"]

    def get_units(self):
        return self.units

    def _validate_input(self, unit, value):
        if not isinstance(value, (int, float)):
            raise TypeError("La valeur doit être un nombre")
        if value < 0:
            raise ValueError("La valeur ne peut pas être négative")
        if unit not in self.units:
            raise ValueError(f"L'unité doit être l'une des suivantes : {', '.join(self.units)}")

    def mm_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "m": value / 1000,
            "km": value / 1000000,
            "dm": value / 100,
            "cm": value / 10,
            "mm": value,
            "pouce": value * 0.0393701,
            "pied": value * 0.00328084,
            "mille": value * 0.000000621371,
        }
        return case[unit]

    def dm_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "m": value / 10,
            "km": value / 10000,
            "dm": value,
            "cm": value * 10,
            "mm": value * 100,
            "pouce": value * 3.93701,
            "pied": value * 0.328084,
            "mille": value * 0.0000621371,
        }
        return case[unit]

    def pouce_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "m": value * 0.0254,
            "km": value * 0.0000254,
            "dm": value * 0.254,
            "cm": value * 2.54,
            "mm": value * 25.4,
            "pouce": value,
            "pied": value * 0.0833333,
            "mille": value * 0.0000157828,
        }
        return case[unit]

    def pied_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "m": value * 0.3048,
            "km": value * 0.0003048,
            "dm": value * 3.048,
            "cm": value * 30.48,
            "mm": value * 304.8,
            "pouce": value * 12,
            "pied": value,
            "mille": value * 0.000189394,
        }
        return case[unit]

    def m_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "m": value,
            "km": value / 1000,
            "dm": value * 10,
            "cm": value * 100,
            "mm": value * 1000,
            "pouce": value * 39.3701,
            "pied": value * 3.28084,
            "mille": value * 0.000621371,
        }
        return case[unit]

    def km_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "m": value * 1000,
            "km": value,
            "dm": value * 10000,
            "cm": value * 100000,
            "mm": value * 1000000,
            "pouce": value * 39370.1,
            "pied": value * 3280.84,
            "mille": value * 0.621371,
        }
        return case[unit]

    def cm_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "m": value / 100,
            "km": value / 100000,
            "dm": value / 10,
            "cm": value,
            "mm": value * 10,
            "pouce": value * 0.393701,
            "pied": value * 0.0328084,
            "mille": value * 0.0000062137,
        }
        return case[unit]

    def mille_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "m": value * 1609.34,
            "km": value * 1.60934,
            "dm": value * 16093.4,
            "cm": value * 160934,
            "mm": value * 1609340,
            "pouce": value * 63360,
            "pied": value * 5280,
            "mille": value,
        }
        return case[unit]

if __name__ == "__main__":
    import math

    d = Distance()

    # Tests
    assert d.m_to("m", 5) == 5
    assert d.m_to("km", 5) == 0.005
    assert math.isclose(d.m_to("pied", 5), 16.4042, rel_tol=1e-2)

    assert d.km_to("m", 5) == 5000
    assert math.isclose(d.km_to("mille", 5), 3.10686, rel_tol=1e-2)

    assert d.cm_to("mm", 5) == 50
    assert math.isclose(d.cm_to("pouce", 5), 1.968505, rel_tol=1e-2)

    assert math.isclose(d.mille_to("km", 5), 8.0467, rel_tol=1e-2)

    assert d.mm_to("m", 5) == 0.005
    assert d.mm_to("cm", 5) == 0.5
    assert math.isclose(d.mm_to("pouce", 5), 0.19685, rel_tol=1e-2)

    assert d.dm_to("m", 5) == 0.5
    assert d.dm_to("km", 5) == 0.0005
    assert math.isclose(d.dm_to("pouce", 5), 19.685, rel_tol=1e-2)

    assert d.pouce_to("m", 5) == 0.127
    assert d.pouce_to("cm", 5) == 12.7
    assert math.isclose(d.pouce_to("mille", 5), 0.000078914, rel_tol=1e-2)

    assert d.pied_to("m", 5) == 1.524
    assert d.pied_to("cm", 5) == 152.4
    assert math.isclose(d.pied_to("mille", 5), 0.00094697, rel_tol=1e-2)

    print("Tous les tests ont réussi !")