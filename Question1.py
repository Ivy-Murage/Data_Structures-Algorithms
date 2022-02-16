# function that checks if there is a duplicate in a  list

# Big O-natation is 0(n) in the worst case scenario
def check_duplicate(list1):
    if len(list1) <= 0:
        return -1
    for i in list1:
        # checks if the duplicated number has been repeated an even or odd number of times
        counter = list1.count(i)
        if counter % 2 == 0:
            return False
    return True


if __name__ == "__main__":
    # Prompts user to enter a list of numbers
    myList = list(map(int, input("Enter elements for your list: ").split()))
    result = check_duplicate(myList)
    if result == -1:
        print("This list is empty")
    print(result)
