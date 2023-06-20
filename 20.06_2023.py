string=input('Введите слово:')

reversed_string = ''.join(reversed(string))

if reversed_string == string:
    print(f'{string} является палиндромом')
else:
    print(f'{string} не является палиндромом')