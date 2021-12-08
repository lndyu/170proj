from parse import read_input_file, write_output_file
import os

def solve_simple(tasks,constant=0.807,time = 0):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    #current state of the search

    total_tasks = len(tasks)
    total_profit = 0
    completed = set()
    resulting_sequence = []
    while(time < 1440 and len(completed) != total_tasks):
        heuristic_tasks = [(heuristic(task,time,constant),task) for task in tasks if task not in completed]
        selected = max(heuristic_tasks,key=lambda x:x[0])
        task = selected[1]
        resulting_sequence.append(task)
        total_profit += profit(task,time)
        completed.add(task)
        time += task.get_duration()
    extra_task = resulting_sequence.pop()
    #print(total_profit)
    return [a.get_task_id() for a in resulting_sequence],total_profit - profit(extra_task,time)


#this is our heuristic. What is the approximate penalty if we don
def heuristic(task,current_time,constant):
    
    return (profit(task,current_time)*(constant)**(max(1,(task.get_deadline() - current_time))/task.get_duration())/task.get_duration() )

#this is the profit if we select task at this time
def profit(task,current_time):
    if(current_time + task.get_duration() > 1440):
        return 0
    overdue = current_time + task.get_duration() - task.deadline
    return task.get_late_benefit(overdue)


    


# Here's an example of how to run your solver.
# if __name__ == '__main__':
#     for input_path in os.listdir('inputs/'):
#         output_path = 'outputs/' + input_path[:-3] + '.out'
#         tasks = read_input_file(input_path)
#         output = solve(tasks)
#         write_output_file(output_path, output)
"""
size = 'small'
i = 1

tasks_list = read_input_file('inputs/' + size + '/' + size + '-' + str(i) + '.in')
result = solve_simple(tasks_list,0.9142)
print(result[1])



max_profit = 0
for i in range(100,200):
    result = solve_simple(tasks_list,float(i)/100)
    if(max_profit < result[1]):
        print(result[1])
        max_profit = result[1]
"""
def optimal_solve(tasks_list):
    result = None
    profit = 0
    optimal = 0
    prev = 0
    for i in range(750,950):
        output = solve_simple(tasks_list,float(i)/1000)
        if(output[1] > profit):
            optimal = i
            profit = output[1]
            result = output[0]
            if(prev > profit):
                break
    return result,profit


### THIS IS THE CURRENT SIZE WE ARE FILLING
size = 'small'
"""
i=5
tasks_list = read_input_file('inputs/' + size + '/' + size + '-' + str(i) + '.in')
result = solve_simple(tasks_list,0)
print(result[1])

write_output_file('outputs/' + size + '/' + size + '-' + str(i) + '.out',result[0])
"""

for i in range(1,301):
    ### if size = small, set condition to i != 184. Otherwise, set condition to i != 0
    if(i != 0):
        tasks_list = read_input_file('inputs/' + size + '/' + size + '-' + str(i) + '.in')
        result = optimal_solve(tasks_list)[0]
        print(i)
        write_output_file('outputs/' + size + '/' + size + '-' + str(i) + '.out',result)
        