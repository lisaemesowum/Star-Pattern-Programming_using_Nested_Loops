# *         
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********

row = 10

for i in range(row):
    for b in range(i + 1): #each rows add one
        print("*", end="")
    print()
    
    
print()


# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * * 
# * * * * * * * 
# * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * * 

row = 10

for i in range(row):
    for b in range(i + 1): #each rows add one
        print("* ", end="")
    print()