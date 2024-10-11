# Fonction pour convertir Celsius en Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

# Fonction pour convertir Fahrenheit en Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

# Fonction pour convertir Celsius en Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Fonction pour convertir Kelvin en Celsius
def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("La température en Kelvin ne peut pas être négative.")
    return kelvin - 273.15

# Fonction pour convertir Fahrenheit en Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

# Fonction pour convertir Kelvin en Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    if kelvin < 0:
        raise ValueError("La température en Kelvin ne peut pas être négative.")
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

# Programme principal
value = float(input("Entrez la température à convertir : "))
from_unit = input("Entrez l'unité actuelle (C pour Celsius, F pour Fahrenheit, K pour Kelvin) : ").upper()
to_unit = input("Entrez l'unité de destination (C pour Celsius, F pour Fahrenheit, K pour Kelvin) : ").upper()

try:
    if from_unit == 'C' and to_unit == 'F':
        result = celsius_to_fahrenheit(value)
        print(f'{value}°C est égal à {result}°F')
    elif from_unit == 'C' and to_unit == 'K':
        result = celsius_to_kelvin(value)
        print(f'{value}°C est égal à {result} K')
    elif from_unit == 'F' and to_unit == 'C':
        result = fahrenheit_to_celsius(value)
        print(f'{value}°F est égal à {result}°C')
    elif from_unit == 'F' and to_unit == 'K':
        result = fahrenheit_to_kelvin(value)
        print(f'{value}°F est égal à {result} K')
    elif from_unit == 'K' and to_unit == 'C':
        if value < 0:
            print("Erreur : la température en Kelvin ne peut pas être négative.")
        else:
            result = kelvin_to_celsius(value)
            print(f'{value} K est égal à {result}°C')
    elif from_unit == 'K' and to_unit == 'F':
        if value < 0:
            print("Erreur : la température en Kelvin ne peut pas être négative.")
        else:
            result = kelvin_to_fahrenheit(value)
            print(f'{value} K est égal à {result}°F')
    else:
        print("Conversion non supportée ou unité non valide. Veuillez entrer 'C', 'F' ou 'K'.")
except ValueError as e:
    print(e)
