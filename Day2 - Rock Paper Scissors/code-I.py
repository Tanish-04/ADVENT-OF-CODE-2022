with open("C:\\Users\\tains\\ADVENT-OF-CODE-2022\\Day2 - Rock Paper Scissors\\input.txt") as f:
    mapping = list(line.split(' ', 1) for line in f)

res = []
for i in mapping:
    res.append([i[0].replace('\n',''), i[1].replace('\n', '')])

score = 0
for i in res:
    # 1 for Rock, 2 for Paper, 3 for Scissors
    # 0 for lost, 3 for draw, 6 for win
    # if res[i]

    if i[0] == 'A' and i[1] == 'Y':
        score += 2 + 6

    elif i[0] == 'C' and i[1] == 'Y':
        score += 2 + 0

    elif i[0] == 'B' and i[1] == 'X':
        score += 1 + 0

    elif i[0] == 'C' and i[1] == 'X':
        score += 1 + 6

    elif i[0] == 'A' and i[1] == 'Z':
        score += 3 + 0

    elif i[0] == 'B' and i[1] == 'Z':
        score += 3 + 6

    elif i[0] == 'A' and i[1] == 'X':
        score += 1 + 3
    elif i[0] == 'B' and i[1] == 'Y':
            score += 2 + 3
    elif i[0] == 'C' and i[1] == 'Z':
            score += 3 + 3
print(score)


