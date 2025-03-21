line = list(input())
s = line[0]
n = 0
new_line = ""
for i in range(len(s)):
    if s == line[i]:
        n+=1
    else:
        print("huy")
        n = 0
        s = line[i]
        new_line.join(line[i])
print(n)
print(new_line)