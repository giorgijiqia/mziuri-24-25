#exercise 1

file_name = "output.txt"
text = "hello"

with open(file_name, "w") as file:
    file.write(text)

print(f"The text has been written to {file_name}.")

file.close()

#exercise 2

file_path = 'output.txt'

with open(file_path, 'r') as file:
    content = file.read()
    print(content)
    character_count = len(content)
    print(f' {character_count}')


#exercise 3


with open('output.txt', 'a') as file:
    file.write('\nworld')



#exercise 5

file1_name = 'file1.txt'
file2_name = 'file2.txt'
output_file_name = 'merged_file.txt'

with open(file1_name, 'w', encoding='utf-8') as file1:
    file1.write("hello\n")

with open(file2_name, 'w', encoding='utf-8') as file2:
    file2.write("world.\n")


with open(file1_name, 'r', encoding='utf-8') as file1, open(file2_name, 'r', encoding='utf-8') as file2, open(
        output_file_name, 'w', encoding='utf-8') as output_file:
    content1 = file1.read()
    content2 = file2.read()

    output_file.write(content1)
    output_file.write("\n")
    output_file.write(content2)

print(f"The contents of '{file1_name}' and '{file2_name}' have been successfully merged into '{output_file_name}'.")

#exercise 6


file_name = 'output.txt'

with open(file_name, 'r') as file:
    content = file.read()

print(content.upper())