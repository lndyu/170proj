from parse import read_input_file, write_output_file, read_output_file
import os

def determine_profit(size,number):
    task_ids = read_output_file('project-fa21-skeleton/outputs/' + size + '/' + size + '-' + str(number) + '.out')
    tasks = read_input_file('project-fa21-skeleton/inputs/' + size + '/' + size + '-' + str(number) + '.in')
    
    current_time = 0
    current_profit = 0
    print(task_ids)
    for task in [tasks[a-1] for a in task_ids]:
        print(task.get_task_id())
        current_time += task.get_duration()
        current_profit += task.get_late_benefit(current_time-task.deadline)
    print('Profit: ' + str(current_profit))
    print('Time: ' + str(current_time))

determine_profit("small",1)