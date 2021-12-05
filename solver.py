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
    total_profit = 0
    completed = set()
    while(time<1440):
        heuristic_tasks = [(heuristic(task,time),task) for task in tasks if task not in completed]
        selected = max(heuristic_tasks,key=lambda x:x[0])
        total_profit += profit(selected,time)
        completed.add(selected)
        time += selected.get_duration()
    return(total_profit)

#this is our heuristic. What is the approximate penalty if we don
def heuristic(task,current_time):
    return profit(task,current_time)/task.get_duration()

#this is the profit if we select task at this time
def profit(task,current_time):
    overdue = current_time + task.get_duration() - task.deadline()
    return task.get_late_benefit(overdue)


    


# Here's an example of how to run your solver.
# if __name__ == '__main__':
#     for input_path in os.listdir('inputs/'):
#         output_path = 'outputs/' + input_path[:-3] + '.out'
#         tasks = read_input_file(input_path)
#         output = solve(tasks)
#         write_output_file(output_path, output)