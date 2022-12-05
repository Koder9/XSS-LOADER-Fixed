import sys
from time import sleep
import random
from colorama import Fore

class colors:
    OKBLUE = Fore.BLUE
    WARNING = Fore.RED
    FAIL = Fore.RED
    CBLACK = Fore.BLACK
    CRED = Fore.RED
    CGREEN = Fore.GREEN
    CYELLOW = Fore.YELLOW
    CBLUE = Fore.CYAN
    CWHITE = Fore.WHITE


color_random = [colors.CBLUE, colors.CWHITE, colors.OKBLUE, colors.CGREEN, colors.WARNING,colors.CRED]
random.shuffle(color_random)


def entryy():
    x = color_random[0] + """
                                   
             ╭━╮╭━┳━━━┳━━━╮╱╱╭╮╱╱╭━━━┳━━━┳━━━┳━━━┳━━━╮
             ╰╮╰╯╭┫╭━╮┃╭━╮┃╱╱┃┃╱╱┃╭━╮┃╭━╮┣╮╭╮┃╭━━┫╭━╮┃
             ╱╰╮╭╯┃╰━━┫╰━━╮╱╱┃┃╱╱┃┃╱┃┃┃╱┃┃┃┃┃┃╰━━┫╰━╯┃
             ╱╭╯╰╮╰━━╮┣━━╮┣━━┫┃╱╭┫┃╱┃┃╰━╯┃┃┃┃┃╭━━┫╭╮╭╯
             ╭╯╭╮╰┫╰━╯┃╰━╯┣━━┫╰━╯┃╰━╯┃╭━╮┣╯╰╯┃╰━━┫┃┃╰╮
             ╰━╯╰━┻━━━┻━━━╯╱╱╰━━━┻━━━┻╯╱╰┻━━━┻━━━┻╯╰━╯

\n"""

    for c in x:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.0045)
    y = "\t|||||||||||||||||||||||||||||||||||||||||||||||||||||\n\n"
    for c in y:
        print(colors.CRED + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    y = "\t||                 XSS-LOADER TOOL                 ||\n\n"
    for c in y:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    x = "\t||                                                 ||\n\n"
    for c in x:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    z = "\t||             CODED BY HULYA  TMRSWRR             ||\n\n"
    for c in z:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    y = "\t|||||||||||||||||||||||||||||||||||||||||||||||||||||\n\n"
    for c in y:
        print(colors.CRED + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    y = "\t||              WELCOME TO XSS-LOADER              ||\n\n"
    for c in y:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)

    y = "\t|||||||||||||||||||||||||||||||||||||||||||||||||||||\n\n"
    for c in y:
        print(colors.CRED + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
