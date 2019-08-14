from random import randint

word = ["dream", "dreamer", "erase", "eraser"]

for i in range(100):
    print(word[randint(0,3)], end="")
print("")

