def print_fn(fun):
    def inside():
        print("Welcome to print_fn....")
        fun()
    return inside

@print_fn
def result():
    print("Currently in result function")

result()
