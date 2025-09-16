# Decorator = A function that extends the behavior of another function
#             without directly modifying it.
# Syntax sugar: @decorator_name above a function definition

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles*")
        return func(*args, **kwargs)   # ensure original function result is returned
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge*")
        return func(*args, **kwargs)
    return wrapper


# Applying multiple decorators (order matters!)
@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream")


if __name__ == "__main__":
    get_ice_cream("rocky road")
