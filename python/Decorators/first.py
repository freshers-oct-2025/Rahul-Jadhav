def add_toppings(func):
    def wrapper():
        print("Add chocolate toppings")
        func()
        print("Add cherry on top")
    return wrapper

@add_toppings
def make_cake():
    print("Cake ready!")

make_cake()
