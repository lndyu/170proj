from parse import read_input_file, write_output_file
import os

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    #current state of the search
    time = 0
    while(time<1440):
        heuristic_tasks = [(heuristic(task),task) for task in tasks]
        heuristic_tasks.sort(key=lambda x:x[0],reverse = True)

#this is our heuristic. What is the approximate penalty if we don
def heuristic(task,current_time):


    


# Here's an example of how to run your solver.
# if __name__ == '__main__':
#     for input_path in os.listdir('inputs/'):
#         output_path = 'outputs/' + input_path[:-3] + '.out'
#         tasks = read_input_file(input_path)
#         output = solve(tasks)
#         write_output_file(output_path, output)