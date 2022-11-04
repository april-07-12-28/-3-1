txt_all = []
import os
for filename in os.listdir("txt"):
    with open(os.path.join("txt", filename), 'r',encoding="utf8") as f:
        txt_1 = f.readlines()
        a = len(txt_1)
        b = filename
        txt = []
        txt.append(b)
        txt.append(str(a))
        i = 0
        while i < len(txt_1):
            txt.append(txt_1[i])
            i += 1
        txt_all.append(txt)


txt_all.sort(key=len)
print(txt_all)
i= 0
text = []
while i < len(txt_all) :
    text_num = " ".join(map(str,txt_all[i]))
    text.append(text_num)
    i += 1
print(text)
f = open("text.txt", 'w',encoding='utf8')
for element in text:
    f.writelines(element)
    f.write('\n')
f.close()