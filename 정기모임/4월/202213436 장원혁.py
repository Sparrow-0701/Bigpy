score_r={'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5,'D0':1.0,'F':0}
t_grade=0
t_score=0
gl=[]
for i in range(20):
    gl.append(input().split())
for i in gl:
    _, grade, score=i
    if score == 'P':
        continue
    t_grade+= float(grade)
    t_score += score_r[score]*float(grade)
print(t_score/t_grade)