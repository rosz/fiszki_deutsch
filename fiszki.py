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
    words = create_dict('slowka.csv')
    numbers = create_dict('liczebniki.csv')

    choose_dict = input("Które słowa chcesz przećwiczyć?\nliczebniki / ogólne\n")

    while choose_dict == "liczebniki":
        key = random.choice(list(numbers))
        print("\n" + key)
        value = input()
        while value != numbers[key]:
            print("jeszcze raz? t/n")
            response = input()
            if response == "t":
                value = input()
            elif response == "n":
                print(key + " = " + numbers[key])
                break
            else:
                break

    while choose_dict == "ogólne":
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
