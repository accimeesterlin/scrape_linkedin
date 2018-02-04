import json
from pprint import pprint

data = json.load(open("contacts.json"))


def set_max(arr, limit):
    for index, contact in enumerate(arr):
        if index <= int(limit) - 1:
            print("_______________________________________")
            print("_______________________________________")
            print("Index: ", index + 1)
            print("Name: ", contact["name"])
            print("Occupation: ", contact["occupation"])
            print("Link: ", contact["link"])


def search_contact(detail, val, limit):
    status = False
    results = []
    for index, contact in enumerate(data):
        if contact[detail].find(val) != -1:
            status = True
            current_search = {}
            current_search["name"] = contact["name"]
            current_search["link"] = contact["link"]
            current_search["occupation"] = contact["occupation"]
            results.append(current_search)
    if status == False:
        print("No results found!!!")
    set_max(results, limit)


# TODO
# Cleaning
def honoring_user_input(_input):
    if _input == "Company Name":
        text = input("Enter the company name: ")
        num = input("How many results do you want? ")
        search_contact("occupation", text, num)
    elif _input == "Name":
        text = input("Enter the name: ")
        num = input("How many results do you want? ")
        search_contact("name", text, num)
    elif _input == "Title":
        text = input("Enter the title: ")
        num = input("How many results do you want? ")
        search_contact("occupation", text, num)


options = ["Company Name", "Name", "Title"]



# Let user enter based on the option
def let_user_pick(options):
    print("Search people by: ")
    for idx, element in enumerate(options):
        print("{}) {}".format(idx + 1, element))
    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            honoring_user_input(options[int(i) - 1])
            return options[int(i) - 1]  # value selected
    except:
        pass
    return None


let_user_pick(options)
