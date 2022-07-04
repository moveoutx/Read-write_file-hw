from pprint import pprint

data = "recipes.txt"


def recipe_reader(book):
    with open(book) as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            ingredients = []
            quantity = file.readline()
            for item in range(int(quantity)):
                tmp_dict = {'ingredient_name': '', 'quantity': '', 'measure': ''}
                good = file.readline()
                i, a, m = [word.strip() for word in good.split(" | ")]
                tmp_dict['ingredient_name'] = i
                tmp_dict['quantity'] = a
                tmp_dict['measure'] = m
                ingredients.append(tmp_dict)
            cook_book[dish] = ingredients
            file.readline()
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = recipe_reader(data)
    for dish in dishes:
        for item in cook_book.get(dish):
            shop_list.setdefault(item.get('ingredient_name'), {'measure': item.get('measure'), 'quantity': int(item.get('quantity')) * int(person_count)})
    return shop_list


pprint(recipe_reader(data), indent=1, width=120, depth=3, sort_dicts=False)
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
