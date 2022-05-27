import re
from lib import vars


def reset_counter():
    with open(f'{vars.database_location}counter.txt', 'w') as f:
        counter_str = str(0)
        f.write(counter_str)


def build_string():
    text_file = open(f'{vars.database_location}current_cuento.txt', "r")
    cuento_str = text_file.read()
    text_file.close()

    return cuento_str


def print_per_sentence(cuento_str):
    with open(f'{vars.database_location}counter.txt', 'r') as file:
        numb = file.readlines()
        counter = int(numb[0])

    list_sentences = re.split('[.]', cuento_str)
    tot_sent = len(list_sentences) - 1
    list_sentences.pop()
    if counter < tot_sent:
        print(f'{list_sentences[counter]}.')
        counter = counter + 1

        with open(f'{vars.database_location}counter.txt', 'w') as f:
            counter_str = str(counter)
            f.write(counter_str)
    else:
        reset_counter()
        print('¡Este cuento se acabó! Si continuas, empezará de nuevo')
