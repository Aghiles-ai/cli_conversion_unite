# Projet de Conversion de Mesures

Ce projet contient des scripts Python pour convertir différentes unités de mesure, y compris la température, la distance et le poids.

## Lien vers le projet

Trello : [Lien vers le Trello](https://trello.com/b/qARpQtj5/ueprocessusdud%C3%A9veloppementlo)

Google doc : [Lien vers le google doc](https://docs.google.com/document/d/15TDHAYLjEUg6Lcgy5mWOdMLP7plT2saxSefvznrAIZE/edit?tab=t.0)

## Fonctionnalités

Ce projet propose plusieurs modules pour effectuer des conversions dans différentes unités de mesure. Voici les fonctionnalités disponibles :

### Conversions

- **Distance** : Convertit entre différentes unités de distance (mètres, kilomètres, miles, etc.).
  - Implémenté dans [conversions/Distance.py](conversions/Distance.py)
  
- **Monnaie (hors ligne)** : Convertit entre différentes devises (euros, dollars, yens, etc.) en utilisant des taux de change fixes.
  - Implémenté dans [conversions/Monnaie_hors_ligne.py](conversions/Monnaie_hors_ligne.py)
  
- **Monnaie (temps réel)** : Convertit entre différentes devises (euros, dollars, yens, etc.) en utilisant des taux de change en temps réel.
  - Implémenté dans [conversions/Monnaie_temps_reel.py](conversions/Monnaie_temps_reel.py)
  
- **Poids** : Convertit entre différentes unités de poids (grammes, kilogrammes, livres, etc.).
  - Implémenté dans [conversions/Poids.py](conversions/Poids.py)
  
- **Surface** : Convertit entre différentes unités de surface (mètres carrés, hectares, acres, etc.).
  - Implémenté dans [conversions/Surface.py](conversions/Surface.py)
  
- **Température** : Convertit entre différentes unités de température (Celsius, Fahrenheit, Kelvin, etc.).
  - Implémenté dans [conversions/Temperature.py](conversions/Temperature.py)

### Menu

- **Menu Principal** : Interface utilisateur pour accéder aux différentes conversions.
  - Implémenté dans [Menu_V2.py](Menu_V2.py)


### Favoris

- **Favoris** : Suivi des conversions les plus utilisées et affichage des favoris dans le menu principal. Le fichier contenants les favoris est peut etre trouver dans `conversion/favoris.csv`
  - Implémenté dans [Menu_V2.py](Menu_V2.py)