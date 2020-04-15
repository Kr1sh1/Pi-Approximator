from random import uniform
from decimal import Decimal, getcontext
from time import time, sleep
from math import sqrt
from threading import Thread
from colorama import init, Fore

n = 0
m = 0

def print_approximation():
    init()
    start_time = time()
    getcontext().prec = 20
    while True:
        sleep(1)
        approx_pi = (Decimal(m*4)/Decimal(n))
        time_running = int(time() - start_time)
        print(f"{Fore.GREEN}Approximate value of pi: {approx_pi}{Fore.BLUE} Number of total points: {n}"
        f"{Fore.YELLOW} Number of points within first quadrant of the circle: {m}{Fore.RED} Time running: {time_running}s", end="\r")


def main():
    global n, m

    try:
        while True:
            x_point = uniform(0, 1)
            y_point = uniform(0, 1)
            n += 1
            if y_point <= sqrt(1 - pow(x_point, 2)):
                m += 1
        
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    Thread(target=print_approximation, daemon=True).start()
    main()
