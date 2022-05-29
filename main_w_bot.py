from operations import define_cuento, input_handling, build_cuento
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from lib import vars
from common import push_slack


app = App(token=vars.slack_bot_token)

init_message = input_handling.welcome_message()
push_slack.push_to_slack(init_message)


# direct messages from the bot
@app.message('next')
def say_hello(say):
    cuento_str = build_cuento.build_string()
    sentence = build_cuento.print_per_sentence(cuento_str)
    build_cuento.increase_counter()
    say(sentence)


@app.message('prev')
def say_hello(say):
    build_cuento.counter_minus_one()
    cuento_str = build_cuento.build_string()
    sentence = build_cuento.print_per_sentence(cuento_str)
    say(sentence)


# commands, only visible to the user
@app.command("/new")
def start_new_cuento_command(ack, respond, command):
    ack()
    build_cuento.reset_counter()
    define_cuento.delete_non_cuentos_files()
    list_cuentos = define_cuento.get_cuentos()
    cuento_number = define_cuento.set_random_cuento(list_cuentos)
    define_cuento.set_cuento(cuento_number, list_cuentos)
    cuento_str = build_cuento.build_string()
    sentence = build_cuento.print_per_sentence(cuento_str)
    build_cuento.increase_counter()
    respond(sentence)


@app.command("/help")
def help_menu(ack, respond, command):
    ack()
    help_menu_slack = input_handling.help_menu_slack()
    respond(help_menu_slack)


@app.command("/reset")
def counter_to_zero(ack, respond, command):
    ack()
    build_cuento.reset_counter()
    cuento_str = build_cuento.build_string()
    sentence = build_cuento.print_per_sentence(cuento_str)
    build_cuento.increase_counter()
    respond(sentence)


if __name__ == '__main__':
    handler = SocketModeHandler(app, vars.slack_app_token)
    handler.start()
