# 13
#
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#

from util import CollatzSequence


def main():
    sequences = {1: [1]}
    for n in range(1, 1_000_000 + 1):
        sequence = []
        for s in CollatzSequence(n):
            if s in sequences:
                sequence += sequences[s]
                sequences[n] = sequence
                break

            sequence.append(s)
    chain_lengths = {k: len(v) for k, v in sequences.items()}
    return sorted(chain_lengths.items(), reverse=True, key=lambda x: x[1])[0][0]


if __name__ == "__main__":
    main()
