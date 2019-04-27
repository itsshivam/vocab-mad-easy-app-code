import codecs
f1 = codecs.open("quest_initial.txt", encoding = "utf-8")
quest_list = []
def new_quest(line):
    if "Q." in line:
        return 1
    elif "1." in line:
        return 2
    elif "2." in line:
        return 3
    elif "3." in line:
        return 4
    elif "4." in line:
        return 5
    elif "Ans." in line:
        return 6
    else:
        return 0
quest = []
for line in f1:
    verify = new_quest(line)
    if verify == 0:
        quest.append(line)
    elif verify == 1:
        quest.append(line[3:])
    elif verify == 2:
        quest.append(line[3:])
    elif verify == 3:
        quest.append(line[3:])
    elif verify == 4:
        quest.append(line[3:])
    elif verify == 5:
        quest.append(line[3:])
    elif verify == 6:
        quest.append(line[5:])
        quest_list.append(quest)
        quest = []
    else:
        quest.append(line)
f1.close()

for quest in quest_list:
    for line in quest:
        print line
    print "\n"
