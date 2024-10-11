import Poids



dict_poids = {
    1: "mg",
    2: "g",
    3: "kg",
    4: "t",
    5: "livre",
    6: "once"
}

dict_temp ={
    1: "c",
    2: "f",
    3: "k"
}

def main():
    while True:  # Boucle principale pour permettre un retour au menu
        print("Choisissez le type d'unité que vous voulez")
        print("1 : masse")
        print("2 : température")
        print("0 : quitter")  # Option pour quitter le programme

        num = int(input("Entrez le numéro qui vous convient : "))
        while num < 0 or num > 2:  # Validation de l'entrée
            print("Votre choix n'est pas valide, choisissez entre 0 et 2.")
            num = int(input("Entrez le numéro qui vous convient : "))
        
        if num == 0:  # Quitte le programme
            print("Merci et à bientôt !")
            break

        if num == 1:  # Gestion de la masse
            while True:  # Boucle pour choisir l'unité de masse
                print("Choisissez l'unité de départ")
                print("1 : mg")
                print("2 : g")
                print("3 : kg")
                print("4 : t")
                print("5 : livre")
                print("6 : once")
                print("0 : retour")
                unit = int(input("Entrez le numéro qui vous convient : "))

                if unit == 0:
                    break  # Retourne au choix du type d'unité
                elif unit < 1 or unit > 6:
                    print("Votre choix n'est pas valide, choisissez entre 0 et 6.")
                else:
                    # Choisir l'unité de résultat
                    while True:
                        print("Choisissez l'unité de résultat")
                        print("1 : mg")
                        print("2 : g")
                        print("3 : kg")
                        print("4 : t")
                        print("5 : livre")
                        print("6 : onces")
                        print("0 : retour")
                        unit_res = int(input("Entrez le numéro qui vous convient : "))
                        
                        if unit_res == 0:
                            break  # Retourne au choix du type d'unité
                        elif unit_res < 1 or unit_res > 6:
                            print("Votre choix n'est pas valide, choisissez entre 0 et 6.")
                        else:

                            print(dict_poids[unit]," => " ,dict_poids[unit_res])
                            value = float(input("valeur= "))

                            unit = dict_poids[unit]
                            unit_res= dict_poids[unit_res]
                            match unit:
                                case "mg":
                                    resulat=Poids.mg_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)
                                
                                case "g":
                                    resulat=Poids.g_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                                case "kg":
                                    resulat=Poids.Kg_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                                case "t":
                                    resulat=Poids.T_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)
                                    

                                case "livre":
                                    resulat=Poids.livre_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                                case "once":
                                    resulat=Poids.once_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                            print("*****************************************")

                            


                            #inroduire les fonction de poids


                            break  # Quitte la boucle d'unités après un choix valide
                    break  # Quitte la boucle de masse après un choix valide

        elif num == 2:  # Gestion de la température
            while True:  # Boucle pour choisir l'unité de température
                print("Choisissez l'unité de départ")
                print("1 : Celsius")
                print("2 : Fahrenheit")
                print("3 : Kelvin")
                print("0 : retour")
                unit = int(input("Entrez le numéro qui vous convient : "))

                if unit == 0:
                    break  # Retourne au choix du type d'unité
                elif unit < 1 or unit > 3:
                    print("Votre choix n'est pas valide, choisissez entre 0 et 3.")
                else:
                    print(f"Vous avez choisi l'unité de température : {unit}")

                    # Choisir l'unité de résultat
                    while True:  # Boucle pour choisir l'unité de résultat
                        print("Choisissez l'unité du résultat")
                        print("1 : Celsius")
                        print("2 : Fahrenheit")
                        print("3 : Kelvin")
                        print("0 : retour")
                        unit_res = int(input("Entrez le numéro qui vous convient : "))
                        
                        if unit_res == 0:
                            break  # Retourne au choix du type d'unité
                        elif unit_res < 1 or unit_res > 3:
                            print("Votre choix n'est pas valide, choisissez entre 0 et 3.")
                        else:
                            print(unit,";" ,unit_res)
                            #inroduire les fonction de poids
                            break  # Quitte la boucle d'unités après un choix valide
                break  # Quitte la boucle de température après un choix valide

if __name__ == "__main__":
    main()
