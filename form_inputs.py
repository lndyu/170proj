import Task
import parse
import random


def create_input(size):
    tasks_list = []
    for i in range(1,size+1):
        deadline = random.randint(1,1440)
        duration = random.randint(1,60)
        profit = round(random.uniform(0,100),2)
        new_task = Task.Task(i,deadline,duration,profit)
        tasks_list.append(new_task)
    parse.write_input_file(str(size)+'.in',tasks_list)

create_input(100)
create_input(150)
create_input(200)
