import tkinter as tk
from tkinter import messagebox
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


# def partition_problem_BR(set):
#     """
#     :param set: a set of numbers.
#     :return (T/F) T: Satisfies the Partition Problem, F otherwise.
#     This brute-force approach generates all possible subsets and checks
#     if there is a subset that sums to half of the total sum of the set.
#     """
#     sumOfSet = sum(set)
#     if sumOfSet % 2 != 0:  # If the sum is odd, we can't split it evenly
#         return False
#
#     target = sumOfSet // 2  # Each subset needs to sum up to half the total sum
#     powerSetSize = 2 ** len(set)  # Number of subsets
#     setSize = len(set)
#
#     # Iterate over all possible subsets using binary representation
#     for counter in range(powerSetSize):
#         subSetSum = 0
#         for j in range(setSize):
#             if (counter & (1 << j)) > 0:  # Check if the j-th element is in the subset
#                 subSetSum += set[j]
#
#         # Check if this subset meets the target sum
#         if subSetSum == target:
#             return True  # Partition is possible
#
#     return False  # No partition found


def partition_problem_dynamic(set):
    total_sum = sum(set)
    if total_sum % 2 != 0:
        return False    # If the total sum is odd, we can't split it evenly
    target = total_sum // 2
    n = len(set)
    part = [[True for i in range(n + 1)] for j in range(target + 1)] # this is the initialization for partition table
    for i in range(n + 1):
        part[0][i] = True # this will initialize the top row as True

    for i in range(1, target + 1):
        part[i][0] = False # this will initialize the leftmost column as False , EXCEPT [0][0] !!

    for i in range(1, target + 1):
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
            if i >= set[j - 1]:
                part[i][j] = part[i][j] or part[i - set[j - 1]][j - 1] # this shall fill the partition table bottom - up

    return part[target][n]



## Here we can say that if the length of the list is small do a brute force
## However this will be inefficient because why would i even want to use the brute force !!


def check_partition():
    try:
        # Parse the input list
        input_values = entry.get()
        set_values = list(map(int, input_values.split()))

        # Check the partition possibility
        result = partition_problem_dynamic(set_values)

        # Display the result
        if result:
            result_text.set("Partition is possible.")
            history_list.insert(tk.END, f"Set: {set_values} -> Possible")
        else:
            result_text.set("Partition is not possible.")
            history_list.insert(tk.END, f"Set: {set_values} -> Not Possible")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a list of integers separated by spaces.")


def reset_fields():
    entry.delete(0, tk.END)
    result_text.set("")
    history_list.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Advanced Partition Problem Solver")
root.geometry("500x400")

# Result text variable
result_text = tk.StringVar()

# Frames for better layout
input_frame = tk.Frame(root)
input_frame.pack(pady=10)
result_frame = tk.Frame(root)
result_frame.pack(pady=10)
history_frame = tk.Frame(root)
history_frame.pack(pady=10, fill="both", expand=True)

# Input section
input_label = tk.Label(input_frame, text="Enter numbers separated by spaces:")
input_label.grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(input_frame, width=50)
entry.grid(row=0, column=1, padx=5, pady=5)

# Buttons for actions
check_button = tk.Button(input_frame, text="Check Partition", command=check_partition)
check_button.grid(row=1, column=0, padx=5, pady=5)
reset_button = tk.Button(input_frame, text="Reset", command=reset_fields)
reset_button.grid(row=1, column=1, padx=5, pady=5)

# Result display
result_label = tk.Label(result_frame, text="Result:")
result_label.grid(row=0, column=0, padx=5, pady=5)
result_display = tk.Label(result_frame, textvariable=result_text, font=("Arial", 12, "bold"))
result_display.grid(row=0, column=1, padx=5, pady=5)

# History display
history_label = tk.Label(history_frame, text="History:")
history_label.pack(anchor="w")
history_list = tk.Listbox(history_frame, height=10, width=60)
history_list.pack(padx=10, pady=5, fill="both", expand=True)

# Run the main loop
root.mainloop()