from logs import logging_settings
from operations import define_cuento, input_handling, build_cuento


logger = logging_settings.setup_logger('Main', 'main_log')


menu_res = input_handling.intro_menu()


# todo: Add the slack functionality
# todo: add Cuento to database


def hidden_menu(cuento_str):
    while True:
        build_cuento.print_per_sentence(cuento_str)
        hidden_menu_inp = input()
        if hidden_menu_inp.lower() == 'q' or hidden_menu_inp.lower() == 'quit':
            break
        elif hidden_menu_inp.lower() == 'new':
            menu_res = 1
            main(menu_res)
        elif hidden_menu_inp.lower() == 'continue':
            menu_res = 2
            main(menu_res)
        elif hidden_menu_inp.lower() == 'previous':
            # todo: build functionality to go to previous sentence
            print('You want the previous sentence')
        elif hidden_menu_inp.lower() == 'reset':
            # todo: function to reset the counter to 0
            # below is on continue so the same Cuento runs
            menu_res = 2
            main(menu_res)
        elif hidden_menu_inp.lower() == 'help' or hidden_menu_inp.lower() == 'h':
            input_handling.help_menu()
            menu_res = 3
            main(menu_res)


def main(menu_res):
    # for "new"
    if menu_res == 1:
        define_cuento.delete_non_cuentos_files()
        list_cuentos = define_cuento.get_cuentos()
        cuento_number = input_handling.input_choose(list_cuentos)
        define_cuento.set_cuento(cuento_number, list_cuentos)
        cuento_str = build_cuento.build_string()
        hidden_menu(cuento_str)
        exit(0)

    # for "continue"
    elif menu_res == 2:
        cuento_str = build_cuento.build_string()
        hidden_menu(cuento_str)
        exit(0)

    else:
        menu_res = input_handling.intro_menu()
        main(menu_res)

    logger.info('Main completed')


if __name__ == '__main__':
    main(menu_res)
