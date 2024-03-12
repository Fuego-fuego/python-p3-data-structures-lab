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
    spicy_foods_names = list()
    for spicy_food in spicy_foods:
        spicy_foods_items = [ food for food in spicy_food.items()]
        spicy_food_name = spicy_foods_items[0][1]
        spicy_foods_names.append(spicy_food_name)
    return spicy_foods_names
        

def get_spiciest_foods(spicy_foods):    
    spiciest_foods = [spicy_food for spicy_food in spicy_foods if spicy_food['heat_level'] > 5 ]
    return (spiciest_foods)
    

def print_spicy_foods(spicy_foods):
    chilli_emoji = '🌶'
    for spicy_food in spicy_foods:
        print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: { chilli_emoji * spicy_food['heat_level']}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    cuisine_lower = cuisine.lower()
    food = [spicy_food for spicy_food in spicy_foods if spicy_food['cuisine'].lower() == cuisine_lower ]
    return food[0]


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)
    
    
def get_average_heat_level(spicy_foods):    
    number_of_spicy_foods = len(spicy_foods)
    sum = 0
    for spicy_food in spicy_foods:
        sum += spicy_food['heat_level']
    average = sum / number_of_spicy_foods    
    return average


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)    
    return spicy_foods

