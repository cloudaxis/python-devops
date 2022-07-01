from random import choices


def fruit():
    fruits = ["apple", "cherry", "strawberry"]
    return choices(fruits)[0]


def meal(beverage):
    print(f"the beverage is {beverage}")
    chosen_fruit = fruit()
    if chosen_fruit == "apple":
        return f"Your meal is an {chosen_fruit} and {beverage}"
    else:
        return f"your meal is dogfood with {beverage}"