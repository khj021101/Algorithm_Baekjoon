GradeScore = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0}
TotalScore = 0
TotalHour = 0
for i in range(20):
    SubjectName, LectureHour, LetterGrade = input().split()
    if LetterGrade == 'P':
        continue
    else:
        TotalScore += float(LectureHour)*GradeScore[LetterGrade]
        TotalHour += float(LectureHour)
print(TotalScore/TotalHour)

