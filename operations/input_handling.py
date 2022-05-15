

# todo: called from slack with the word "new"
def input_choose(list_cuentos):
    # 27
    num_cuentos = len(list_cuentos) + 1
    cuento_number = 0
    try:
        cuento_number = int(input(f'Input the number of the \"Cuento\" you want to read: '))
        if cuento_number >= num_cuentos:
            print('The number you choose doesn\'t exist')
        elif cuento_number <= 0:
            print('Negative numbers and 0 are not valid')
    except:
        print('Letters and special characters are not permitted')

    return cuento_number


# todo: called from slack with the word "read"
def type_of_read():
    try:
        type_read = input(f'Do you want to read a new \"Cuento\" or continue with the previous one? Type either \"new\" or \"continue\" ')
        cuento_number = int(input(f'Input the number of the \"Cuento\" you want to read: '))
        if type_read == 'new':
            print('The number you choose doesn\'t exist')
        elif type_read == 'continue':
            print('Negative numbers and 0 are not valid')

    except:
        print('Letters and special characters are not permitted')

    return cuento_number
