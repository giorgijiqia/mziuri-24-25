#exercise 1

# multiples_of_5_cubes = tuple(x**3 for x in range(5, 101, 5))
#
# tuple_length = len(multiples_of_5_cubes)
#
# print("Tuple of cubes:", multiples_of_5_cubes)
# print("Length of the tuple:", tuple_length)


#exercise 2

# iterator = iter(multiples_of_5_cubes)
#
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         print("Reached the end of the iterator.")
#         break



#exercise 3


multiples_of_5_cubes_set = {x**3 for x in range(5, 101, 5)}

average = sum(multiples_of_5_cubes_set) / len(multiples_of_5_cubes_set)

print("სიმრავლე:", multiples_of_5_cubes_set)
print("სიმრავლის ელემენტების საშუალო არითმეტიკული:", average)


#exercise 4


# multiples_of_5_cubes_set = {x**3 for x in range(5, 101, 5)}
#
# iterator = iter(multiples_of_5_cubes_set)
#
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         print("Reached the end of the iterator.")
#         break


#exercise 5

# def number_generator():
#     for number in range(1, 6):
#         yield number
#
# iterator = number_generator()
#
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         print("Reached the end of the generator.")
#         break