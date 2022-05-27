from logs import logging_settings
from operations import define_cuento, input_handling, build_cuento
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from lib import vars

logger = logging_settings.setup_logger('Main', 'main_log')
app = App(token=vars.slack_bot_token)
menu_res = input_handling.intro_menu()


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
    handler = SocketModeHandler(app, vars.slack_app_token)
    handler.start()
    main(menu_res)
    logger.info('Main completed')


@app.message('next')
def say_hello(say):
    say(f'You asked for the next command')


@app.command("/new")
def start_new_cuento(ack, respond, command):
    ack()
    respond(f"{command['text']}")


@app.command("/continue")
def continue_cuento(ack, respond, command):
    ack()
    respond(f"{command['text']}")


@app.command("/help")
def help_menu(ack, respond, command):
    ack()
    respond(f"{command['text']}")


@app.command("/next")
def next_sentence(ack, respond, command):
    ack()
    respond(f"{command['text']}")


@app.command("/prev")
def previous_sentence(ack, respond, command):
    ack()
    respond(f"{command['text']}")


@app.command("/reset")
def counter_to_zero(ack, respond, command):
    ack()
    respond(f"{command['text']}")
