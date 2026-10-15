#row 0: 3 star
#row 1: 2 stars
#row 2: 1 stars
#PATTERN --> row - 1 = # of stars we want to print in each row!
BASESIZE = 3
for row in range(BASESIZE) :
    for col in range(BASESIZE-row) :
        print('*',end='') #overrides default newline commpand each ime print runs...stays on same line until all # of starts for the particular row is printed
    print() #newline after each row iteration