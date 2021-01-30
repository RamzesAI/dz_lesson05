#dz6
import re
new_dict = {}
sum_el = 0

with open('dz6.txt', 'r', encoding='utf-8') as f_obf:

    for line in f_obf:
        sp_line = line.split()
        re_line = re.findall(r'\d+', line)

        for i in re_line:
            sum_el = sum_el + int(i)
        new_dict.update({sp_line[0][:-1]: sum_el})
        sum_el = 0

    print(new_dict)