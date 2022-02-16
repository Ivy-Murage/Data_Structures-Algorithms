class Undoablelist(object):
    def __init__(self):
        # list for values
        self.data = []
        # list that holds the operation that was done, index of value and the value
        self.undo_list = []
        self.redo_list = []

    def add(self, item):
        # add an item to the list

        # time complexity is O(1)
        global idx
        idx = len(self.data)
        self.data.append(item)
        # appends a tuple that has  the remove operation that is to be  done, the index and value  in the undo list
        self.undo_list.append(('r', idx, item))
        print(sorted(self.data))

    def delete(self, item):
        # deletes an item from  the list

        # time complexity is O(1)
        if item not in self.data:
            return
        else:
            self.data.remove(item)
            # appends a tuple that has  the add operation that is to be  done, the index and value  in the redo list
            self.undo_list.append(('a', idx, item))
        print(sorted(self.data))

    def undo(self):
        # cancels the last action that was performed which can either be delete or insert
        result = None
        length = len(self.undo_list)
        if length == 0:
            return
        car_tuple = self.undo_list.pop()
        car_tuple_operation = car_tuple[0]
        car_tuple_index = car_tuple[1]
        car_tuple_value = car_tuple[2]

        if car_tuple_operation == 'a':
            # check if the opeartion is remove or add
            # if the operation is add, the value is added back to the list at the position it was initially
            # big O notation  is O(1)
            self.data.insert(car_tuple_index, car_tuple_value)
            # the value and the index is added in the redo list
            self.redo_list.append(('r', car_tuple_index, car_tuple_value))

        elif car_tuple_operation == 'r':
            # big O notation  is O(1)
            self.data.pop(car_tuple_index)
            # if the operation is remove, the value is removed from the list using the pop method.
            self.redo_list.append(('a', car_tuple_index, car_tuple_value))
        print(sorted(self.data))

    def redo(self):
        # it cancels the undo operation that was performed
        length = len(self.redo_list)
        if length == 0:
            return
        car_tuple = self.redo_list.pop()
        car_tuple_operation = car_tuple[0]
        car_tuple_index = car_tuple[1]
        car_tuple_value = car_tuple[2]

        if car_tuple_operation == 'a':
            # big O notation  is O(1)
            self.data.insert(car_tuple_index, car_tuple_value)
            # big O notation  is O(1)
        elif car_tuple_operation == 'r':
            self.data.pop(car_tuple_index)
        print(sorted(self.data))


final = Undoablelist()
final.add(23)
final.add(1)
final.add(7)
final.add(18)
final.undo()
final.undo()
final.undo()
final.redo()
final.redo()
final.redo()
final.delete(7)
final.undo()
final.redo()


