

def intro_menu():
    try:
        main_input = input(f'Good morning Kate, how is today\'s learning going to be?\nWould you like to read a new \"Cuento\" or continue where you left?\nChoose by using the keyword \"new\" or \"continue\" or \"help\":\n')
        if main_input.lower() == 'new' or main_input.lower() == 'n':
            menu_res = 1
            return menu_res
        elif main_input.lower() == 'cont' or main_input.lower() == 'c':
            menu_res = 2
            return menu_res
        elif main_input.lower() == 'help' or main_input.lower() == 'h':
            help_menu()
        elif main_input.lower() == 'next' or main_input.lower() == 'prev' or main_input.lower() == 'reset' or main_input == '':
            print('This option is only valid while you are reading a \"Cuento\", do not try to fool me -.-\n')
            menu_res = 3
            return menu_res
        elif main_input.lower() == 'quit' or main_input.lower() == 'q':
            exit(0)
        else:
            print('You are not choosing one of the possible options\n')
            menu_res = 3
            return menu_res
    except:
        print('You break it! You know who to call.')
        exit(1)


def input_choose(list_cuentos):
    num_cuentos = len(list_cuentos) + 1
    cuento_number = 0
    try:
        cuento_number = int(input(f'Input the number of the \"Cuento\" you want to read: '))
        if cuento_number >= num_cuentos:
            print('The number you choose doesn\'t exist')
        elif cuento_number <= 0:
            print('Negative numbers and 0 are not valid')
    except:
        print('Letters and special characters are not permitted, continue reading...')

    return cuento_number


def help_menu():
    help_message = 'No worries, I am here to help.\n'\
                   'My functionality is reduced to the following commands that you can always type while you are reading one of the fairytales\n'\
                   '\"new\":             You will be requested to choose a new Cuento to read.\n' \
                   '\"cont\":            You will start the Cuento where you left.\n' \
                   '\"next\":            The next sentence of the Cuento will appear. Same as pressing the enter key.\n'\
                   '\"prev\":            The previous sentence of the Cuento will appear.\n'\
                   '\"reset\":           The counter of your Cuento will reset and the current Cuento will start from the beginning.\n'\
                   '\"quit\" or \"q\":   Exits the program.\n'\
                   '\"help\" or \"h\":   Brings back this message.\n'\
                   '* Remember that if you press the enter key without keyword, you will continue to the next sentence.\n\n'

    print(help_message)

    return help_message


def help_menu_slack():
    help_message = 'No worries, I am here to help.\n'\
                   'My functionality is reduced to the following commands:\n' \
                   'next:            I will reply with the next sentence from the Cuento.\n' \
                   'prev:            I will reply with the previous sentence from the Cuento.\n' \
                   '/new:             I will choose a random new Cuento for you to read.\n' \
                   '/reset:           You will start the Cuento from the beginning as soon as you type \"next\".\n'\
                   '/help or \"h\":   Brings back this message.\n'\

    print(help_message)

    return help_message


def welcome_message():
    welc_message = 'Good morning Kate, how is today\'s learning going to be?\n' \
                   'Type \"next\" or \"prev\" to get the next or previous sentence accordingly.\n ' \
                   'If you have doubts type \"/help\" to get a menu with more details, or ask you know who :)'

    return welc_message
