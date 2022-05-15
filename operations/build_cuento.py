import re
from lib import vars


def build_string(cuento_to_read):
    text_file = open(f'{vars.database_location}Cuentos/{cuento_to_read}.txt', "r")
    cuento_str = text_file.read()
    text_file.close()

    return cuento_str


# todo: to be called from slack with word "next"
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
        with open(f'{vars.database_location}counter.txt', 'w') as f:
            counter_str = str(0)
            f.write(counter_str)
        print('¡Este cuento se acabó! Si quieres leerlo de nuevo vuelve a escribir ´/next´')