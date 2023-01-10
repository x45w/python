has_ticket = True

knife_length = 25

if has_ticket:
    print("有车票,准备安检!")

    if knife_length > 20:
        print("刀过长,有 %d 公分长! " %knife_length)
        print("不允许乘车!")

    else:
        print("安检通过,旅途愉快!")

else:
    print("请先买票!")