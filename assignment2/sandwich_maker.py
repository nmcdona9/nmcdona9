
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for i in ingredients:
            if self.machine_resources[i] < ingredients[i]:
                return False
        return True


def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
                 Hint: no output"""
        if self.check_resources(self.machine_resources):
            for ingredients, quantity in order_ingredients.items():
                self.machine_resources[ingredients] -= quantity
            print(f"Successfully made sandwich")
        else:
            print(f"Insufficient resources to make a sandwich")