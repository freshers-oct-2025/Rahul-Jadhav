file = open("example.txt", "w")
file.write("Hello, Python File Handling!\n")
file.write("This is the second line.")
file.close()


file = open("example.txt", "r")
content = file.read()       
print(content)
file.close()


file = open("example.txt", "r")

print(file.readline())  
print(file.readline())   

file.close()


file = open("example.txt", "a")
file.write("\nNew line added later!")
file.close()


with open("example.txt", "r") as file:
    data = file.read()
    print(data)
