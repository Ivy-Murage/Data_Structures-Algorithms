from itertools import combinations, chain
# create the items class


class Pellets(object):

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):
        result ="Value = {}. Weight: {}".format(self.value, self.weight)
        return result


# build the items in a list
def get_items():
    weight_list = [1, 3, 4, 5, 6, 8, 11, 12]
    values_list = [1200, 1700, 2000, 2500, 3000, 4100, 7000, 7500]
    collection = []
    for i in range(len(weight_list)):
        # big notation is O(n)
        collection.append(Pellets(values_list[i], weight_list[i]))
    return collection


# create the powerset
def powerset(iterable):
    s = list(iterable)
    # powerset removes the empty set
    return list(chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1)))


# the main code
# big O notation is O(n^2) in the worst case scenario
def choose_best(pset, max_weight):
    best_val = 0.0
    best_set = None
    for items in pset:
        items_val = 0.0
        items_weight = 0.0
        for item in items:
            items_val += item.get_value()
            items_weight += item.get_weight()
        if items_weight <= max_weight and items_val > best_val:
            best_val = items_val
            best_set = items
    return best_set, best_val


# code to test
def test_best(max_weight=20):
    items = get_items()
    pset = powerset(items)
    taken, val = choose_best(pset, max_weight)
    print('Total value of items taken is', val)
    for item in taken:
        print(item)


# run it 
if __name__ == '__main__':
    test_best()
