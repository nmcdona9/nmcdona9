class Cashier:
    def __init__(self):
        pass

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
