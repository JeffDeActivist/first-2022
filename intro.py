def first_fun(name):
    print(name, "You just wrote your first function in python")


first_fun("jeff")

n = int(input("enter a number"))


def even_num():
    for i in range(n):
        if i % 2 == 0:
            print(i)


even_num()


def fun_inside_other(fun2):
    for i in range(n):
        if i % 2 == 0:
            print(i)

    def inner_fun():
        print("jeff keep trying")

    inner_fun()


fun_inside_other(first_fun("jeff2"))
