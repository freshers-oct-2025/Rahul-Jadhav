nums = [10, 20, 30]
for n in nums:
    print(n)

for i in range(len(nums)):
    print(i, nums[i])

for i, n in enumerate(nums):
    print(f"Index {i} -> {n}")

for i, n in enumerate(nums, start=1):
    print(f"Index {i} -> {n}")
for n in reversed(nums):
    print(n)
for n in sorted(nums, reverse=True):
    print(n)
for n in sorted(nums):
    print(n)


matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for val in row:
        print(val)

print("-------------------------------------------------------------------------------------------")

t = (1, 2, 3)
for item in t:
    print(item)
for i in range(len(t)):
    print(f"t[{i}] = {t[i]}")

for i, val in enumerate(t):
    print(f"Index {i} -> {val}")
for val in reversed(t):
    print(val)
for val in sorted(t):
    print(val)
for val in sorted(t, reverse=True):
    print(val)

print("-------------------------------------------------------------------------------------------")

s = {10, 20, 30}
for val in s:
    print(val)

for i, val in enumerate(s):
    print(f"Index {i} -> {val}")

for val in sorted(s):
    print(val)
for val in sorted(s, reverse=True):
    print(val)

for val in s:
    if val > 15:
        print(f"{val} is greater than 15")


print("-------------------------------------------------------------------------------------------")

person = {'name': 'Rahul', 'age': 22, 'city': 'Pune'}
for key in person:
    print(f"{key} -> {person[key]}")

for key, value in person.items():
    print(f"{key} -> {value}")

for key in sorted(person.keys()):
    print(f"{key} -> {person[key]}")

for key in sorted(person.keys(), reverse=True):
    print(f"{key} -> {person[key]}")

for key, val in person.items():
    print(key, ":", val)

for i, (k, v) in enumerate(person.items()):
    print(i, k, v)

for k in list(person.keys()):
    if k == 'age':
        del person[k]
print(person)
print("-------------------------------------------------------------------------------------------")

students = [
    {'name': 'Rahul', 'marks': 90},
    {'name': 'Amit', 'marks': 85}
]
for stu in students:
    for k, v in stu.items():
        print(k, ":", v)
subjects = {
    'math': [90, 85, 80],
    'science': [88, 92, 84]
}
for subject, marks in subjects.items():
    print(subject, ":", end=" ")
    for m in marks:
        print(m, end=" ")
    print()
print("-------------------------------------------------------------------------------------------")


