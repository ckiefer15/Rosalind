f = open("/Users/we2423hd/Documents/untitled5/rosalind_dna.txt")



def countNucleotide():
    thymine = 0
    cytosine = 0
    guanine = 0
    adenine = 0

    next = f.read(1)
    while next != "":

        if(next == "T"):
            thymine += 1
        elif(next == "C"):
            cytosine += 1
        elif(next == "G"):
            guanine += 1
        elif(next == "A"):
            adenine += 1
        next = f.read(1)
    return adenine, cytosine, guanine, thymine

a, b, c, d = countNucleotide()
f.close()
print(str(a) + " " + str(b) + " " + str(c) + " " + str(d))
