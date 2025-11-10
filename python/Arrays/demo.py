from array import *
import numpy as np

val=array('i',[10,20,30,40,50])
val2=array('d',[10.5,20.5,30.5])
val3=array('w',['a','b','c','d'])
val4=array('b',[1,0,1,1,0])
val5=array('f',[1.5,2.5,3.5])
val6=array('h',[1000,2000,3000])
val7=array('I',[100,200,300,400])



print(val)

print(val.buffer_info())
print(val.typecode)
print(val.count(20))
print(val.index(30))
#print(val.tolist())
print(val[2])
val.reverse()
print("Reversed Array: ", val) 
val.append(60)
print("Appended Array: ", val)
val.insert(2,25)
print("Inserted Array: ", val)
val.remove(20)
print("Removed Array: ", val)

print("Popped Array",val.pop())

print("Extended Array",val.extend([70,80,90]))
print("Final Array: ", val)
print("-------------------------------------------------------------------------------------------")

for i in val:
    print(i)
for i in range(len(val)):
    print(i,val[i])
for i, n in enumerate(val):
    print(f"Index {i} -> {n}")

new_array = array(val.typecode,( a for a in val))
print("New Array: ", new_array)



print("--------------------User Input Array: --------------------------------------------")

arr2=array('i',[])  

n=int(input("Enter the length of the array:"))

for i in range(n):
    x=int(input("Enter the next value:"))
    arr2.append(x)  

print("User Input Array: ",arr2)

search=int(input("Enter the value to be searched:"))
for i in range(len(arr2)):
    if arr2[i]==search:
        print(f"Value {search} found at index {i}")
        break
else:
    print(f"Value {search} not found in the array")


print(arr2.index(search))


