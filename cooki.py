#EX 1
import os
def my_cook_book ():
    cook_book = {}
    with open('ing.txt', 'r', encoding='utf-8') as f:
        for line in f:
            dish = line.strip()
            ingridients_count = int(f.readline())
            ingridients = []
            for i in range(ingridients_count):
                ing = f.readline().strip().split('|')
                ingridients.append({'ingridient_name': ing[0], 'quantity': int(ing[1]), 'measure': ing[2]})
            cook_book[dish] = ingridients
            f.readline()
    return cook_book
print (my_cook_book())

#EX 2
def get_shop_list_by_dishes(dishes, person_count):
    ingredient_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient['ingridient_name'] not in ingredient_list:
                ingredient_list[ingridient['ingridient_name']] = {'measure': ingridient['measure'], 'quantity': ingridient['quantity']*person_count}
            else:
                ingredient_list[ingridient['ingridient_name']]['quantity'] += ingridient['quantity']*person_count
    return ingredient_list


#EX 3
def list_new(txt):
    dict_file = {}
    list_file = os.listdir("txt")
    for i in list_file:
        with open(txt + '\\' + i, 'r', encoding='utf-8') as f:
            file_1 = f.readlines()
            dict_file[i] = len(file_1)
    return dict_file


list_new('txt')


def file_result(txt):
    list_utem = list(list_new(txt).items())
    list_s = [i[0] for i in sorted(list_utem, key=lambda items: items[1])]
    os.remove('write_file.txt')
    for name_file in list_s:
        with open('write_file.txt', 'a', encoding='utf-8') as f_1:
            with open(txt + '\\' + name_file, 'r', encoding='utf-8') as f:
                text_file = f.readlines()
            f_1.write(name_file + '\n')
            f_1.write(str(len(text_file)) + '\n')
            f_1.writelines(text_file)
            f_1.write('\n')

    return


file_result('txt')


    

    
