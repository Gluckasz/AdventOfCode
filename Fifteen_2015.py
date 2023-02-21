import copy
data = open("/Users/lukasz/Desktop/Aoc 2015/Fifteen_2015_data.txt", "r")
ingredients = []
for line in data.readlines():
    line_split = line.split()
    ingredients.append((int(line_split[2][:-1]), int(line_split[4][:-1]), int(line_split[6][:-1]), int(line_split[8][:-1])))
ingredients_sum = []
for ingredient in ingredients:
    ingredients_sum.append(sum(ingredient))
total_scores = {0}
print(ingredients)
def find_ingredients(ingredients_amount, best_ingredient, current_ingredient, end_loop_condition, end_loop_counter):
    for ingredient in ingredients_amount:
        if ingredient < 0:
            total_scores.add(multiplication)
            return 1
    points = []
    for i in range(len(ingredients[0])):
        sum = 0
        for j in range(len(ingredients_amount)):
            sum += ingredients[j][i] * ingredients_amount[j]
        points.append(sum)
    multiplication = 1
    for row in points:
        if row < 0:
            multiplication *= 0
        else:
            multiplication *= row
    ingredients_amount[points.index(max(points))] -= 1
    print(ingredients_amount, points, ingredients_amount[ingredients_amount.index(max(ingredients_amount))])
    if points[best_ingredient] <= 0:
        return 1
    for i in range(len(points)):
        if points[i] == min(points):
            print(i)
            max_value = 0
            for j in range(len(ingredients)):
                if ingredients[j][i] > max_value:
                    max_value = ingredients[j][i]
                    max_value_address = j
            current_ingredient = max_value_address
            break
    for i in range(len(points)):
        if points[i] <= 0:
            max_value = 0
            for j in range(len(ingredients)):
                if ingredients[j][i] > max_value:
                    max_value = ingredients[j][i]
                    max_value_address = j
            current_ingredient = max_value_address
    if current_ingredient >= len(ingredients_amount):
        current_ingredient = 0
    ingredients_amount[current_ingredient] += 1
    end_loop_counter += 1
    if end_loop_counter == 3:
        end_loop_counter = 0
        if end_loop_condition == points:
            total_scores.add(multiplication)
            return 1
        end_loop_condition = points
    find_ingredients(ingredients_amount.copy(), best_ingredient, current_ingredient, end_loop_condition, end_loop_counter)
    ingredients_amount[current_ingredient] -= 1
    total_scores.add(multiplication)
find_ingredients([0, 0, 100, 0], 2, 0, 0, 0)
print(max(total_scores))
