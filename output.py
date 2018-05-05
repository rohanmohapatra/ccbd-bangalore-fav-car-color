import matplotlib.pyplot as plt
import numpy as np

f = open('output-specific.txt','r')

x = f.read()
listofvals=[]
listofcolor=[]
listofcolori=[]
x = x.split("\n")
x = [i.split("\t") for i in x]
for val in x:
    try:
        listofvals.append(val[1])
        listofcolor.append(val[0])
    except IndexError:
        continue
#print(listofvals)
listofvals = [int(i) for i in listofvals]
index = listofvals.index(max(listofvals))
print("Bangalore's Favourite Color(specific) : %s" %''.join(x[index][0]))
for i in range(len(listofcolor)):
   listofcolori.append(i)
plt.figure(figsize=(50,50))
barlist = plt.bar(listofcolori,listofvals,align="center",edgecolor="black",linewidth=2.0)
for i in range(len(listofcolor)):
    try:
        barlist[i].set_facecolor(listofcolor[i])
    except ValueError:
        if (listofcolor[i]=="autogreen"):
            barlist[i].set_facecolor("lightgreen")
        if (listofcolor[i]=="golden"):
            barlist[i].set_facecolor("yellow")
        if (listofcolor[i]=="tintred"):
            barlist[i].set_facecolor("red")
        if (listofcolor[i]=="vermillion"):
            barlist[i].set_facecolor("orange")
        if (listofcolor[i]=="lightred"):
            barlist[i].set_facecolor("tomato")
        

plt.xticks(listofcolori, listofcolor,rotation=90)
plt.show()
f.close()
