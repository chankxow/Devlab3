grade = int(input())

if  grade > 100 :
    print('Error : Value must be less than or equal to 100.')
elif grade >= 90 :
    print('A')
elif grade >= 85 :
    print('B+')
elif grade >= 80 :
    print('B')
elif grade >= 75 :
    print('C+')
elif grade >= 70 :
    print('C')
elif grade >= 65 :
    print('D+')
elif grade >= 60 :
    print('D')
elif grade < 60 and grade > 0 :
    print('F')
elif grade < 0 :
    print('Error : Value must be greater than or equal to 0.')