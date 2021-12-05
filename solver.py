from parse import read_input_file, write_output_file
import os

overall_best = 0

def solve(tasks,current_profit = 0):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    #select the igloo
    #create new list of tasks with modifications
    #recursively call on new list
    


# Here's an example of how to run your solver.
# if __name__ == '__main__':
#     for input_path in os.listdir('inputs/'):
#         output_path = 'outputs/' + input_path[:-3] + '.out'
#         tasks = read_input_file(input_path)
#         output = solve(tasks)
#         write_output_file(output_path, output)