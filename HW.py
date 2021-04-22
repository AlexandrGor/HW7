
def read_recipes(filename):
    with open(filename, 'rt', encoding = 'utf-8') as file:
        new_dish = True
        amount = False
        ingredients = False
        for line in file:
            line = line.strip()
            line = line.strip(' ')
            if line:
                if new_dish:
                    current_dish = line
                    cook_book.update({current_dish: []})
                    new_dish = False
                    amount = True
                    continue
                if amount:
                    #cook_book[current_dish] += [{'ingredient_name': '', 'quantity': '', 'measure': ''}] * int(line)
                    amount = False
                    ingredients = True
                    continue
                if ingredients:
                    lis = line.split('|')
                    lis = [str.strip(' ') for str in lis]
                    cook_book[current_dish] += [{'ingredient_name': lis[0], 'quantity': int(lis[1]), 'measure': lis[2]}]
                    continue
            else:
                new_dish = True
                ingredients = False
cook_book = {}
read_recipes('recipes.txt')
print(cook_book)
