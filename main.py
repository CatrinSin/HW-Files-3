with open('1.txt', encoding='utf-8') as file_1:
    lines_1 = file_1.readlines()
    lines_1.insert(0, f'1.txt\n {len(lines_1)}\n')


with open('2.txt', encoding='utf-8') as file_2:
    lines_2 = file_2.readlines()
    lines_2.insert(0, f'2.txt\n {len(lines_2)}\n')

with open('3.txt', encoding='utf-8') as file_3:
    lines_3 = file_3.readlines()
    lines_3.insert(0, f'3.txt\n {len(lines_3)}\n')

lines_4 = []
lines_4.append(lines_1)
lines_4.append(lines_2)
lines_4.append(lines_3)
lines_5 = sorted(lines_4, key=len)

with open('4.txt', 'w', encoding='utf-8') as file_4:
    for line in lines_5:
        file_4.write(''.join(line) + '\n')
