def find_duplicates(input_list):
    """Finds all duplicate items in a list."""
    seen = set()
    duplicates = set()
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

if __name__ == "__main__":
    items_str = input("Enter a list of items, separated by commas: ")
    items_list = [item.strip() for item in items_str.split(',')]
    
    if not items_list or items_list == ['']:
        print("No items entered.")
    else:
        duplicates = find_duplicates(items_list)
        if duplicates:
            print(f"The duplicate items are: {', '.join(duplicates)}")
        else:
            print("No duplicate items found.")