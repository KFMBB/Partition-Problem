import tkinter as tk
from tkinter import messagebox
import time


def sum(set):
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


def partition_problem_dynamic(set):
    start_time = time.time()  # Start timing
    total_sum = sum(set)
    if total_sum % 2 != 0:
        return False, [], [], 0  # If the total sum is odd, we can't split it evenly

    target = total_sum // 2
    n = len(set)
    part = [[False for _ in range(n + 1)] for _ in range(target + 1)]
    subset = [[[] for _ in range(n + 1)] for _ in range(target + 1)]  # To store subsets that make the target sum

    for i in range(n + 1):
        part[0][i] = True  # Initialize the top row as True
        subset[0][i] = []  # Empty subset for sum 0

    for i in range(1, target + 1):
        part[i][0] = False  # Initialize the leftmost column as False

    for i in range(1, target + 1):
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
            subset[i][j] = subset[i][j - 1]  # Initially, take the subset without the current element

            if i >= set[j - 1]:
                if part[i - set[j - 1]][j - 1]:
                    part[i][j] = True
                    subset[i][j] = subset[i - set[j - 1]][j - 1] + [set[j - 1]]

    # If there's no partition, return false
    if not part[target][n]:
        return False, [], [], 0

    # Extract the subset that sums to target
    subset1 = subset[target][n]
    subset2 = [item for item in set if item not in subset1]  # Get the complement subset

    end_time = time.time()  # End timing
    runtime = end_time - start_time

    return True, subset1, subset2, runtime


def check_partition():
    try:
        # Parse the input list
        input_values = entry.get()
        set_values = list(map(int, input_values.split()))

        # Check the partition possibility and retrieve the subsets along with runtime
        result, subset1, subset2, runtime = partition_problem_dynamic(set_values)

        # Display the result
        if result:
            result_text.set(f"Partition is possible.\nSubset 1: {subset1}\nSubset 2: {subset2}")
            history_list.insert(tk.END, f"Set: {set_values} -> Possible, Subsets: {subset1} and {subset2}, Runtime: {runtime:.4f} seconds")
        else:
            result_text.set("Partition is not possible.")
            history_list.insert(tk.END, f"Set: {set_values} -> Not Possible, Runtime: {runtime:.4f} seconds")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a list of integers separated by spaces.")


def reset_fields():
    entry.delete(0, tk.END)
    result_text.set("")
    history_list.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Advanced Partition Problem Solver")
root.geometry("600x400")

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
