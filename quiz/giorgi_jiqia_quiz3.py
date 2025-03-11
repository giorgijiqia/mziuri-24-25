#exercise 1

def get_string_lengths(string_list):
     return [len(string) for string in string_list]


my_strings = ["hello", "world", "Python"]
lengths = get_string_lengths(my_strings)
print(lengths)


#exercise 2

def unique_elements(list1, list2):

    # return list(set(list1) ^ set(list2))
    return list(set(list1).symmetric_difference(set(list2)))


list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
print(unique_elements(list_a, list_b))

#exercise 3

def tuples_to_dict(tuples_list):
    result_dict = dict(tuples_list)
    for key, value in result_dict.items():
        print(f"{key}: {value}")


tuples_list = [("ჯასურ", 90,), ("ბეკი", 25)]
tuples_to_dict(tuples_list)

#exercise 4

def check_availability(products):
    result = []
    for product, quantity in products.items():
        if quantity > 5:
            result.append((product, "საკმარისია"))
        else:
            result.append((product, "არაა საკმარისი"))
    return result

product = {'ბადრიჯანი': 3, 'ხახვი': 6, 'კომბოსტო': 2}
print(check_availability(product))


#exercise 5

def words_starting_with_a(words):
    result = {}
    for word in words:
        if word[0] == "a":
        # if word.startswith('a'):

            result[word] = len(word)
    return result

word = ['apple', 'banana', 'apricot', 'grape', 'avocado']
print(words_starting_with_a(word))


#bonus exercise 6

# pop()
# del
# remove()

#bonus exercise 8

# symmetric_difference()
# union()
# difference()
# intersection()

#bonus exercise 10

#items()