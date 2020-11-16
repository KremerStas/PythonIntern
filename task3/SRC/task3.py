import os
import csv


class Barrel:
    def __init__(self, file_name):
        self.url = os.path.join(os.getcwd(), file_name)
        res = {}
        with open('log.log.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            res['count_top'] = 0
            res['count_scoop'] = 0
            res['success_top'] = 0
            res['success_scoop'] = 0
            res['fail_top'] = 0
            res['fail_scoop'] = 0
            res['total_fails'] = 0
            for row in reader:
                if row['wanna'] == 'wanna top':
                    res['count_top'] += 1
                    if row['res'] == 'успех' and row['count']:
                        res['success_top'] += int(row['count'])
                    elif row['res'] == 'фейл' and row['count']:
                        res['fail_top'] += int(row['count'])
                        res['total_fails'] += 1
                else:
                    res['count_scoop'] += 1
                    if row['res'] == 'успех' and row['count']:
                        res['success_scoop'] += int(row['count'])
                    elif row['res'] == 'фейл' and row['count']:
                        res['fail_scoop'] += int(row['count'])
                        res['total_fails'] += 1

            res['total_fails'] = res['total_fails'] * 100 / (res['count_scoop'] + res['count_top'])
            self.count_top = res['count_top']
            self.count_scoop = res['count_scoop']
            self.total_fails = res['total_fails']
            self.success_top = res['success_top']
            self.success_scoop = res['success_scoop']
            self.fail_top = res['fail_top']
            self.fail_scoop = res['fail_scoop']


if __name__ == '__main__':
    file = Barrel('log.log.csv')
    print(f' Процент ошибок, который был допущен за указанный период: {file.total_fails}')
    print(f' Количество попыток налить воду в бочку было: {file.count_top}')
    print(f' Количество попыток забрать воду из бочки было: {file.count_scoop}')
    print(f' Объем воды, который был налит в бочку за указанный период: {file.success_top}')
    print(f' Объем воды, который был забран из бочки за указанный период: {file.success_scoop}')
    print(f' Объем воды, который был не налит в бочку за указанный период: {file.fail_top}')
    print(f' Объем воды, который был не забран из бочки за указанный период: {file.fail_scoop}')