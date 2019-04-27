import codecs
f1 = codecs.open("A_words.txt", encoding = "utf-8")
a_list = []
for line in f1:
    a_list.append(line)
f1.close()

f2 = codecs.open("B_words.txt", encoding = "utf-8")
b_list = []
for line in f2:
    b_list.append(line)
f2.close()

f3 = codecs.open("C_words.txt", encoding = "utf-8")
c_list = []
for line in f3:
    c_list.append(line)
f3.close()

a = 0
b = 0
c = 0
j = 0
main_list = []

while a<len(a_list) and b<len(b_list) and c<len(a_list):
    if a < len(a_list):
        main_list.append(a_list[a])
        a += 1
    if b < len(b_list):
        main_list.append(b_list[b])
        b += 1
    if c < len(c_list):
        main_list.append(c_list[c])
        c += 1

f = codecs.open("main_file.txt", "w", encoding = "utf-8")
for x in main_list:
    f.write(x)
f.close()
