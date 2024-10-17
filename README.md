# Projet de Conversion de Mesures

Ce projet contient des scripts Python pour convertir différentes unités de mesure, y compris la température, la distance et le poids.

## Lien vers le projet

Trello : [Lien vers le Trello](https://trello.com/b/qARpQtj5/ueprocessusdud%C3%A9veloppementlo)

Google doc : [Lien vers le google doc](https://docs.google.com/document/d/15TDHAYLjEUg6Lcgy5mWOdMLP7plT2saxSefvznrAIZE/edit?tab=t.0)

## Fonctionnalités

### Conversion de Température

Le fichier [Temperature.py](Temperature.py) contient des fonctions pour convertir les températures entre Celsius, Fahrenheit et Kelvin.

### Conversion de Distance

Le fichier [Distance.py](Distance.py) contient des fonctions pour convertir les distances entre différentes unités (par exemple, mètres, kilomètres, miles).

### Conversion de Poids

Le fichier [Poids.py](Poids.py) contient des fonctions pour convertir les poids entre différentes unités (par exemple, grammes, kilogrammes, livres).

### Conversion de la surface

Le fichier [Surface.py](Surface.py) contient des fonctions pour convertir les surfaces entre différentes unités (par exemple, mètres carrés, kilomètres carrés, acres).

### Conversion de la monnaie

Le fichier [Money.py](Money.py) contient des fonctions pour convertir les devises entre différentes unités (par exemple, USD, EUR, GBP).

## Utilisation

Pour utiliser les fonctions de conversion, importez les modules nécessaires dans votre script Python et appelez les fonctions avec les paramètres appropriés.

Exemple d'utilisation pour convertir des températures :

```python
from Temperature import celsius_to, fahrenheit_to

# Convertir 100 Celsius en Fahrenheit
print(celsius_to(unit='f', value=100))

# Convertir 212 Fahrenheit en Celsius
print(fahrenheit_to(unit='c', value=212))
```