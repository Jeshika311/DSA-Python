string = str(input("Enter a string : "))
words = string.split()

anagrams = {}

for word in words:
    sorted_str = "".join(sorted(word.replace(" " , "").lower()))
    if sorted_str not in anagrams:
        anagrams[sorted_str] = []
    anagrams[sorted_str].append(word)

anagram = list(anagrams.values())
print(f"Anagram groups : {anagram}")