with open("C:\\Users\\tains\\ADVENT-OF-CODE-2022\\Day3\\input.txt") as f:
    # print(L)
    mapping = list(line for line in f)

res = []
for i in mapping:
    res.append(i.replace('\n', ''))
finalList = []
for i in range(len(res)):
    temp = len(res[i])
    finalList.append([res[i][0:temp // 2], res[i][temp // 2:temp]])

intersection = []
for intersect in finalList:
    intersection.append(set(intersect[0]).intersection(set(intersect[1])))

priorities = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26,
    'A':27,
    'B':28,
    'C':29,
    'D':30,
    'E':31,
    'F':32,
    'G':33,
    'H':34,
    'I':35,
    'J':36,
    'K':37,
    'L':38,
    'M':39,
    'N':40,
    'O':41,
    'P':42,
    'Q':43,
    'R':44,
    'S':45,
    'T':46,
    'U':47,
    'V':48,
    'W':49,
    'X':50,
    'Y':51,
    'Z':52,
}
sum = 0
for i in intersection:
    for j in i:
        sum += priorities[j]
print(sum)
# print(intersection)