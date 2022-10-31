
# Задача №1.


def create_cook_book(filename):
    from pprint import pprint
    with open(filename, 'r', encoding="utf-8") as file:
        my_file = file.readlines()
        number = len(my_file)
        cook_book = dict()
        numbers_of_str = 0
        while numbers_of_str < number:
            my_dish = my_file[numbers_of_str].strip()
            numbers_of_str += 1
            ingredients_number = int(my_file[numbers_of_str].strip())
            numbers_of_str += 1
            my_dishes_ingredients_counter = ingredients_number
            ingredients_list = list()
            for number_1 in range(my_dishes_ingredients_counter):
                ingredients_str = my_file[numbers_of_str].strip()
                ingredients_ = ingredients_str.split(sep=' |')
                numbers_of_str += 1
                ingredients_list.append({'ingredient_name': ingredients_[0], 'quantity': ingredients_[1],
                                         'measure': ingredients_[2]})
            cook_book[my_dish] = ingredients_list
            file.readline()
            numbers_of_str += 1
        #pprint(cook_book)
        print('Книга рецептов успешно создана.')
        return cook_book


create_cook_book('home_work_2_1.txt')


# Задача №2.


def get_shop_list_by_dishes(dish_list, person):

    cook_book = create_cook_book('home_work_2_1.txt')
    shop_list_by_dishes = dict()
    my_ingredient_list = list()
    for dish in dish_list:
        dish = dish.capitalize()
        for k in cook_book:
            if dish == k:
                dish_recipe = cook_book[k]
                for elem in range(len(dish_recipe)):
                    if dish_recipe[elem]['ingredient_name'] not in my_ingredient_list:
                        my_ingredient_list.append(dish_recipe[elem]['ingredient_name'])
                        my_ingredient = dish_recipe[elem]['ingredient_name']
                        quantity = int(dish_recipe[elem]['quantity']) * person_count
                        ingredient_quantity = {'measure': dish_recipe[elem]['measure'], 'quantity': quantity}
                        shop_list_by_dishes[my_ingredient] = ingredient_quantity
                    else:
                        my_ingredient = dish_recipe[elem]['ingredient_name']
                        quantity = shop_list_by_dishes[my_ingredient]['quantity'] + int(dish_recipe[elem]['quantity']) * person_count
                        ingredient_quantity = {'measure': dish_recipe[elem]['measure'], 'quantity': quantity}
                        shop_list_by_dishes[my_ingredient] = ingredient_quantity
    print('Список покупок: ', shop_list_by_dishes)


dishes_list = input('Введите список блюд через запятую: ')
dishes = dishes_list.split(sep=',')
person_count = int(input('Введите количество участников: '))
get_shop_list_by_dishes(dishes, person_count)

# Задача №3.


def merging_files(file_list):
    filename_dict = {}
    text_dict ={}
    for txt_file in file_list:
        with open(txt_file, 'r', encoding="utf-8") as f:
            text_str_list = f.readlines()
            nof_str_text = len(text_str_list)
            filename_dict[nof_str_text] = txt_file
            text_dict[txt_file] = text_str_list
    filename_list_tuple = sorted(filename_dict.items())
    for elem in filename_list_tuple:
        print((elem[0]))
        with open('total_file.txt', 'a', encoding='utf-8') as f:
            f.write(elem[1]+'\n')
            f.write(str(elem[0])+'\n')
            f.writelines(text_dict[elem[1]])
    print('Текстовый файл успешно создан.')
    return


txt_list = ('1.txt', '2.txt', '3.txt')
merging_files(txt_list)


