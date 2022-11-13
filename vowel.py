import re

string_ex = str(input())

string_re =re.sub("[aeiouAEIOU]","",string_ex)

print(string_re)
