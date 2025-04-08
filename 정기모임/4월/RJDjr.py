year=int(input('불기연도를 입력하시오'))
if year>=1000 and year<=3000:
    year-=543
    print('당신의 서기연도는',year)
else:
    print('너의 불기연도는 잘못됐어!')
