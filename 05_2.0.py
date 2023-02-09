name = input("name:")

students = ""
top = 0
mark_av = []

while name != "X":

    mark = int(input("Mark:"))
    mark_av.append(mark)
    if mark > top:
        top = mark
        students = name

    name = input("Name:")


print(students, top)

average = sum(mark_av)
av2 = average/len(mark_av)
print(av2)


