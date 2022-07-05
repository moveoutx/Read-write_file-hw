from pprint import pprint
from collections import defaultdict

data = "recipes.txt"
file_1 = "1.txt"
file_2 = "2.txt"
file_3 = "3.txt"
res_file = "res_file.txt"


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
    shop_list = defaultdict()
    cook_book = recipe_reader(data)
    for dish in dishes:
        if dish in cook_book.keys():
            for item in cook_book.get(dish):
                if item['ingredient_name'] in shop_list.keys():
                    in_list = int(shop_list[item['ingredient_name']].get('quantity')) + int(item.get('quantity')) * int(person_count)
                    for ingrs, val in shop_list.items():
                        if ingrs == item['ingredient_name']:
                            val['quantity'] = in_list
                else:
                    shop_list.setdefault(item.get('ingredient_name'), {'measure': item.get('measure'),
                                                                       'quantity': int(item.get('quantity')) * int(
                                                                           person_count)})
        else:
            print(f'Блюда: {dish} - нет в меню')

    return shop_list


def file_reader(file_name_1, file_name_2, file_name_3):
    res_file_data = {}
    file_dict1 = {}
    file_dict2 = {}
    file_dict3 = {}
    strings_1 = []
    strings_2 = []
    strings_3 = []

    with open(file_name_1) as file:
        for line in file:
            strings_1.append(line.strip())
    with open(file_name_2) as file:
        for line in file:
            strings_2.append(line.strip())
    with open(file_name_3) as file:
        for line in file:
            strings_3.append(line.strip())

    length_1 = len(strings_1)
    length_2 = len(strings_2)
    length_3 = len(strings_3)

    file_dict1.setdefault('name', file_name_1)
    file_dict2.setdefault('name', file_name_2)
    file_dict3.setdefault('name', file_name_3)
    file_dict1.setdefault('length', length_1)
    file_dict2.setdefault('length', length_2)
    file_dict3.setdefault('length', length_3)
    file_dict1.setdefault('strings', strings_1)
    file_dict2.setdefault('strings', strings_2)
    file_dict3.setdefault('strings', strings_3)

    res_file_data.setdefault(file_name_1, file_dict1)
    res_file_data.setdefault(file_name_2, file_dict2)
    res_file_data.setdefault(file_name_3, file_dict3)
    pprint(res_file_data)
    return res_file_data


file_reader(file_1, file_2, file_3)


def file_writer(res_file_data):
    sorting_val = 0
    while sorting_val < 10:
        sorting_val += 1
        for ion in res_file_data.values():
            if ion['length'] == sorting_val:
                with open(res_file, 'a') as file:
                    file.write(ion['name'])
                    file.write('\n')
                    file.write(str(ion['length']))
                    file.write('\n')
                    file.write('\n'.join(ion['strings']))
                    file.write('\n')


file_writer(file_reader(file_1, file_2, file_3))


pprint(recipe_reader(data), indent=1, width=120, depth=3, sort_dicts=False)
pprint(get_shop_list_by_dishes(["Омлет", "Амлет", "Омлет"], 2))
