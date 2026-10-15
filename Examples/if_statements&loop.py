grade = 88
#same as range for loop in c++
for i in [90, 80, 70, 60]:
    if grade >= i:
        print (chr(63 + (10-int(i/10))))
        break