#exercise 1



length = 8
width = 5

perimeter = 2 * (length + width)
print(perimeter)




#exercise 2



number = int(input("შეიყვანეთ რიცხვი: "))

if number < 2:
    print("არაა მარტივი რიცხვი")
else:
    for i in range(2, number):
        if number % i == 0:
            print("არაა მარტივი რიცხვი")
            break
    else:
        print("მარტივი რიცხვია")



#exercise 3


a = 0
total = 0
number = 1

while a < 20:
    total += number
    a += 1
    number += 2
print(total,)




#exercise 4


number = 1

while number <= 100:
    print(number,)

    if number % 5 == 0:
        break

    number += 1



#exercise 5


for i in range(1, 31):
    if i % 2 != 0:
        continue
    print(i)


#exercise 6



num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

if num1 > num2:
    maximum = num1
else:
    maximum = num2

print("მაქსიმალური რიცხვი არის:", maximum)




#bonus exercise 1

score = int(input("შეიყვანეთ ქულა: "))

if score >= 80:
    print("თქვენ გაქვთ კარგი ქულა.")
elif score >= 40:
    print("თქვენ გაქვთ საშვალო ქულა.") #elif საშვალებას გვაძლევს რომ დავამატოთ უფრო მეტი პირობა როდესაც if პირობა არ სრულდება
else:
    print("თქვენ გაქვთ ცუდი ქულა.")








number = int(input("შეიყვანეთ რიცხვი: "))

divisors = {i for i in range(1, number + 1)
if number % i == 0}

print(number, "-ის გამყოფები:", divisors)