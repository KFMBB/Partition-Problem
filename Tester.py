def sum_list(userlist) :

    sum = 0                           # the function will return the summation of the given list

    for i in userlist :

        sum += userlist[i]

    return sum


def bubble_sort(arr):

    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def partition_problem(userlist) :
    sumOfList = sum_list(userlist)

    if sumOfList % 2 != 0 :             # check if the summation of the list is even
        return -1                       # the list can not be divided into 2 sub lists

    goal = sumOfList / 2                # the number that the each sub list needs to sum up to

    bubble_sort(userlist)

    sumofelements = 0

    sublist1 = []
    sublist2 = []
    i = 0
    flag = True
    while flag :
        sumofelements += userlist[i]
        sublist1.append(userlist[i])
        i+=1
        if sumofelements == goal :
            flag = False
            break
    for i in userlist :
        sublist2.append(i)




