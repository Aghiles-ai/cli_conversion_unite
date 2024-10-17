import Poids as Poids
import Temperature as Temperature
import Distance



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


dict_distance={
    1: "mm",
    2: "cm",
    3: "dm",
    4: "m",
    5: "km",
    6: "pouce",
    7: "pied",
    8: "mile"
}

def main():
    while True:  # Boucle principale pour permettre un retour au menu
        print("Choisissez le type d'unité que vous voulez")
        print("1 : masse")
        print("2 : température")
        print("3 : distance")
        print("0 : quitter")  # Option pour quitter le programme
        while True:
            try:
                num = int(input("Entrez le numéro qui vous convient : "))
                if num < 0 or num > 3:
                    print("Votre choix n'est pas valide, choisissez entre 0 et 3.")
                else:
                    break  # Sort de la boucle si l'entrée est un entier valide et dans la plage
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")


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

                
                while True:
                    try:
                        unit = int(input("Entrez le numéro qui vous convient : "))
                        if unit < 0 or unit > 6:
                            print("Votre choix n'est pas valide, choisissez entre 0 et 6.")
                        else:
                            break  # Sort de la boucle si l'entrée est un entier valide et dans la plage
                    except ValueError:
                        print("Veuillez entrer un nombre entier valide.")

                if unit == 0:
                    break  # Retourne au choix du type d'unité
                
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
                        
                        while True:
                            try:
                                unit_res = int(input("Entrez le numéro qui vous convient : "))
                                if unit_res < 0 or unit_res > 6:
                                    print("Votre choix n'est pas valide, choisissez entre 0 et 6.")
                                else:
                                    break  # Sort de la boucle si l'entrée est un entier valide et dans la plage
                            except ValueError:
                                print("Veuillez entrer un nombre entier valide.")
                        
                        if unit_res == 0:
                            break  # Retourne au choix du type d'unité
                        
                        else:

                            print(dict_poids[unit]," => " ,dict_poids[unit_res])

                            while True:
                                try:
                                    value = float(input("valeur= "))
                                    if value < 0 :
                                        print("Votre choix n'est pas valide, inserez une valuer posive.")
                                    else:
                                        break  # Sort de la boucle si l'entrée est un entier valide et dans la plage
                                except ValueError:
                                    print("Veuillez entrer un nombre  valide.")

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
                while True:
                    try:
                        unit = int(input("Entrez le numéro qui vous convient : "))
                        if unit < 0 or unit > 3:
                            print("Votre choix n'est pas valide, choisissez entre 0 et 3.")
                        else:
                            break  # Sort de la boucle si l'entrée est un entier valide et dans la plage
                    except ValueError:
                        print("Veuillez entrer un nombre entier valide.")

                if unit == 0:
                    break  # Retourne au choix du type d'unité
                
                else:
                    

                    # Choisir l'unité de résultat
                    while True:  # Boucle pour choisir l'unité de résultat
                        print("Choisissez l'unité du résultat")
                        print("1 : Celsius")
                        print("2 : Fahrenheit")
                        print("3 : Kelvin")
                        print("0 : retour")
                        while True:
                            try:
                                unit_res = int(input("Entrez le numéro qui vous convient : "))
                                if unit_res < 0 or unit_res > 3:
                                    print("Votre choix n'est pas valide, choisissez entre 0 et 3.")
                                else:
                                    break  # Sort de la boucle si l'entrée est un entier valide et dans la plage
                            except ValueError:
                                print("Veuillez entrer un nombre entier valide.")
                        
                        if unit_res == 0:
                            break  # Retourne au choix du type d'unité
                        
                        else:
                            print(dict_temp[unit]," => " ,dict_temp[unit_res])
                            

                            unit = dict_temp[unit]
                            unit_res= dict_temp[unit_res]
                            
                            match unit:
                                case "c":
                                    while True:
                                        try:
                                            value = float(input("valeur= "))
                                            if value<-273.15:
                                                print("La température en Celsius ne peut pas être inférieure à -273.15°C")
                                            else:
                                                break
                                            
                                        except ValueError:
                                            print("Veuillez entrer un nombre entier valide.")
                                    
                                    resulat=Temperature.celsius_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                                
                                case "f":
                                    while True:
                                        try:
                                            value = float(input("valeur= "))
                                            if value<-459.67:
                                                print("La température en Celsius ne peut pas être inférieure à -459.67°F")
                                            else:
                                                break
                                            
                                        except ValueError:
                                            print("Veuillez entrer un nombre entier valide.")

                                    resulat=Temperature.fahrenheit_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                                case "k":
                                    while True:
                                        try:
                                            value = float(input("valeur= "))
                                            if value<0:
                                                print("La température en Celsius ne peut pas être inférieure à 0K")
                                            else:
                                                break
                                            
                                        except ValueError:
                                            print("Veuillez entrer un nombre entier valide.")
                                            
                                    resulat=Temperature.kelvin_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                            print("*****************************************")


                            break  # Quitte la boucle d'unités après un choix valide
                break  # Quitte la boucle de température après un choix valide

        elif num == 3:  # Gestion de la température
            while True:  # Boucle pour choisir l'unité de température
                print("Choisissez l'unité de départ")
                print("1 : mm")
                print("2 : cm")
                print("3 : dm")
                print("4 : m")
                print("5 : km")
                print("6 : pouce")
                print("7 : pied")
                print("8 : mile")
                print("0 : retour")
                while True:
                    try:
                        unit = int(input("Entrez le numéro qui vous convient : "))
                        if unit < 0 or unit > 8:
                            print("Votre choix n'est pas valide, choisissez entre 0 et 8.")
                        else:
                            break  # Sort de la boucle si l'entrée est un entier valide et dans la plage
                    except ValueError:
                        print("Veuillez entrer un nombre entier valide.")
                

                if unit == 0:
                    break  # Retourne au choix du type d'unité
                
                else:
                    

                    # Choisir l'unité de résultat
                    while True:  # Boucle pour choisir l'unité de résultat
                        print("Choisissez l'unité du resultat")
                        print("1 : mm")
                        print("2 : cm")
                        print("3 : dm")
                        print("4 : m")
                        print("5 : km")
                        print("6 : pouce")
                        print("7 : pied")
                        print("8 : mile")
                        print("0 : retour")

                        while True:
                            try:
                                unit_res = int(input("Entrez le numéro qui vous convient : "))
                                if unit_res < 0 or unit_res > 8:
                                    print("Votre choix n'est pas valide, choisissez entre 0 et 8.")
                                else:
                                    break  # Sort de la boucle si l'entrée est un entier valide et dans la plage
                            except ValueError:
                                print("Veuillez entrer un nombre entier valide.")

                        if unit_res == 0:
                            break  # Retourne au choix du type d'unité
                        
                        else:
                            print(dict_distance[unit]," => " ,dict_distance[unit_res])
                            while True:
                                try:
                                    value = float(input("valeur= "))
                                    if value < 0 :
                                        print("Votre choix n'est pas valide, inserez une valuer posive.")
                                    else:
                                        break  # Sort de la boucle si l'entrée est un entier valide et dans la plage
                                except ValueError:
                                    print("Veuillez entrer un nombre  valide.")

                            unit = dict_distance[unit]
                            unit_res= dict_distance[unit_res]
                            
                            match unit:
                                case "mm":
                                    resulat=Distance.mm_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)
                                
                                case "cm":
                                    resulat=Distance.cm_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                                case "dm":
                                    resulat=Distance.dm_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                                case "m":
                                    resulat=Distance.m_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                                case "km":
                                    resulat=Distance.km_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                                case "pouce":
                                    resulat=Distance.pouce_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                                case "pied":
                                    resulat=Distance.pied_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                                case "mile":
                                    resulat=Distance.mile_to(unit=unit_res,value=value)
                                    print(value," ",unit," = ",resulat," ",unit_res)

                            print("*****************************************")


                            break  # Quitte la boucle d'unités après un choix valide
                break  # Quitte la boucle de température après un choix valide

if __name__ == "__main__":
    main()
