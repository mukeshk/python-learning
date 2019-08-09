"""
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

"""
if __name__ == '__main__':
    def sortSecond(item):
        return item[1]

    students = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        students.append([name,score])
    
    if len(students)>0:
        students.sort(key=sortSecond)
        lowScore=students[0][1]
        secondLowScore=-1
        for item in students :
            if lowScore < item[1] :
                secondLowScore=item[1]
                break
        outputStudents=[]
        for item in students :
            if item[1]==secondLowScore:
                outputStudents.append(item[0]) 
        outputStudents.sort()
        for item in outputStudents:
            print item          

