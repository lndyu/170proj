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
    total_tasks = len(tasks)
    resulting_sequence = []
    total_profit = 0
    constant_range = [0.01 * x for x in range(1, 201)]
    for constant in constant_range:
        time = 1440
        completed = set()
        temp_sequence = []
        temp_profit = 0
        while(time>0 and len(completed) != total_tasks):
            heuristic_tasks = [(heuristic(task,time,constant),task) for task in tasks if task not in completed]
            selected = max(heuristic_tasks,key=lambda x:x[0])
            task = selected[1]
            temp_sequence.append(task.get_task_id())
            temp_profit += profit(task,time)
            completed.add(task)
            time -= task.get_duration()
        if temp_profit > total_profit: 
            resulting_sequence = temp_sequence
            total_profit = temp_profit
    resulting_sequence.pop()
    final_result = []
    for i in range(len(resulting_sequence)):
        final_result.append(resulting_sequence[len(resulting_sequence)-i-1])
    return final_result

#this is our heuristic. What is the approximate penalty if we don
def heuristic(task,current_time,constant):
    return (constant*profit(task,current_time)-task.get_max_benefit())/task.get_duration() 

#this is the profit if we select task at this time
def profit(task,current_time):
    overdue = current_time + task.get_duration() - task.deadline
    return task.get_late_benefit(overdue)


    


# Here's an example of how to run your solver.
# if __name__ == '__main__':
#     for input_path in os.listdir('inputs/'):
#         output_path = 'outputs/' + input_path[:-3] + '.out'
#         tasks = read_input_file(input_path)
#         output = solve(tasks)
#         write_output_file(output_path, output)

size = 'small'

for i in range(1,301):
    if(i != 184):
        print(i)
        tasks_list = read_input_file('inputs/' + size + '/' + size + '-' + str(i) + '.in')
        result = solve(tasks_list)
        write_output_file('outputs/' + size + '/' + size + '-' + str(i) + '.out',result)
