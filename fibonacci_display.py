#!/usr/bin/env python3
"""
フィボナッチ数列を段階的に表示するプログラム
Fibonacci Sequence Progressive Display
"""

import time
import sys
from fibonacci import fibonacci_generator, fibonacci_up_to, fibonacci_nth


class FibonacciDisplay:
    """フィボナッチ数列を段階的に表示するクラス"""

    def __init__(self):
        self.delay = 0.5  # デフォルトの遅延時間（秒）

    def display_with_delay(self, count, delay=None):
        """
        指定された個数のフィボナッチ数を時間間隔を置いて表示

        Args:
            count (int): 表示する個数
            delay (float): 表示間隔（秒）
        """
        if delay is None:
            delay = self.delay

        print(f"フィボナッチ数列を{count}個、{delay}秒間隔で表示します...\n")

        for i, fib in enumerate(fibonacci_generator(count)):
            print(f"F({i}) = {fib}")
            sys.stdout.flush()  # バッファをフラッシュして即座に表示
            if i < count - 1:  # 最後の要素の後は待機しない
                time.sleep(delay)

        print("\n表示完了！")

    def display_step_by_step(self, count):
        """
        ユーザーがEnterキーを押すたびに次の数を表示

        Args:
            count (int): 表示する個数
        """
        print(f"フィボナッチ数列を{count}個、ステップバイステップで表示します")
        print("Enterキーを押すと次の数が表示されます\n")

        for i, fib in enumerate(fibonacci_generator(count)):
            if i > 0:
                input("Enterキーを押してください... ")
            print(f"F({i}) = {fib}")

        print("\n表示完了！")

    def display_with_animation(self, count, delay=0.1):
        """
        アニメーション風に数列を表示

        Args:
            count (int): 表示する個数
            delay (float): アニメーション間隔（秒）
        """
        print(f"フィボナッチ数列を{count}個、アニメーション形式で表示します...\n")

        fib_list = []
        for i, fib in enumerate(fibonacci_generator(count)):
            fib_list.append(fib)

            # 画面をクリア（Linuxの場合）
            print("\033[2J\033[H", end="")

            # タイトル表示
            print("=== フィボナッチ数列 ===")
            print(f"進捗: {i + 1}/{count}\n")

            # これまでの数列を表示
            print("数列:", " → ".join(map(str, fib_list)))
            print(f"\n現在の値: F({i}) = {fib}")

            sys.stdout.flush()
            time.sleep(delay)

        print("\n\n表示完了！")

    def display_comparison(self, count):
        """
        複数の表示方法を比較

        Args:
            count (int): 表示する個数
        """
        print("=== フィボナッチ数列の比較表示 ===\n")

        # リスト形式
        print("1. リスト形式:")
        fib_list = list(fibonacci_generator(count))
        print(fib_list)
        print()

        # 段階的表示（高速）
        print("2. 段階的表示（0.2秒間隔）:")
        for i, fib in enumerate(fibonacci_generator(count)):
            print(f"F({i}) = {fib}", end="  ")
            sys.stdout.flush()
            time.sleep(0.2)
        print("\n")

        # 合計値の計算
        print("3. 合計値:")
        total = sum(fibonacci_generator(count))
        print(f"最初の{count}個の合計 = {total}")
        print()

    def display_tree_style(self, count):
        """
        ツリー形式で表示

        Args:
            count (int): 表示する個数
        """
        print("=== フィボナッチ数列（ツリー形式） ===\n")

        for i, fib in enumerate(fibonacci_generator(count)):
            indent = "  " * min(i, 10)  # インデントは最大10レベル
            bar = "├─" if i < count - 1 else "└─"
            print(f"{indent}{bar} F({i}) = {fib}")
            time.sleep(0.3)

        print("\n表示完了！")


def main():
    """メイン関数"""
    display = FibonacciDisplay()

    print("=" * 50)
    print("フィボナッチ数列段階的表示プログラム")
    print("=" * 50)
    print()
    print("表示モードを選択してください:")
    print("1. 時間間隔表示（自動で順次表示）")
    print("2. ステップバイステップ表示（手動で次へ）")
    print("3. アニメーション表示（更新形式）")
    print("4. 比較表示（複数形式）")
    print("5. ツリー形式表示")
    print("0. 終了")
    print()

    try:
        mode = input("モードを選択 [1-5, 0]: ").strip()

        if mode == "0":
            print("プログラムを終了します。")
            return

        if mode not in ["1", "2", "3", "4", "5"]:
            print("無効な選択です。")
            return

        # 表示個数の入力
        count = int(input("表示する個数を入力してください: "))

        if count <= 0:
            print("正の整数を入力してください。")
            return

        if count > 100:
            print("個数が多すぎます。100以下にしてください。")
            return

        print()

        # モードに応じた処理
        if mode == "1":
            delay = float(input("表示間隔（秒）を入力してください [0.5]: ") or "0.5")
            print()
            display.display_with_delay(count, delay)

        elif mode == "2":
            display.display_step_by_step(count)

        elif mode == "3":
            display.display_with_animation(count)

        elif mode == "4":
            display.display_comparison(count)

        elif mode == "5":
            display.display_tree_style(count)

    except ValueError as e:
        print(f"入力エラー: {e}")
    except KeyboardInterrupt:
        print("\n\nプログラムを中断しました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    main()
