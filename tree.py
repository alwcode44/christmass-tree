num = 10 
row = 0 
while row < num:
    space = num-row-1
    while space > 0:
        print(" ",end="")
        space = space-1
    star = row*2+1
    while star > 0:
        print("*",end="")
        star = star-1
    row = row+1
    print()
print("       |||  [*]  ")
print("   [*] ||| [*][*]")
print("------------------")
print()
print("HAPPY CHRISTMAS!")
print("Designed by Alwin X")
print("S1 CSE")
