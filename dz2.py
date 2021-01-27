my_f = open('dz2.txt', 'r')
content = my_f.readlines()

count_str = 0
for str_numb in content:
    count_str = count_str + 1
    join_str = ''.join(str_numb.split())


    count_letter = 0
    for letter_str in join_str:
        count_letter = count_letter + 1
    print(f'in {count_str} string {count_letter} letters')
print(f'There are {count_str} strings in this file')
