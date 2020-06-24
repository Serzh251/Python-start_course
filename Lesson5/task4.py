# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
from googletrans import Translator
translator = Translator()
content = ''
try:
    with open('task4_origin_text.txt', encoding='utf-8') as my_file:
        content = my_file.read()
except IOError:
    print("Error input in file task4_origin_text!")
print(content)
result = translator.translate(content, src='en', dest='ru')

print(result.text)
try:
    with open('task4_translate_text.txt', 'w', encoding='utf-8') as f:
        f.write(result.text)
except IOError:
    print("Error output in file task4_translate_text!")