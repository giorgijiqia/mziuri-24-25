#exercise 2

person = {
    "name": "Giorgi",
    "age": 30,
    "city": "Tbilisi",
    "occupation": "Teacher"
}

print(person)


#exercise 3

person = {
    "name": "Giorgi",
    "age":30,
    "city": "Tbilisi",
    "occupation": "Teacher"
}

person["hobby"] = "ჭამა და ძილი"

del person["age"]

print(person)


#exercise 4


def merge_dictionaries(dict1, dict2):
    merged_dict = dict1
    merged_dict.update(dict2)
    return merged_dict

dict1 = {
    "name": "Giorgi",
    "age": 30
}

dict2 = {
    "city": "Tbilisi",
    "occupation": "Teacher"
}

merged_result = merge_dictionaries(dict1, dict2)
print(merged_result)



#exercise 5


def filter_dictionary(input_dict):
    filtered_dict = {}

    for key, value in input_dict.items():
        if value > 10:
            filtered_dict[key] = value

    return filtered_dict


my_dict = {
    "a": 4,
    "b": 14,
    "c": 12,
    "d": 7,
    "e": 22
}

filtered_result = filter_dictionary(my_dict)
print(filtered_result)


#exercise 6

numbers = [1, 2, 3, 4, 5]

cubes_dict = {}

for number in numbers:
    cubes_dict[number] = number ** 3

print(cubes_dict)



#exercise 7

def frequency_counter(input_list):
    frequency_dict = {}

    for item in input_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[
                item] = 1
    return frequency_dict


my_list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 2, 1]

frequency_result = frequency_counter(my_list)
print(frequency_result)

#exercise 8

def invert_dictionary(input_dict):
    inverted_dict = {}

    for key, value in input_dict.items():
        if value in inverted_dict:
            if type(inverted_dict[value]) == list:
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
        else:
            inverted_dict[value] = key

    return inverted_dict

my_dict = {
    "a": 1,
    "b": 2,
    "c": 2,
    "d": 3,
    "e": 1
}

inverted_result = invert_dictionary(my_dict)
print(inverted_result)



#bonus exercise 1

def create_dictionary(list1, list2):
    if len(list1) != len(list2):
        return "ლისტების სიგრძე უნდა ემთხვეოდეს"

    result_dict = {}
    for i in range(len(list1)):
        result_dict[list1[i]] = list2[i]

    return result_dict

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

result = create_dictionary(list1, list2)
print(result)