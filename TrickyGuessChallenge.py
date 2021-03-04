import random

from netcat import Netcat


def check_if_word_is_possible(source, word, min_count):
    count = 0
    for char in word:
        if source.__contains__(char):
            count = count + 1

    if count >= min_count:
        return True
    else:
        return False


def minimize_list(list_to_minimize, nnc, last):
    random_word = random.choice(list_to_minimize)
    print("Random Word Is: " + random_word)

    nnc.write(bytes(random_word, 'utf-8'))

    output = nc.read()

    try:
        c = int(output)
        step = []
        for word in list_to_minimize:
            if check_if_word_is_possible(random_word, word, c) and word != last:
                step.append(word)

        print(step.__len__())
        minimize_list(step, nnc, word)
    except:
        print(output)


wordsListFile = open(r"C:\Users\97254\Desktop\CheckPoint\words.txt", "r")
lst = wordsListFile.readlines()
finalList = [word.strip() for word in lst]

nc = Netcat("tricky-guess.csa-challenge.com", 2222)
print(nc.read(10000))
print(nc.read())

minimize_list(lst, nc, "")
