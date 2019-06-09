import math

# 律速段階の問題らしい
# 最も移動速度が遅い部分に依存する
# 最も移動速度が遅い部分の移動先のところで全て貯まると仮定して良い
def main():
    n = int(input())
    a = [int(input()) for i in range(5)]
    min_move = min(a)
    print(math.ceil(n/min_move)+4)

if __name__ == '__main__':
    main()
