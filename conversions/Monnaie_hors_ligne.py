class Monnaie_hors_ligne:
    def __init__(self):
        self.units = ["euro", "dollar_americain", "dollar_canadien", "livre_sterling", "yen"]

    def get_units(self):
        return self.units
    
    def _validate_input(self, unit, value):
        if not isinstance(value, (int, float)):
            raise TypeError("La valeur doit être un nombre")
        if value < 0:
            raise ValueError("La valeur ne peut pas être négative")
        if unit not in self.units:
            raise ValueError("L'unité doit être :" + ", ".join(self.units))
        
    def euro_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "euro": value,
            "dollar_americain": value * 1.18,
            "dollar_canadien": value * 1.48,
            "livre_sterling": value * 0.86,
            "yen": value * 129.29,
        }
        return case[unit]
    
    def dollar_americain_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "euro": value * 0.85,
            "dollar_americain": value,
            "dollar_canadien": value * 1.25,
            "livre_sterling": value * 0.73,
            "yen": value * 109.73,
        }
        return case[unit]
    
    def dollar_canadien_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "euro": value * 0.68,
            "dollar_americain": value * 0.80,
            "dollar_canadien": value,
            "livre_sterling": value * 0.58,
            "yen": value * 86.85,
        }
        return case[unit]
    
    def livre_sterling_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "euro": value * 1.16,
            "dollar_americain": value * 1.37,
            "dollar_canadien": value * 1.72,
            "livre_sterling": value,
            "yen": value * 149.57,
        }
        return case[unit]
    
    def yen_to(self, unit, value):
        self._validate_input(unit, value)
        case = {
            "euro": value * 0.0077,
            "dollar_americain": value * 0.0091,
            "dollar_canadien": value * 0.0115,
            "livre_sterling": value * 0.0067,
            "yen": value,
        }
        return case[unit]
    
if __name__ == "__main__":
    import math

    monnaie = Monnaie_hors_ligne()

    assert monnaie.euro_to("dollar_americain", 1) == 1.18
    assert monnaie.euro_to("dollar_canadien", 1) == 1.48
    assert monnaie.euro_to("livre_sterling", 1) == 0.86
    assert monnaie.euro_to("yen", 1) == 129.29

    assert monnaie.dollar_americain_to("euro", 1) == 0.85
    assert monnaie.dollar_americain_to("dollar_canadien", 1) == 1.25
    assert monnaie.dollar_americain_to("livre_sterling", 1) == 0.73
    assert monnaie.dollar_americain_to("yen", 1) == 109.73

    assert monnaie.dollar_canadien_to("euro", 1) == 0.68
    assert monnaie.dollar_canadien_to("dollar_americain", 1) == 0.80
    assert monnaie.dollar_canadien_to("livre_sterling", 1) == 0.58
    assert monnaie.dollar_canadien_to("yen", 1) == 86.85

    assert monnaie.livre_sterling_to("euro", 1) == 1.16
    assert monnaie.livre_sterling_to("dollar_americain", 1) == 1.37
    assert monnaie.livre_sterling_to("dollar_canadien", 1) == 1.72
    assert monnaie.livre_sterling_to("yen", 1) == 149.57

    assert monnaie.yen_to("euro", 1) == 0.0077
    assert monnaie.yen_to("dollar_americain", 1) == 0.0091
    assert monnaie.yen_to("dollar_canadien", 1) == 0.0115
    assert monnaie.yen_to("livre_sterling", 1) == 0.0067
    assert monnaie.yen_to("yen", 1) == 1

    print("Tous les tests ont réussi.")
        
