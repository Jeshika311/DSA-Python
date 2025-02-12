def partitions(s):
    if len(s) == 0:
        return [[]]
    else:
        result = []
        first = next(iter(s))
        rest = s - {first}
        for p in partitions(rest):
            result.append([{first}] + p)
            for i in range(len(p)):
                result.append([p[i] | {first}] + p[:i] + p[i+1:])
        return result
            
def input_set():
    set_input = input("Enter elements of sets seperated by some space : ")
    s = set(set_input.split())
    return s 

s = input_set()
partitions_s = partitions(s)
for i,p in enumerate(partitions_s):
    print(f"Partitions {i+1} : {p}")