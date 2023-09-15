### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources



    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for i in ingredients:
            if self.machine_resources[i] < ingredients[i]:
                return False
        return True


    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        coin_values = {"1": 1.0, "0.5": 0.5, "0.25": 0.25, "0.05": 0.05}
        total = 0.0



        total = int(input(f"How many large dollars?: ")) * 1
        total += int(input(f"How many half dollars?: ")) * .5
        total += int(input(f"how many quarters?: ")) * .25
        total += int(input(f"How many nickels?: ")) * .05

        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            if change > 0:
                print(f"You have ${change: .2f} in change.")
            print("Payment success!!! Preparing your sammie!")
            return True
        else:
            print("insufficient funds...")
        return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        if self.check_resources(self.machine_resources):
            for ingredients, quantity in order_ingredients.items():
                self.machine_resources[ingredients] -= quantity
            print(f"Successfully made sandwich")
        else:
            print(f"Insufficient resources to make a sandwich")

### Make an instance of SandwichMachine class and write the rest of the codes ###



sandwich_maker = SandwichMachine(resources)

is_on = True

while(is_on):
    choice = input("Enter what size sandwich small/medium/large/off/report: ")

    if choice == "off":
        is_on = False

    if choice == "report":
        is_on = True
        breadslices = sandwich_maker.machine_resources["bread"]
        print(f"Bread remaining: {breadslices} slices")
        hamslices = sandwich_maker.machine_resources["ham"]
        print(f"Ham slices remaining: {hamslices}")
        cheeseslices = sandwich_maker.machine_resources["cheese"]
        print(f"Cheese ounces remaining {cheeseslices}")
        exitvariable = input("Press any key to exit the program")
        exit(0)


    sandwich = recipes[choice]

    if sandwich_maker.check_resources(sandwich['ingredients']):
        money = sandwich_maker.process_coins()
        if sandwich_maker.transaction_result(money, sandwich['cost']):
            sandwich_maker.make_sandwich(choice, sandwich['ingredients'])





    # balance_owed = 0.00
    #
    # if choice == "small":
    #     choice.make_sandwich("small", choice.machine_resources)
    #     balance_owed = 5.50
    #
    # elif choice == "medium":
    #     choice.make_sandwich("medium", choice.machine_resources)
    #     balance_owed = 6.50
    #
    # elif choice == "large":
    #     choice.make_sandwich("large", choice.machine_resources)
    #     balance_owed = 7.50
    #
    # elif choice == "off":
    #     print("Shutting down, bye bye!!")
    #     exit(0)
    #
    # else:
    #     print("Error")
    #     exit(0)

