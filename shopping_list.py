class ShoppingList:
    """
    A class to represent a shopping list.

    Attributes
    ----------
    items : list
        A list to store shopping items.

  metodes
    -------
    add_item(item):
        Adds an item to the shopping list.
    
    remove_item(item):
        Removes an item from the shopping list if it exists.
    
    get_items():
        Returns the list of shopping items.
    """
    def __init__(self):
        self.items = {}  # Brug en ordbog til at gemme varer og antal

    def add(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity  # Hvis varen allerede findes, øg antallet
        else:
            self.items[item] = quantity  # Ellers tilføj varen med den angivne mængde

    def remove(self, item, quantity=None):
        if item in self.items:
            if quantity is None or self.items[item] <= quantity:
                del self.items[item]  # Fjern varen helt, hvis ingen mængde er angivet, eller hvis den bliver nul
            else:
                self.items[item] -= quantity  # Reducer antallet af varen

    def get_items(self):
        return self.items  # Returner hele indkøbslisten som en ordbog

# Test af klassen
if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add("Apples", 2)
    shopping_list.add("Bananas", 3)
    print(shopping_list.get_items())  # Output: {'Apples': 2, 'Bananas': 3}
    
    shopping_list.remove("Apples", 1)
    print(shopping_list.get_items())  # Output: {'Apples': 1, 'Bananas': 3}
    
    shopping_list.remove("Apples")
    print(shopping_list.get_items())  # Output: {'Bananas': 3}
