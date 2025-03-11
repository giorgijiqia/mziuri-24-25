#exercise 1

a = float(input("შეიყვანეთ ფუძე: "))
b = float(input("შეიყვანეთ ხარისხი: "))

print(a ** b)


#exercise 2

number1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
number2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

difference = max(number1, number2) - min(number1, number2)
print(difference)


#exercise 3

number = int(input("შეიყვანეთ რიცხვი: "))
result = ("კენტი", "ლუწი")[number % 2 == 0]

print(str(number) + " არის: " + result)




#exercise 4

num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

print("ორივე დადებითი" * (num1 > 0 and num2 > 0) + " 1 რიცხვი უარყოფითია" * (num1 < 0 or num2 < 0))


#bonus exercise 1

number1 = int(input("შეიყვანე პირველი რიცხვი: "))
number2 = int(input("შეიყვანე მეორე რიცხვი: "))
print(float(number1 + number2))
print(float(number1 - number2))
print(float(number1 * number2))
print(float(number1 / number2))
