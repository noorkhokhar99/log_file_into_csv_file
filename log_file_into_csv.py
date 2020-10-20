import csv

with open('Kamas_Poultry_Farm_shed1.log') as file:
    lines = file.read().splitlines()
    lines = [lines[x:x+3] for x in range(0, len(lines), 3)]

    with open('test.csv', 'w+') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(lines)
