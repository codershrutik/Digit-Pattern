def pattern(n):

    #traversing though eleemnts
    #n assuming it is a string
    for i in n:
        print("|", end = " ")

        #print i no. of *s in each line
        print("*" * int(i))

n = "49857"
pattern(n)