x = ('a','b','c','d','e','f','g','h','i','j','k','l')
y = ('3','5','4','1','3','7','1','1','2','2','5','2')
counter = 0
while counter <= 11:
    print(y[counter] + "(2x(" + x[counter] + ",1)+3x(" + x[counter] + ",2) + 1x(" + x[counter] + ",3))") 
    counter += 1

