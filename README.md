# Banker's Algorithm with GUI

This is an implementation of the banker's algorithm with a graphical user interface (GUI) written in Python. The banker's algorithm is a resource allocation and deadlock avoidance algorithm that tests for safety by simulating the allocation of predetermined maximum possible amounts of all resources, and then makes a "s-state" check to test for possible deadlock conditions.

## Usage
To use this program, follow these simple steps:

1. Enter the number of processes and the number of available resources in your system.
2. Enter the maximum resource claims for each process.
3. Enter the current allocated resources for each process.
4. Enter the available resources.
5. Click the `Check` button to see if the current state is safe or not.

The program will display whether the state is safe or not alongside the safe sequence if available.

## Dependencies

This program requires the `tkinter` module which comes pre-installed with most Python distributions. Therefore, you do not need to install any additional dependencies to use this program.

However, it is important to note that this program was developed and tested using Python 3. If you are using an older version of Python, there may be compatibility issues.

## Code Explanation

The implementation of the banker's algorithm with GUI is done using the object-oriented programming (OOP) paradigm in Python. The code comprises mainly of two classes: `BankersAlgorithm` and `Application`.

The `BankersAlgorithm` class contains methods for setting the maximum resource claims for each process (`set_max_claim`), setting the current allocated resources for each process (`set_current_alloc`), setting the available resources (`set_available`), and checking if the current state is safe (`is_safe_state`). 

The `Application` class is responsible for creating the GUI using the `tkinter` module. It has methods for handling user input (`handle_submit`) and checking if the state is safe (`handle_check`). 

When the user enters the required information, the `handle_submit` method creates a new instance of the `BankersAlgorithm` class and sets the maximum resource claims, current allocated resources, and available resources. Then, when the user clicks on the `Check` button, the `handle_check` method calls the `is_safe_state` method of the `BankersAlgorithm` object to check if the state is safe or not. 

If the state is safe, the `safe_label` in the GUI will display the message "SAFE" along with the safe sequence, and the `unsafe_label` will remain blank. On the other hand, if the state is unsafe, the `unsafe_label` will display the message "UNSAFE", and the `safe_label` will remain blank.

Overall, this implementation serves as an effective tool for simulating the banker's algorithm and preventing deadlock in resource allocation systems.
