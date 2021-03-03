import json


def run():

    python_dict = {1: "apple", 2: "banana"}

    # access dictionary
    print("---access dictionary")
    print(python_dict[1])
    print(python_dict.get(2))
    print(python_dict.get(3, "No data"))
    print()

    # update dictionary
    print("---update dictionary")
    python_dict[3] = "coconut"
    print(python_dict)
    python_dict[3] = "pineapple"
    print(python_dict)
    python_dict.pop(3)
    print(python_dict)
    print()

    # iterate over dictionary
    print("---iterate over dictionary")
    for key in python_dict:
        print(f"{key}: {python_dict[key]}")
    print()

    for value in python_dict.values():
        print(value)
    print()

    # unpacking dictionary
    print("---unpacking dictionary")
    def unpack_dictionary_test(c, b, a=None):
        print(f"a: {a}")
        print(f"b: {b}")
        print(f"c: {c}")
    sample_dct = {"a": "aaa", "b": "bbb", "c": "ccc"}
    unpack_dictionary_test(**sample_dct)
    print()

    # json files can be easily converted to python dictionary and vice versa
    # same with yaml files
    print("---json dict")
    python_dict = {"id": 22202, "name": "Peter", "surname": "Cooper"}
    # dictionary to json
    with open("./sample_data/sample_json.json", "w") as file:
        json.dump(python_dict, file)
    # json to dictionary
    with open("./sample_data/sample_json.json", "r") as file:
        json_dict = json.load(file)
        print(type(json_dict))
    print(python_dict == json_dict)
    print()





if __name__ == '__main__':
    run()
