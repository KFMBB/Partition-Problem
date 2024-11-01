# The objective of this project is to devise a dynamic programming approach to address the partition problem.
def sum(set):
    """
    :param set: a list of numbers.
    :return sum: summation of the elements in a given list.
    """
    summation = 0

    for i in set:

        summation += i

    return summation


def partition_problem_BR(set):
    """
    :param set: a set of numbers.
    :return (T/F) T: Satisfies the Partition Problem, F otherwise.
    This brute-force approach generates all possible subsets and checks
    if there is a subset that sums to half of the total sum of the set.
    """
    sumOfSet = sum(set)
    if sumOfSet % 2 != 0:  # If the sum is odd, we can't split it evenly
        return False

    target = sumOfSet // 2  # Each subset needs to sum up to half the total sum
    powerSetSize = 2 ** len(set)  # Number of subsets
    setSize = len(set)

    # Iterate over all possible subsets using binary representation
    for counter in range(powerSetSize):
        subSetSum = 0
        for j in range(setSize):
            if (counter & (1 << j)) > 0:  # Check if the j-th element is in the subset
                subSetSum += set[j]

        # Check if this subset meets the target sum
        if subSetSum == target:
            return True  # Partition is possible

    return False  # No partition found