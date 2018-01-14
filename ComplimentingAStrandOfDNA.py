s = open("/Users/we2423hd/Documents/untitled5/rosalind_revc.txt").read()
compliment = ""
for line in reversed(s):
    if (line == "T"):
        compliment += "A"
    elif (line == "C"):
        compliment += "G"
    elif (line == "G"):
        compliment += "C"
    elif (line == "A"):
        compliment += "T"
print(compliment)
results = open("/Users/we2423hd/Documents/untitled5/Results.txt", mode='w')
results.write(compliment)
results.close()