#exercise1

while True:
    try:
        num1 = float(input("შეიტანეთ პირველი რიცხვი: "))
        num2 = float(input("შეიტანეთ მეორე რიცხვი: "))

        if num2 == 0:
            print("შეცდომა: გაყოფა ნულის მიერ არ შეიძლება. სცადეთ ხელახლა.")
            continue

        result = num1 / num2
        print(f"პირველი რიცხვის {num1} გაყოფის შედეგი მეორე რიცხვზე {num2} არის: {result}")
        break
    except ValueError:
        print("შეცდომა: გთხოვთ, შეიტანოთ რიცხვები სწორად.")



#exercise 2


def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "შეცდომა: ნულის მიერ გაყოფა შეუძლებელია"
    except Exception as e:
        return f"შეცდომა: {e}"

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers("abc", 5))


#exercise 3

def get_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return "შეცდომა: ინდექსი არ არსებობს"

my_list = [10, 20, 30]
print(get_element(my_list, 2))
print(get_element(my_list, 5))


#exercise 4


try:
    with open("myresult.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("შეცდომა: ფაილი 'myresult.txt' არ არსებობს.")


#exercise 5


import math


def find_roots(a, b, c):
    try:
        delta = b ** 2 - 4 * a * c

        if delta > 0:
            root1 = (-b + math.sqrt(delta)) / (2 * a)
            root2 = (-b - math.sqrt(delta)) / (2 * a)
            return f"ფესვები: {root1} და {root2}"

        elif delta == 0:
            root = -b / (2 * a)
            return f"ფესვი: {root}"

        else:
            return "ფესვები არ არსებობს (უარყოფითი დისკრიმინანტი)."

    except ZeroDivisionError:
        return "შეცდომა: a-ი არ შეიძლება იყოს ნული."
    except ValueError:
        return "შეცდომა: გთხოვთ, შეიტანოთ სწორი რიცხვები."

try:
    a = float(input("შეიტანეთ a (კვადრატული განტოლების კოეფიციენტი): "))
    b = float(input("შეიტანეთ b (კვადრატული განტოლების კოეფიციენტი): "))
    c = float(input("შეიტანეთ c (კვადრატული განტოლების კოეფიციენტი): "))

    result = find_roots(a, b, c)
    print(result)

except ValueError:
    print("შეცდომა: გთხოვთ, შეიტანოთ რიცხვები სწორად.")



#exercise 6


def check_triangle_and_calculate_mean(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        mean = (a + b + c) / 3
        return mean
    else:
        raise ValueError("შეცდომა: ამ რიცხვებით ვერ მიიღება სამკუთხედის ფორმირება.")

try:
    a = int(input("შეიტანეთ პირველი გვერდი (a): "))
    b = int(input("შეიტანეთ მეორე გვერდი (b): "))
    c = int(input("შეიტანეთ მესამე გვერდი (c): "))

    result = check_triangle_and_calculate_mean(a, b, c)
    print(f"სამკუთხედის გვერდების საშუალო არითმეტიკული: {result}")

except ValueError as e:
    print(e)