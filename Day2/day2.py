# https://adventofcode.com/2022/day/2

convert = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}

# part 1
# with open("input.txt", "r") as f:
#     score = 0
#     for line in f.readlines():
#         o = convert[line[0]]  # opponent
#         y = convert[line[2]]  # you
#
#         score += y + 1
#         if o == y:
#             score += 3
#         elif o == (y - 1) % 3:
#             score += 6

# part 2
with open("input.txt", "r") as f:
    score = 0
    for line in f.readlines():
        o = convert[line[0]]  # opponent
        e = convert[line[2]]  # ending

        score += (e * 3)
        if e == 0:
            score += ((o - 1) % 3) + 1
        elif e == 1:
            score += o + 1
        else:
            score += ((o + 1) % 3) + 1

print(score)