from parse import read_input_file, write_output_file
import os

def max_est(tasks):
    total_duration = 0
    total_profit = 0
    for task in tasks:
        total_duration += task.get_duration()
        total_profit += task.get_max_benefit()
    
    average_duration = total_duration/len(tasks)
    average_profit = total_profit/len(tasks)
    print(str(average_profit/average_duration * 1440))

for i in range(1,300):
    print("Current input:" + str(i))
    tasks_list = read_input_file('project-fa21-skeleton/inputs/medium/medium-' + str(i) + '.in')
    max_est(tasks_list)