# import numpy
### Day 3 Solution by Stephen Chavez
### Date: Dec 11, 2018
### Based on existing Solution : https://github.com/Kurocon/AdventOfCode2018/blob/master/days/day3.py

import re
from collections import defaultdict


def main():
    parsed_input = readFile()
    squares = defaultdict(list)
    for claim in parsed_input:
        id = claim["claim_id"]
        offset_x = claim["x_offset"]
        offset_y = claim["y_offset"]
        width = claim["width"]
        height = claim["height"]

        x_squares = [(x+offset_x, offset_y) for x in range(width)]
        claim_squares = [(x, y+i) for x, y in x_squares for i in range(height)]
        for square in claim_squares:
            squares[square].append(id)


    overlapping_squares = sum([1 for key, value in squares.items() if len(value) > 1])
    print("There are {} overlapping squares".format(overlapping_squares))

    unique_claims = set(x['claim_id'] for x in parsed_input)
    overlapping_claims = set()

    # PART 2
    for key, value in squares.items():
        if len(value) > 1:
            for v in value:
                overlapping_claims.add(v)

    result = unique_claims - overlapping_claims
    print ("The unique claim is {}".format(result))

def readFile():
    PARSE_REGEX = r'#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)'
    parsed_input = []

    with open("input.txt", 'r') as fp:
        for line in fp:
            match = re.match(PARSE_REGEX, line)
            if match:
                parsed_input.append({
                    'claim_id': int(match.group(1)),
                    'x_offset': int(match.group(2)),
                    'y_offset': int(match.group(3)),
                    'width': int(match.group(4)),
                    'height': int(match.group(5))
                })
            else:
                print("Error: No match for line {}".format(line))

    return parsed_input

main()
