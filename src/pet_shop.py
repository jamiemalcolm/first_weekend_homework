# WRITE YOUR FUNCTIONS HERE

# accessing dictionary one level in
def get_pet_shop_name(shop):
    return shop["name"]

# accessing dictionary 2 levels in


def get_total_cash(shop):
    return shop["admin"]["total_cash"]

# updating dictionary 2 levels in


def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] += amount

# accessing dictionary 2 levels in


def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

# update dictionary 2 levels in


def increase_pets_sold(shop, num_sold):
    shop["admin"]["pets_sold"] += num_sold


# access dictionay one level in and get length of list

def get_stock_count(shop):
    stock = 0
    for pet in shop:
        stock = len(shop["pets"])
        return stock


# accssing dictionary one level in then counting items in a list that match param

def get_pets_by_breed(shop, breed):
    num_of_breed = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            num_of_breed.append(pet)
    return num_of_breed
# def get_pets_by_breed(shop, description):
#     num_of_breed = []
#     for key, val in shop.items():
#         print(key)
#         if key == "pets":
#             for i, k in enumerate(val):
#                 print(i, k)
#                 if k["breed"] == description:
#                     num_of_breed.append(k)
#     return num_of_breed

# find the pet by name given and return if true, return none if false


def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet

# remove a given pet.


def remove_pet_by_name(shop, sold_pet):
    for pet in shop["pets"]:
        if pet["name"] == sold_pet:
            shop["pets"].remove(pet)


# add pet to stock

def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)


# get customer funds

def get_customer_cash(customers):
    return customers["cash"]
