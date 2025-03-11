# exercise 1

with open('titanic.txt', mode='r') as file:
    lines = file.readlines()

headers = lines[0].strip().split(',')

print("Headers:", headers)

gender_index = headers.index('Sex')
survival_index = headers.index('Survived')
class_index = headers.index('Pclass')
ticket_price_index = headers.index('Fare')

female_count = 0
male_count = 0
female_survived = 0
male_survived = 0

for line in lines[1:]:
    row = line.strip().split(',')

    gender = row[gender_index]
    survival = row[survival_index]
    passenger_class = row[class_index]
    ticket_price = (row[ticket_price_index])

    if gender.lower() == 'female':
        female_count += 1
        if survival == '1':
            female_survived += 1
    elif gender.lower() == 'male':
        male_count += 1
        if survival == '1':
            male_survived += 1

total_passengers = female_count + male_count
female_percentage = (female_count / total_passengers) * 100
male_percentage = (male_count / total_passengers) * 100

print(f"Female count: {female_count}, Female percentage: {female_percentage:.2f}%")
print(f"Male count: {male_count}, Male percentage: {male_percentage:.2f}%")
print(f"Female survivors: {female_survived}, Male survivors: {male_survived}")

#exercise 2

class Ticket:
    def __init__(self, movie_title, ticket_price, quantity, language="Geo"):
        self.movie_title = movie_title
        self.ticket_price = ticket_price
        self.quantity = quantity
        self.language = language

    def __str__(self):
        return f"Movie: {self.movie_title}, Price per Ticket: {self.ticket_price} GEL, " \
               f"Quantity Available: {self.quantity}, Language: {self.language}"


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"User: {self.name}, Balance: {self.balance} GEL"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} GEL successfully added to your balance.")
        else:
            print("Deposit amount must be positive.")

ticket = Ticket("Avatar 2", 20, 100)
print(ticket)

user = User("Giorgi", 50)
print(user)

user.deposit(30)
print(user)