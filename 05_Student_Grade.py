name_l = []
students = ""
top = 0
mark_av = []
grades = []

name = input("name:")
name_l.append(name)



while name != "X":

    mark = int(input("Mark:"))
    mark_av.append(mark)

    if mark >= 90:
        grade = 'A+'
        grades.append(grade)
    elif mark >= 85 and mark <= 89:
        grade = 'A'
        grades.append(grade)
    elif mark >= 80 and mark <= 84:
        grade = 'A-'
        grades.append(grade)
    elif mark >= 75 and mark <= 79:
        grade = 'B+'
        grades.append(grade)
    elif mark >= 70 and mark <= 74:
        grade = 'B'
        grades.append(grade)
    elif mark >= 65 and mark <= 69:
        grade = 'B-'
        grades.append(grade)
    elif mark >= 60 and mark <= 64:
        grade = 'C+'
        grades.append(grade)
    elif mark >= 55 and mark <= 59:
        grade = 'C'
        grades.append(grade)
    elif mark >= 50 and mark <= 54:
        grade = 'C-'
        grades.append(grade)
    elif mark >= 40 and mark <= 49:
        grade = 'D'
        grades.append(grade)
    else:
        grade = 'E'
        grades.append(grade)

    name = input("Name:")
    if name != 'X':
        name_l.append(name)



    if mark > top and name != 'X':
        top = mark
        students = name



print(students, top)

average = sum(mark_av)
av2 = average/len(mark_av)
print(av2)


for i in range(len(name_l)):
    print(grades[i-1], name_l[i-1])













