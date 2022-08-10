from random import randint
tup = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10))
print(f"Os valores sorteados foram", end=" ")
for num in tup:
    print(f"{num}", end=" ")
print(f"\nO maior valor é {max(tup)}")
print(f"O menor valor é {min(tup)}")
