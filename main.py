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


cook_buk = recipe_reader(data)
pprint(cook_buk, indent=1, width=120, depth=3, sort_dicts=False)
