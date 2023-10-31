import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMachine(resources)
cashier_instance = data.cashier





def main():
    is_on = True

    while (is_on):
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


if __name__=="__main__":
    main()
