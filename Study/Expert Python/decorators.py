import time

# Decorators usage


def func(f):
    def wrapper():
        print("\nStarted")
        f()
        print("Ended\n\n")

    return wrapper


def func2():
    print("I am func2")


x = func(func2)
print(x)
x()


# Testing decorators with function timers
# timer function: it points out how long it took to run the whole function

def timer(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = function()
        total = time.time() - start
        print(f"Time: {total}")
        return rv

    return wrapper


@timer
def test():
    for i in range(100_000):
        pass


@timer
def test2():
    time.sleep(2)


test()
test2()
