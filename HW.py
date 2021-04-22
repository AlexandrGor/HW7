def read_recipes(filename):
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            print(line, end='')
read_recipes('recipes.txt')
