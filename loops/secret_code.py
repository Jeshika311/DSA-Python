string = str(input("Enter any string : "))
words = string.split(" ")
option = int(input("Enter 1 for coding and 2 for decoding : "))
if(option==1):
    new_word = []
    for word in words:
        if(len(word)>=3):
            s1 = "str"
            s2 = "hyu"
            st_new = s1 + word[1:] + word[0] + s2
            new_word.append(st_new)
        else:
            new_word.append(word[::-1])
    print(" ".join(new_word))

if(option==2):
    new_word = []
    for word in words:
        if(len(word)>=3):
            st_new = word[3:-3]
            st_new = st_new[-1] + st_new[:-1]
            new_word.append(st_new)
        else:
            new_word.append(word[::-1])
    print(" ".join(new_word))