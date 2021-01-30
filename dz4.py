with open('dz4.txt', 'r') as f_obj:
    with open('dz4-1.txt', 'w', encoding='utf-8') as new_f_obj:
        new_f_obj.writelines(f'Один {f_obj.readline()[4:]}')
        new_f_obj.writelines(f'Два {f_obj.readline()[4:]}')
        new_f_obj.writelines(f'Три {f_obj.readline()[5:]}')
        new_f_obj.writelines(f'Четыре {f_obj.readline()[4:]}')
