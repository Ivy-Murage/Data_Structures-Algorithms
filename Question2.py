# prompts the user to enter a list of numbers
def get_input():
    global myList
    myList = list(map(int, input("Enter the numbers to store in the list: ").split()))
    # checks whether the numbers in the list are less or equal to zero
    # Big O notation is O(n) in the worst case scenario
    less = all(element <= 0 for element in myList)
    if less is True:
        print("All numbers should be greater than zero. Try again")
        get_input()
    else:
        print("The entered list {}: ".format(myList))
        get_sum()


# Big O notation  is O(n)
def get_sum():
    # arranges the values in the list from the largest to the smallest
    sortedlist = sorted(myList, reverse=True)
    print(sortedlist)
    while True:
        # prompts the user to enter the number of values they want to add
        num = int(input("Enter the numbers you want to find the sum: "))
        if num > len(sortedlist):
            print("The number should be less than the number of values  in the list")
        else:
            break
    newlist = sortedlist[:num]
    listsum = 0
    for element in newlist:
        # Big notation is O(1) for adding
        listsum = listsum + element
    print(newlist)
    print(listsum)


get_input()
