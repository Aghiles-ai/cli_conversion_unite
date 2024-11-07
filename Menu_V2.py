import importlib
import os
import sys
import pandas as pd

class ConversionCLI:
    def __init__(self):
        self.categories = {}
        self.load_conversion_modules()

    def clear_screen(self):
        # Efface l'écran de la console
        os.system('cls' if os.name == 'nt' else 'clear')

    def load_conversion_modules(self):
        conversion_dir = 'conversions'
        if not os.path.exists(conversion_dir):
            print(f"\033[91mLe dossier '{conversion_dir}' n'existe pas.\033[0m")
            return

        sys.path.append(os.path.abspath(conversion_dir))
        
        for filename in os.listdir(conversion_dir):
            if filename.endswith('.py') and not filename.startswith('__'):
                module_name = filename[:-3]
                try:
                    module = importlib.import_module(module_name)
                    class_name = module_name.capitalize()
                    if hasattr(module, class_name):
                        self.categories[class_name] = getattr(module, class_name)()
                    else:
                        print(f"\033[91mLa classe '{class_name}' n'a pas été trouvée dans le module '{module_name}'.\033[0m")
                except Exception as e:
                    print(f"\033[91mErreur lors du chargement du module '{module_name}': {str(e)}\033[0m")

        if not self.categories:
            print("\033[91mAucun module de conversion n'a été chargé.\033[0m")

    def display_menu(self):
        while True:
            self.clear_screen()
            print("\n\033[94m=== Menu principal ===\033[0m")
            for i, category in enumerate(self.categories.keys(), 1):
                print(f"{i}. {category}")
            print("0. Quitter")
            print("\033[94m======= Favoris ==========\033[0m")

            df = pd.read_csv("conversions/Favoris.csv", delimiter=",")
            # Tri des données par la colonne "Count" en ordre décroissant
            df_sorted = df.sort_values(by="Count", ascending=False)
            # Sélection des 5 premières valeurs de la colonne "Conversion"
            list_top = df_sorted["Conversion"].head(5).tolist()

            # Affichage des favoris avec des lettres A, B, C, D, E
            for i, conversion in enumerate(list_top):
                String=f"{chr(65 + i)}. {conversion}"
                print(String.replace("_to_", " -> "))

            choice = input("\nChoisissez une catégorie (ou 0 pour quitter): ")
            if choice == '0':
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(self.categories):
                category=list(self.categories.keys())[int(choice) - 1]
                self.display_submenu(category)
            elif choice.upper() in 'ABCDE' and len(list_top) > ord(choice.upper()) - 65:
                conversion_choice = list_top[ord(choice.upper()) - 65]
                category = df_sorted[df_sorted["Conversion"] == conversion_choice]["Category"].values[0]
                from_unit, to_unit = conversion_choice.split("_to_")
                value = self.get_value(category, from_unit)
                self.perform_conversion(category, from_unit, to_unit, value)
            else:
                print("\033[91mChoix invalide. Veuillez réessayer.\033[0m")
                input()

    def display_submenu(self, category):
        while True:
            self.clear_screen()
            print(f"\n\033[94m=== Menu {category} ===\033[0m")
            units = self.categories[category].get_units()
            for i, unit in enumerate(units, 1):
                print(f"{i}. {unit}")
            print("0. Retour au menu principal")
            print("\033[94m======================\033[0m")

            choice = input("\nChoisissez une unité source (ou 0 pour retourner): ")
            if choice == '0':
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(units):
                from_unit=units[int(choice) - 1]
                value = self.get_value(category, from_unit)
                self.display_thirdmenu(category, from_unit, value)
                break
            else:
                print("\033[91mChoix invalide. Veuillez réessayer.\033[0m")
                input()

    def get_value(self, category, from_unit):
        while True:
            self.clear_screen()
            try :
                value = float(input(f"\nEntrez la valeur en {from_unit}: "))
                return value
            except :
                print("\033[91mValeur invalide. Veuillez réessayer.\033[0m")
                input()

        
    def display_thirdmenu(self, category, from_unit, value):
        while True :
            self.clear_screen()
            print("\n\033[94mUnités de conversion disponibles:\033[0m")
            units = self.categories[category].get_units()
            for i, unit in enumerate(units, 1):
                if unit != from_unit:
                    print(f"{i}. {unit}")

            to_unit_choice = input("\nChoisissez l'unité de conversion: ")
            if to_unit_choice.isdigit() and 1 <= int(to_unit_choice) <= len(units):
                to_unit = units[int(to_unit_choice) - 1]
                if to_unit != from_unit:
                    try:
                        self.perform_conversion(category, from_unit, to_unit, value)
                        return

                    except Exception as e:
                        print(f"\033[91mErreur lors de la conversion: {str(e)}\033[0m")
                        input()
                        
                else:
                    print("\033[91mL'unité source et de destination ne peuvent pas être identiques.\033[0m")
                    input()
            else:
                print("\033[91mChoix invalide.\033[0m")
                input()


    def perform_conversion(self, category, from_unit, to_unit, value):
        self.clear_screen()
        result = getattr(self.categories[category], f"{from_unit}_to")(unit=to_unit, value=value)
        print(f"\n\033[92m{value} {from_unit} = {result} {to_unit}\033[0m")
        
        # Mise à jour du fichier CSV
        conversion_type = f"{from_unit}_to_{to_unit}"
        file_name = "./conversions/Favoris.csv"
        
        # Charger le fichier CSV
        try:
            df = pd.read_csv(file_name, delimiter=",")
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Conversion", "Count"])

        # Vérifier si la conversion existe déjà
        if conversion_type in df["Conversion"].values:
            # Incrémenter le compteur
            df.loc[df["Conversion"] == conversion_type, "Count"] += 1
        else:
            # Ajouter une nouvelle ligne si la conversion n'existe pas
            new_row = pd.DataFrame({"Conversion": [conversion_type], "Count": [1]})
            df = pd.concat([df, new_row], ignore_index=True)

        # Sauvegarder les modifications dans le CSV
        df=df.sort_values(by="Count", ascending=False)
        df.to_csv(file_name, index=False)

        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    cli = ConversionCLI()
    cli.display_menu()
