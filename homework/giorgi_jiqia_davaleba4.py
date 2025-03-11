##exercise 1


a = 1500
while a < 2100:
    a +=5
    print(a)



# exercise 2

a = 1500

total = 0

while a <= 2100:
    if a % 5 == 0 and a % 7 == 0:
        total += a
    a += 1

print("ჯამი: ",total)

#exercise 3


a = 0
total = 0

while a <= 100:
    if a % 2 == 0:
        total += a
    a += 1

print("ლუწი რიცხვებისჯამი:",total)


#exercise 4

a = 1500

total = 0

while a <= 2100:
    if a % 5 == 0 and a % 7 == 0:
        total += a
        print(total)
        if total > 20000:
            break

    a += 1

print("ჯამი :",total)


#exercise 5

a = 15

while a <= 150:
    if a % 5 != 0:
        a += 1
        continue
    if a in [50, 75, 80]:
        a += 1
        continue
    print(a)
    a += 1