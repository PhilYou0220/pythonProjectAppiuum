import random

# print(number)
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(0, 200):
    # 从字符串里取数
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)
    number3 = random.randint(0, 9)
    number4 = random.randint(0, 9)
    number5 = random.randint(0, 9)
    number6 = random.randint(0, 9)
    english1 = random.choice(alphabet)
    english2 = random.choice(alphabet)
    a = str(number1) + english1 + str(number2) + english2 + str(number3) + str(number4) + str(number5) + str(number6)
    print(a)
