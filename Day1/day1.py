### Day 1 Solution by Stephen Chavez
### Date: Dec 10, 2018

def main():
    currentFreq = 0
    found = False
    freqMap = set([0])

    with open("inputData.txt", 'r') as fp:
        for freq in fp:
            currentFreq += int(freq)
        print("Part 1: " + str(currentFreq))

    currentFreq = 0;

    while found == False:
        with open("inputData.txt", 'r') as fp:
            for freqChange in fp:
                currentFreq += int(freqChange)

                if currentFreq in freqMap:
                    print("Part 2: The freq is " + str(currentFreq))
                    found = True
                    break

                freqMap.add(currentFreq)

main()
