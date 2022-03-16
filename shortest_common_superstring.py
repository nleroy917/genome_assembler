#!/usr/bin/env python

"""
    usage:
        shortest_common_superstring.py [options] sequences.txt
    where the options are:
        -h,--help : print usage and quit

    sequences.txt is a file with one sequence to be included in each row.
"""

from sys import argv, stderr
from getopt import getopt, GetoptError
from itertools import permutations
from typing import List

def read_sequences(filename):
    '''Read the sequences (one per line) from the filename and return a list
    '''
    sequences = []
    with open(filename, 'r') as f:
        for line in f:
            sequences.append(line.strip())
    return sequences

def _overlap(a: str, b: str, min_length: int = 3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's suffx in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match


def _pick_maximal_overlap(reads, k):
    reada, readb = None, None
    best_olen = 0
    for a, b in permutations(reads, 2):
        olen = _overlap(a, b, k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    return reada, readb, best_olen

def calculate_scs(reads: List[str]):
    """
    Implement the greedy shortest-common-superstring strategy discussed in 
    class. From the reads, find two string with the maximal overlap and merge 
    them. Keep doing this until you have only 1 string left
    """
    # return string A if only string A was passed
    if len(reads) == 1:
        return reads[0]

    read_a, read_b, olen = _pick_maximal_overlap(reads, 1)

    while olen > 0: 
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = _pick_maximal_overlap(reads, 1)

    return ''.join(reads)

def main(filename):
    # read the sequences from the file
    sequences = read_sequences(filename)
    print("Read the sequences", file=stderr)

    # calculate the shortest common superstring
    superstring = calculate_scs(sequences)

    # print the result
    print(superstring)

if __name__ == "__main__":
    try:
        opts, args = getopt(argv[1:], "h", ["help"])
    except GetoptError as err:
        print(err)
        print(__doc__, file=stderr)
        exit(1) 

    for o, a in opts:
        if o in ("-h", "--help"):
            print(__doc__, file=stderr)
            exit()
        else:
            assert False, "unhandled option"

    if len(args) != 1:
        print(__doc__, file=stderr)
        exit(2)

    main(args[0])
