import json
import CASLib

def main():
    while True:
        print("\nChoose an action:")
        print("1. Search for an element")
        print("2. Search by group")
        print("3. Find elements in a specific state")
        print("4. Compare properties between two elements")
        print("5. Filter elements by property range")
        print("6. List all element symbols")
        print("7. Quit")

        choice = input("\nEnter your choice (1-7): ")
        if choice == '1':
            element = str(input("What is the desired element? "))
            print(get_element(element))
        elif choice == '2':
            # Extract unique group names
            groups = set(details['group'] for details in periodic_table.values())
            print("Available groups:")
            for group in groups:
                print(group)
            group = input("Enter the group name: ")
            print(search_by_group(group))
        elif choice == '3':
            state = input("Enter the state (Solid, Liquid, Gas): ")
            print(elements_in_state(state))
        elif choice == '4':
            element1 = input("Enter the symbol of the first element: ").strip()
            element2 = input("Enter the symbol of the second element: ").strip()
            print(compare_elements(element1, element2))
        elif choice == '5':
            property_name = input("Enter the property name: ")
            min_value = float(input("Enter the minimum value: "))
            max_value = float(input("Enter the maximum value: "))
            print(filter_by_property(property_name, min_value, max_value))
        elif choice == '6':
            print(list_all_symbols())
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()