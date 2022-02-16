wts = [1, 3, 4, 5, 6, 8, 11, 12]
vals = [1200, 1700, 2000, 2500, 3000, 4100, 7000, 7500]
capacity = 20

# Make the table (list comprehension)

w, h = capacity + 1, len(vals)

table = [[0 for x in range(w)] for y in range(h)]

# First iterate over the items (rows)
# second iterate over the columns which represent weights

for index in range(len(vals)):
    for weight in range(w):
        # If the item weights more than the capacity at that column?
        # Take above value, that problem was solved
        if wts[index] > weight:
            table[index][weight] = table[index - 1][weight]
            continue

        # if the value of the item < capacity
        prior_value = table[index - 1][weight]
        #         val of current item  + val of remaining weight
        new_option_best = vals[index] + table[index - 1][weight - wts[index]]
        table[index][weight] = max(prior_value, new_option_best)
solution_arr = []

for x in table:
    for y in x:
        solution_arr.append(y)

print(max(solution_arr))