import json

# Load the JSON file
with open('element_identities.json', 'r') as file:
    periodic_table = json.load(file)
# Access details for an element (e.g., Oxygen)

def get_element(element):
    if element in periodic_table:
        for key, value in periodic_table[element].items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print("Element not found.")

def search_by_group(group):
    result = {symbol: details for symbol, details in periodic_table.items() if details['group'] == group}
    return result if result else "No elements found in this group."

def elements_in_state(state):
    result = {symbol: details for symbol, details in periodic_table.items() if details['state_at_room_temperature'] == state}
    return result if result else "No elements found in this state."

def compare_elements(element1, element2):
    if element1 in periodic_table and element2 in periodic_table:
        details1 = periodic_table[element1]
        details2 = periodic_table[element2]
        comparison = {key: (details1[key], details2[key]) for key in details1 if key in details2}
        return comparison
    return "One or both elements not found."

def filter_by_property(property_name, min_value, max_value):
    result = {
        symbol: details
        for symbol, details in periodic_table.items()
        if details.get(property_name) and min_value <= details[property_name] <= max_value
    }
    return result if result else "No elements found in this range."

def extreme_element(property_name, highest=True):
    filtered_elements = {symbol: details[property_name] for symbol, details in periodic_table.items() if property_name in details and details[property_name] is not None}
    if not filtered_elements:
        return "Property not found in elements."
    extreme = max(filtered_elements, key=filtered_elements.get) if highest else min(filtered_elements, key=filtered_elements.get)
    return {extreme: periodic_table[extreme]}

def list_all_symbols():
    return list(periodic_table.keys())

def save_filtered_elements(filtered_elements, filename):
    with open(filename, 'w') as file:
        json.dump(filtered_elements, file, indent=4)
    print(f"Filtered elements saved to {filename}")


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