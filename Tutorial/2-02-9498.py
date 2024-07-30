score_input = input()
score = int(score_input)
n_score = score//10
if(n_score >= 9):
    print('A')
elif(n_score == 8):
    print('B')
elif(n_score == 7):
    print('C')
elif(n_score == 6):
    print('D')
else:
    print('F')