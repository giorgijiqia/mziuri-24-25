# exercise 1


# for num in range(2, 1001):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)



# exercise 2



# a = 0
# b = 1
#
# while a <= 100:
#     print(a)
#     a, b = b, a + b


# exercise 3


# number = input("შეიყვანეთ ნებისმიერი მთელი რიცხვი: ")
#
# count = 0
# for char in number:
#     if char.isdigit() or (char == '-' and count == 0):
#         count += 1
#
# print("ციფრების რაოდენობა:", count)



# exercise 4



# number = input("შეიყვანეთ ნებისმიერი მთელი რიცხვი: ")
#
# total = 0
# for char in number:
#     if char.isdigit():
#         total += int(char)
#
# print("ციფრების ჯამი:", total)


# exercise 5


# number = input("შეიყვანეთ ნებისმიერი მთელი რიცხვი: ")
#
# first_digit = None
#
# for char in number:
#     if char.isdigit():
#         first_digit = char
#         break
#
# if first_digit is not None:
#     print("პირველი ციფრი:", first_digit)
# else:
#     print("არასათანადო რიცხვი.")
