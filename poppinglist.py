my_list = [2, 7.5, "Dipesh", 12]
num = input("Enter the item you want to pop:")

if num.isalpha() == True:
    pos = my_list.index(num)
    my_list.pop(pos)
else:
    fnum = float(num)
    pos = my_list.index(fnum)
    my_list.pop(pos)
print(my_list)