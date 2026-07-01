## Basic Monte
import random
import argparse

def int_1_100(v):
    # ensures S is an int and 1 <= S <= 100
    try:
        s = int(v)
    except ValueError:
        raise argparse.ArgumentTypeError("S must be an int")
    if not 1 <= s <= 100:
        raise argparse.ArgumentTypeError("S must be between 1 & 100")
    return s

def int_1_100000(v):
    # ensures N is an int and 1 <= N <= 100000
    try:
        s = int(v)
    except ValueError:
        raise argparse.ArgumentTypeError("N must be an int")
    if not 1 <= s <= 100000:
        raise argparse.ArgumentTypeError("N must be between 1 & 100000")
    return s

def run(S, N):
    # stores all possible values for number of increasing steps
    result = [0] * (S + 1)
    
    # iterate each walk
    for n in range(N):
        # gen rand walk with bitstring
        # 1 -> up | 0 -> down
        walk = random.getrandbits(S)
        walk_up = walk.bit_count() # count increasing steps
        result[walk_up] += 1

    # turn count -> prob
    for i in range(S+1):
        result[i] /= N

    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--s", type=int_1_100, default=10)
    parser.add_argument("--n", type=int_1_100000, default=10000)
    parser.add_argument("--show", action="store_true")

    args = parser.parse_args()
    S = args.s
    N = args.n

    result = run(S, N)

    default_walk = 100 - S
    
    # prints the table
    print(f"{'Price':>7} | {'Probability':>11}")
    print("-"*25)
    for walk_up, proportion in enumerate(result):
        # if --show not used then skip
        if proportion == 0 and not args.show:
            continue
        # convert number of increasing steps into a share price
        price = default_walk + 2 * walk_up
        print(f"{price:7d} | {proportion:11.5f}")
    
    # correctness verification
    # the below bit gives sanity checks: gives sum of all probabilities and calculates expected share price

    ## print(f"Total prob: {sum(result):.10f}")
    
    ## expected_price = 0

    ## for walk_up, probability in enumerate(result):
    ##     price = default_walk + 2 * walk_up
    ##     expected_price += price * probability

    ## print(f"Expected price: {expected_price:.5f}")