num=0
string=''
for i in range(3):
    a = input()
    if i == 2:
        num -= int(a)
        string = int(string) - int(a)
    else:
        num += int(a)
        string += a
print(num, string)