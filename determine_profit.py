from parse import read_input_file, write_output_file, read_output_file
import os

def determine_profit(size,number):
    task_ids = read_output_file('outputs/' + size + '/' + size + '-' + str(number) + '.out')
    tasks = read_input_file('inputs/' + size + '/' + size + '-' + str(number) + '.in')
    
    current_time = 0
    current_profit = 0
    task_ids.pop()
    for task in [tasks[a-1] for a in task_ids]:
        current_time += task.get_duration()
        current_profit += task.get_late_benefit(current_time-task.deadline)
    #print('Profit: ' + str(current_profit))
    #print('Time: ' + str(current_time))
    return (current_profit,current_time)

total_profit = 0
for i in range(1,301):
    if(i != 184):
        profit = determine_profit("small",i)[0]
        total_profit += profit
        print(i)
        print(profit)

print(total_profit/299)
"""
profit = determine_profit("small",1)[0]
print(profit)
"""

