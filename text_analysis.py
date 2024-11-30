

main_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

number_of_characters_text = len(main_text)
number_of_word_text = len(main_text.split(" "))
number_of_sentence_text = len(main_text.split("."))

print(number_of_characters_text)
print(number_of_word_text)
print(number_of_sentence_text)


