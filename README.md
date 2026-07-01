# Simple Monte Carlo Simulation

Implements a simple Monte Carlo simulation for random walks of a share price.

Price begins at £100. Each step can either increase or decrease by £1. Increases and Decreases have equal probability.

N random walks are done across S steps. The sim outputs a table showing the probability distribution of the resulting share price.

## Requirements

The program needs python 3.10 or higher in order to run correctly.
For example, I ran it using python 3.13.7.

## How to run

The program runs in the command line.

The program has 3 optional command-line arguments.

| Argument | Description | Values | Default |
|---|---|---|---|
| `--s` | Number of steps for each walk | 1-100| 10 |
| `--n` | Number of simulated walks | 1-100000 | 10000 |
| `--show` | If included shows all possible final prices, including ones with zero probability | N/A | False |

To run the program with default values:

`python monte.py`

Set number of steps:

`python monte.py --s 15`

Set number of walks:

`python monte.py --n 15000`

Show all possible prices:

`python monte.py --show`

Combined:

`python monte.py --s 15 --n 15000 --show`

## Probability of 100 when S = 10, N = 10000

When the sim was run using:

`python monte.py --s 10 --n 10000`

the result was:

|  Price | Probability |
|---|---|
90 | 0.00110
92 | 0.00980
94 | 0.04470
96 | 0.12270
98 | 0.20120
100 | 0.24540
102 | 0.20470
104 | 0.11710
106 | 0.04100
108 | 0.01080
110 | 0.00150

Giving P(100) = 0.24540

## Program Logic

Since each step can only go up or down with equal probability the result for a step can be represented by a randomly generated bit 0 or 1 (0 for decrease in value, 1 for increase).

The number of occurances of each possible number of increasing steps is stored in an array `result`.

For each of the N simulated walks the entire walk can be generated using a random bitstring of size S, using `random.getrandbits(S)`.

Then, the number of increasing steps can be counted using `.bit_count()`. This is stored in the variable `walk_up`. Then the value in `result` at index `walk_up` is incremented by 1.

After each walk has been simulated, the counts stored in `result` are converted to probabilities by dividing each value by `N`.

For outputting the final results, each of probabilities for the number of increasing steps are converted into share price by doing `price = 100 - S + 2 * walk_up`.
