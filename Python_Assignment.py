#Created by Ahsan Siddiqi

#------------------ Code for Displaying the Menu (I made this wayyy too complex than it needs to be)---------------------

#Dictionary for the Menu
menu = {
    "egg" : 0.99,
    "bacon" : 0.49,
    "sausage" : 1.49,
    "hash brown" : 1.19,
    "toast" : 0.79,
    "coffee" : 1.49,
    "tea" : 1.09
}

#Dictionaries for the Combos
SmallBreakfast = {
    "Contains" : "1 egg, 1 hash brown, 2 slices of toast, 2 strips of bacon(chicken), and 1 sausage",
    "Price" : menu["egg"] + menu["hash brown"] + 2 * menu["toast"] + 2 * menu["bacon"] + menu["sausage"]
}
RegularBreakfast = {
    "Contains" : "2 eggs, 1 has brown, 2 slices of toast, 4 strips of bacon(chicken), 2 sausages",
    "Price" : 2 * menu["egg"] + menu["hash brown"] + 2 * menu["toast"] + 4 * menu["bacon"] + 2 * menu["sausage"]
}
BigBreakfast = {
    "Contains" : "3 eggs, 2 hashbrowns, 4 slices of toast, 6 strips of bacon(chicken), and three sausages",
    "Price" : 3 * menu["egg"] + 2 * menu["hash brown"] + 4 * menu["toast"] + 6 * menu["bacon"] + 3 * menu["sausage"]
}

#code to round values to 2 decimal places (was very annoying to integrate so i just put it here) - another side note: I have to add the dollar signs here because in the code later on the dollar sign cannot be added to a single key indiviaually without complications)
SmallBreakfast["Price"] = " $" + str(round(SmallBreakfast["Price"], 2))
RegularBreakfast["Price"] = " $" + str(round(RegularBreakfast["Price"], 2))
BigBreakfast["Price"] = " $" + str(round(BigBreakfast["Price"], 2))

#function for displaying the menu
def DisplayBreakfastMenu():
    print("Welcome to Ahsan's Breakfast Resturant! (100% Halal)")
    print("MENU:")
    for items in menu:
        print(items + ": " + " $" + str(menu[items]))

#function for displaying the combos
def combos():
    print("COMBOS:")
    print("Small Breakfast Combo")
    for items in SmallBreakfast:
        print(items + ": ")
        print(str(SmallBreakfast[items]))
    print("Regular Breakfast Combo")
    for items in RegularBreakfast:
        print(items + ": ")
        print(str(RegularBreakfast[items]))
    print("Big Breakfast Combo")
    for items in BigBreakfast:
        print(items + ": ")
        print(str(BigBreakfast[items]))

#function that activates the function the displays the combos at the user's request (CombosYN is the variable name for the input of "yes or "no")
def DisplayCombosMenu():
    CombosYN = input("Would you like to see the combo's menu? (no discounts lol)? Yes or No:")
    if CombosYN.lower().strip() == "yes":
        combos()
    elif CombosYN.lower().strip() == "no":
        pass
    else:
        while CombosYN != "yes" or "no":
            CombosYN = input("Please type Yes or No:")
            if CombosYN.lower().strip() == "yes":
                combos()
                break
            if CombosYN.lower().strip() == "no":
                break

DisplayBreakfastMenu()
DisplayCombosMenu()

#------------------- Code for selecting the items ----------------------

def userorder():
    order =""
    quantity = ""

    while order != "q":
        order = input("What would you like to order? small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")
        quantity = input("How many would you like?: ")


userorder()
