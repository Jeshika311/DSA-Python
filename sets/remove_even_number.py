def input_set():
    set_input = input("Enter elements seperated by space : ")
    s = set(map(int , set_input.split()))
    return s 

s = input_set()
new_set = [] #empty list to store items

for i in s:
    if i%2!=0:
        new_set.append(i) #add odd numbers to list
    
s2 = set(new_set) #convert list into set
print(s2)