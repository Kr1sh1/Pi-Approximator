from random import uniform
from decimal import Decimal
from decimal import getcontext
from time import time
from math import sqrt

def main():
    n = 0
    m = 0
    getcontext().prec = 100
    start_time = time()

    try:
        while True:
            x_point = uniform(0, 1)
            y_point = uniform(0, 1)
            n += 1
            if y_point <= sqrt(1 - pow(x_point, 2)):
                m += 1
            
            approx_pi = (Decimal(m*4)/Decimal(n))
        
    except KeyboardInterrupt:
        time_running = int(time() - start_time)
        print(f"Approximate value of pi: {approx_pi}, number of total points: {n}, "
        f"number of points within first quadrant of the circle: {m}, time running: {time_running}s")
        return

if __name__ == "__main__":
    main()