import copy


def run():

    print("Copy using = operator")
    old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
    new_list = old_list

    old_list[2][2] = 9

    print('Old List:', old_list)
    print('ID of Old List:', id(old_list))

    print('New List:', new_list)
    print('ID of New List:', id(new_list))
    print()


    print("Copy using copy module")
    old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
    new_list = copy.copy(old_list)

    new_list[2][2] = 9

    print('Old List:', old_list)
    print('ID of Old List:', id(old_list))

    print('New List:', new_list)
    print('ID of New List:', id(new_list))
    print()


    print("Copy using deepcopy")
    old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
    new_list = copy.deepcopy(old_list)

    new_list[2][2] = 9

    print('Old List:', old_list)
    print('ID of Old List:', id(old_list))

    print('New List:', new_list)
    print('ID of New List:', id(new_list))
    print()

if __name__ == "__main__":
    run()
