import re
from cuento import cuento


# todo: Add the slack push. The idea is to have the /next to call each new sentence
# todo: Add a menu to choose which story you want to "read"
# todo: Add a reset counter to 0 controlled by the user


def print_per_sentence():
    with open('counter.txt', 'r') as file:
        numb = file.readlines()
        counter = int(numb[0])

    list_sentences = re.split('[.]', cuento)
    tot_sent = len(list_sentences) - 1
    list_sentences.pop()
    if counter < tot_sent:
        print(f'{list_sentences[counter]}.')
        counter = counter + 1

        with open('counter.txt', 'w') as f:
            counter_str = str(counter)
            f.write(counter_str)
    else:
        with open('counter.txt', 'w') as f:
            counter_str = str(0)
            f.write(counter_str)
        print('¡Este cuento se acabó! Si quieres leerlo de nuevo vuelve a escribir ´/next´')


if __name__ == '__main__':
    print_per_sentence()
