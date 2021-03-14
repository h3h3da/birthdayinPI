# -*- coding: utf-8 -*-

f = open("result.txt")
lines = f.readlines()
print(len(lines))
day_pos_dic = {}
for line in lines:
    # print(line)
    day = line.split(" ")[0]
    pos = line.split(" ")[1]
    day_pos_dic[day] = pos
print("Init Done!")
sd = input("请输入要查询的生日：")
while sd != "exit":
    if sd not in day_pos_dic.keys():
        print("输入有误！")
        sd = input("请输入要查询的生日：")
        continue
    print(day_pos_dic[sd])
    sd = input("请输入要查询的生日：")
print("Done!")