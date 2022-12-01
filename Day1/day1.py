# https://adventofcode.com/2022/day/1

# part 1
# max_cal = 0
# with open("calories.txt", "r") as f:
#     cal_count = 0
#     for line in f.readlines():
#         if line == "\n":
#             if cal_count > max_cal:
#                 max_cal = cal_count
#             cal_count = 0
#         else:
#             cal_count += int(line)
#
# print(max_cal)  # 70374

# part 2
top_cal = [0, 0, 0]
with open("calories.txt", "r") as f:
    cal_count = 0
    for line in f.readlines():
        if line == "\n":
            min_top_cal = min(top_cal)
            if cal_count > min_top_cal:
                i = top_cal.index(min_top_cal)
                top_cal[i] = cal_count
            cal_count = 0
        else:
            cal_count += int(line)

print(top_cal)  # [65240, 68996, 70374]
print(sum(top_cal))  # 204610
