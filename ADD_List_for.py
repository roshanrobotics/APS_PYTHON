# l = [10,20,30,40,50,60]
l=[10,4,8,3,4,5,6,9,77,2,55]
even =0
#for i in range(6):
for i in range(len(l)): 
    even = l[i]%2
    if even == 0:
        even = even +l[i]
        print(even)
print(even)