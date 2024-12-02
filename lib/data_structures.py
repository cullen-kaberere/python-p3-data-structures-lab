
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level']>5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        print(f"{name} ({cuisine}) | Heat Level: {'🌶'*heat_level}")

print_spicy_foods(spicy_foods) 

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    matching_foods =  [food for food in spicy_foods if food['cuisine'] == cuisine]

    if matching_foods:
        return matching_foods[0]
    else:
        return None
print(get_spicy_food_by_cuisine(spicy_foods,"Thai"))

def print_spiciest_foods(spicy_foods):
    spiciest_food = [food for food in spicy_foods if food['heat_level']>5]

    for food in spiciest_food:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        print (f"{name} ({cuisine}) | Heat Level: {'🌶'*heat_level}")
    
    return spiciest_food
print_spiciest_foods(spicy_foods)   


def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)

    num_foods = len(spicy_foods)

    return total_heat / num_foods


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)

    return spicy_foods    

spicy_food = {"name" : "Griot", "cuisine" :"Haitian", "heat_level" : 10}

create_spicy_food(spicy_foods, spicy_food)
