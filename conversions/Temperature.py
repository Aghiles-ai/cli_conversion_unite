class Temperature:
    def __init__(self):
        self.units = ["celsius", "fahrenheit", "kelvin"]

    def get_units(self):
        return self.units

    def _validate_input(self, unit, value):
        if not isinstance(value, (int, float)):
            raise TypeError("La valeur doit être un nombre")
        if unit not in self.units:
            raise ValueError("L'unité doit être 'celsius', 'fahrenheit' ou 'kelvin'")

    def celsius_to(self, unit, value):
        self._validate_input(unit, value)
        if value < -273.15:
            raise ValueError("La température en Celsius ne peut pas être inférieure à -273.15°C")
        
        case = {
            "celsius": value,
            "fahrenheit": (value * 9.0/5.0) + 32,
            "kelvin": value + 273.15,
        }
        
        return case[unit]

    def fahrenheit_to(self, unit, value):
        self._validate_input(unit, value)
        if value < -459.67:
            raise ValueError("La température en Fahrenheit ne peut pas être inférieure à -459.67°F")
        
        case = {
            "celsius": (value - 32) * 5.0/9.0,
            "fahrenheit": value,
            "kelvin": (value - 32) * 5.0/9.0 + 273.15,
        }
        
        return case[unit]

    def kelvin_to(self, unit, value):
        self._validate_input(unit, value)
        if value < 0:
            raise ValueError("La température en Kelvin ne peut pas être inférieure à 0K")
        
        case = {
            "celsius": value - 273.15,
            "fahrenheit": (value - 273.15) * 9.0/5.0 + 32,
            "kelvin": value,
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
    

    temp = Temperature()

    assert temp.celsius_to("fahrenheit", 0) == 32
    assert temp.celsius_to("kelvin", 0) == 273.15

    assert math.isclose(temp.fahrenheit_to("celsius", 0), -17.77777777777778, rel_tol=1e-9)
    assert math.isclose(temp.fahrenheit_to("kelvin", 0), 255.3722222222222, rel_tol=1e-9)

    assert math.isclose(temp.kelvin_to("celsius", 0), -273.15, rel_tol=1e-9)
    assert math.isclose(temp.kelvin_to("fahrenheit", 0), -459.67, rel_tol=1e-9)

    print("Tests passés avec succès")