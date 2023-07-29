# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


text = """She sells sea shells on the sea shore The shells
    that she sells are sea shells I'm sure.So if she sells sea
    shells on the sea shore I'm sure that the shells are sea
    shore shells"""
text = text.lower()
text = text.replace('.', ' ')
# text = text.replace("'", ' ')
text = text.split()
# text_list = list(text)
# print(text_list)
text_set = set(text)
print(text_set)


print(len(text_set))
