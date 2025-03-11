#exercise 1


# number = int(input("შეიყვანეთ რიცხვი: "))
#
# divisors = { i for i in range(1, number + 1)
# if number % i == 0}
#
# print(number, "-ის გამყოფები:", divisors)



#exercise 2


# number1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
# number2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
#
# for a in range(1, min(number1,number2) + 1):
#     if number1 % a == 0 and number2 % a == 0:
#         print(a)





#exercsie 3

# number1 = int(input("enter number: "))
# number2 = int(input("enter number: "))
# max_num = 0
#
# min_num = min(number1, number2)
# for a in range(1,min_num+1):
#     if number1 % a == 0 and number2 % a == 0:
#         max_num = a
# print(max_num)







#exercise 4

# num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
# num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
#
# a = max(num1, num2)
#
# while a % num1 != 0 or a % num2 != 0:
#     a += 1
#
# print("უმცირესი საერთო ჯერადი არის:", a)