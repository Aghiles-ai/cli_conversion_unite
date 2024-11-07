import importlib
import os
import sys

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
            print("\033[94m======================\033[0m")

            choice = input("\nChoisissez une catégorie (ou 0 pour quitter): ")
            if choice == '0':
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(self.categories):
                self.display_submenu(list(self.categories.keys())[int(choice) - 1])
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
                self.perform_conversion(category, units[int(choice) - 1])
                break
            else:
                print("\033[91mChoix invalide. Veuillez réessayer.\033[0m")
                input()

    def perform_conversion(self, category, from_unit):
        verif = True
        while verif:
            try :
                value = float(input(f"\nEntrez la valeur en {from_unit}: "))
                verif = False
            except :
                print("\033[91mValeur invalide. Veuillez réessayer.\033[0m")
                input()

        while True :
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
                        result = getattr(self.categories[category], f"{from_unit}_to")(unit=to_unit, value=value)
                        self.clear_screen()
                        print(f"\n\033[92m{value} {from_unit} = {result} {to_unit}\033[0m")
                    except Exception as e:
                        print(f"\033[91mErreur lors de la conversion: {str(e)}\033[0m")
                        input()
                        
                    input("\nAppuyez sur Entrée pour continuer...")
                    return
                else:
                    print("\033[91mL'unité source et de destination ne peuvent pas être identiques.\033[0m")
                    input()
            else:
                print("\033[91mChoix invalide.\033[0m")
                input()

if __name__ == "__main__":
    cli = ConversionCLI()
    cli.display_menu()
