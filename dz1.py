my_f = open('text.txt', 'w', encoding='utf-8')

while True:
    my_text = input('Input text: ')
    my_f.writelines(f'\n{my_text}')
    if not my_text:
        break