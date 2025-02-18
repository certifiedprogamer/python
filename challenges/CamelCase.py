import string


def CamelCase(word: str):
    word = word.lower()
    word = word.title()
    for i in word:
        if i in string.punctuation or i == " ":
            wordindex = word.index(i)
            break
    first_word = word[0:wordindex].lower()
    word = word.replace(word[0:wordindex], first_word, 1)
    word = word.replace(" ", "")
    print(word)
    clean_txt = ''.join(ch for ch in word if ch not in string.punctuation)
    print(clean_txt)


g = "cats AND*Dogs-are Awesome"
CamelCase(g)
