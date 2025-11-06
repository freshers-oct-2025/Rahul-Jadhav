nums=[12,15,18,21,26,10,15,20]

for i in nums:
    if i % 5 == 0:
        print(i)
        break
else:
    print(f"{i} is not divisible by 5")