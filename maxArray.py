#หาค่าmax


n = 3
number = []

for i in range(n):
  i_num = int(input())
  number.append(i_num)
  
a = max(number)
print(f"MAX : {a}")
