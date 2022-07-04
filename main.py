print("TASK_1")

word = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
counter = 0

with open('mbox-short.txt', encoding='utf-8') as file:
    for line in file:
        if word in line:
            print(line, end='')
with open('mbox-short.txt', encoding='utf-8') as file:
    counter = 0
    for line in file:
        if "Author:" in line:
            print((line.split()).pop(1))




print("TASK_2")
li = []
with open('romeo.txt', encoding='utf-8') as file:
    for line in file:
        li.extend(line.split())

li.sort()
print(li)



print("TASK_3")

def read_last(lines, file):
    with open(file, encoding='utf-8') as romeo:
        txt_str = romeo.readlines()[-lines:]
    for i in txt_str:
        print(i)


read_last(1, 'romeo.txt')



print("TASK_4")
def longest_words(file):
    words_list = []
    with open(file, encoding='utf-8') as text:
        words = text.read().split()
        super_len = len(max(words))
        for i in words:
            if len(i) > super_len:
                words_list.append(i)
        return words_list


print(longest_words('romeo.txt'))

print("TASK_5")
files = ['pushkin2.txt', 'byron.txt', 'romeo.txt']
with open('poems.txt', 'w', encoding="utf8") as main_file:
    for i in files:
        with open(i, encoding="utf8") as sub_file:
            a = sub_file.read()
            main_file.write(a)