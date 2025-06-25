word = 'abcdefghijklmnopqrstuvwxyz '
HW = [16,5,11,11,15,27,23,15,18,11,4]
ans = []
for i in range(len(HW)):
    ans.append(word(HW[i]))
print(ans)