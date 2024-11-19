import json
import CASLib
import PeriodicalLib
import matplotlib.pyplot as plt

# Load the JSON file
with open('element_identities.json', 'r') as file:
    periodic_table = json.load(file)
# Access details for an element (e.g., Oxygen)

def main():
    while True:
        print("\nWhat do you want to do today:")
        print("1. Search for an element")
        print("2. Search for a compound")
        print("3. Go plotting!")
        print("4. Quit")

        choice = input("\nEnter your choice (1-4): ")
        if choice == '1':
            print("1. Search for an element")
            print("2. Search by group")
            print("3. Find elements in a specific state")
            print("4. Compare properties between two elements")
            print("5. Filter elements by property range")
            print("6. List all element symbols")
            print("7. Quit")

            choice = input("\nEnter your choice (1-7): ")
            if choice == '1':
                element = str(input("What is the desired element? ").strip()).capitalize()
                print(PeriodicalLib.get_element(element))
            elif choice == '2':
                # Extract unique group names
                groups = set(details['group'] for details in periodic_table.values())
                print("Available groups:")
                for group in groups:
                    print(group)
                group = input("Enter the group name: ")
                print(PeriodicalLib.search_by_group(group))
            elif choice == '3':
                state = input("Enter the state (Solid, Liquid, Gas): ")
                print(PeriodicalLib.elements_in_state(state))
            elif choice == '4':
                element1 = input("Enter the symbol of the first element: ").strip()
                element2 = input("Enter the symbol of the second element: ").strip()
                print(PeriodicalLib.compare_elements(element1, element2))
            elif choice == '5':
                property_name = input("Enter the property name: ")
                min_value = float(input("Enter the minimum value: "))
                max_value = float(input("Enter the maximum value: "))
                print(PeriodicalLib.filter_by_property(property_name, min_value, max_value))
            elif choice == '6':
                print(PeriodicalLib.list_all_symbols())
            elif choice == '7':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        elif choice == '2':
            search_type = input("Are you searching by CAS RN or Compound name? (Enter 'CAS' or 'Name'): ").strip().lower()
            if search_type == 'cas':
                cas_rn = input("Enter the CAS RN: ").strip()
                print(CASLib.get_compound_details(cas_rn))
            elif search_type == 'name':
                query = input("Enter the compound name (use * for wildcard): ").strip()
                if '*' in query:
                    query = query.replace('*', '%')
                print(CASLib.search_compounds(query))
            else:
                print("Invalid input. Please enter 'CAS' or 'Name'.")
        elif choice == '3':
            
            print("1. Plot a property of an element")
            print("2. Plot a property of a group")
            print("3. Plot a property of all elements")
            print("4. Quit")

            choice = input("\nEnter your choice (1-4): ")
            if choice == '1':
                element = str(input("What is the desired element? ").strip()).capitalize()
                property_name = input("Enter the property name: ")
                PeriodicalLib.plot_element_property(element, property_name)
            elif choice == '2':
                group = input("Enter the group name: ")
                property_name = input("Enter the property name: ")
                PeriodicalLib.plot_group_property(group, property_name)
            elif choice == '3':
                property_name = input("Enter the property name: ")
                PeriodicalLib.plot_all_elements_property(property_name)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()