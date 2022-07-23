# Ученик школы Флэша решил преисполниться и посмотрел филосовское видео "Идущего к реке", но чтобы выписать отдельные
# цитаты из видео, нашел монолог текстом. Ученик ошалел от длины монолога, и ему стало очень интересно, сколько же слов
# было всего сказано в этом видео. Задача: посчитать количество слов, учитывая предлоги, но не учитывая знаки препинания
# во всём тексте. В фале находится текст монолога с пробелами, а также строчки разделены пустыми строками. Сложные слова
# и словосочетания по типу только-только, газо-пылевое учитывать как два слова.

A = {'.', ',', ':', ';', '/', '"', '!', '?', '(', ')', '=', '+', '\n'}

with open('kur11.txt', encoding='utf-8') as file: #считываем файл и строки в нём
    f = file.readlines()
for p in A: # заменяем все знаки препинания на пустоту, либо пробел по условию
    for i in range(len(f)):
        f[i] = f[i].replace(p, '')
        f[i] = f[i].replace('-',' ')
print(len(' '.join(f).split())) # список преобразуем в строку, потом обратно в список, объединив тем самым все слова
# и подсчитываем через len

# Решение. Создаём массив со знаками препинания. Считываем файл, после этого циклом заменяем все знаки препинания в
# файле на "" (пустоту) либо на пробел если это тире, и выводим количество слов (список преобразуем в строку, потом
# обратно в список, объединив тем самым все слова и подсчитываем через len. Получаем ответ 505.
