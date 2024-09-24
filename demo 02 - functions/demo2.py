import webbrowser
import random
# There are 2 types of functions:
# 1 performs a task
# 2 returns a value

# performs a task:


def who_is_john_lennon():
    print("He was a Beatle, a member of the greatest band ever")
    print("...other than Parry Gripp.")

# also performs a task:


def who_is_parry_grip():
    print("Parry Gripp is a God of Music.")
    webbrowser.open("https://www.youtube.com/watch?v=EiO9_PJ0h8Q%22")


# returns a value
def get_awesome_song_link():
    links = ["https://www.youtube.com/watch?v=npjF032TDDQ",
             "https://www.youtube.com/watch?v=EiO9_PJ0h8Q",
             "https://www.youtube.com/watch?v=jcaej-i3QQo"
             ]
    return random.choice(links)


webbrowser.open(get_awesome_song_link())
