fp = "/Users/we2423hd/Documents/Rosalind/rosalind_prot.txt"

def calculateGC(dnaString):
    gcCount = 0
    for letter in dnaString:
        if(letter == "G" or letter == "C"):
            gcCount += 1
        else:
            continue
    return gcCount/len(dnaString)

with open(fp) as data:
    highestGC = 0
    highestLine = ""

    for line in data:
        dnaString = ""
        for l in range(line,):
            if (line[0] == '>'):
                break
            else:
                dnaString+=l
        gcScore = calculateGC(dnaString)

        if(gcScore > highestGC):
            highestGC = gcScore
            highestLine = line
        else:







