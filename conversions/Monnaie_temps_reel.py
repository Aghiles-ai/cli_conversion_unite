# Vérifie si la bibliothèque currencyconverter est installée
try:
    from currency_converter import CurrencyConverter
except ImportError:
    # Si ce n'est pas installé, installe-le
    import os
    os.system("pip install --user currencyconverter")
    from currency_converter import CurrencyConverter

# Ton code commence ici
class Monnaie_temps_reel:
    def __init__(self):
        self.units = ["euro", "dollar_americain", "dollar_canadien", "livre_sterling", "yen"]
        # Crée une instance de CurrencyConverter pour récupérer les taux de change en temps réel
        self.converter = CurrencyConverter()

    def get_units(self):
        return self.units
    
    def _validate_input(self, unit, value):
        if not isinstance(value, (int, float)):
            raise TypeError("La valeur doit être un nombre")
        if value < 0:
            raise ValueError("La valeur ne peut pas être négative")
        if unit not in self.units:
            raise ValueError("L'unité doit être :" + ", ".join(self.units))
    
    def _get_real_time_rate(self, from_unit, to_unit):
        """
        Récupère le taux de change en temps réel entre deux unités en utilisant CurrencyConverter.
        """
        # Conversion des noms des unités vers leur code de devise
        currency_codes = {
            "euro": "EUR",
            "dollar_americain": "USD",
            "dollar_canadien": "CAD",
            "livre_sterling": "GBP",
            "yen": "JPY"
        }
        
        from_currency = currency_codes.get(from_unit)
        to_currency = currency_codes.get(to_unit)
        
        if not from_currency or not to_currency:
            raise ValueError(f"Devises inconnues : {from_unit} ou {to_unit}")
        
        # Utilisation de CurrencyConverter pour obtenir le taux en temps réel
        return self.converter.convert(1, from_currency, to_currency)
    
    def euro_to(self, unit, value):
        self._validate_input(unit, value)
        rate = self._get_real_time_rate("euro", unit)
        return value * rate
    
    def dollar_americain_to(self, unit, value):
        self._validate_input(unit, value)
        rate = self._get_real_time_rate("dollar_americain", unit)
        return value * rate
    
    def dollar_canadien_to(self, unit, value):
        self._validate_input(unit, value)
        rate = self._get_real_time_rate("dollar_canadien", unit)
        return value * rate
    
    def livre_sterling_to(self, unit, value):
        self._validate_input(unit, value)
        rate = self._get_real_time_rate("livre_sterling", unit)
        return value * rate
    
    def yen_to(self, unit, value):
        self._validate_input(unit, value)
        rate = self._get_real_time_rate("yen", unit)
        return value * rate

if __name__ == "__main__":
    monnaie = Monnaie_temps_reel()

    # Test de conversion avec des taux en temps réel
    print(monnaie.euro_to("dollar_americain", 1))  # Convertir 1 EUR en USD
    print(monnaie.dollar_americain_to("euro", 1))  # Convertir 1 USD en EUR
    print(monnaie.dollar_canadien_to("yen", 10))   # Convertir 10 CAD en JPY

