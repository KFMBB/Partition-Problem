
# Advanced Partition Problem Solver

## Overview

The **Advanced Partition Problem Solver** is a Python application that solves the Partition Problem using two approaches: a brute-force solution and a dynamic programming solution. The program determines if a given set of integers can be divided into two subsets with equal sums and provides a user-friendly GUI built with `tkinter` for interactive use.

This project logs the runtime for the dynamic programming solution on each input set, allowing users to assess the performance of the algorithm.

## Features

- **Brute-Force Solution**: A straightforward method that checks all possible subsets to determine if partitioning is feasible (included for demonstration and comparison).
- **Dynamic Programming Solution**: Efficiently finds solutions for larger sets, returning partition subsets (if found) and the computation runtime.
- **Interactive User Interface**: Allows users to enter integer sets, check partition results, and view runtime for the dynamic programming solution.
- **History Log**: Records each result, including partition feasibility, subsets, and runtime for easy review.

## Setup

1. **Requirements**: Python 3.x is required to run the application.
2. **Install `tkinter`**: This library is usually included with Python installations. If needed, install it with:
   ```bash
   sudo apt-get install python3-tk  # For Debian/Ubuntu
   ```
3. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

## Usage

1. **Run the Application**:
   ```bash
   python partition_solver.py
   ```
2. **Enter Input Set**: In the input field, type integers separated by spaces.
3. **Random input generation**: Users can test the implementation on a randomly generated set.
4. **Check Partition**: Click the "Check Partition" button to determine if the set can be split into two equal subsets.
5. **View Results**: The application will display whether partitioning is possible, the two subsets (if possible), and the computation runtime.
6. **Reset Fields**: Click "Reset" to clear all input and history.

## Code Structure

### Key Functions

- `sum(set)`: Computes the sum of the elements in the input set.
  
- `partition_problem_BR(set)`: Implements a brute-force solution to the Partition Problem by generating all subsets. Not efficient for large sets due to exponential time complexity.
  
- `partition_problem_dynamic(set)`: Uses a dynamic programming approach to determine if a set can be partitioned into two equal subsets. Returns whether a partition is possible, the two subsets, and the runtime for analysis.

- `check_partition()`: Parses user input and checks partition feasibility using the dynamic programming solution. Results and runtime are logged in the GUI’s history.

- `reset_fields()`: Clears all input fields and history logs in the GUI.

### GUI Components

- **Input Frame**: Accepts integer input from the user.
- **Result Frame**: Displays partition results, including subsets and runtime if partitioning is possible.
- **History Frame**: Logs each test’s results, including partition feasibility and runtime, for easy reference.

## Sample Run and Results

Using the input set `1 5 3 9 12`:
- **Result**: Partition possible.
- **Subsets**: `[9, 3]` and `[12, 5, 1]`
- **Runtime**: Approximately `0.0001` seconds.

Using the input set `1 2 3 4 5 6`:
- **Result**: Partition not possible.
- **Runtime**: Approximately `0.0002` seconds.

| Input Set           | Input Size | Partition Possible | Runtime (seconds) |
|---------------------|------------|--------------------|--------------------|
| `[1, 5, 3, 9, 12]` | 5          | Yes               | 0.0001            |
| `[1, 2, 3, 4, 5, 6]` | 6        | No                | 0.0002            |

## Known Limitations

- **Brute-force Limitation**: The brute-force approach has exponential time complexity and is not practical for large sets.
- **Memory Usage**: The dynamic programming solution requires a matrix to store subset sums, which can lead to high memory consumption for large input sets.

