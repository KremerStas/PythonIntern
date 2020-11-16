import random
import datetime
import csv

with open('log.log.csv', mode='w', newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=",")
    employee_writer.writerow(["time", "user", "wanna", "count", "res"])
    total = 200
    current = 32
    for i in range(15000):
        now_time = datetime.datetime.now()
        rand = random.randrange(1, 11)
        rand_choice = random.randrange(1, 3)
        if rand_choice == 2:
            scoop = rand * random.randrange(1, 26)
            if scoop > current:
                res = 'фейл'
            else:
                res = 'успех'
                current -= scoop
            employee_writer.writerow([f'{now_time}', f'username{rand}', 'wanna scoop', f'{scoop}', f'{res}'])

        else:
            top = rand * random.randrange(1, 26)
            if top > total - current:
                res = 'фейл'
            else:
                res = 'успех'
                current += top
            employee_writer.writerow([f'{now_time}', f'username{rand}', 'wanna top', f'{top}', f'{res}'])

    employee_writer.writerow(['META DATA'])
    employee_writer.writerow(['200', 'объем бочки'])
    employee_writer.writerow(['32', 'текущий объем воды в бочке'])

print(current)






