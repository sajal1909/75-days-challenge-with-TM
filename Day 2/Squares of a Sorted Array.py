count = 0
curr = ''
for i in nums:
    if i == curr:
        count += 1
    else:
        if count <= 0:
            curr = i
            count = 1
        else:
            count -= 1

return curr