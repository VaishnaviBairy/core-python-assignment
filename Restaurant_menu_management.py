def update_menu(menu, add_item, remove_item, check_item):
    if remove_item in menu:
        menu.remove(remove_item)
    else:
        print(f"{remove_item} not found in the menu.")
    
    menu.append(add_item)
    
    availability = f"{check_item} is available" if check_item in menu else f"{check_item} is not available"
    return menu, availability


initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"

updated_menu, availability = update_menu(initial_menu, add_item, remove_item, check_item)
print(f"Updated menu: {updated_menu}")
print(f"Availability: {availability}")
