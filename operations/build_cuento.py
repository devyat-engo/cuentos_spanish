import re
from lib import vars


def reset_counter():
    with open(f'{vars.database_location}counter.txt', 'w') as f:
        counter_str = str(0)
        f.write(counter_str)


def counter_minus_one():
    with open(f'{vars.database_location}counter.txt', 'r') as file:
        numb = file.readlines()
        counter = int(numb[0])
        prev_counter = counter - 2
        prev_counter = str(prev_counter)

    with open(f'{vars.database_location}counter.txt', 'w') as f:
        f.write(prev_counter)


def build_string():
    text_file = open(f'{vars.database_location}current_cuento.txt', "r")
    cuento_str = text_file.read()
    text_file.close()

    return cuento_str


def print_per_sentence(cuento_str):
    clean_sentences = []
    with open(f'{vars.database_location}counter.txt', 'r') as file:
        numb = file.readlines()
        counter = int(numb[0])

    cuento_str = cuento_str.replace('. ', '.')
    cuento_str = cuento_str.replace('\n', '')
    list_sentences = re.split('[.]', cuento_str)
    tot_sent = len(list_sentences) - 1
    list_sentences.pop()
    # for sentence in list_sentences:
    #     clean_sentences.append(sentence.replace(". ", "."))
    if counter < tot_sent:
        print(f'{list_sentences[counter]}.')
        counter = counter + 1

        with open(f'{vars.database_location}counter.txt', 'w') as f:
            counter_str = str(counter)
            f.write(counter_str)

        return f'{list_sentences[counter]}.'

    else:
        reset_counter()
        print('¡Este cuento se acabó! Si continuas, empezará de nuevo')

        return '¡Este cuento se acabó! Si continuas, empezará de nuevo'
