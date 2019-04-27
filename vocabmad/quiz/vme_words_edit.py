# import codecs
# f1 = codecs.open("rough.txt", encoding = "utf-8")
# f2 = codecs.open("final_rough.txt", "w", encoding = "utf-8")
# for line in f1:
#     if line=="\n":
#         pass
#     else:
#         f2.write(line)
# f1.close()
# f2.close()

import codecs
f1 = codecs.open("vme_initial.txt", encoding = "utf-8")
def word(line):
    c = 0
    for x in line:
        if x==")":
            c+=1
    if c==3:
        return True
    else:
        return False
word_knowledge = []
word_list = []
for line in f1:
    if word(line):
        word_list.append(word_knowledge)
        word_knowledge = []
        word_knowledge.append(line)
    else:
        word_knowledge.append(line)
f1.close()

word_list.pop(0)

def find_word(line):
    word = ""
    for i in range(len(line)):
        if line[i] == ":":
            break
        else:
            word += line[i]
    return word

def find_pronun(line):
    i = line.index(":")
    pronun = line[i+2:]
    return pronun

f2 = codecs.open("word_list.txt", "w", encoding = "utf-8")
for word in word_list:
    for i in range(0, len(word)):
        if i==0:
            f2.write("Word: ")
            main_word = find_word(word[0])
            f2.write(main_word)
            f2.write("\n")
            f2.write("Pronunciation: ")
            pronun = find_pronun(word[0])
            f2.write(pronun)
        if i==1:
            f2.write("Hindi meaning: ")
            f2.write(word[1])
        if "Syn: " in word[i]:
            end = i
            a = 1
            b = 1
            for j in range(2,i):
                if main_word.lower() in word[j].lower():
                    f2.write("EM %d EX %d: " %(b-1, a))
                    a+=1
                    f2.write(word[j][2:])
                else:
                    f2.write("EM %d: " %b)
                    b+=1
                    a = 1
                    f2.write(word[j][2:])
            f2.write("Synonym: ")
            f2.write(word[i])
        if "Note: " in word[i]:
            f2.write("Note: ")
            f2.write(word[i])
        if "Mnemotrick" in word[i]:
            if i==len(word)-1:
                f2.write("Mnemonic trick 1: ")
                f2.write(word[i][13:])
            else:
                c = 1
                for j in range(i+1, len(word)):
                    x = "Mnemonic trick %d:" %c
                    c+=1
                    f2.write(x)
                    f2.write(word[j][2:])
    f2.write("\n\n")
f2.close()
