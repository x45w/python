import random

player = int(input("请输入您要出的拳 石头(1)/剪刀(2)/布(3):"))

computer = random.randint(1,3)
print("玩家选择的拳头是: %d - 电脑出的拳是%d" %(player,computer))

# 玩家赢的情况
if ((player ==1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家赢了,电脑输了!")
    
# 平局
elif (player == computer):
    print("平局了!")

# 其他情况,电脑赢
else:
    print("电脑赢了,玩家输了!")