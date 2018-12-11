### Day 2 Solution by Stephen Chavez
### Date: Dec 10, 2018
from collections import defaultdict
import difflib

def main():

    countTwo = 0
    countThree = 0

    with open("input.txt", 'r') as fp:
        for line in fp:
            charMap = defaultdict(int)
            for c in line:
                charMap[c] += 1

            for count in charMap.itervalues():
                if count == 2:
                    countTwo += 1
                    break
            for count in charMap.itervalues():
                if count == 3:
                    countThree += 1
                    break

    print ("Part 1: Checksum: %d" % (countTwo * countThree))

    commonLetters()

def commonLetters():
    lines = []

    found = False

    with open("input.txt", 'r') as fp:
        for line in fp:
            lines.append(line)

    for strA in lines:
        if not found:
            for strB in lines:
                if strA != strB:
                    matchDiff = difflib.SequenceMatcher(None, strA, strB)
                    blocks = matchDiff.get_matching_blocks()
                    numOfMatches = sum([x.size for x in blocks])
                    if numOfMatches == (len(strA) - 1) and numOfMatches == (len(strB) - 1):
                        found = True
                        print("Part 2: id: %s is similar to this id: %s" % (strA, strB))
                        break

main()
