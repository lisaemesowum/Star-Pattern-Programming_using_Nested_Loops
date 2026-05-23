# *
# * *
# * * *
# * * * *
# * * * * *

rows = 6
for a in range(rows):     #the number of rows
    for b in range(a + 1): # number of rows add by 1
        print("* ", end="")
    print()
print()    


# to make it wider
rows= 10
for a in range(rows):
    for b in range(a + 1):
        print("*  ", end="")
    print()