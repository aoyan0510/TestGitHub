#!/usr/bin/env python3
"""
フィボナッチ数列を出力するプログラム
Fibonacci Sequence Generator
"""


def fibonacci_generator(n):
    """
    フィボナッチ数列の最初のn個の数を生成する

    Args:
        n (int): 生成する数列の個数

    Yields:
        int: フィボナッチ数列の各要素
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fibonacci_up_to(max_value):
    """
    指定された値以下のフィボナッチ数列を生成する

    Args:
        max_value (int): 最大値

    Yields:
        int: フィボナッチ数列の各要素
    """
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b


def fibonacci_nth(n):
    """
    フィボナッチ数列のn番目の数を計算する

    Args:
        n (int): 位置（0から始まる）

    Returns:
        int: n番目のフィボナッチ数
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def main():
    """メイン関数"""
    print("=== フィボナッチ数列プログラム ===\n")

    # 最初の10個のフィボナッチ数を出力
    print("最初の10個のフィボナッチ数:")
    fib_list = list(fibonacci_generator(10))
    print(fib_list)
    print()

    # 100以下のフィボナッチ数を出力
    print("100以下のフィボナッチ数:")
    fib_list_100 = list(fibonacci_up_to(100))
    print(fib_list_100)
    print()

    # 特定の位置のフィボナッチ数を出力
    position = 15
    print(f"{position}番目のフィボナッチ数: {fibonacci_nth(position)}")
    print()

    # ユーザー入力による出力
    try:
        n = int(input("生成するフィボナッチ数列の個数を入力してください: "))
        if n > 0:
            print(f"\n最初の{n}個のフィボナッチ数:")
            for i, fib in enumerate(fibonacci_generator(n)):
                print(f"F({i}) = {fib}")
        else:
            print("正の整数を入力してください。")
    except ValueError:
        print("有効な整数を入力してください。")
    except KeyboardInterrupt:
        print("\n\nプログラムを終了します。")


if __name__ == "__main__":
    main()
