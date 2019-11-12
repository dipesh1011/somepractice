list1 = [1,3 ,5, 7]
list2 = [9, 10, 11, 13]

list1.insert(1,2)
print(list1)

list1.append(8)
print(list1)
list2.pop(1)
print(list2)

list1.sort(reverse = True)
print(list1)
print(list1.sort())
list3 = list1.extend(list2)

players = ["Benzema", "Kroos", "Ronaldo","Vinicius"]
print(players)

players.pop(2)
print(players)

players.insert(2, "Rodygo")
print(players)

print("The length of list players is:",len(players))

print("The index of player Vinicius in list is:",players.index("Vinicius"))

print(players[1:3])

'''listn = []
for i in range(1,5):
    list = input("Enter elements of list")
    listn.append(list)
print(listn)

listn[0] = int(listn[0])

print(listn)'''

marks = []
tmark = 0
for i in range(0,5):
    mark = int(input("Enter your marks:"))
    marks.append(mark)
for i in range(0,5):
    print(marks)
    print(marks[i])
    #tmark = tmark + marks[i]
    markt = sum(marks)
print("The sum is:",markt)
#print("The total mark is:",tmark)

per = markt/500 * 100
print("Your percentage is:",per,"%")

name = input("Enter your name:")
z = (input("Which alpahbet do you want to count:"))

print(name.upper().count(z.upper()))