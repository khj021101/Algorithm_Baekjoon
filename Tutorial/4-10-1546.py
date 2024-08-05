subject_num = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)
def normalize(score):
    return (score/max_score)*100
new_score_list = list(map(normalize, score_list))
print(sum(new_score_list)/len(new_score_list))