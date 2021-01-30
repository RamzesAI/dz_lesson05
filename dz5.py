out_f = open('dz5.txt', 'w')
user_line = input('input line of numbers:\n>>>')
line_numbers = out_f.write(user_line)
out_f.close()

out_f = open('dz5.txt', 'r')
calc_l = out_f.readline()
result = 0
for el in calc_l.split():
    result = result + int(el)
print(f'\nResut of addition numbers in dz5.txt: {result}')