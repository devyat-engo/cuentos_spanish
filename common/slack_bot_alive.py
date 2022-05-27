from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from lib import vars


# base slack bot, not used here, integrated in main.py
# Slack Bot configuration
# Enable Event Subscriptions
# Generate App-level Token
# Enable Socket mode
# Enable Slash Commands and set them up accordingly to the functions listening below
# Enable Event Subscriptions:
# - Subscribe to bot events
# -- message.channels
# -- message.groups
# -- message.im
# Setup Bot Token Scopes:
# - channels:history
# - chat write
# - commands
# - groups:history
# - im:history


app = App(token=vars.slack_bot_token)


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


if __name__ == "__main__":
    handler = SocketModeHandler(app, vars.slack_app_token)
    handler.start()
