from logs import logging_settings
from operations import define_cuento, input_handling, build_cuento


logger = logging_settings.setup_logger('Main', 'main_log')

# todo: Add the slack push. The idea is to have the /next to call each new sentence
# todo: Add a menu to choose which story you want to "read"
# todo: Add a reset counter to 0 controlled by the user


def main():
    define_cuento.delete_non_cuentos_files()
    list_cuentos = define_cuento.get_cuentos()
    cuento_number = input_handling.input_choose(list_cuentos)
    cuento_to_read = define_cuento.set_cuento(cuento_number, list_cuentos)

    cuento_str = build_cuento.build_string(cuento_to_read)
    build_cuento.print_per_sentence(cuento_str)

    logger.info('Main completed')


if __name__ == '__main__':
    main()
