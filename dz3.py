my_f = open('dz3.txt', 'r')
content = my_f.readlines()
less_list = []
middle_salary = 0
count_str = 0
for cotent_str in content:
    count_str = count_str + 1
    new_list = cotent_str.split()
    middle_salary = (middle_salary + int(new_list[1]))

    if int(new_list[1]) < 20000:
        less_list.append(new_list[0])
print()
print(f'Those employees have salary less 20 000:\n{less_list}')
print(middle_salary / count_str)
