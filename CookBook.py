with open('recipes.txt', 'r', encoding='utf-8') as file:
    book_cook = {}
    for line in file:
        book_list = []
        key = line.strip()
        count = int(file.readline())
        for row in range(count):
            book_dict = {}
            row_list = file.readline().split('|')
            book_dict['ingredient_name'] = row_list[0]
            book_dict['quantity'] = row_list[1]
            book_dict['measure'] = row_list[2].strip()
            book_list.append(book_dict)
        book_cook[key] = book_list
        file.readline()

# print(f'book_cook = {book_cook}')

with open('book_cook.txt', 'w', encoding='utf-8') as f:
    f.write(f'{book_cook}')


def get_shop_list_by_dishes(dishes, person_count):
    list_by_dishes = {}
    for dish in dishes:
        ingredients = book_cook.get(dish)
        for ingredient in ingredients:
            if list_by_dishes.get(ingredient['ingredient_name']):
                total = (int(
                    list_by_dishes.get(ingredient['ingredient_name']).get(
                        'quantity')) + int(
                    (ingredient['quantity']))) * person_count
                temp_dict = {'measure': ingredient['measure'],
                             'quantity': total}
            else:
                temp_dict = {'measure': ingredient['measure'],
                             'quantity': int(ingredient['quantity'])}
            list_by_dishes[ingredient['ingredient_name']] = temp_dict
    print(list_by_dishes)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
