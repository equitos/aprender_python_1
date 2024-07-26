from time import sleep
from random import randint
dic = {}

print("-"*60)
for i in range(1, 5):
    dic[f"jogadoe {i}"] = randint(1, 6)
    print(f"o jogador{i} tirou {dic[f"jogadoe {i}"]}")
    sleep(1)
print("-"*60)

for i in sorted(dic.items(), key = lambda x:x[1], reverse=True):
    print(f"{i[0]} tirou {i[1]}")
print("-"*60)
