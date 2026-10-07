grade = 68
for i in [90, 80, 70, 60]:
    if grade >= i:
        print (chr(63 + (10-int(i/10)))) # 63 + (10 - 90/10) = 64 = A
        break
    