def plural_form (value, form1, form2, form3):

    if (value % 10 == 1) and (value != 11):
        print(f'{value} {form1}')

    elif (value % 10 in range(2, 5)) and (value not in range(12,15)):
        print(f'{value} {form2}')

    elif (value % 10 == 0) or value in range(11,20):
        print(f'{value} {form3}')

print(plural_form(22, 'яблоко', 'яблока', 'яблок'))
