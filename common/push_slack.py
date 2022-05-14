import requests
import json
from lib import vars


def push_to_slack(output_message):
    headers = {
        'Content-Type': 'application/json',
        'authorization': f'Bearer {vars.slack_bot_token}'
    }

    text_sent = f'{output_message}'

    data = {
        'text': text_sent
    }

    response_slack = requests.post(vars.slack_webhook, data=json.dumps(data), headers=headers)
