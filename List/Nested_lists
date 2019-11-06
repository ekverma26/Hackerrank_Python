''Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.''

CODE:-
if __name__ == '__main__':
    l=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])

    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][1]<l[j][1]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
    k=l[0][1]
    l2=[]
    for i in range(len(l)):
        if l[i][1]!=k:
            l2.append(l[i])

    k=l2[0][1]
    l3=[]
    for i in l2:
        if i[1]==k:
            l3.append(i[0])
    l3.sort()
    for i in l3:
        print(i)
