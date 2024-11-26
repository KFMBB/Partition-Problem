import tkinter as tk
from tkinter import messagebox
import random

# Function to calculate the sum of all numbers in a list
def sum(set):
    summation = 0
    for i in set:
        summation += i
    return summation

# Function to solve the partition problem
def partition_problem_dynamic(set):
    total_sum = sum(set)  # Find the total sum of all numbers
    if total_sum % 2 != 0:  # If the total sum is odd, partitioning is not possible
        return False, [], []

    target = total_sum // 2  # Each subset should sum up to half of the total
    n = len(set)  # Number of items in the list

    # Create a 2D table to track possible sums
    part = [[False for _ in range(n + 1)] for _ in range(target + 1)]
    subset = [[[] for _ in range(n + 1)] for _ in range(target + 1)]  # Store subsets for the solution

    # Initialize the table
    for i in range(n + 1):
        part[0][i] = True  # A sum of 0 is always possible (with an empty subset)
        subset[0][i] = []  # Empty subset for sum 0

    for i in range(1, target + 1):
        part[i][0] = False  # If there are no items, sums other than 0 are not possible

    # Fill the table by checking each item
    for i in range(1, target + 1):  # Loop through all possible sums
        for j in range(1, n + 1):  # Loop through all items
            part[i][j] = part[i][j - 1]  # Exclude the current item by default
            subset[i][j] = subset[i][j - 1]  # Copy the subset without the current item

            if i >= set[j - 1]:  # If the current item can be included
                if part[i - set[j - 1]][j - 1]:  # Check if the remaining sum is possible
                    part[i][j] = True  # Mark as possible
                    subset[i][j] = subset[i - set[j - 1]][j - 1] + [set[j - 1]]  # Add the current item

    # If we can't find a solution, return False
    if not part[target][n]:
        return False, [], []

    # Otherwise, return the subsets
    subset1 = subset[target][n]
    subset2 = [item for item in set if item not in subset1]  # The remaining items
    return True, subset1, subset2

# This function checks if a partition is possible and displays the result
def check_partition():
    try:
        # Get the input from the user
        input_values = entry.get()
        set_values = list(map(int, input_values.split()))  # Convert the input to a list of numbers

        # Solve the partition problem
        result, subset1, subset2 = partition_problem_dynamic(set_values)

        # Show the result
        if result:
            result_text.set(f"Partition is possible.\nSubset 1: {subset1}\nSubset 2: {subset2}")
            history_list.insert(tk.END, f"Set: {set_values} -> Possible, Subsets: {subset1} and {subset2}")
        else:
            result_text.set("Partition is not possible.")
            history_list.insert(tk.END, f"Set: {set_values} -> Not Possible")
    except ValueError:
        # Show an error if the input is invalid
        messagebox.showerror("Input Error", "Please enter a list of integers separated by spaces.")

# This function clears all fields and the history
def reset_fields():
    entry.delete(0, tk.END)  # Clear the input field
    result_text.set("")  # Clear the result display
    history_list.delete(0, tk.END)  # Clear the history list
    random_count_entry.delete(0, tk.END)  # Clear the random count input field

# This function generates a random list of numbers based on the user's input
def generate_random_list():
    try:
        count = int(random_count_entry.get())  # Get the number of elements to generate
        if count <= 0:
            raise ValueError  # Show an error if the number is invalid
        random_list = [random.randint(1, 100) for _ in range(count)]  # Generate the random numbers
        entry.delete(0, tk.END)  # Clear the input field
        entry.insert(0, " ".join(map(str, random_list)))  # Insert the random numbers into the input field
    except ValueError:
        # Show an error if the input for count is invalid
        messagebox.showerror("Input Error", "Please enter a valid positive integer for the number of elements.")

# Create the main application window
root = tk.Tk()
root.title("Advanced Partition Problem Solver")  # Set the title of the window
root.geometry("700x500")  # Set the size of the window

result_text = tk.StringVar()  # Variable to display the result

# Create sections for the layout
input_frame = tk.Frame(root)
input_frame.pack(pady=10)
random_frame = tk.Frame(root)
random_frame.pack(pady=10)
result_frame = tk.Frame(root)
result_frame.pack(pady=10)
history_frame = tk.Frame(root)
history_frame.pack(pady=10, fill="both", expand=True)

# Input section
input_label = tk.Label(input_frame, text="Enter numbers separated by spaces:")
input_label.grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(input_frame, width=50)
entry.grid(row=0, column=1, padx=5, pady=5)

check_button = tk.Button(input_frame, text="Check Partition", command=check_partition)
check_button.grid(row=1, column=0, padx=5, pady=5)
reset_button = tk.Button(input_frame, text="Reset", command=reset_fields)
reset_button.grid(row=1, column=1, padx=5, pady=5)

# Random list generator section
random_label = tk.Label(random_frame, text="Number of elements for random list:")
random_label.grid(row=0, column=0, padx=5, pady=5)
random_count_entry = tk.Entry(random_frame, width=10)
random_count_entry.grid(row=0, column=1, padx=5, pady=5)
generate_button = tk.Button(random_frame, text="Generate Random List", command=generate_random_list)
generate_button.grid(row=0, column=2, padx=5, pady=5)

# Result display section
result_label = tk.Label(result_frame, text="Result:")
result_label.grid(row=0, column=0, padx=5, pady=5)
result_display = tk.Label(result_frame, textvariable=result_text, font=("Arial", 12, "bold"))
result_display.grid(row=0, column=1, padx=5, pady=5)

# History display section
history_label = tk.Label(history_frame, text="History:")
history_label.pack(anchor="w")
history_list = tk.Listbox(history_frame, height=10, width=80)
history_list.pack(padx=10, pady=5, fill="both", expand=True)

# Run the application
root.mainloop()
