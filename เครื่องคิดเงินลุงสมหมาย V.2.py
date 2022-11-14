input_ = 1
number = []
while input_ != 0:
    try:        
        if ( input_ > 0 ):
            input_ = int(input())
            number.split()
    except:
        input_ = 0

com = str(input())

if com == ["MaX","max"]:
    number.sort(reverse=True)
    for i in range (len(number)):
        print(number[i],"",end="")
elif com == ["Min","min"]:
    print(" ".join(number(reversed=True)))