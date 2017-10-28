import random
import csv


def create_dict(csv_file):
    words = csv.reader(open(csv_file, 'r'))
    words_dict = {}
    for row in words:
        k, v = row
        words_dict[k] = v
    return words_dict


def give_key():
    choose_dict = input("Które słowa chcesz przećwiczyć?\nliczebniki / ogólne\n")

    words = {}
    if choose_dict == "ogólne":
        words = create_dict('slowka.csv')
    elif choose_dict == "liczebniki":
        words = create_dict('liczebniki.csv')

    while words:
        key = random.choice(list(words))
        print("\n" + key)
        value = input()
        while value != words[key]:
            print("jeszcze raz? t/n")
            response = input()
            if response == "t":
                value = input()
            elif response == "n":
                print(key + " = " + words[key])
                break
            else:
                break
