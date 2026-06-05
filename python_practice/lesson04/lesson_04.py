from shlex import join

string_example = "Text example"
string_example_ukr = "Тектс Українською"
lorem_ipsum_text = "              Lorem Ipsum is - simply dummy text of the printing and - typesetting industry Lorem.           "

print(string_example)
print(string_example_ukr)

copy_string = string_example
print(id(string_example))
print(id(copy_string))
print("---------slices------------------")
print(string_example[0])
print(string_example[:3])
print(string_example[3:])
print(string_example[::2])
print(string_example[1::2])

part_of_example = string_example[:3]
print(part_of_example)
print("---------change string------------------")

# конкатенація
full_example = string_example + string_example_ukr
print(full_example)

# f string
f_name = f"Brr is {string_example}, brrr in ukraine {string_example_ukr}"
print(f_name)

# Дублювання стрінги чз множення
print(f_name*5)

print(id(string_example))
print(id(string_example_ukr))
print(id(f_name))
print(id(part_of_example))

print("---------Split------------------")

split_text = lorem_ipsum_text.split("-")
print(split_text)
print(lorem_ipsum_text.split())
print(type(split_text))

print(f"Частина 1 {split_text[0]}")
print(f"Частина 1 {split_text[1]}")

copy_lorem_ipsum_text = "Lorem Ipsum is -                          simply dummy text of the printing and -                 typesetting industry."

space_split = copy_lorem_ipsum_text.split(" ")
#  Дефолтний спліт забирає пробіли
default_split = copy_lorem_ipsum_text.split()

for element in default_split:
    new_element = f"this element is: {element}"
    print(new_element)

sentence_to_check = default_split

correct_sentence = True
for element in space_split:
    if element == "":
        correct_sentence = False

print(f"Sentence correct: {correct_sentence}")

# print(space_split)
# print(default_split)
print("-------------------ent_start_example----------------------")

print(lorem_ipsum_text.startswith("Lorem"))
print(lorem_ipsum_text.startswith("Lorem1"))
print(lorem_ipsum_text.endswith("industry."))
print(lorem_ipsum_text.endswith("industry!"))

for word in lorem_ipsum_text.split():
    word_lower = word.lower()
    print(f"Word - \"{word_lower}\" starts with \'l\': {word_lower.startswith("l")}")

print(lorem_ipsum_text.upper()) # верхній регістр кожне млова
print(lorem_ipsum_text.lower()) # нижній регістр кожне млова
print(lorem_ipsum_text.title()) # з великої кожне слово розділене не буквою
print(lorem_ipsum_text.capitalize()) # з великої стрінгу

print("-----",lorem_ipsum_text)
print(lorem_ipsum_text.islower())
print(lorem_ipsum_text.isupper()) # ?????????
print(lorem_ipsum_text.istitle())

print(lorem_ipsum_text.find("Lorem"))
print(lorem_ipsum_text.find("text"))

is_index = lorem_ipsum_text.find("text")
result_lorem = lorem_ipsum_text[:is_index]

print(result_lorem)

if lorem_ipsum_text.find("Lorem") >= 0: # не ок
    print(True)

if "Lorem" in lorem_ipsum_text:
    print("Lorem in the sentence")

print("-----------------------")
search_word = "of"
search_word_index = lorem_ipsum_text.find(search_word)
len_of_search_word = len(search_word)
end_index = search_word_index + len_of_search_word
one_more_resulted_lorem = lorem_ipsum_text[end_index:]
print(one_more_resulted_lorem)

print("------------Replace-----------")
print(lorem_ipsum_text.replace("Lorem", "Lorem1",1))

print("------------Join-----------")

split_text = lorem_ipsum_text.split()
print(split_text)

join_sting = " cat ".join(split_text)
print(join_sting)

print(lorem_ipsum_text.count("si"))
print(lorem_ipsum_text.strip(" "))