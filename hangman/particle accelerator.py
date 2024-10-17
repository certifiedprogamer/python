# Kerry Sowers
import random


def hangman_initialize():
    words = ["integer", "function", "boolean",
             "float", "string", "dictionary", "lambda"]
    chosen_word = random.choice(words)
    return chosen_word


if __name__ == "__main__":
    w = hangman_initialize()
    g = w
    for l in w:
        print(l)
        g = g.replace(l, "x")

    print(w)
    print(g)

    for l in w:
        print(w.find(l))

    while True:
        guess = input("go crazy ")
        m = w.find(guess)
        m2 = m + 1
        g = g.replace(g[m:m2], guess)
        print(g)
