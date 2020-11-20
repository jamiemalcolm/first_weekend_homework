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
