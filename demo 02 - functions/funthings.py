import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print("Let's play with colors.")
print(f"{bcolors.WARNING} warning text {bcolors.ENDC}")
print("color should be reset")
print(f"{bcolors.HEADER} header text {bcolors.ENDC}")
print(f"{bcolors.OKBLUE} blue text {bcolors.ENDC}")
print(f"{bcolors.OKCYAN} cyan text {bcolors.ENDC}")
print(f"{bcolors.OKGREEN} green text {bcolors.ENDC}")
print(f"{bcolors.BOLD} bold text {bcolors.ENDC}")
print(f"{bcolors.FAIL} fail text {bcolors.ENDC}")
print(f"{bcolors.UNDERLINE} underlined text {bcolors.ENDC}")


def typetext(str, end="\n"):
    for character in str:
        print(character, end="", flush=True)
        time.sleep(.1)
    print(end, end="")


typetext("im a bunch of text that needs printed")
typetext("im a bunch of text that needs printed")
