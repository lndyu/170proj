# CS 170 Project Fall 2021

Take a look at the project spec before you get started!

Requirements:

Python 3.6+

Files:
- `parse.py`: functions to read/write inputs and outputs
- `solver.py`: where you should be writing your code to solve inputs
- `Task.py`: contains a class that is useful for processing inputs

When writing inputs/outputs:
- Make sure you use the functions `write_input_file` and `write_output_file` provided
- Run the functions `read_input_file` and `read_output_file` to validate your files before submitting!
- These are the functions run by the autograder to validate submissions

To get a list of output files, you change the "size" variable to whatever you need, either the string "small", "medium", or "large". 
If your input is small, make sure you adjust the condition if i != _. If the input is small, it should be i != 184. Otherwise, you can make it if i != 0. Then, simply run solver.py. 