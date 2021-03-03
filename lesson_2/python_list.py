

def run():
    python_list = [1, "Python", [1, "Python"]]
    print(python_list)
    print(python_list[0])
    print(python_list[2][1])
    print()

    # list slicing
    # sample_list[from:to:step]
    print("---list slicing")
    sample_list = "1 2 3 4 5 6 7 8 9".split(' ')
    print(sample_list[0:9])
    print(sample_list[4:-1])
    print(sample_list[::3])
    print()

    # reverse list
    print("---reverse list")
    print(python_list.reverse()) # NB! Doesn't return anything, changes the object itself
    print(python_list)
    print(python_list[::-1])
    print()

    # add\change elements
    print("---add\change elements")
    sample_list.append("10")
    print(sample_list)

    sample_list.extend(["11", "12"])
    print(sample_list)

    sample_list.insert(12, "13")
    print(sample_list)

    sample_list[11:] = ["1200", "1300"]
    print(sample_list)

    del(sample_list[11:])
    print(sample_list)

    sample_list.remove('11')
    print(sample_list)

    sample_list.clear()
    print(sample_list)
    print()

    # unpacking list into variable
    print("---unpacking list")
    lst = [1,2]
    a, b = lst
    print(a)
    print(b)

    # unpacking list (or any other iterable)
    print("xxxx")
    def list_unpacking_test(a, b):

        print(f"a: {a}")
        print(f"b: {b}")

    lst = [1,2]
    list_unpacking_test(*lst)
    print()


    # tuple in Python is similar to a list, but you cannot change its elements
    print("---tuple")
    python_tuple = (1, 2, 3)
    print(python_tuple[0])
    try:
        python_tuple[0] = 111
    except TypeError:
        print("Cannot do this with a tuple")
    print()

    # be careful creating tuple with one element
    sample_tuple = (1)
    print(type(sample_tuple))

    sample_tuple = (1,)
    print(type(sample_tuple))
    print()


    # set in Python is also similar to a list. But it contains only unique elements, set is unordered, each element is immutable, but whole set is mutable
    print("---set")
    python_set = {1, 2, 2, 2, 3, 3, 4, 5, 5, 5}
    print(python_set)
    try:
        # you cannot access set by the index
        python_set[1]
    except TypeError:
        print("Cannot do this with a set")

    python_set.add(6)
    python_set.update([7,8])
    print(python_set)

    # you cannot add list to a set, because list is a mutable object, while objects in a set are always immutable
    try:
        python_set.add([7,8])
    except TypeError:
        print("Cannot do this with a set")

    python_set.remove(8)
    print(python_set)
    print()


if __name__ == "__main__":
    run()
