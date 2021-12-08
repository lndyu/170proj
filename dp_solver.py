from parse import read_input_file, write_output_file, read_output_file
from itertools import permutations
import os

current_best = 0

def solve(tasks,size,instance):

    solution_order = read_output_file('outputs/' + size + '/' + size + '-' + str(instance) + '.out')

    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    current_time = 1440
    current_igloo = len(solution_order)
    while(current_igloo - 7 > 0):

        first_part = solution_order[0:current_igloo-7]
        middle_part = solution_order[current_igloo-7:current_igloo]
        last_part = solution_order[current_igloo:len(tasks)]
        current_best = 0
        current_permuation = None
        total_duration = sum([tasks[i].get_duration() for i in middle_part])
        for permutation in permutations(middle_part):
            tasks_list = []
            for task_id in permutation:
                tasks_list.append(tasks[task_id-1])
            current_profit = test_profit(tasks_list,current_time-total_duration)
            if(current_profit>current_best):
                current_best = current_profit
                print(current_best)
                current_permuation = permutation
        
        current_igloo -= 1
        current_time += tasks[current_permuation[6]].get_duration()
        
        solution_order = first_part + list(current_permuation) + last_part
    print(solution_order)
    print(test_profit([tasks[i] for i in solution_order],0))


    

#this is the profit if we select task at this time
def profit(task,current_time):
    overdue = current_time + task.get_duration() - task.deadline
    return task.get_late_benefit(overdue)

#test the profit for a sequence of tasks
def test_profit(tasks,current_time):
    total_profit = 0
    for task in tasks:
        current_time += task.get_duration()
        total_profit += profit(task,current_time)
    return total_profit


    


# Here's an example of how to run your solver.
# if __name__ == '__main__':
#     for input_path in os.listdir('inputs/'):
#         output_path = 'outputs/' + input_path[:-3] + '.out'
#         tasks = read_input_file(input_path)
#         output = solve(tasks)
#         write_output_file(output_path, output)

size = 'small'
i = 1


tasks_list = read_input_file('inputs/' + size + '/' + size + '-' + str(i) + '.in')
solution_order = read_output_file('outputs/' + size + '/' + size + '-' + str(i) + '.out')

result = solve(tasks_list,size,i)
#write_output_file('outputs/' + size + '/' + size + '-' + str(i) + '.out',result)
