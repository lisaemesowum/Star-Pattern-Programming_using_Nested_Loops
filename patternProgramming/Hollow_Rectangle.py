# ***************
# *             *
# *             *
# ***************


rows = 5
column = 15

# * * * * * * * * * * * * * * * 
# * * * * * * * * * * * * * * * 
# * * * * * * * * * * * * * * * 
# * * * * * * * * * * * * * * * 
# * * * * * * * * * * * * * * * 
for a in range(rows):
    for b in range(column):
        if a == 0 or a == rows - 1 or b == 0 or b - column - 1:
            print("*" , end=" ")
        else:
            print(" ",end="") 
    print()
    
print()
    
    

# *************************
# *                       *
# *                       *
# *                       *
# *                       *
# *                       *
# *                       *
# *                       *
# *                       *
# *************************

rows = 10
column = 25

for a in range(rows):
    for b in range(column):
        if a == 0 or a == rows - 1 or b == 0 or b == column - 1:
            print("*" , end="")
        else:
            print(" ",end="") 
    print()