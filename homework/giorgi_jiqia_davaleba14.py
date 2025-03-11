# #exercise 1

# input_file = open('numbers.txt', 'r')
# numbers = []
#
# for line in input_file:
#     numbers.append(int(line))
#
# input_file.close()
#
# squared_numbers = []
# for num in numbers:
#     squared_numbers.append(num ** 2)
#
# output_file = open('squared_numbers.txt', 'w')
#
# for squared in squared_numbers:
#     output_file.write(f"{squared}\n")
#
# output_file.close()
#
# print(squared_numbers)


#exercise 2

oscar_winners = []


with open('oscars.txt', 'r') as file:
    for line in file:
        oscar_winners.append(line.strip().split(','))


try:
    year_input = int(input("Enter a year: "))
except ValueError:
    print("Invalid year input!")
    exit()

winners = [winner[3] for winner in oscar_winners if int(winner[0]) == year_input]

if winners:
    print(f"Oscar winners in {year_input}:")
    for winner in winners:
        print(winner)
else:
    print(f"No winners in {year_input}.")

youngest = oscar_winners[0]

for winner in oscar_winners:
    if int(winner[2]) < int(youngest[2]):
        youngest = winner

print(f"The youngest winner is: {youngest[3]} ({youngest[4]}) - Age: {youngest[2]}")