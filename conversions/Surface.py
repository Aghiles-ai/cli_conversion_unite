class Surface:
    def __init__(self):
        self.units = ["m2", "km2", "hectare", "acre", "p2", "mile2", "pouce2"]

    def get_units(self):
        return self.units

    def _validate_input(self, unit, value):
        if not isinstance(value, (int, float)):
            raise TypeError("La valeur doit être un nombre")
        if value < 0:
            raise ValueError("La valeur ne peut pas être négative")
        if unit not in self.units:
            raise ValueError(f"L'unité doit être parmi {self.units}")

    def m2_to(self, unit, value):
        self._validate_input(unit, value)
        
        case = {
            "m2": value,
            "km2": value / 1_000_000,
            "hectare": value / 10_000,
            "acre": value / 4046.86,
            "p2": value * 10.7639,
            "mile2": value / 2_589_988.11,
            "pouce2": value * 1550.0031,
        }
        
        return case[unit]

    def km2_to(self, unit, value):
        self._validate_input(unit, value)
        
        case = {
            "m2": value * 1_000_000,
            "km2": value,
            "hectare": value * 100,
            "acre": value * 247.105,
            "p2": value * 1.076e+7,
            "mile2": value / 2.58999,
            "pouce2": value * 1.55e+9,
        }
        
        return case[unit]

    def hectare_to(self, unit, value):
        self._validate_input(unit, value)
        
        case = {
            "m2": value * 10_000,
            "km2": value / 100,
            "hectare": value,
            "acre": value * 2.47105,
            "p2": value * 107_639,
            "mile2": value / 258.998811,
            "pouce2": value * 1.55e+7,
        }
        
        return case[unit]

    def acre_to(self, unit, value):
        self._validate_input(unit, value)
        
        case = {
            "m2": value * 4046.86,
            "km2": value / 247.105,
            "hectare": value / 2.47105,
            "acre": value,
            "p2": value * 43_560,
            "mile2": value / 640,
            "pouce2": value * 6.273e+6,
        }
        
        return case[unit]

    def p2_to(self, unit, value):
        self._validate_input(unit, value)
        
        case = {
            "m2": value / 10.7639,
            "km2": value / 1.076e+7,
            "hectare": value / 107_639,
            "acre": value / 43_560,
            "p2": value,
            "mile2": value / 27_878_400,
            "pouce2": value * 144,
        }
        
        return case[unit]

    def pouce2_to(self, unit, value):
        self._validate_input(unit, value)
        
        case = {
            "m2": value * 0.00064516,
            "km2": value * 6.4516e-10,
            "hectare": value * 6.4516e-8,
            "acre": value * 1.59423e-7,
            "p2": value * 0.00694444,
            "mile2": value * 2.49098e-10,
            "pouce2": value,
        }
        
        return case[unit]

    def mile2_to(self, unit, value):
        self._validate_input(unit, value)
        
        case = {
            "m2": value * 2_589_988.11,
            "km2": value * 2.58999,
            "hectare": value * 258.998811,
            "acre": value * 640,
            "p2": value * 27_878_400,
            "mile2": value,
            "pouce2": value * 4_014_489_600,
        }
        
        return case[unit]


if __name__ == "__main__":
    # Vérifie si la bibliothèque est installée
    try:
        import math
    except ImportError:
        # Si ce n'est pas installé, installe-le
        import os
        os.system("pip install --user math")
        import math

    surface = Surface()

    # Tests pour mile2_to
    assert math.isclose(surface.mile2_to("m2", 1), 2_589_988.11, rel_tol=1e-2)
    assert math.isclose(surface.mile2_to("p2", 1), 27_878_400, rel_tol=1e-2)
    assert math.isclose(surface.mile2_to("pouce2", 1), 4_014_489_600, rel_tol=1e-2)

    # Tests pour pouce2_to
    assert math.isclose(surface.pouce2_to("m2", 1), 0.00064516, rel_tol=1e-2)
    assert math.isclose(surface.pouce2_to("p2", 1), 0.00694444, rel_tol=1e-2)
    assert math.isclose(surface.pouce2_to("mile2", 1), 2.49098e-10, rel_tol=1e-2)

    # Tests pour m2_to
    assert surface.m2_to("km2", 1_000_000) == 1
    assert math.isclose(surface.m2_to("acre", 4046.86), 1, rel_tol=1e-2)
    assert math.isclose(surface.m2_to("p2", 1), 10.76, rel_tol=1e-2)

    # Tests pour km2_to
    assert surface.km2_to("m2", 1) == 1_000_000
    assert math.isclose(surface.km2_to("acre", 1), 247.105, rel_tol=1e-2)

    # Tests pour hectare_to
    assert surface.hectare_to("m2", 1) == 10_000
    assert math.isclose(surface.hectare_to("acre", 1), 2.47105, rel_tol=1e-2)

    # Tests pour acre_to
    assert surface.acre_to("m2", 1) == 4046.86
    assert math.isclose(surface.acre_to("hectare", 1), 0.404686, rel_tol=1e-2)

    # Tests pour p2_to
    assert surface.p2_to("m2", 10.7639) == 1
    assert math.isclose(surface.p2_to("acre", 43_560), 1, rel_tol=1e-2)

    print("Tous les tests ont réussi !")
