n=3
for y in range(n+1):
#will define number of rows 
    for x in range(n-y):
#will define number of spaces in each row 
        print(" ", end=" ")
    for z in range(y):
#will print values of left triangle
        print(2 ** z, end=" ")
    for z in range(y, -1, -1):
#will print values of right triangle
        print(2 ** z, end=" ")
    print()
    
