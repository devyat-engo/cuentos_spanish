import re
from cuento import cuento


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
        print('¡Este cuento se acabó Kate! Si quieres leerlo de nuevo vuelve a escribir "/next", de lo contrario dile a Enrique que te prepare un nuevo cuento')


if __name__ == '__main__':
    print_per_sentence()
