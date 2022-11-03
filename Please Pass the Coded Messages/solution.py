from itertools import permutations 
def solution(l):
    possibilities = list(permutations(l))
    for i in range(len(possibilities)):
        converted = list(possibilities[i])
        possibilities[i] = ("".join(map(str, converted)))
    possibilities.sort(reverse=True)
    for j in range(len(l)):
        for i in range(len(possibilities)):
            print(possibilities[i])
            if int(possibilities[i]) % 3 == 0:
                return possibilities[i]
            possibilities[i] = possibilities[i][:-1]
    else:
        return 0