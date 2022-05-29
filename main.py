from logs import logging_settings
from operations import define_cuento, input_handling, build_cuento
from lib import vars

logger = logging_settings.setup_logger('Main', 'main_log')


def hidden_menu(cuento_str):
    while True:
        build_cuento.print_per_sentence(cuento_str)
        build_cuento.increase_counter()
        hidden_menu_inp = input()
        if hidden_menu_inp.lower() == 'q' or hidden_menu_inp.lower() == 'quit':
            break
        elif hidden_menu_inp.lower() == 'new':
            menu_res = 1
            main(menu_res)
        elif hidden_menu_inp.lower() == 'cont':
            menu_res = 2
            main(menu_res)
        elif hidden_menu_inp.lower() == 'prev':
            build_cuento.counter_minus_one()
        elif hidden_menu_inp.lower() == 'reset':
            build_cuento.reset_counter()
        elif hidden_menu_inp.lower() == 'help' or hidden_menu_inp.lower() == 'h':
            input_handling.help_menu()
            menu_res = 3
            main(menu_res)


def main(menu_res):
    # for "new"
    if menu_res == 1:
        build_cuento.reset_counter()
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


if __name__ == '__main__':
    menu_res = input_handling.intro_menu()
    main(menu_res)
    logger.info('Main completed')
