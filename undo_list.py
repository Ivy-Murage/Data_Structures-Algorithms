# Python Program to implement the above approach.

# this is the main list which will be printed after doing any of the above operations
main_list = []

# this is the list for tracking the operations being performed
undo_list = []

# this is the redo list which will keep track of the undo operations done.
redo_list = []                                                             \


def add(value):
    """
    this is the function to add the value to the list
    """
    # index at will we will add the value
    idx=len(main_list)
    # value will be added to the main_list
    main_list.append(value)
    # we will update undo_list, by appending the operation as 'r', as we are adding value to the list, so its undo operation will do the reverse of it, so we will append operation as 'r'.
    undo_list.append(('r',idx,value))
    print(main_list)




def remove(value):
    """
    this is the function to remove the value from the list
    """
    # length of the main_list
    length=len(main_list)
    # if the length of the main_list is 0
    if(length==0):
        return
    # if the value is not present in the main_list
    if value not in main_list:
        return
    # index of the value that we have to remove
    idx = main_list.index(value)
    # removing value from the main_list
    main_list.remove(value)
    # we will update undo_list, by appending the operation as 'a', as we are removing value from the list , so its undo operation will do the reverse of it , so we will append operation as 'a'.
    undo_list.append(('a', idx, value))
    print(main_list)




def undo():
    """
    this is the function to undo the value

    """
     #length of the undo_list
    length = len(undo_list)
     # if  the length of the undo_list is 0 ,means there is nothing to do undo operation
    if(length==0):
        return
    # selecting the latest undo operation that we have to perform
    cur_tuple=undo_list.pop();
    # selecting the type of the operation that we have to perform
    cur_tuple_operation=cur_tuple[0]
    # selecting the index at which we will perform latest undo operation.
    cur_tuple_index=cur_tuple[1]
     # selecting the value on which we will perform the latest undo operation
    cur_tuple_value=cur_tuple[2]
     # if the operation we have to do undo is 'a'
    if(cur_tuple_operation=='a'):
        # adding value to main_list
        main_list.insert(cur_tuple_index,cur_tuple_value)
        # also we will update redo_list by appending the operaion as 'r' as  the undo current operation is 'a' , so redo operation will restore the most recent undo operation beging performed.
        redo_list.append(('r',cur_tuple_index,cur_tuple_value))
    # if the operation we have to do undo is 'r'
    elif(cur_tuple_operation=='r') :
        # removing the value from the main_list
        main_list.pop(cur_tuple_index)
        # also we will update redo_list,by appending the operation as 'a', as the undo current operation is 'r' , so redo operation will restore the most recent undo operation beging performed.
        redo_list.append(('a',cur_tuple_index,cur_tuple_value))
    print(main_list)




def redo():
    """
    this is the function to redo the value
    """
    #length of the redo_list
    length=len(redo_list)
    # if the length of the redo list is 0
    if(length==0):
        return
    # selecting the latest redo operation that we have to perform.
    cur_tuple=redo_list.pop();
    # selecting the type of the operation that we have to perform
    cur_tuple_operation=cur_tuple[0]
    # selecting the index at which we will perform latest redo operation.
    cur_tuple_index=cur_tuple[1]
    # selecting the value on which we will perform the latest redo operation.
    cur_tuple_value=cur_tuple[2]
    # if the operation we have to do redo is 'a'
    if(cur_tuple_operation=='a'):
         # adding value to main_list
        main_list.insert(cur_tuple_index,cur_tuple_value)
    # if the operation we have to do redo is 'r'
    elif(cur_tuple_operation=='r'):
         # removing the value from the main_list
        main_list.pop(cur_tuple_index)
    print(main_list)


add(1)
add(2)
add(3)
remove(2)
add(5)
add(4)
undo()
undo()
undo()
undo()
undo()
undo()
redo()
redo()
redo()
redo()
redo()
redo()